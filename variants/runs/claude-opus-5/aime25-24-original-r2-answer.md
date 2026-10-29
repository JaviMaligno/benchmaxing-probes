## Planteamiento

**Ceros de $f$.** $\sin(7\pi\sin 5x)=0 \iff 7\pi\sin(5x)=k\pi$ con $k\in\mathbb{Z}$, es decir
$$\sin(5x)=\frac{k}{7},\qquad k=-7,\dots,7.$$

Sea $u=5x$. Cuando $0<x<2\pi$, se tiene $0<u<10\pi$: exactamente **5 periodos** completos de $\sin u$ (extremos excluidos).

**Conteo por cada $k$:**

- $k=0$: $\sin u=0$ en $u=m\pi$ con $m=1,\dots,9$ (se excluyen $u=0$ y $u=10\pi$) → $9$ soluciones.
- $k=\pm1,\dots,\pm6$ (12 valores): $|k/7|<1$, así que hay $2$ soluciones por periodo → $2\cdot 5=10$ cada uno → $12\cdot 10=120$.
- $k=\pm 7$: $\sin u=1$ en $u=\tfrac{\pi}{2}+2\pi m$ ($5$ soluciones) y $\sin u=-1$ en $u=\tfrac{3\pi}{2}+2\pi m$ ($5$ soluciones) → $10$.

$$n=9+120+10=139.$$

**Tangencias.** Derivando:
$$f'(x)=35\pi\cos\big(7\pi\sin 5x\big)\cos(5x).$$
En un cero se cumple $7\pi\sin 5x=k\pi$, luego $\cos(k\pi)=\pm1\neq 0$. Por tanto $f'(x)=0$ exige $\cos(5x)=0$, o sea $\sin(5x)=\pm1$, que corresponde precisamente a $k=\pm7$.

$$t=10.$$

**Resultado:** $n+t=139+10=149$.

\boxed{149}