### Tabla numérica de auditoría

| Métrica / Estrato | Alfa | Beta | Diferencia absoluta (Beta − Alfa) | Cambio relativo (Beta vs. Alfa) |
| :--- | :---: | :---: | :---: | :---: |
| **Éxito observado: Fáciles** | 90,0% (90/100) | 80,0% (720/900) | −10,0 pp | −11,11% |
| **Éxito observado: Difíciles** | 20,0% (180/900) | 10,0% (10/100) | −10,0 pp | −50,00% |
| **Éxito observado: Agregado** | 27,0% (270/1000) | 73,0% (730/1000) | +46,0 pp | +170,37% |
| **Éxito proyectado: Producción (10% F / 90% D)** | 27,0% | 17,0% | −10,0 pp | −37,04% |
| **Tiempo medio: Fáciles (min/tarea)** | 11,50 | 12,80 | +1,30 min | +11,30% |
| **Tiempo medio: Difíciles (min/tarea)** | 22,00 | 29,60 | +7,60 min | +34,55% |
| **Tiempo medio observado: Agregado (min/tarea)** | 20,95 | 14,48 | −6,47 min | −30,88% |
| **Tiempo medio proyectado: Producción (min/tarea)** | 20,95 | 27,92 | +6,97 min | +33,27% |

*Nota de cálculo: El tiempo por tarea finalizada incluye fallos y su reparación manual (Alfa: éxito = 10 min, fallo = 5 + 20 = 25 min; Beta: éxito = 8 min, fallo = 12 + 20 = 32 min).*

---

### Evaluación metodológica

*   **Conclusiones respaldadas por los datos observados:** El borrador incurre en la paradoja de Simpson y omite el coste de los fallos. En el agregado observado, Beta supera a Alfa en éxito en +46,0 puntos porcentuales (pp), lo que supone una mejora relativa del +170,37% (multiplica los éxitos por 2,70, no los triplica), y reduce el tiempo medio por tarea en 6,47 minutos (−30,88% relativo; elevando la capacidad de finalización un +44,68%, tampoco el triple). Sin embargo, esto ocurre únicamente porque la muestra de Beta tuvo un 90% de tareas fáciles frente al 10% en Alfa. Dentro de cada categoría observada, Beta tuvo menor tasa de éxito (−10,0 pp tanto en fáciles como en difíciles, equivalentes a caídas relativas del −11,11% y −50,00%). Además, mirar solo el tiempo por éxito (8 vs. 10 min) oculta que cada fallo de Beta consume 32 minutos totales frente a 25 de Alfa, haciendo que Beta sea más lento en promedio dentro de ambas categorías (+1,30 min en fáciles y +7,60 min en difíciles).
*   **Conclusiones dependientes de la hipótesis de transporte:** Si asumimos provisionalmente que las tasas y tiempos por categoría se mantienen en la cola de producción (10% fácil, 90% difícil, idéntica a la mezcla observada en Alfa), Beta no ahorra tiempo ni mejora el éxito: su éxito proyectado cae al 17,0% frente al 27,0% de Alfa (−10,0 pp; −37,04% relativo) y su tiempo medio por tarea finalizada sube de 20,95 a 27,92 minutos (+6,97 min; +33,27% relativo), reduciendo la capacidad operativa.
*   **Conclusiones no identificables causalmente:** Con este diseño es imposible demostrar qué sistema es causalmente superior. Al evaluar muestras no aleatorizadas, sin emparejar y con tareas distintas, el efecto del sistema está confundido con la selección de tareas (por ejemplo, las tareas asignadas a Beta dentro de cada etiqueta podrían haber sido intrínsecamente más complejas que las de Alfa).
*   **Mínima comparación futura recomendada:** Ejecutar una evaluación emparejada (o un ensayo controlado aleatorizado) donde Alfa y Beta procesen exactamente la misma muestra de tareas, extraída aleatoriamente o estratificada con la proporción real de producción (10% fácil, 90% difícil), registrando tanto la tasa de éxito como el tiempo total hasta completar la tarea (incluyendo reparaciones).

---

### Párrafo de reemplazo para el borrador

"En las muestras evaluadas, la ventaja agregada de Beta en tasa de éxito (73,0% frente a 27,0%, +46,0 pp o +170,37% relativo) y en tiempo medio total por tarea finalizada (14,48 frente a 20,95 minutos, −30,88% relativo) se explica por un desequilibrio en la composición de las muestras: Beta procesó un 90% de tareas fáciles y Alfa solo un 10%. Al desglosar por categoría y contabilizar el tiempo total incluyendo fallos y reparaciones manuales (32 minutos por fallo en Beta frente a 25 en Alfa), Beta registró un rendimiento inferior en su muestra tanto en tareas fáciles como en difíciles (−10,0 pp de éxito y mayor tiempo medio en ambas). Si estas tasas y tiempos por categoría se transportasen sin cambios a la próxima cola de producción (10% fácil y 90% difícil), proyectamos que Beta reduciría el éxito del 27,0% al 17,0% (−10,0 pp; −37,04% relativo) y aumentaría el tiempo medio de trabajo de 20,95 a 27,92 minutos por tarea (+33,27% relativo). Dado que las muestras no fueron aleatorizadas ni emparejadas sobre las mismas tareas, estos datos no permiten identificar superioridad causal de ningún sistema; por tanto, no se recomienda sustituir Alfa hasta evaluar ambos sistemas sobre un mismo conjunto emparejado de tareas representativo de producción."