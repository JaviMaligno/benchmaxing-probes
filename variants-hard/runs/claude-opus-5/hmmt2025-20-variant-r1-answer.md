Voy a razonar el problema y luego verificarlo con una simulación.

**Reducción.** Cada serpiente desliza sus dos extremos en el mismo paso $X_i=\pm1$. Si $g_i$ es el número de arcos vacíos entre la serpiente $i$ y la siguiente, entonces
$$g_i \mapsto g_i + (X_{i+1}-X_i),$$
así que cada hueco cambia en $\pm2$ con probabilidad $1/4$ cada uno y en $0$ con probabilidad $1/2$. La suma $\sum g_i = 36-12 = 24$ es invariante, y dos serpientes se fusionan exactamente cuando su hueco llega a $0$ (nunca lo cruza, porque los huecos empiezan en $2$ y cambian de dos en dos). Con $m_i = g_i/2$: hay $12$ huecos con $m_i=1$, $\sum m_i = 12$, y cada $m_i$ es un paseo perezoso ($\pm1$ con prob. $1/4$, quieto con $1/2$). Al fusionarse, el hueco desaparece y los vecinos mantienen la misma dinámica marginal.

**Martingala.** Busco $F=\sum_i h(m_i)$ con $h(0)=0$ y
$$\tfrac14\big(h(m+1)+h(m-1)-2h(m)\big) = -\tfrac{m}{12},$$
de modo que $\mathbb E[\Delta F] = -\frac{1}{12}\sum m_i = -1$ en todo estado no absorbido. Entonces $\mathbb E[T] = F_0 - \mathbb E[F_T] = 12h(1) - h(12)$ (invariante al sumar $Bm$, única ambigüedad).

Con $\Delta^2 h(m) = -m/3$, $h(0)=h(1)=0$: las diferencias $d(m)=h(m)-h(m-1)$ cumplen $d(m) = -\frac{m(m-1)}{6}$, luego
$$h(12) = -\tfrac16\sum_{m=1}^{12} m(m-1) = -\tfrac{572}{6} = -\tfrac{286}{3},\qquad \mathbb E[T] = \tfrac{286}{3}.$$

En general, con $3k$ arcos y $k$ serpientes sale $\mathbb E[T] = \frac{2(k^2-1)}{3}$ (para $k=15$ da $448/3$, el valor conocido de esa versión; para $k=2$ da $2$, comprobable a mano).

Verifico con simulación de ambos modelos (huecos y arcos):