## Reducción del problema

**Paso 1: trabajar con los huecos.** Las 15 serpientes ocupan 15 arcos en total (al fusionarse las longitudes se suman), así que siempre quedan $45-15=30$ arcos vacíos. Si hay $k$ serpientes, sean $g_1,\dots,g_k$ los huecos (arcos vacíos consecutivos) entre serpientes vecinas, con $\sum g_i=30$. Inicialmente $k=15$ y $g_i=2$ para todo $i$.

**Paso 2: dinámica de un hueco.** Si la serpiente $i$ se desplaza $s_i\in\{-1,+1\}$, entonces $g_i$ cambia en $s_{i+1}-s_i$, es decir:
$$g_i\to g_i+2,\ 0,\ -2\quad\text{con probabilidades }\tfrac14,\tfrac12,\tfrac14 .$$
Los huecos son siempre pares; poniendo $h_i=g_i/2$ queda $\sum h_i=15=:n$, con $h_i$ inicialmente iguales a $1$, y cada $h_i$ varía en $\pm1$ con probabilidad $\tfrac14$ cada uno y queda igual con probabilidad $\tfrac12$. Una fusión ocurre exactamente cuando un hueco llega a $0$ (y entonces se elimina de la lista; los huecos vecinos **no** cambian de longitud). El proceso termina cuando $k=1$, con $h_1=n=15$ congelado.

## Función potencial

Busco $F=\sum_{i\ \text{vivos}} f(h_i)$ con $f(0)=0$ (para que los huecos muertos no aporten) y $f(n)=0$ (para que $F=0$ al absorberse). Como cada incremento tiene la misma ley marginal,
$$\mathbb{E}[\Delta F]=\tfrac14\sum_i\big(f(h_i+1)+f(h_i-1)-2f(h_i)\big).$$
Para que esto valga $-1$ en **toda** configuración (sin importar $k$), basta pedir que la segunda diferencia sea lineal sin término constante:
$$f(h+1)-2f(h)+f(h-1)=-\frac{4h}{n},\qquad 1\le h\le n-1,$$
pues entonces $\mathbb{E}[\Delta F]=-\frac{1}{n}\sum_i h_i=-1$.

Como $\Delta^2(h^3)=6h$, la solución con $f(0)=f(n)=0$ es
$$f(h)=\frac{2}{3n}\,h\,(n^2-h^2).$$

Así $F_t+t$ es una martingala y, por el teorema de parada óptima (espacio de estados finito), $\mathbb{E}[T]=F(\text{inicial})$.

## Cálculo

Con $n=15$ y los $15$ huecos iniciales iguales a $1$:
$$\mathbb{E}[T]=n\cdot f(1)=n\cdot\frac{2(n^2-1)}{3n}=\frac{2(n^2-1)}{3}=\frac{2\cdot224}{3}=\frac{448}{3}.$$

Verificación en casos pequeños del mismo modelo: para $n=2$ da $2$ y para $n=3$ da $16/3$, que coinciden con el cálculo directo por enumeración.

$$\boxed{\dfrac{448}{3}}$$