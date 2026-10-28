## Diagnóstico

Tres fallos en el código actual: (1) la key es `delivery_id`, que el broker cambia en cada reenvío, así que el proveedor nunca deduplica: a t+50h ejecuta una segunda preparación del mismo (almacén, pedido); (2) "consultar DB y luego llamar" es check-then-act: dos workers ven "sin fila" a la vez y ambos llaman a `prepare`; (3) no se registra el intento antes de llamar, así que tras la caída de 09:01 nadie sabe que hubo aceptación a las 09:00, y como 36h < 96h de reenvíos, el reintento llega fuera de la ventana de deduplicación.

## Evaluación del colega

Acierta en la clave compuesta `warehouse_id:order_id` (los IDs se repiten entre almacenes) y en capturar el UNIQUE para la carrera del insert final. Es incompleto: consultar la DB no elimina el check-then-act (hace falta reclamar antes de llamar), y el caso posterior a 36h **sí es prevenible** a nivel de aplicación: sin API de búsqueda no se puede *resolver* la incertidumbre, pero sí *impedir* la doble preparación bloqueando antes de que venza la ventana, en vez de reintentar a ciegas.

## Propuesta (estados y transiciones)

Estados: `nuevo → claimed → finalizado | bloqueado`. La fila `claimed` lleva owner, epoch, started_at. UNIQUE(warehouse_id, order_id) en claims y en finales.

- **T1**: al recibir un delivery, si no hay fila final ni claim: INSERT de claim (commit) antes de cualquier `prepare`. Conflicto UNIQUE → otro worker tiene el relevo.
- **T2**: con lease vigente y `now − started_at < 34h` (margen bajo 36h): `prepare("warehouse:order", payload)`. Con respuesta: una transacción inserta la fila final (receipt) y marca `finalizado`.
- **T3**: reenvío sin fila final: si el claim es < 34h → reintentar la misma key (idempotente dentro de ventana); si ≥ 34h sin receipt → `bloqueado`, no llamar a `prepare`, revisión humana.
- **T4**: lease caducada → epoch+1 a favor del nuevo worker. El antiguo, al despertar, relee epoch y edad **antes de enviar y antes del insert final** (transacción condicionada por owner); si no coinciden, abandona sin tocar al proveedor.

Caída justo antes de enviar: queda claim sin aceptación; el reenvío en ventana reintenta y esa es la primera aceptación → final. Caída justo después: aceptada a T, respuesta perdida; reenvío en ventana devuelve el resultado previo → final; fuera de ventana, T3 bloquea.

## Trazas adversas

1. **El escenario del enunciado solo con la corrección del colega**: 09:00 `prepare` aceptada, respuesta perdida, sin fila; 09:01 caída; a t+50h el worker consulta, no hay fila, llama `prepare` con la misma key… pero 50h > 36h desde la primera aceptación → el proveedor puede ejecutar otra preparación: doble paquete. Hace falta T3 (bloqueo por edad del claim).
2. **Worker antiguo pausado**: A envía a T y queda pausado; su lease caduca; B toma relevo (T4), reintenta en ventana, recupera el resultado previo y escribe la fila final. A despierta a T+40h: sin guardas reintentaría (misma key, >36h → segunda ejecución) o insertaría su receipt caducado. Con T4, A relee epoch ≠ suya → no envía.

## Límites

- Sin búsqueda, un `bloqueado` puede ser falso positivo (el envío nunca salió); solo lo resuelve un humano.
- "Puede ejecutar otra preparación": es riesgo, no certeza.
- Sin fencing del proveedor, un worker pausado entre su relectura de epoch y el envío puede emitir un `prepare` tardío; las guardas (edad <34h, lease, epoch) lo acotan pero no lo anulan: queda una ventana residual, documentada.
- Se asume que el proveedor responde de forma atómica ante llamadas concurrentes con la misma key dentro de la ventana; si no, no tiene solución con esta API.