Sea $n = 2027$ y sea $z$ una raíz $n$-ésima de la unidad con $z \neq 1$. Queremos calcular

$$
S = \sum_{k=1}^{n} \frac{1}{1+z^k}.
$$

Observemos primero que $z^1,z^2,\dots,z^n$ son exactamente las $n$ raíces $n$-ésimas de la unidad, cada una una vez. Por tanto,

$$
S = \sum_{\omega^n = 1} \frac{1}{1+\omega}.
$$

Aunque $\omega=1$ es una de las raíces, aquí $z\neq 1$ y los términos $z,z^2,\dots,z^n$ sí incluyen el valor $1$ exactamente una vez (cuando $k=n$). Así que conviene tratar aparte $k=n$.

Cuando $k=n$, tenemos $z^n=1$, de modo que

$$
\frac{1}{1+z^n} = \frac{1}{2}.
$$

Para $k=1,\dots,n-1$, los números $\omega=z^k$ son las raíces $n$-ésimas de la unidad distintas de $1$. Para esas raíces se cumple la identidad

$$
\frac{1}{1+\omega} + \frac{1}{1+\omega^{-1}} = \frac{1}{1+\omega} + \frac{\omega}{1+\omega} = 1.
$$

Agrupando $\omega$ con $\omega^{-1}$, cada par contribuye $1$. Hay $n-1=2026$ raíces distintas de $1$, que se agrupan en $(n-1)/2 = 1013$ parejas. Por lo tanto,

$$
\sum_{k=1}^{n-1} \frac{1}{1+z^k} = 1013.
$$

Sumando el término $k=n$:

$$
S = 1013 + \frac{1}{2} = \frac{2027}{2}.
$$

Por lo tanto,

\[
\boxed{\frac{2027}{2}}
\]