## Resultados clave

Beta gana en el agregado observado (73% vs 27%), pero Alfa gana en **ambas** categorías por separado: es una paradoja de Simpson causada por la mezcla de tareas (Alfa fue evaluado con 90% difíciles y Beta con 90% fáciles). Bajo la hipótesis de transporte a la cola de producción (10% fácil / 90% difícil), **Alfa proyecta 27% de éxito y 20,95 min/tarea; Beta proyecta 17% y 27,92 min/tarea**: Beta sería peor en éxito y en tiempo.

| Métrica | Alfa | Beta |
|---|---|---|
| Éxito fáciles | 90/100 = 90% | 720/900 = 80% |
| Éxito difíciles | 180/900 = 20% | 10/100 = 10% |
| Éxito agregado observado | 270/1000 = 27% | 730/1000 = 73% |
| Éxito proyectado (10/90) | 0,1·90 + 0,9·20 = **27%** | 0,1·80 + 0,9·10 = **17%** |
| Min/tarea finalizada, muestra observada | (270·10 + 730·25)/1000 = **20,95** | (730·8 + 270·32)/1000 = **14,48** |
| Min/tarea finalizada, proyección | 0,27·10 + 0,73·25 = **20,95** | 0,17·8 + 0,83·32 = **27,92** |

(Un fallo Alfa cuesta 5+20 = 25 min totales; un fallo Beta, 12+20 = 32 min, incluyendo la reparación manual.)

**Mejora relativa vs. puntos porcentuales.** En el agregado observado, Beta supera a Alfa en +46 puntos porcentuales (27→73), un +170% relativo (el "triplica" del borrador es el cociente 73/27 ≈ 2,7×, no una mejora del 300%). Por categoría ocurre lo contrario: Alfa supera a Beta en +10 puntos en fáciles (90 vs 80, +12,5% relativo) y +10 puntos en difíciles (20 vs 10, +100% relativo). En la proyección, Alfa supera a Beta en +10 puntos (27 vs 17, +58,8% relativo) y ahorra 6,97 min por tarea (25% menos tiempo).

**Qué queda respaldado.** Solo los conteos y tasas de cada muestra tal como se observaron, y el hecho aritmético de que la ventaja agregada de Beta desaparece al condicionar por categoría: es un artefacto de composición, no de rendimiento.

**Qué depende del transporte.** Toda la proyección (27% vs 17%; 20,95 vs 27,92 min) asume que las tasas y tiempos por categoría/resultado se mantienen en la cola futura. Esa hipótesis no está demostrada: las tareas "fáciles" y "difíciles" de cada muestra son distintas entre sí y podrían no parecerse a las de producción.

**Qué no es identificable causalmente.** Ninguna afirmación de superioridad causal de un sistema sobre otro: las muestras no fueron aleatorizadas, contienen tareas distintas y no están emparejadas, así que la asignación de tareas confunde cualquier comparación. Tampoco puede afirmarse "ahorro de tiempo en producción" con los 8 vs 10 minutos del borrador, porque esos son solo tiempos de éxito e ignoran los fallos, cuya reparación (20 min) domina el coste cuando la tasa de fallo es alta.

**Comparación mínima que resolvería la decisión.** Un diseño emparejado: muestrear tareas de la cola real (o con su mezcla 10/90), ejecutar **ambos** sistemas sobre las mismas tareas, y medir éxito y minutos totales por tarea finalizada, incluida la reparación manual. Con eso la diferencia por tarea se estima directamente sin depender del transporte ni de la mezcla.

**Párrafo de reemplazo del borrador:**

> En las muestras disponibles, Beta obtuvo 73% de éxito agregado frente al 27% de Alfa, pero esa comparación no es válida: cada sistema se evaluó con una mezcla de tareas opuesta y, al separar por categoría, Alfa supera a Beta tanto en fáciles (90% vs 80%) como en difíciles (20% vs 10%). Si las tasas y tiempos por categoría se mantuvieran en la cola de producción (10% fácil, 90% difícil) —hipótesis no verificada—, Alfa proyectaría 27% de éxito y 20,95 minutos por tarea finalizada, frente a 17% y 27,92 minutos de Beta, porque los fallos de Beta son más caros (32 min con reparación) y serían mayoría. Con datos no aleatorizados, de tareas distintas y sin emparejar, no podemos afirmar superioridad causal de ningún sistema. Recomendamos no sustituir Alfa todavía y ejecutar una comparación emparejada de ambos sistemas sobre las mismas tareas de la cola real, midiendo el tiempo total incluida la corrección manual, antes de decidir.