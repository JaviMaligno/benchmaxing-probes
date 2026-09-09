## Tabla numérica

| Métrica | Alfa | Beta | Diferencia (pp) | Relativo |
|---|---|---|---|---|
| Éxito fáciles | 90/100 = 90.0% | 720/900 = 80.0% | Alfa +10.0 | Alfa 1.125× (+12.5%) |
| Éxito difíciles | 180/900 = 20.0% | 10/100 = 10.0% | Alfa +10.0 | Alfa 2.00× (+100%) |
| Éxito agregado observado | 270/1000 = 27.0% | 730/1000 = 73.0% | Beta +46.0 | Beta 2.70× (+170%) |
| Mezcla de la muestra (fácil/difícil) | 10% / 90% | 90% / 10% | — | — |
| Éxito proyectado (10% fácil, 90% difícil) | 27.0% | 17.0% | Alfa +10.0 | Alfa 1.588× (+58.8%) |
| Min. por éxito | 10 | 8 | — | — |
| Min. por fallo (modelo + 20 de reparación) | 5+20 = 25 | 12+20 = 32 | — | — |
| Min. medios por tarea finalizada (observado) | 20 950/1000 = **20.95** | 14 480/1000 = **14.48** | Beta −6.47 | Beta −30.9% |
| Min. medios por tarea finalizada (proyectado) | 0.27·10 + 0.73·25 = **20.95** | 0.17·8 + 0.83·32 = **27.92** | Alfa −6.97 | Alfa −25.0% (Beta +33.3%) |
| Tareas finalizadas/hora (proyectado) | 2.86 | 2.15 | — | Alfa 1.33× |

## Qué queda respaldado, qué no

**Respaldado por los datos tal cual:** los cuatro conteos por categoría y los dos agregados. Y un hecho aritmético central: Beta gana en el agregado (73% vs 27%) mientras *pierde* en ambas categorías (80 vs 90 en fáciles, 10 vs 20 en difíciles). Es una inversión de Simpson, y su causa es identificable con los datos: las muestras tienen mezclas opuestas (Alfa 90% difíciles, Beta 90% fáciles). El agregado mide sobre todo la dificultad de la cola asignada, no la capacidad del sistema.

**Depende del supuesto de transporte (no demostrado):** todo lo proyectado. Si las tasas y los tiempos por categoría se transportan a una cola 10/90, Alfa termina en 27% y Beta en 17%, y el tiempo medio por tarea finalizada pasa a favorecer a Alfa (20.95 vs 27.92 min). Bajo ese supuesto, la ventaja de Beta en tiempo observado (14.48 min) se invierte por completo: procede íntegramente de haber recibido tareas fáciles.

**No identificable causalmente:** ninguna afirmación de superioridad causal. Las muestras no están aleatorizadas, no están emparejadas y contienen tareas distintas. Dificultad, tipo de tarea y sistema están confundidos; no se puede separar el efecto del sistema del efecto de la cola. Tampoco es identificable la calidad relativa dentro de una misma tarea, ni si "difícil" significa lo mismo en ambas muestras.

**Errores concretos del borrador:** "sube del 27% al 73%" compara mezclas distintas, no sistemas; "triplica la capacidad" es 2.70×, y bajo la cola de producción es Alfa quien rinde 1.33× más tareas finalizadas por hora; "8 en vez de 10 minutos" compara solo los éxitos e ignora que cada fallo Beta cuesta 32 minutos frente a 25 de Alfa; "hemos demostrado que es causalmente superior" no se sostiene con un diseño no aleatorizado; y ocultar la mezcla y los fallos elimina justo la información que invierte la conclusión.

**Comparación mínima que resolvería la decisión:** ejecutar ambos sistemas sobre el *mismo* conjunto de tareas extraídas de la cola real de producción (diseño emparejado), o asignación aleatoria estratificada por dificultad con la etiqueta de dificultad fijada antes de ver los resultados. Métrica primaria: minutos totales hasta tarea finalizada, incluidos los 20 de reparación, reportada por estrato y agregada con los pesos reales 10/90.

## Párrafo sustitutivo

En las muestras observadas Beta alcanza 73% de éxito y Alfa 27%, pero esa comparación no es interpretable: las dos muestras tienen mezclas de dificultad opuestas (Beta recibió 90% de tareas fáciles; Alfa, 90% de difíciles). Desagregando, Alfa supera a Beta en ambas categorías: 90% frente a 80% en fáciles y 20% frente a 10% en difíciles, +10 puntos en cada una. Aplicando provisionalmente esas tasas a la cola prevista (10% fácil, 90% difícil) —un supuesto de transporte que no hemos validado—, Alfa proyecta 27% y Beta 17%, y el coste medio por tarea finalizada, incluyendo los 20 minutos de reparación manual de cada fallo, sería de 20.95 minutos con Alfa frente a 27.92 con Beta, un 33% más. La ventaja de tiempo que Beta muestra hoy (14.48 vs 20.95 minutos) se explica por haber trabajado sobre tareas fáciles. Como el diseño no está aleatorizado ni emparejado y las tareas difieren, no podemos atribuir causalmente ninguna diferencia al sistema. No procede sustituir Alfa con esta evidencia; la decisión requiere una prueba emparejada o aleatorizada estratificada por dificultad sobre la cola real, midiendo tiempo total hasta la tarea finalizada.