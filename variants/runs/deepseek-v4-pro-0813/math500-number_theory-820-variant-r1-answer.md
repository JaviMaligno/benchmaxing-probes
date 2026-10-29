Vamos a razonar.

Sean $\gcd(m,n)=g=2310$ y $\operatorname{lcm}(m,n)=g^3$. Escribimos

$$
m=g a,\qquad n=g b,\qquad \gcd(a,b)=1.
$$

Entonces

$$
\operatorname{lcm}(m,n)=gab=g^3,
$$

por lo que

$$
ab=g^2=2310^2.
$$

Ahora factorizamos $2310$:

$$
2310=2\cdot 3\cdot 5\cdot 7\cdot 11.
$$

Entonces

$$
2310^2=2^2\cdot 3^2\cdot 5^2\cdot 7^2\cdot 11^2.
$$

Cada primo $p$ debe repartirse entre $a$ y $b$ de modo que el exponente total sea $2$ y $\gcd(a,b)=1$; es decir, cada $p^2$ va completamente a $a$ o completamente a $b$.

Hay $2$ opciones por cada uno de los $5$ primos, luego $2^5=32$ pares ordenados $(a,b)$.

Además, la condición $m<n$ equivale a $a<b$.

Los pares ordenados cumplen que $ab=g^2$ es fijo. Por cada par con $a<b$ hay un par con $a>b$, salvo el caso $a=b$, que no ocurre porque $g^2$ no es cuadrado perfecto. Por tanto, la mitad de los $32$ pares cumplen $a<b$:

$$
\frac{32}{2}=16.
$$

Cada valor de $a$ determina un único $m=2310a$, así que hay $16$ posibles valores de $m$.

$$
\boxed{16}
$$