Para hallar el conjunto $U$ de todos los números complejos $m$ tales que las $4$ raíces de $(x^2+2x+5)(x^2-2mx+25)=0$ son concíclicas en el plano complejo, analizamos las raíces de cada factor cuadrático.

### Paso 1: Ecuación de las circunferencias que pasan por las dos primeras raíces
Las raíces del primer factor $x^2+2x+5=0$ son:
$$z_1 = -1 + 2i, \qquad z_2 = -1 - 2i$$
Como $z_1$ y $z_2$ son complejos conjugados ($z_2 = \bar{z}_1$), la mediatriz del segmento que une $z_1$ y $z_2$ es el eje real. Por lo tanto, cualquier circunferencia $C$ que pase por $z_1$ y $z_2$ tiene su centro en algún punto $c \in \mathbb{R}$.

El cuadrado del radio de dicha circunferencia es:
$$R^2 = |z_1 - c|^2 = (-1 - c)^2 + 2^2 = c^2 + 2c + 5$$
Así, la ecuación de la circunferencia $C$ en el plano complejo es $|z - c|^2 = c^2 + 2c + 5$, que al desarrollarse se escribe como:
$$|z|^2 - c(z + \bar{z}) = 2c + 5$$

---

### Paso 2: Condición para las otras dos raíces
Sean $z_3$ y $z_4$ las raíces de $x^2 - 2mx + 25 = 0$. Por las fórmulas de Vieta, se cumple que:
$$z_3 + z_4 = 2m \quad \text{y} \quad z_3 z_4 = 25$$

Para que $z_3$ y $z_4 = \frac{25}{z_3}$ pertenezcan a la misma circunferencia $C$, ambas deben satisfacer su ecuación:
1. $|z_3|^2 - c(z_3 + \bar{z}_3) = 2c + 5$
2. $|z_4|^2 - c(z_4 + \bar{z}_4) = 2c + 5$

Sustituyendo $z_4 = \frac{25}{z_3}$ en la segunda ecuación y multiplicando por $|z_3|^2$, obtenemos:
$$625 - 25c(z_3 + \bar{z}_3) = (2c + 5)|z_3|^2$$

De la primera ecuación tenemos que $c(z_3 + \bar{z}_3) = |z_3|^2 - (2c + 5)$. Sustituyendo esto en la ecuación anterior:
$$625 - 25\left(|z_3|^2 - (2c + 5)\right) = (2c + 5)|z_3|^2$$
Agrupando términos:
$$(25 - |z_3|^2)(25 + 2c + 5) = 0 \implies (|z_3|^2 - 25)(c + 15) = 0$$

Esto divide el problema en dos casos.

---

### Paso 3: Análisis de los dos casos

#### Caso 1: $|z_3|^2 = 25$
En este caso, $|z_3| = 5$. Como $z_3 z_4 = 25 = |z_3|^2 = z_3 \bar{z}_3$, se deduce que $z_4 = \bar{z}_3$.
Entonces:
$$m = \frac{z_3 + z_4}{2} = \frac{z_3 + \bar{z}_3}{2} = \operatorname{Re}(z_3)$$
Dado que $|z_3| = 5$, la parte real de $z_3$ puede tomar cualquier valor en el intervalo $[-5, 5]$ (para todo $m \in [-5, 5]$ con $m \neq -1$, existe $c = \frac{10}{m+1} \in \mathbb{R}$ que define la circunferencia correspondiente).

Por lo tanto, este caso describe el segmento de recta $[-5, 5]$ sobre el eje real, cuya longitud es:
$$L_1 = 5 - (-5) = 10$$

#### Caso 2: $c = -15$
Cuando $c = -15$, la ecuación de la circunferencia $C$ es:
$$|z|^2 + 15(z + \bar{z}) + 25 = 0 \iff |z + 15|^2 = 200$$
Para cualquier punto $z_3 \in C$, el punto $z_4 = \frac{25}{z_3}$ también pertenece automáticamente a $C$. Queremos determinar el lugar geométrico de $m = \frac{1}{2}\left(z_3 + \frac{25}{z_3}\right)$ cuando $z_3$ recorre $C$.

De la ecuación de $C$ sabemos que $|z_3|^2 + 25 = -15(z_3 + \bar{z}_3)$. Calculamos por un lado:
$$2m + 2\bar{m} = \left(z_3 + \frac{25}{z_3}\right) + \left(\bar{z}_3 + \frac{25}{\bar{z}_3}\right) = (z_3 + \bar{z}_3)\frac{|z_3|^2 + 25}{|z_3|^2} = -15\frac{(z_3 + \bar{z}_3)^2}{|z_3|^2}$$
Y por otro lado:
$$|2m|^2 = \left|z_3 + \frac{25}{z_3}\right|^2 = \frac{(|z_3|^2 - 25)^2 + 25(z_3 + \bar{z}_3)^2}{|z_3|^2}$$
Como $(|z_3|^2 - 25)^2 = (|z_3|^2 + 25)^2 - 100|z_3|^2 = 225(z_3 + \bar{z}_3)^2 - 100|z_3|^2$, sustituimos en $|2m|^2$:
$$4|m|^2 = 250\frac{(z_3 + \bar{z}_3)^2}{|z_3|^2} - 100$$
Eliminando $\frac{(z_3 + \bar{z}_3)^2}{|z_3|^2} = -\frac{2(m + \bar{m})}{15}$, obtenemos:
$$4|m|^2 = -\frac{500}{15}(m + \bar{m}) - 100 \implies |m|^2 + \frac{25}{3}(m + \bar{m}) + 25 = 0$$
Completando el cuadrado:
$$\left|m + \frac{25}{3}\right|^2 = \left(\frac{25}{3}\right)^2 - 25 = \frac{400}{9} = \left(\frac{20}{3}\right)^2$$
Al recorrer $z_3$ toda la circunferencia $C$, $m$ describe completamente la circunferencia de centro $-\frac{25}{3}$ y radio $r = \frac{20}{3}$. Su longitud (perímetro) es:
$$L_2 = 2\pi r = 2\pi \left(\frac{20}{3}\right) = \frac{40\pi}{3}$$

---

### Paso 4: Suma de las longitudes
Sumando las longitudes del segmento de recta y de la circunferencia obtenemos el perímetro total de $U$:
$$L = L_1 + L_2 = 10 + \frac{40\pi}{3}$$

\boxed{10 + \frac{40\pi}{3}}