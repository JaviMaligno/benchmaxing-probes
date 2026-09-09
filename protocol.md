# Benchmaxing — protocolo de calibración (2026-09-09)

Estado: piloto exploratorio, sin resultados al redactar este protocolo.
Testimonios: experiencia propia del autor y conversaciones directas; no atribuir citas, nombres, frecuencia ni detalles que aún no haya aportado. Separar de testimonios publicados.
Hipótesis: algunas capacidades de diagnóstico, conservación de restricciones y gestión de incertidumbre pueden no quedar bien representadas por rankings agregados. Una discrepancia no identifica su causa de entrenamiento.

Acceso: Claude Code, autenticación claude.ai / Max confirmada. No desplegar Azure mientras esta vía funcione. Primera fase: dos llamadas, una por modelo exacto claude-opus-5 y claude-fable-5, effort high. Sin herramientas, memoria ni personalizaciones; esto evalúa razonamiento sobre un expediente, no autonomía en repositorios. Límite CLI 0.50 USD por llamada como protección adicional, salida máxima 1800 tokens. No considerar ese límite garantía de facturación ni la métrica de coste API como cargo efectivo de suscripción. Sin reintentos automáticos ni fallback. Parar si hay límites o acceso denegado.

D1, criterios previos (cada uno 0 ausente/incorrecto, 1 parcial, 2 completo):
1. Causa observada: guard desactivado, respuesta incierta y cambio de request ID permiten segundo cargo; comentario no prueba configuración.
2. Namespace: tenant+order; tanto Redis como propuesta de clave y restricción global pueden mezclar tenants.
3. Guard previo al efecto externo: puede perder trabajo tras fallo; TTL/reinicio no resuelven exactamente una captura.
4. Persistencia y concurrencia: estado durable, exclusión o reserva única tenant+order; unique DB aislado no deshace un doble cargo externo.
5. Límite temporal: ledger 24h frente a retries 72h; clave estable sola no garantiza exactamente una captura; bloquear/reconciliar estados inciertos y explicitar sacrificio de disponibilidad o necesidad de ampliar contrato proveedor.
6. Regresión: timeout tras captura, concurrencia, tenants coincidentes, retry >24h; no inventar que ejecutó pruebas.

Fallo crítico: afirmar garantía completa con la propuesta del compañero o con clave estable sin resolver expiración e incertidumbre. Puntuaciones son lista diagnóstica, no índice de inteligencia. Guardar texto íntegro y métricas.
Si ambos resuelven D1 sin fallos sustantivos: documentar efecto techo y pasar a contexto distribuido/cambios de requisitos con herramientas; no gastar repeticiones de Fable en variantes cosméticas.
Si ambos fallan: revisar claridad/solubilidad antes de aumentar dificultad.
Si hay diferencias: replicar con casos nuevos isomorfos, contrabalancear orden y revisar a ciegas; una llamada no establece superioridad.
Congelar después tareas distintas, inéditas y criterios antes de evaluación final. Conservar todos los pilotos, empates y resultados contrarios. No seleccionar pruebas por qué modelo gana.

## Estado de ejecución
Claude Code acepta configuración y autenticación Max. Se inició una llamada a claude-opus-5; tras una espera prolongada sin respuesta ni métricas se detuvo exclusivamente su proceso identificado. D1-opus.json no contiene una respuesta evaluable. No se llamó a Fable ni a Azure. No hay puntuaciones ni conclusiones experimentales. Sin datos de uso no se puede afirmar consumo cero de la llamada interrumpida. Antes de reanudar: diagnosticar la ejecución CLI con una petición mínima y timeout; evitar repetir el expediente completo. Las 48 ejecuciones propuestas inicialmente no están lanzadas ni programadas.

## Corrección tras revisión
La etiqueta anterior de bloqueo fue prematura. Véase execution-review.md. Se han recuperado respuestas válidas de Opus y verificado el runner con stream-json; el límite original de 1800 tokens producía truncamiento y continuación automática. La fase corregida usa 8192 tokens; estos resultados deben distinguirse de la reproducción con 1800. Fable se prueba únicamente después de verificar Opus, por Claude Code Max.
