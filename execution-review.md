# Revisión de la ejecución

La conclusión anterior de bloqueo no estaba justificada: la ejecución original se interrumpió sin trazas y su causa exacta no puede reconstruirse. Dos peticiones mínimas posteriores (subprocess con stdin cerrado y tubería PowerShell original) finalizaron correctamente.

La reproducción del expediente con 1800 tokens mostró un defecto concreto: 1745 tokens de razonamiento dejaron muy poco espacio a la respuesta en la primera petición, que quedó truncada. Claude Code continuó automáticamente; terminó con success/end_turn en 54.2 segundos, 3471 tokens de salida acumulados y dos bloques de texto. Leer solo result pierde el inicio de la respuesta.

Corrección: 8192 tokens de salida por petición, max-turns=1, límite adicional CLI 0.50 USD, stdin cerrado explícitamente, captura separada de stderr y stream-json y timeout 180s. El timeout es guardarraíl, no diagnóstico. max-turns no debe interpretarse como límite garantizado de peticiones HTTP, ya que el caso truncado tuvo varias peticiones dentro de un turno. Reconstruir texto de todos los eventos assistant; excluir bloques de razonamiento. Conservar el JSONL original.

Verificación: D1-opus-fixed terminó success/end_turn, un bloque de texto, 4178 tokens de salida totales (2518 de razonamiento), coste equivalente de lista 0.1077945 USD. Sin herramientas ni llamadas a Azure. La autenticación es claude.ai/Max; el evento de límites de las peticiones mínimas indica isUsingOverage=false y sobreuso deshabilitado por organización. El coste de lista no representa necesariamente factura adicional.

Coste equivalente registrado hasta Opus corregido: 0.2468985 USD (dos peticiones mínimas y dos ejecuciones D1). No incluye la llamada original interrumpida, cuyo uso no se recuperó. No afirmar gasto efectivo cero de toda la investigación.

Nota de calibración: Opus identifica el doble cargo, tenant, unique posterior al cargo y expiración 24h/72h. Su reparación deja imprecisa la transición/reintento de estados pending; exige prueba a 30h sin definir claramente cómo bloquear una operación incierta. No usar este resultado aislado como evidencia de benchmaxing ni de superioridad de otro modelo.

## Comparación de calibración D1 (una ejecución por modelo)
Opus corregido: 61.2 s, 0.1077945 USD equivalentes de lista. Fable: 49.3 s, 0.248781 USD equivalentes de lista. Ambos success/end_turn, mismo expediente, effort high, salida máxima 8192, sin herramientas. Es tiempo observado de proceso, no un benchmark de latencia. Diagnóstico y pruebas de este turno: total registrado 0.4956795 USD equivalentes de lista, distinto de factura adicional de Max.

Observación preliminar sin evaluación ciega: ambos identifican la causa directa y rechazan la propuesta del compañero. Hay diferencias sustantivas: Opus propone intención durable antes de capturar, pero no especifica bien cómo tratar pending, y pide que el retry de 30h pase sin definir toda la transición. Fable consulta filas antes de capturar pero sigue insertando después del efecto externo; acepta un doble cargo tras expiración como límite no prevenible y propone documentarlo en vez de fallo. Esa imposibilidad está formulada demasiado ampliamente: se puede prevenir una segunda captura bloqueando estados inciertos de forma durable, aunque se sacrifique completar automáticamente el cobro. Su afirmación de que event ID también sirve requiere que un pedido nunca produzca eventos distintos, algo no establecido.

Por tanto el caso distingue detalles de diseño, pero no demuestra ventaja general de Fable ni benchmaxing de Opus. No todos aciertan de forma completa. El siguiente paso metodológico sería comprobar esas diferencias con fixtures nuevos y revisores ciegos, sin seleccionar por ganador. No se lanzaron más pruebas.
