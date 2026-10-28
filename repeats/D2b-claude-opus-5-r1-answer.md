## ¿Cumple la regla? No

Dos fallos, uno de ellos grave:

1. **El lease no es una valla.** Cinco minutos de lease en *nuestra* DB no impiden que el worker pausado despierte a t+10h y llame a `print`; no hay fencing en el proveedor. El lease es un mecanismo de disponibilidad, no de corrección.
2. **"Riesgo inevitable tras seis horas" es falso.** Pasadas las 6h la memoria del proveedor ya no deduplica, luego reenviar produce una segunda carta física. Pero la regla permite **detener la automatización en casos inciertos**: a t+10h la decisión correcta es parar, no reimprimir. El duplicado es elegido, no inevitable.

(La implementación original tiene además dos bugs: `print(attempt_uuid, …)` cambia de clave en cada intento, así que la deduplicación del proveedor nunca actúa; y "consultar, imprimir, insertar" deja ventana entre workers.)

## Alternativa: estados persistentes

Tabla `recibos` con `UNIQUE (organization_id, case_id)`, y columnas `print_key` (= `org:case`, estable y derivada), `estado`, `primer_intento_at`, `epoch`, `message_uuid`.

- **NUEVO** (fila ausente): en transacción local, `INSERT` de la fila en estado `EN_VUELO` **antes** de llamar al proveedor (intención escrita primero). El `UNIQUE` elige un único ganador; los perdedores nunca imprimen. Después `print("org:case", body)`. Respuesta aceptada → `COMPLETADO`. Rechazo explícito y determinista del proveedor → reintento acotado con la misma clave. **Timeout o respuesta perdida → `INCIERTO`** (nunca se interpreta como "no se hizo").
- **INCIERTO**: no se imprime jamás de forma automática. Se crea tarea de revisión humana y se conserva la fila. Las reentregas posteriores leen el estado y terminan sin efecto externo.
- **COMPLETADO**: ack y salida idempotente.

**Ventana entre guardar estado y emitir el efecto.** Una caída ahí deja `EN_VUELO` sin desenlace conocido. La única recuperación automática legítima es reintentar **con la misma clave estable y solo mientras `now < primer_intento_at + margen conservador` (p. ej. 5h sobre 6h)**: ahí el propio proveedor deduplica. Vencido el margen, la fila pasa a `INCIERTO`. Es decir, la ventana de 6h no es un riesgo que se acepta: es exactamente la frontera entre reintento seguro y revisión humana.

**Worker antiguo que reanuda.** Invariante único: *un worker solo imprime si acaba de ganar un CAS a `EN_VUELO` (comparando `epoch` y estado) y está dentro del margen de 6h del primer intento*. El worker viejo relee su fila; si está `COMPLETADO`/`INCIERTO` o el `epoch` cambió, aborta sin imprimir. Dentro de las 6h, además, la clave estable lo cubriría.

## Separación de garantías

- **Prevención de duplicados (safety):** `UNIQUE` + clave estable + deduplicación de 6h + CAS + prohibición de imprimir desde estado incierto. No depende de timeouts ni de relojes.
- **Que toda carta se imprima (liveness):** reentregas de 48h, barrido de `EN_VUELO` dentro del margen, y cola de revisión humana con SLA para `INCIERTO`. Pasadas las 6h la liveness se delega a personas; nunca se compra debilitando la safety.

## Pruebas

1. **t+10h:** fila `EN_VUELO` de las 10:00; reentrega con nuevo `attempt_uuid` y mismo `message_uuid` → `print` no se invoca, estado `INCIERTO`, ticket creado, total 1 carta.
2. **Caída antes del envío:** commit de `EN_VUELO` y muerte previa al `print`; reintento a t+30min → `print` una sola vez con clave `org:case`. Variante con dos workers concurrentes: un solo ganador de `UNIQUE`/CAS.
3. **Respuesta perdida a t+2h:** reintento con misma clave → proveedor deduplica, 1 carta física, estado `COMPLETADO`.
4. **Dos organizaciones, mismo expediente:** `A:123` y `B:123` → dos filas, dos claves, dos cartas; sin colisión cruzada.