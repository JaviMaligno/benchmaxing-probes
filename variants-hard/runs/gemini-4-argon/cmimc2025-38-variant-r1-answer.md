Para determinar la longitud total de las curvas que conforman el conjunto $S$, analizamos las condiciones bajo las cuales las cuatro raíces de la ecuación dada son concíclicas.

### Paso 1: Encontrar las raíces y la ecuación general de la circunferencia
Las cuatro raíces provienen de los dos factores cuadráticos:
1. Para $x^2 + 4x + 5 = 0$, las raíces son:
   $$z_1 = -2 + i, \quad z_2 = -2 - i$$
2. Para $x^2 - 2mx + 25 = 0$, sean $z_3$ y $z_4$ sus raíces. Por las relaciones de Vieta, cumplen:
   $$z_3 + z_4 = 2m \quad \text{y} \quad z_3 z_4 = 25$$

Dado que $z_1$ y $z_2$ son complejos conjugados, la mediatriz del segmento que los une es el eje real. Por lo tanto, cualquier circunferencia $C_c$ que pase por $z_1$ y $z_2$ debe tener su centro $c$ en el eje real ($c \in \mathbb{R}$).

El radio $R$ de dicha circunferencia cumple:
$$R^2 = |z_1 - c|^2 = (-2 - c)^2 + 1^2 = c^2 + 4c + 5$$
La ecuación de la circunferencia $C_c$ para cualquier punto $z \in \mathbb{C}$ es $|z - c|^2 = R^2$, que al desarrollarse se escribe como:
$$|z|^2 - c(z + \bar{z}) - (4c + 5) = 0$$

### Paso 2: Imponer la condición de conciclicidad para $z_3$ y $z_4$
Para que las cuatro raíces sean concíclicas, debe existir algún $c \in \mathbb{R}$ tal que tanto $z_3$ como $z_4$ satisfagan la ecuación de $C_c$:
$$|z_3|^2 - c(z_3 + \bar{z}_3) - (4c + 5) = 0 \quad (1)$$
$$|z_4|^2 - c(z_4 + \bar{z}_4) - (4c + 5) = 0 \quad (2)$$

Como $z_4 = \frac{25}{z_3}$, sustituimos esto en la ecuación $(2)$ y multiplicamos por $|z_3|^2$:
$$625 - 25c(z_3 + \bar{z}_3) - (4c + 5)|z_3|^2 = 0 \quad (3)$$

De la ecuación $(1)$, despejamos $c(z_3 + \bar{z}_3) = |z_3|^2 - (4c + 5)$ y lo sustituimos en $(3)$:
$$625 - 25\left(|z_3|^2 - (4c + 5)\right) - (4c + 5)|z_3|^2 = 0$$
Agrupando términos:
$$25(30 + 4c) - (30 + 4c)|z_3|^2 = 0 \implies (4c + 30)\left(25 - |z_3|^2\right) = 0$$

Esto divide el problema en dos casos posibles.

---

### Caso 1: $|z_3|^2 = 25$
Si $|z_3| = 5$, como $z_3 z_4 = 25 = |z_3|^2 = z_3 \bar{z}_3$, se deduce que $z_4 = \bar{z}_3$.
Podemos escribir $z_3 = 5e^{i\theta}$ y $z_4 = 5e^{-i\theta}$ para $\theta \in [0, \pi]$. Entonces:
$$m = \frac{z_3 + z_4}{2} = 5\cos\theta \in [-5, 5]$$
Sustituyendo $|z_3|^2 = 25$ y $z_3 + \bar{z}_3 = 2m$ en $(1)$, obtenemos:
$$25 - 2cm - 4c - 5 = 0 \implies c(m + 2) = 10$$
Para todo $m \in [-5, 5]$ con $m \neq -2$ (en $m = -2$ las cuatro raíces son colineales en la recta $\text{Re}(z) = -2$), existe un único $c = \frac{10}{m+2} \in \mathbb{R}$.

Así, este caso aporta el segmento de recta $[-5, 5]$ (salvo un punto), cuya longitud es:
$$L_1 = 5 - (-5) = 10$$

---

### Caso 2: $4c + 30 = 0 \implies c = -\frac{15}{2}$
Para $c = -\frac{15}{2}$, la ecuación de la circunferencia $C_{-15/2}$ es:
$$|z|^2 + \frac{15}{2}(z + \bar{z}) + 25 = 0$$
Observamos que si $z_3 \in C_{-15/2}$, entonces $z_4 = \frac{25}{z_3}$ satisface automáticamente la ecuación de la misma circunferencia. Sea $r^2 = |z_3|^2$ y $s = z_3 + \bar{z}_3$. De la ecuación de la circunferencia tenemos:
$$s = -\frac{2}{15}(r^2 + 25)$$

Expresamos $\text{Re}(m)$ y $|m|^2$ para $2m = z_3 + \frac{25}{z_3}$ en función de $r$ y $s$:
1. Para la parte real:
   $$4\text{Re}(m) = 2m + 2\bar{m} = (z_3 + \bar{z}_3) + 25\frac{z_3 + \bar{z}_3}{|z_3|^2} = s\left(\frac{r^2 + 25}{r^2}\right) = -\frac{2}{15}\frac{(r^2 + 25)^2}{r^2}$$
   De aquí obtenemos:
   $$\frac{(r^2 + 25)^2}{r^2} = -30\text{Re}(m)$$

2. Para el módulo al cuadrado:
   $$4|m|^2 = \left(z_3 + \frac{25}{z_3}\right)\left(\bar{z}_3 + \frac{25}{\bar{z}_3}\right) = r^2 + \frac{625}{r^2} + 25\frac{s^2 - 2r^2}{r^2} = \frac{(r^2 - 25)^2 + 25s^2}{r^2}$$
   Usando que $(r^2 - 25)^2 = (r^2 + 25)^2 - 100r^2$ y $s^2 = \frac{4}{225}(r^2 + 25)^2$:
   $$4|m|^2 = \left(1 + \frac{4}{9}\right)\frac{(r^2 + 25)^2}{r^2} - 100 = \frac{13}{9}\frac{(r^2 + 25)^2}{r^2} - 100$$

Sustituyendo $\frac{(r^2 + 25)^2}{r^2} = -30\text{Re}(m)$ en la ecuación anterior:
$$4|m|^2 = \frac{13}{9}(-30\text{Re}(m)) - 100 = -\frac{130}{3}\text{Re}(m) - 100$$
Dividiendo entre $4$ y completando el cuadrado:
$$|m|^2 + \frac{65}{6}\text{Re}(m) + 25 = 0 \implies \left|m + \frac{65}{12}\right|^2 = \left(\frac{65}{12}\right)^2 - 25 = \frac{625}{144} = \left(\frac{25}{12}\right)^2$$

A medida que $z_3$ recorre toda la circunferencia $C_{-15/2}$ (donde $r \in \left[\frac{15 - 5\sqrt{5}}{2}, \frac{15 + 5\sqrt{5}}{2}\right]$), $\text{Re}(m)$ varía entre $-\frac{15}{2}$ y $-\frac{10}{3}$, cubriendo la totalidad de la circunferencia de centro $-\frac{65}{12}$ y radio $R_m = \frac{25}{12}$.

La longitud de esta circunferencia es:
$$L_2 = 2\pi R_m = 2\pi \left(\frac{25}{12}\right) = \frac{25\pi}{6}$$

---

### Conclusión
Sumando las longitudes de ambas curvas que conforman $S$:
$$L_{\text{total}} = L_1 + L_2 = 10 + \frac{25\pi}{6}$$

\boxed{10 + \frac{25\pi}{6}}