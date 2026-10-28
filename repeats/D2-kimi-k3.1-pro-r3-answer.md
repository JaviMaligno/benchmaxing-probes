### Diagnóstico

El colega mezcla dos problemas. `warehouse_id:order_id` —con codificación no ambigua— es la clave correcta: `delivery_id` cambia en cada reenvío y no identifica la operación. Sin embargo, la ventana de 36 horas no convierte `prepare` en idempotente permanente.

`UNIQUE(warehouse_id, order_id)` en la fila final protege la DB, pero se comprueba **después** de llamar al proveedor: no impide llamadas duplicadas. Además, dos almacenes pueden usar el mismo `order_id`; deben tener operaciones independientes.

El caso incierto después de 36 horas sí puede prevenirse: no reintentando. Lo imposible con esta API es averiguar automáticamente si hubo preparación o completarlo sin arriesgar un duplicado.

### Diseño implementable

Mantener desde el inicio una fila de intención con `UNIQUE(warehouse_id, order_id)`, estado, intento local y receipt:

- **PENDIENTE → EN_ENVIO**: una transacción inserta/reserva la intención y confirma antes de llamar. Solo este estado tiene un intento autorizado.
- **EN_ENVIO → COMPLETADO**: llegó éxito; se guarda receipt y datos finales. La actualización comprueba intento y estado.
- **EN_ENVIO → BLOQUEADO**: respuesta perdida, timeout, caída, lease expirado o resultado incierto. La recuperación no puede distinguir si se envió.
- **BLOQUEADO → COMPLETADO**: solo mediante confirmación externa/manual o recepción válida del único intento.
- **No existen** transiciones automáticas `EN_ENVIO/BLOQUEADO → PENDIENTE/EN_ENVIO`, ni siquiera después de 36 horas.

Sin fallos, el pedido nuevo sigue todo el camino automáticamente. El conflicto `UNIQUE` al reservar evita dos intentos concurrentes; no se usa como sustituto de la reserva previa.

### Trazas adversas

1. **Respuesta perdida:** a las 09:00 la intención ya está `EN_ENVIO`; el proveedor acepta, pero se pierde la respuesta. A las 09:01 cae el worker. A t+50h, el reenvío encuentra la intención y la bloquea: no llama otra vez. Con el código actual podría preparar dos paquetes; incluso con la clave compuesta, ya expiró la deduplicación. La orden homónima de otro almacén usa otra clave y otra fila.

2. **Worker pausado:** W1 reserva, queda pausado antes de enviar y expira su lease. Si W2 “toma el relevo” y envía, W1 puede despertar y enviar también; comprobar un fencing token antes de `prepare` no cierra la carrera entre comprobación y llamada. En el diseño seguro, W2 solo marca `BLOQUEADO`, nunca adquiere otro intento. W1 podría despertar y realizar el único envío posible. El fencing condiciona escrituras locales, no al proveedor.

### Límites

Una caída inmediatamente antes del envío deja el mismo estado durable que una inmediatamente después: ambas deben quedar bloqueadas. Puede quedar un pedido sin preparar; es el coste deliberado de priorizar no duplicar. Sin búsqueda, cancelación o reconciliación externa, ningún algoritmo local puede resolver esa incertidumbre.