## Planteamiento

Coloco coordenadas: $A=(0,0)$, $B=(s,0)$, $C=(s,s)$, $D=(0,s)$, con $s$ el lado. El punto medio de $\overline{AB}$ es $M=(s/2,0)$.

Sea $\ell$ con vector normal unitario $(\cos\theta,\sin\theta)$ pasando por $M$:
$$\ell:\quad \cos\theta\,(x-\tfrac{s}{2})+\sin\theta\,y=0.$$

## Distancias

- Desde $A=(0,0)$: $\left|-\tfrac{s}{2}\cos\theta\right| = 4$, así que tomando $\cos\theta>0$: $s\cos\theta = 8$.
- Desde $C=(s,s)$: $\left|\tfrac{s}{2}\cos\theta + s\sin\theta\right| = |4 + s\sin\theta| = 7$.

Esto da $s\sin\theta = 3$ o $s\sin\theta = -11$.

## Elección del caso correcto

Como $\ell$ corta a $\overline{BC}$, recorta el triángulo de vértice $B$, de modo que $A$ y $C$ quedan del **mismo lado** de $\ell$.

- Con $s\sin\theta=3$: la recta es $8x+3y=4s$; en $x=s$ se obtiene $y=-\tfrac{4s}{3}<0$, fuera de $\overline{BC}$. Se descarta (corta a $\overline{CD}$).
- Con $s\sin\theta=-11$: la recta es $8x-11y=4s$; en $x=s$ queda $y=\tfrac{4s}{11}\in(0,s)$, efectivamente sobre $\overline{BC}$. Además $A$ y $C$ dan valores $-4s$ y $-7s$, ambos negativos: mismo lado, con distancias $4$ y $7$. ✓

## Área

$$s^2 = (s\cos\theta)^2+(s\sin\theta)^2 = 8^2 + 11^2 = 64+121 = 185.$$

\boxed{185}