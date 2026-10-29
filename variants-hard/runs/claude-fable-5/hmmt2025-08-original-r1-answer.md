## Resolución

**Paso 1: Reformular el signo.** Se tiene $\sin(2^n) > 0$ si y solo si $2^n \bmod 2\pi \in (0, \pi)$, es decir, si y solo si la parte fraccionaria de $\dfrac{2^n}{2\pi} = \dfrac{2^{n-1}}{\pi}$ es menor que $\tfrac{1}{2}$.

**Paso 2: Conectar con la expansión binaria de $1/\pi$.** Sea $\alpha = \dfrac{1}{\pi} = 0.b_1 b_2 b_3 \ldots$ en binario (como $\pi$ es irracional, la expansión es única y nunca termina en puros ceros o unos). Entonces

$$\left\{ 2^{n-1}\alpha \right\} = 0.b_n b_{n+1} b_{n+2} \ldots \text{ (en binario)},$$

y esta cantidad es menor que $\tfrac{1}{2}$ exactamente cuando $b_n = 0$ (la igualdad con $\tfrac12$ o con $0$ no puede darse por la irracionalidad de $\pi$, así que $\operatorname{sgn}$ nunca vale $0$). Por lo tanto:

$$\operatorname{sgn}(\sin(2^n)) = \begin{cases} +1 & \text{si } b_n = 0 \\ -1 & \text{si } b_n = 1 \end{cases} = 1 - 2b_n.$$

**Paso 3: Evaluar la suma.**

$$\sum_{n=1}^{\infty} \frac{\operatorname{sgn}(\sin(2^n))}{2^n} = \sum_{n=1}^{\infty} \frac{1 - 2b_n}{2^n} = \sum_{n=1}^{\infty} \frac{1}{2^n} - 2\sum_{n=1}^{\infty} \frac{b_n}{2^n} = 1 - 2\alpha = 1 - \frac{2}{\pi}.$$

**Verificación rápida:** $1 - 2/\pi \approx 0.3634$. Los primeros términos: $\sin(2) > 0$, $\sin(4) < 0$, $\sin(8) > 0$, $\sin(16) < 0$, $\sin(32) > 0$, dando $\tfrac12 - \tfrac14 + \tfrac18 - \tfrac1{16} + \tfrac1{32} = 0.34375$, consistente con el valor exacto.

$$\boxed{1 - \dfrac{2}{\pi}}$$