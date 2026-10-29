## Planteamiento

El signo de $\sin(2^n)$ depende de la posición de $2^n$ módulo $2\pi$:
$$\sin(2^n)>0 \iff \left\{\frac{2^n}{2\pi}\right\} \in \left(0,\tfrac12\right)$$

Sea $\alpha = \dfrac{1}{2\pi}$ con desarrollo binario $\alpha = 0.b_1b_2b_3\ldots$

Entonces $\left\{2^n\alpha\right\} = 0.b_{n+1}b_{n+2}\ldots$, y ese número es menor que $1/2$ exactamente cuando $b_{n+1}=0$. Como $\alpha$ es irracional, nunca se da el caso $\sin(2^n)=0$. Por tanto:
$$\operatorname{sgn}(\sin(2^n)) = 1 - 2b_{n+1}$$

## Cálculo

$$S=\sum_{n\ge1}\frac{1-2b_{n+1}}{2^n} = 1 - 2\sum_{n\ge1}\frac{b_{n+1}}{2^n}$$

Y la cola binaria se expresa con $\alpha$:
$$\sum_{n\ge1}\frac{b_{n+1}}{2^n} = 2\sum_{n\ge1}\frac{b_{n+1}}{2^{n+1}} = 2\left(\alpha - \frac{b_1}{2}\right)$$

Como $\alpha \approx 0{,}15915 < \tfrac12$, se tiene $b_1=0$, luego la suma vale $2\alpha = \dfrac{1}{\pi}$.

$$S = 1 - \frac{2}{\pi}$$

## Verificación numérica

Los signos de $\sin(2),\sin(4),\sin(8),\sin(16),\dots$ son $+,-,+,-,+,+,+,-$, dando sumas parciales $0{,}5 \to 0{,}25 \to 0{,}375 \to 0{,}3125 \to 0{,}34375 \to 0{,}359375 \to 0{,}3671875 \to 0{,}36328$, que convergen a $1-2/\pi \approx 0{,}36338$.

$$\boxed{1-\dfrac{2}{\pi}}$$