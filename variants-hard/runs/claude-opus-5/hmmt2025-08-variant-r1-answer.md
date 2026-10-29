## Planteamiento

El signo de $\sin x$ depende solo de $x \bmod 2\pi$: es $+1$ si $x \bmod 2\pi \in (0,\pi)$ y $-1$ si está en $(\pi, 2\pi)$.

Definamos $\alpha = \dfrac{3}{2\pi} \approx 0{,}4774648\ldots$, de modo que
$$\frac{3\cdot 2^n}{2\pi} = 2^n\alpha .$$

Entonces $\sin(3\cdot 2^n) > 0 \iff \{2^n\alpha\} < \tfrac12$.

## Traducción a dígitos binarios

Sea $\alpha = 0{,}b_1b_2b_3\ldots$ en binario (irracional, así que no hay ambigüedad ni valores exactos $0$ o $1/2$). La parte fraccionaria $\{2^n\alpha\}$ tiene expansión $0{,}b_{n+1}b_{n+2}\ldots$, luego
$$\{2^n\alpha\} < \tfrac12 \iff b_{n+1} = 0 .$$

Por tanto
$$\operatorname{sgn}\big(\sin(3\cdot 2^n)\big) = 1 - 2b_{n+1}.$$

## Suma

$$S = \sum_{n=1}^{\infty}\frac{1-2b_{n+1}}{2^n} = \underbrace{\sum_{n=1}^\infty \frac{1}{2^n}}_{=1} - 2\sum_{n=1}^{\infty}\frac{b_{n+1}}{2^n}.$$

Y la última suma se reindexa:
$$\sum_{n=1}^{\infty}\frac{b_{n+1}}{2^n} = 2\sum_{m=2}^{\infty}\frac{b_m}{2^m} = 2\left(\alpha - \frac{b_1}{2}\right) = 2\alpha,$$
pues $b_1 = 0$ (ya que $\alpha < 1/2$). Así $\sum_{n\ge1} b_{n+1}2^{-n} = 2\alpha = \dfrac{3}{\pi}$, y

$$S = 1 - \frac{6}{\pi}.$$

## Verificación numérica

Los primeros ángulos: $6, 12, 24, 48$ caen en $(\pi,2\pi)\pmod{2\pi}$ (signos $-$), y $96 \equiv 1{,}752$ cae en $(0,\pi)$ (signo $+$), coincidiendo con $b_2b_3b_4b_5b_6 = 11110$. Las sumas parciales $-0{,}9375,\ -0{,}90625,\ -0{,}921875,\ldots$ tienden a $1 - 6/\pi \approx -0{,}90986$.

$$\boxed{1-\dfrac{6}{\pi}}$$