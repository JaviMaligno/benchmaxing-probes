## Razonamiento

**Estructura de la partición.** Un 8960-ágono regular es un zonógono: sus 8960 lados vienen en 4480 pares de lados opuestos paralelos, dando 4480 direcciones distintas, que forman ángulos $k\pi/4480$ con $k = 0, 1, \dots, 4479$.

Un lema clásico sobre particiones de polígonos centralmente simétricos en paralelogramos dice lo siguiente: en cualquier partición de este tipo, los lados de cada paralelogramo son paralelos a lados del polígono. La idea es seguir "cadenas" (trenes) de paralelogramos: partiendo de un lado del polígono, cada paralelogramo que lo toca tiene un lado opuesto paralelo, y la cadena de lados paralelos debe atravesar el polígono hasta salir por el lado opuesto. 

**Cada par de direcciones perpendiculares fuerza un rectángulo.** Tomemos dos direcciones de lados del polígono, $d_1$ y $d_2$. La cadena de paralelogramos que une los dos lados del polígono con dirección $d_1$ debe cruzar la cadena que une los dos lados con dirección $d_2$ (ambas cadenas atraviesan el polígono y, por la geometría de las direcciones, se intersecan). El paralelogramo donde se cruzan tiene lados en las direcciones $d_1$ y $d_2$ simultáneamente.

En particular, si $d_1 \perp d_2$, ese paralelogramo es un **rectángulo**.

**Conteo de pares perpendiculares.** Como $4480$ es par, la dirección $k\pi/4480$ es perpendicular a la dirección $(k + 2240)\pi/4480$. Esto empareja las 4480 direcciones en exactamente
$$\frac{4480}{2} = 2240$$
pares perpendiculares, y cada par obliga a que exista al menos un rectángulo distinto (rectángulos con pares de direcciones diferentes son necesariamente distintos). Por tanto $R \ge 2240$.

**La cota se alcanza.** La partición estándar de un zonógono (construcción inductiva: se añade una "franja" de paralelogramos por cada nueva dirección) produce exactamente un paralelogramo por cada par de direcciones, es decir, exactamente un rectángulo por cada uno de los 2240 pares perpendiculares. Así $R = 2240$ es alcanzable.

$$\boxed{2240}$$