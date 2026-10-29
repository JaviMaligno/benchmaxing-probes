Para resolver este problema paso a paso, podemos analizar las posiciones en la cuadrícula de $3 \times 3$:

1. **Total de configuraciones posibles:**
   La cuadrícula de $3 \times 3$ tiene un total de $9$ nenúfares. Como el nenúfar de la esquina inferior izquierda (inicio) y el de la esquina superior derecha (casa) deben permanecer, tenemos $9 - 2 = 7$ nenúfares restantes.
   Debemos eliminar $4$ de estos $7$ nenúfares (lo cual equivale a **conservar $3$ nenúfares** intermedios). El número total de formas de elegir cuáles $4$ eliminar es:
   $$\binom{7}{4} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = 35$$

2. **Caminos posibles hacia casa:**
   Si nombramos las coordenadas desde $(0,0)$ (abajo a la izquierda) hasta $(2,2)$ (arriba a la derecha), la distancia mínima (distancia de Manhattan) entre el inicio y la casa es de $(2 - 0) + (2 - 0) = 4$ saltos.
   
   Cualquier camino de $4$ saltos requiere pasar por exactamente $3$ nenúfares intermedios. Como al eliminar $4$ nenúfares solo quedan exactamente $3$ nenúfares intermedios en toda la cuadrícula, la única forma en que Kevin pueda llegar a casa es que los $3$ nenúfares que quedan formen uno de estos caminos más cortos de longitud $4$ (moviéndose únicamente hacia arriba y hacia la derecha).

3. **Conteo de caminos válidos:**
   Un camino más corto desde $(0,0)$ hasta $(2,2)$ consiste en $2$ saltos hacia la derecha y $2$ saltos hacia arriba en algún orden. El número de tales caminos es:
   $$\binom{4}{2} = 6$$
   Cada uno de estos $6$ caminos utiliza un conjunto único de $3$ nenúfares intermedios.

4. **Formas en las que no puede llegar a casa:**
   Restamos las configuraciones en las que sí existe un camino del total de configuraciones posibles:
   $$35 - 6 = 29$$

\boxed{29}