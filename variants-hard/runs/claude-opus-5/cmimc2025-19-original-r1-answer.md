## Planteamiento

Sea $N_k$ el número de subconjuntos con $|S|\equiv k \pmod 5$. Por el filtro de raíces de la unidad, con $\omega=e^{2\pi i/5}$:

$$N_k=\frac15\sum_{j=0}^{4}\omega^{-jk}(1+\omega^j)^{18}$$

## Evaluación de los términos

Como $1+\omega^j = 2\cos(\pi j/5)\,e^{i\pi j/5}$, y usando $2\cos(\pi/5)=\varphi$, $2\cos(2\pi/5)=\varphi^{-1}$:

$$(1+\omega)^{18}=\varphi^{18}e^{8\pi i/5},\qquad (1+\omega^2)^{18}=\varphi^{-18}e^{6\pi i/5}$$

(los otros dos son los conjugados). Con $a=\varphi^{18}=2889+1292\sqrt5$, $b=\varphi^{-18}=2889-1292\sqrt5$:

$$N_k-\frac{2^{18}}{5}=\frac25\left[a\cos\frac{2\pi(4-k)}{5}+b\cos\frac{2\pi(3-2k)}{5}\right]$$

Usando $\cos\frac{2\pi}{5}=\frac{\sqrt5-1}{4}$, $\cos\frac{4\pi}{5}=-\frac{\sqrt5+1}{4}$, las partes irracionales se cancelan:

- $k=0$: $\tfrac25\cdot\tfrac{a(\sqrt5-1)-b(\sqrt5+1)}{4}=\tfrac25\cdot\tfrac{7142}{4}=\tfrac{3571}{5}$
- $k=3$: igual, $\tfrac{3571}{5}$
- $k=4$: $\tfrac25(a+b)=\tfrac25\cdot 5778=\tfrac{11556}{5}$
- $k=1,k=2$: $-\tfrac{9349}{5}$ cada uno (la suma de desviaciones debe ser $0$)

Comprobación: $N=(53143,\,50559,\,50559,\,53143,\,54740)$, cuya suma es $262144=2^{18}$. ✓

## Suma final

Las desviaciones positivas suman $\frac{3571+3571+11556}{5}=\frac{18698}{5}$, así que el total de valores absolutos es $\frac{37396}{5}$. Dividiendo por $2^{18}$:

$$\sum_{k=0}^{4}\left|p(k)-\frac15\right|=\frac{37396}{5\cdot 262144}=\frac{9349}{327680}\approx 0{,}02853$$

\boxed{\dfrac{9349}{327680}}