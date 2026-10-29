## Planteamiento

Coloco el cuadrado con $P=(0,s)$, $Q=(s,s)$, $R=(s,0)$, $S=(0,0)$, de modo que $M=\left(\tfrac{s}{2},s\right)$ es el punto medio de $\overline{PQ}$.

Sea $(a,b)$ un vector normal unitario a $m$, con $a^2+b^2=1$. La recta es
$$a\left(x-\tfrac{s}{2}\right)+b(y-s)=0.$$

**Distancia desde $P=(0,s)$:** $\left|-\tfrac{as}{2}\right|=5 \Rightarrow \tfrac{as}{2}=5$ (tomando el signo adecuado), es decir $a=\tfrac{10}{s}$.

**Distancia desde $R=(s,0)$:** $\left|\tfrac{as}{2}-bs\right|=|5-bs|=8$, lo que da $bs=-3$ o $bs=13$.

## Los dos casos

**Caso $bs=-3$:** $a^2+b^2=\dfrac{100+9}{s^2}=1 \Rightarrow s^2=109$. La recta es $10x-3y-2s=0$; en $x=s$ se obtiene $y=\tfrac{8s}{3}>s$, así que $m$ **no** corta al segmento $\overline{QR}$. Se descarta.

**Caso $bs=13$:** $a^2+b^2=\dfrac{100+169}{s^2}=1 \Rightarrow s^2=269$. La recta es $10x+13y=18s$; en $x=s$ se obtiene $y=\tfrac{8s}{13}\in[0,s]$, de modo que sí corta a $\overline{QR}$. Válido.

El área del cuadrado es $s^2=269$.

\boxed{269}