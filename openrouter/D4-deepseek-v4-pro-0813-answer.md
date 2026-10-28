### Cálculo

| Métrica | Alfa muestra | Beta muestra | Alfa proyección (10/90) | Beta proyección (10/90) |
|---|---:|---:|---:|---:|
| Éxito en fáciles | 90/100 = 90 % | 720/900 = 80 % | — | — |
| Éxito en difíciles | 180/900 = 20 % | 10/100 = 10 % | — | — |
| Éxito agregado / proyectado | 270/1000 = 27 % | 730/1000 = 73 % | 27 % | 17 % |
| Minutos por tarea finalizada | 20.95 | 14.48 | 20.95 | 27.92 |

**Tiempos observados:**  
Alfa: \((270×10 + 730×25)/1000 = 20.95\) min/tarea.  
Beta: \((730×8 + 270×32)/1000 = 14.48\) min/tarea.

**Tiempos proyectados a cola 10 % fácil / 90 % difícil:**  
Alfa: \(0.1×(0.9×10+0.1×25)+0.9×(0.2×10+0.8×25)=20.95\).  
Beta: \(0.1×(0.8×8+0.2×32)+0.9×(0.1×8+0.9×32)=27.92\).

**Separación entre puntos porcentuales y mejora relativa:**  
En la muestra, Beta tiene \(+46\) puntos porcentuales de éxito frente a Alfa; eso es \(+170\) % relativo. En tiempo observado, Beta reduce \(6.47\) min/tarea, una mejora relativa del \(30.9\) %.  
En la proyección a producción, Beta tendría \(−10\) puntos porcentuales de éxito, una caída relativa del \(37\) %. En tiempo proyectado, Beta empeora \(6.97\) min/tarea, \(+33.3\) % relativo.

### Conclusiones

Las muestras no permiten identificar causalidad: son no aleatorizadas, de tareas distintas y sin emparejar. La ventaja agregada observada de Beta proviene de su mezcla muestral: Beta fue evaluado con 90 % de tareas fáciles; Alfa, con 90 % difíciles. Por categoría, Alfa gana en fáciles y difíciles. Las proyecciones dependen de transportar tasas y tiempos a la cola futura, hipótesis no demostrada.

### Párrafo que reemplaza el borrador

No hay evidencia causal de que Beta sea superior. La subida aparente del 27 % al 73 % es resultado de comparar muestras con mezclas muy distintas: Beta se probó sobre todo en tareas fáciles y Alfa sobre todo en difíciles. Por categoría, Alfa supera a Beta. Aplicando la mezcla real de producción, 10 % fácil y 90 % difícil, Alfa mantendría 27 % de éxito y 20.95 min/tarea, mientras Beta bajaría a 17 % y 27.92 min/tarea. Antes de sustituir, conviene una comparación aleatorizada o emparejada con la misma mezcla 10/90, mismas tareas y medición de éxito y tiempo total con reparaciones.