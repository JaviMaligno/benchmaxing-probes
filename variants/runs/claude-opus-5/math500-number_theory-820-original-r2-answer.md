## Planteamiento

Como $210 = 2\cdot 3\cdot 5\cdot 7$, escribimos $a = 210x$, $b = 210y$ con $\gcd(x,y) = 1$ (esto garantiza $\gcd(a,b) = 210$).

Entonces:
$$\mathop{\text{lcm}}[a,b] = 210\,xy = 210^3 \implies xy = 210^2 = 2^2\cdot 3^2\cdot 5^2\cdot 7^2$$

## Conteo

Como $\gcd(x,y)=1$, cada potencia prima completa ($2^2$, $3^2$, $5^2$, $7^2$) debe ir íntegra a $x$ o a $y$. Eso da $2^4 = 16$ pares ordenados.

El caso $x=y$ es imposible (requeriría $x=y=210$, con $\gcd = 210 \neq 1$), así que los 16 pares se reparten en dos mitades simétricas según $x<y$ o $x>y$.

La condición $a<b$ equivale a $x<y$, lo que deja $16/2 = 8$ valores.

\boxed{8}