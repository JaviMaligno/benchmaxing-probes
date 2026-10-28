

## Tabla numérica

| Métrica | Alfa | Beta | Diferencia |
|---|---|---|---|
| **Muestra observada** | | | |
| Éxito fácil | 90/100 = 90 % | 720/900 = 80 % | Alfa +10 pp |
| Éxito difícil | 180/900 = 20 % | 10/100 = 10 % | Alfa +10 pp |
| Éxito agregado | 270/1000 = 27 % | 730/1000 = 73 % | Beta +46 pp |
| Min/tarea (éxito 10/8; fallo 25/32) | 20,95 | 14,48 | Beta −6,47 min |
| **Proyección (10 % fácil, 90 % difícil)** | | | |
| Éxito proyectado | 0,1·90+0,9·20 = **27 %** | 0,1·80+0,9·10 = **17 %** | Alfa +10 pp |
| Min/tarea proyectados | 20,95 | 27,92 | Alfa −6,97 min |

Cálculo de tiempos proyectados Beta: 100 fáciles → 80×8 + 20×32 = 1 280; 900 difíciles → 90×8 + 810×32 = 26 640; total 27 920 / 1 000 = 27,92. Alfa mantiene composición idéntica a la observada (100 fáciles, 900 difíciles), por eso coincide.

---

## Párrafo sustitutivo del borrador

En las muestras observadas, el agregado favorece a Beta (73 % frente a 27 %), pero ese contraste es un artefacto de composición: la muestra de Beta contiene un 90 % de tareas fáciles y la de Alfa un 90 % de difíciles. Desglosando por categoría, Alfa supera a Beta tanto en fáciles (90 % vs 80 %) como en difíciles (20 % vs 10 %); se trata de una paradoja de Simpson. El borrador original afirma causalidad, ahorro de tiempo y suficiencia del score global; ninguna de esas tres conclusiones queda respaldada. No puede identificarse efecto causal porque las muestras no están aleatorizadas, las tareas son distintas y no hay emparejamiento: cualquier diferencia podría atribuirse a la dificultad del material, no al sistema. La superioridad agregada de Beta depende enteramente de que su muestra estuvo sesgada hacia lo fácil.

Respecto al tiempo, en la muestra observada Beta promedia 14,48 min/tarea frente a 20,95 de Alfa, pero eso refleja que Beta enfrentó pocas tareas difíciles (pocas reparaciones de 32 min). Transportando tasas a la cola real (10 % fácil, 90 % difícil), la situación se invierte: Beta promedia 27,92 min y Alfa 20,95 min, es decir, Beta costaría ≈7 min más por tarea. No obstante, esta proyección descansa en la hipótesis no demostrada de que las tasas y los tiempos por categoría se mantienen fuera de la muestra; si la distribución real de dificultad dentro de cada categoría difiere, los números cambian. Por tanto, tampoco puede afirmarse con certeza que Alfa ahorrará tiempo en producción.

Lo único que los datos permiten sostener es: (1) dentro de cada categoría observada, Alfa mostró mayor tasa de éxito; (2) el agregado observado no es comparable entre sistemas porque las mezclas de tareas son opuestas; (3) cualquier proyección a la cola futura es condicional al supuesto de transporte.

Para resolver la decisión se requiere una comparación mínima futura: asignar aleatoriamente y por pares un mismo conjunto de tareas —con la mezcla 10/90 de la cola de producción— a ambos sistemas, registrar éxitos, fallos y minutos totales (modelo + reparación) por tarea, y estimar la diferencia de medias con intervalo de confianza. Solo ese diseño eliminaría el sesgo de composición y permitiría hablar de superioridad causal y de ahorro operativo real. Hasta entonces, la sustitución de Alfa por Beta carece de fundamento suficiente.