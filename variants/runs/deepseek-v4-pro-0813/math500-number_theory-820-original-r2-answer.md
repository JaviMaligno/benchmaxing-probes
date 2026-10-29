Sea $210 = 2\cdot 3\cdot 5\cdot 7$. Para cada primo $p\in\{2,3,5,7\}$, si $\gcd(a,b)$ tiene exponente $\min(e_p(a),e_p(b))=1$ y $\operatorname{lcm}(a,b)$ tiene exponente $\max(e_p(a),e_p(b))=3$, entonces los exponentes de $p$ en $a$ y $b$ son $\{1,3\}$.

Como hay 4 primos, hay $2^4=16$ pares ordenados de exponentes posibles para $(a,b)$. De estos, los pares $(a,b)$ cumplen o bien $a<b$, o bien $a>b$, y el único caso con $a=b$ sería el par trivial con los dos exponentes iguales, que no es posible porque los exponentes deben ser $1$ y $3$, distintos.

Por tanto, los 16 pares ordenados se reparten simétricamente: 8 tienen $a<b$ y 8 tienen $a>b$.

Así, el número de posibles valores de $a$ es:

\[
\boxed{8}
\]