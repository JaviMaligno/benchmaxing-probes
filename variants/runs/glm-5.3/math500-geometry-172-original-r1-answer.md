**Paso 1: Configurar coordenadas.**

Tomemos un triángulo de referencia con $A=(0,0)$, $B=(1,0)$, $C=(0,1)$, cuyo área es $\frac{1}{2}$. El resultado escalará proporcionalmente al triángulo real.

**Paso 2: Hallar el centroide y la línea paralela a $BC$.**

El centroide es:
$$G = \left(\frac{1}{3}, \frac{1}{3}\right).$$

La recta $BC$ tiene ecuación $x + y = 1$, así que la recta por $G$ paralela a $BC$ es $x + y = \frac{2}{3}$.

**Paso 3: Hallar $M$, $N$ y $E$.**

- Intersección con $AB$ (donde $y=0$): $M = \left(\frac{2}{3}, 0\right)$.
- Intersección con $AC$ (donde $x=0$): $N = \left(0, \frac{2}{3}\right)$.
- $E$ es el punto medio de $AC$ (punto de la mediana $BE$): $E = \left(0, \frac{1}{2}\right)$.

**Paso 4: Área del triángulo $ENG$.**

$$[ENG] = \frac{1}{2}\left| \det\begin{pmatrix} N-E \\ G-E \end{pmatrix} \right| = \frac{1}{2}\left| \det\begin{pmatrix} 0 & \tfrac{1}{6} \\ \tfrac{1}{3} & -\tfrac{1}{6} \end{pmatrix} \right| = \frac{1}{2}\left| 0 - \frac{1}{18} \right| = \frac{1}{36}.$$

**Paso 5: Escalar al triángulo real.**

Como el triángulo de referencia tiene área $\frac{1}{2}$, la razón de áreas es:
$$\frac{[ENG]}{[ABC]} = \frac{1/36}{1/2} = \frac{1}{18}.$$

Con $[ABC] = 144$:
$$[ENG] = \frac{144}{18} = 8.$$

$$\boxed{8}$$