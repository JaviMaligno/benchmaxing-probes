## Planteamiento

El signo de $\sin(3\cdot 2^n)$ depende de en qué mitad del círculo cae $3\cdot 2^n \pmod{2\pi}$:
- $\operatorname{sgn}(\sin x) = +1$ si $x \bmod 2\pi \in (0,\pi)$,
- $\operatorname{sgn}(\sin x) = -1$ si $x \bmod 2\pi \in (\pi, 2\pi)$.

Definamos $\theta = \dfrac{3}{2\pi} \approx 0{,}4774648\ldots$, de modo que $3\cdot 2^n = 2\pi \cdot 2^n\theta$. Entonces

$$\operatorname{sgn}(\sin(3\cdot 2^n)) = \begin{cases} +1 & \text{si } \{2^n\theta\} < \tfrac12,\\ -1 & \text{si } \{2^n\theta\} > \tfrac12,\end{cases}$$

donde $\{\cdot\}$ denota la parte fraccionaria. Como $\pi$ es irracional, $2^n\theta$ nunca es exactamente un múltiplo entero ni semientero, así que el signo nunca es $0$.

## Conexión con los dígitos binarios

Escribamos la expansión binaria $\theta = 0.b_1 b_2 b_3\ldots$ (válida pues $0<\theta<1$). Entonces $\{2^n\theta\} = 0.b_{n+1}b_{n+2}\ldots$, y la condición $\{2^n\theta\} < \tfrac12$ equivale a $b_{n+1} = 0$. Por lo tanto:

$$\operatorname{sgn}(\sin(3\cdot 2^n)) = 1 - 2b_{n+1}.$$

## Suma de la serie

$$S = \sum_{n=1}^{\infty} \frac{1-2b_{n+1}}{2^n} = \sum_{n=1}^{\infty}\frac{1}{2^n} - 2\sum_{n=1}^{\infty}\frac{b_{n+1}}{2^n} = 1 - 4\sum_{m=2}^{\infty}\frac{b_m}{2^m}.$$

Pero $\displaystyle\sum_{m=1}^{\infty}\frac{b_m}{2^m} = \theta$, y como $\theta \approx 0{,}477 < \tfrac12$, se tiene $b_1 = 0$. Entonces $\sum_{m\ge 2} b_m/2^m = \theta$, y

$$S = 1 - 4\theta = 1 - 4\cdot\frac{3}{2\pi} = 1 - \frac{6}{\pi}.$$

## Verificación numérica

Los primeros términos: $\sin(6)<0$, $\sin(12)<0$, $\sin(24)<0$, $\sin(48)<0$, $\sin(96)>0$, lo que da la suma parcial $-\tfrac12-\tfrac14-\tfrac18-\tfrac1{16}+\tfrac1{32} = -0{,}90625$, consistente con $1 - 6/\pi \approx -0{,}90986$.

$$\boxed{1 - \dfrac{6}{\pi}}$$