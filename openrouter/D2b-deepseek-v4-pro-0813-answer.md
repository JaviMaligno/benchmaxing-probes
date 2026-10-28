La propuesta no cumple. Su lease de 5 minutos con reenvío automático al expirar puede duplicar: si el primer `print` se aceptó y luego el worker queda pausado, otro worker reenviará; dentro de 6 horas el proveedor deduplica por clave, pero a t+10h ya no, y además el worker viejo podría reanudarse e imprimir otra vez. “Aceptar riesgo tras 6 horas” viola la regla de máximo una carta por (organización, expediente).

**Alternativa correcta: estados persistentes y no reenviar en caso incierto**

Crear una tabla durable con `UNIQUE(org, expediente)` y estados:

- `NUEVO`: listo para imprimir.
- `ENVIANDO`: un worker tiene lease vigente.
- `INCIERTO`: hubo fallo o lease expirado; requiere revisión manual.
- `COMPLETADO`: impresión confirmada.

**Transiciones concretas**

1. **NUEVO → ENVIANDO**: en una transacción local, insertar/actualizar la fila a `ENVIANDO` con `lease_owner = worker_id` y `lease_until = now + 5 min`, sólo si no existe o está en `NUEVO`. Si existe `COMPLETADO`, no hacer nada. Si existe `INCIERTO`, detener la automatización para revisión. Si existe `ENVIANDO` con lease vigente, no hacer nada; si el lease venció, marcarla `INCIERTO` y detener.

2. **Antes de emitir el efecto externo**: el worker debe comprobar que sigue siendo dueño con lease vigente. Esta comprobación no es atómica con `print`, pero es suficiente porque si el lease expira, **ningún otro worker reimprime automáticamente**: lo pasa a `INCIERTO`. Por tanto, aunque el worker viejo se reanude tarde, debe abortar si su lease caducó. Si aun así imprimiera sin comprobar, no habrá otro envío automático: máximo una carta.

3. **Éxito de `print`**: confirmar con `UPDATE ... SET estado='COMPLETADO' WHERE estado='ENVIANDO' AND lease_owner=:worker AND lease_until > now()`. Si la condición falla, no confirmar.

4. **Lease expirado**: otro worker lo marca `INCIERTO` y detiene. No hay reenvío automático. Sólo un operador puede pasar `INCIERTO` a `NUEVO` si confirma que no se imprimió, o a `COMPLETADO` si confirma que sí se imprimió.

La ventana entre guardar estado y emitir efecto se cubre: se reserva `ENVIANDO` antes de imprimir, y al vencer el lease no se reintenta automáticamente; se detiene. Esto previene duplicados. La garantía de impresión se cumple para operaciones nuevas sin fallos (`NUEVO → ENVIANDO → print → COMPLETADO`); ante incertidumbre se sacrifica completitud automática, como permite la regla.

**Pruebas**

- **t+10h**: worker A reserva `ENVIANDO`, `print` es aceptado pero se pierde la respuesta, lease expira. Llega reentrega; worker B ve lease vencido y marca `INCIERTO`; no llama a `print`. A se reanuda, ve que ya no es dueño y aborta. Resultado: una impresión.
- **Caída antes del envío**: worker A reserva `ENVIANDO`, cae antes de `print`; lease expira. Worker B marca `INCIERTO`; no se imprime. Revisión manual decide reintento.
- **Dos organizaciones igual expediente**: filas `(org1,exp1)` y `(org2,exp1)` son independientes por `UNIQUE(org,expediente)`; ambas imprimen sin conflicto y la clave de `print` incluye organización, no solo expediente.

No uses recibo posterior al `print`; la reserva previa con estado `ENVIANDO` y la política de no reenvío automático al expirar son la fuente de verdad.