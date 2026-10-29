Para hallar la distancia desde el centro de la caja rectangular hasta el plano $\mathcal{Q}$, situemos la caja en el espacio tridimensional como $[0, A] \times [0, B] \times [0, C]$, cuyo centro es el punto $M = \left(\frac{A}{2}, \frac{B}{2}, \frac{C}{2}\right)$.

### Paso 1: Ecuación del plano y vértices del hexágono
Como la sección transversal es un hexágono, el plano $\mathcal{Q}$ corta las $6$ caras de la caja. Escogiendo la orientación de los ejes adecuadamente, podemos escribir la ecuación normalizada del plano $\mathcal{Q}$ como:
$$ux + vy + wz = d$$
donde $u, v, w > 0$ y $u^2 + v^2 + w^2 = 1$.

La distancia $D$ desde el centro de la caja $M$ hasta el plano $\mathcal{Q}$ está dada por:
$$D = \left| d - \frac{uA + vB + wC}{2} \right|$$

Para que el plano corte las $6$ caras formando un hexágono, debe separar los cuatro vértices $(0,0,0), (A,0,0), (0,B,0), (0,0,C)$ de los otros cuatro vértices $(A,B,0), (A,0,C), (0,B,C), (A,B,C)$. Es decir, $uA, vB, wC < d$ mientras que $uA+vB, vB+wC, wC+uA > d$.

Los $6$ vértices del hexágono se encuentran sobre las $6$ aristas que conectan ambos conjuntos de vértices. Recorriendo el perímetro del hexágono en orden:
1. $V_1 = \left(A, 0, \frac{d-uA}{w}\right)$
2. $V_2 = \left(A, \frac{d-uA}{v}, 0\right)$
3. $V_3 = \left(\frac{d-vB}{u}, B, 0\right)$
4. $V_4 = \left(0, B, \frac{d-vB}{w}\right)$
5. $V_5 = \left(0, \frac{d-wC}{v}, C\right)$
6. $V_6 = \left(\frac{d-wC}{u}, 0, C\right)$

---

### Paso 2: Longitudes de los lados del hexágono
Calculando las longitudes de los segmentos consecutivos sobre cada una de las $6$ caras de la caja:
- En la cara $x = A$:
  $$s_1 = |V_1 V_2| = (d - uA)\sqrt{\frac{1}{v^2} + \frac{1}{w^2}} = 44$$
- En la cara $z = 0$:
  $$s_2 = |V_2 V_3| = (uA + vB - d)\sqrt{\frac{1}{u^2} + \frac{1}{v^2}} = 60$$
- En la cara $y = B$:
  $$s_3 = |V_3 V_4| = (d - vB)\sqrt{\frac{1}{u^2} + \frac{1}{w^2}} = 54$$
- En la cara $x = 0$:
  $$s_4 = |V_4 V_5| = (vB + wC - d)\sqrt{\frac{1}{v^2} + \frac{1}{w^2}} = 52$$
- En la cara $z = C$:
  $$s_5 = |V_5 V_6| = (d - wC)\sqrt{\frac{1}{u^2} + \frac{1}{v^2}} = 50$$
- En la cara $y = 0$:
  $$s_6 = |V_6 V_1| = (uA + wC - d)\sqrt{\frac{1}{u^2} + \frac{1}{w^2}} = 66$$

---

### Paso 3: Diferencias entre lados opuestos
Observemos las diferencias entre cada par de lados opuestos (paralelos) del hexágono:
$$\begin{aligned}
|s_1 - s_4| &= |2d - (uA + vB + wC)|\sqrt{\frac{1}{v^2} + \frac{1}{w^2}} = 2D\sqrt{\frac{1}{v^2} + \frac{1}{w^2}} = |44 - 52| = 8 \\
|s_2 - s_5| &= |2d - (uA + vB + wC)|\sqrt{\frac{1}{u^2} + \frac{1}{v^2}} = 2D\sqrt{\frac{1}{u^2} + \frac{1}{v^2}} = |60 - 50| = 10 \\
|s_3 - s_6| &= |2d - (uA + vB + wC)|\sqrt{\frac{1}{u^2} + \frac{1}{w^2}} = 2D\sqrt{\frac{1}{u^2} + \frac{1}{w^2}} = |54 - 66| = 12
\end{aligned}$$

Dividiendo entre $2$ y elevando al cuadrado cada ecuación, obtenemos:
$$\begin{aligned}
D^2\left(\frac{1}{v^2} + \frac{1}{w^2}\right) &= 16 \\
D^2\left(\frac{1}{u^2} + \frac{1}{v^2}\right) &= 25 \\
D^2\left(\frac{1}{u^2} + \frac{1}{w^2}\right) &= 36
\end{aligned}$$

---

### Paso 4: Resolución para $D$
Definamos $x = \frac{D^2}{u^2}$, $y = \frac{D^2}{v^2}$ y $z = \frac{D^2}{w^2}$. El sistema anterior se convierte en:
$$\begin{aligned}
y + z &= 16 \\
x + y &= 25 \\
x + z &= 36
\end{aligned}$$

Sumando las tres ecuaciones y dividiendo entre $2$:
$$x + y + z = \frac{16 + 25 + 36}{2} = \frac{77}{2}$$

Restando cada ecuación de esta suma total:
$$\begin{aligned}
x &= \frac{77}{2} - 16 = \frac{45}{2} \\
y &= \frac{77}{2} - 36 = \frac{5}{2} \\
z &= \frac{77}{2} - 25 = \frac{27}{2}
\end{aligned}$$

Como $u^2 + v^2 + w^2 = 1$, se cumple que $\frac{D^2}{x} + \frac{D^2}{y} + \frac{D^2}{z} = 1$, por lo que:
$$\frac{1}{D^2} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z} = \frac{2}{45} + \frac{2}{5} + \frac{2}{27}$$

Buscando el mínimo común múltiplo de los denominadores ($\text{mcm}(45, 5, 27) = 135$):
$$\frac{1}{D^2} = \frac{6 + 54 + 10}{135} = \frac{70}{135} = \frac{14}{27}$$

Por lo tanto:
$$D^2 = \frac{27}{14} \implies D = \sqrt{\frac{27}{14}} = \frac{3\sqrt{42}}{14}$$

\boxed{\frac{3\sqrt{42}}{14}}