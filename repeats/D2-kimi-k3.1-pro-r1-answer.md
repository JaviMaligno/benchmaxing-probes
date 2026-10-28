**Diagnóstico.** El colega acierta en que la clave debe ser estable y estar ambientada por almacén: `warehouse_id:order_id`; `delivery_id` cambia en cada reenvío y no sirve como identidad. Pero consultar la DB y después llamar deja una carrera: dos workers pueden no ver fila y llamar ambos. El `UNIQUE` final detecta el conflicto **después** de los efectos externos; no los impide. Además, tras 36 horas no es imposible *prevenir* una segunda preparación —basta bloquear—, sino imposible *reintentar automáticamente con seguridad* o averiguar el resultado anterior.

**Propuesta implementable.** Crear antes de llamar una fila durable de intención, con `UNIQUE(warehouse_id,order_id)`, clave estable, payload, `estado`, `receipt`, `retry_until`, `lease_owner`, `lease_until` y `epoch`. El plazo local, con margen de seguridad, se fija al crear la intención y **no se renueva** al cambiar de worker.

Estados y transiciones:

- Evento nuevo → transacción que inserta `PENDIENTE`; si ya existe, no crear otra intención.
- `PENDIENTE` o `EN_CURSO` con lease vencido → `EN_CURSO`: transacción que incrementa `epoch` y concede lease. Solo se permite llamar si estamos dentro del plazo.
- Tras confirmar éxito → `FINAL`: en una transacción, insertar la fila final y guardar receipt, condicionando la actualización a que `epoch` siga siendo la del worker.
- Error de red, caída o respuesta perdida → permanece `EN_CURSO`, resultado incierto. Puede reintentarse con **la misma clave** dentro del plazo.
- Incertidumbre al vencer `retry_until` → `BLOQUEADA`; nunca nuevo `prepare` automático.
- `FINAL` + eventos repetidos → ignorar; `BLOQUEADA` requiere revisión.

Una caída antes del commit no deja intención ni llamada. Una caída después del commit pero justo antes de enviar deja la misma evidencia que una caída justo después de enviar: no pueden distinguirse localmente. Durante la ventana, reintentar es seguro en ambos casos; después, se bloquea aunque a veces sea innecesario.

**Traza 1.** A las 09:00 el proveedor acepta; se pierde la respuesta y a las 09:01 cae el worker. La intención queda incierta. A t+50h no se reenvía: pasa a `BLOQUEADA`. Usar la clave estable no garantiza deduplicación fuera de las 36 horas. Otro almacén con el mismo `order_id` tiene otra clave compuesta y una preparación independiente.

**Traza 2.** W1 obtiene `epoch=7` y queda pausado; W2 adquiere `epoch=8`, llama y finaliza. W1 despierta: las comprobaciones y actualizaciones condicionadas por `epoch` impiden que sobrescriba la DB, pero **no pueden impedir físicamente** una llamada externa si ya había pasado su comprobación previa. Dentro de la ventana, la clave repetida evita otra preparación; fuera, podría producirla.

**Límites.** Sin fencing en el proveedor, no existe exclusión absoluta entre un worker pausado y su sustituto: comprobar el lease y enviar no es atómico. Leases y fencing protegen PostgreSQL, no el efecto externo. Por eso el traspaso fuera de la ventana solo puede terminar en revisión. Si se exige garantía estricta incluso ante pausas arbitrarias, la API no permite combinarla con failover automático.