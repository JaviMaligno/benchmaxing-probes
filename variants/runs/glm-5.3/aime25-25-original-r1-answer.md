## Planteamiento

La condición «que ninguna persona tenga dos vecinos» equivale a que **no haya tres sillas consecutivas ocupadas** (la del centro tendría dos personas al lado). Así, $N$ es el número de cadenas binarias de longitud 16 con exactamente 8 sillas ocupadas y sin tres ocupadas seguidas.

## Método de los huecos

Colocamos las 8 sillas vacías; éstas crean **9 huecos** (extremos + espacios entre ceros). Repartimos los 8 ocupados en esos huecos, con **a lo más 2 por hueco**:

$$x_1+x_2+\cdots+x_9=8,\qquad 0\le x_i\le 2$$

Por inclusión-exclusión (coeficiente de $x^8$ en $(1+x+x^2)^9=\left(\frac{1-x^3}{1-x}\right)^9$):

$$N=\binom{16}{8}-9\binom{13}{8}+\binom{9}{2}\binom{10}{8}=12870-11583+1620=2907$$

(Se resta el exceso si un hueco lleva $\ge 3$ y se corrige el doble conteo si dos huecos llevan $\ge 3$; tres huecos necesitarían 9 ocupados, imposible.)

## Verificación alternativa

Agrupando los unos en $k$ bloques de tamaño 1 o 2 (composición de 8 con partes $\le 2$, hay $\binom{k}{8-k}$ formas), y repartiendo los ceros restantes con al menos uno entre bloques:

$$\sum_{k=4}^{8}\binom{k}{8-k}\binom{9}{k}=126+1260+1260+252+9=2907\;\checkmark$$

## Resultado

$$N\bmod 1000 = 2907 \bmod 1000$$

\boxed{907}