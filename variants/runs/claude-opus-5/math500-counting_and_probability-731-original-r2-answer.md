## Planteamiento

Coloco el centro en el origen: los vértices son $(\pm a, \pm b)$, con $AB = 2a$, $AD = 2b$, así que $k = a/b$. Tomo $b = 1$, $a = k$.

**Condición de cercanía.** El punto $P=(x,y)$ está más cerca de $O$ que del vértice $(\pm a, \pm b)$ cuando queda del lado de $O$ respecto a la mediatriz del segmento, es decir
$$\pm ax \pm by < \frac{a^2+b^2}{2}.$$
Exigir las cuatro desigualdades a la vez equivale a tomar el caso peor:
$$a|x| + b|y| < \frac{a^2+b^2}{2} = c.$$

Por simetría basta trabajar en el primer cuadrante $[0,k]\times[0,1]$, de área $k$, con $c=\frac{k^2+1}{2}$.

## Cálculo del área (caso $k \ge 1$)

La recta $kx + y = c$ corta:
- el eje $x$ en $X = \dfrac{k^2+1}{2k} \le k$ (pues $k\ge 1$),
- la recta $y=1$ en $x = \dfrac{c-1}{k} = \dfrac{k^2-1}{2k} \ge 0$.

La región es entonces un trapecio con lados horizontales de longitudes $\frac{k^2+1}{2k}$ (en $y=0$) y $\frac{k^2-1}{2k}$ (en $y=1$), y altura $1$:
$$\text{Área} = \frac{1}{2}\left(\frac{k^2+1}{2k} + \frac{k^2-1}{2k}\right) = \frac{1}{2}\cdot\frac{2k^2}{2k} = \frac{k}{2}.$$

## Caso $k < 1$

Ahora la recta corta el eje $y$ en $\frac{k^2+1}{2}<1$ y el lado $x=k$ en $y=\frac{1-k^2}{2}\ge 0$. El trapecio tiene lados verticales $\frac{k^2+1}{2}$ y $\frac{1-k^2}{2}$, con base $k$:
$$\text{Área} = k\cdot\frac{1}{2}\left(\frac{k^2+1}{2}+\frac{1-k^2}{2}\right) = \frac{k}{2}.$$

## Probabilidad

En ambos casos el área favorable del cuadrante es $k/2$ frente al área total $k$:
$$P = \frac{k/2}{k} = \frac{1}{2},$$
independientemente de $k$. (Verificación con el cuadrado $k=1$: la región $|x|+|y|<1$ tiene área $2$ dentro de un cuadrado de área $4$.)

\boxed{\dfrac{1}{2}}