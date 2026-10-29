Con $\gcd(a,b)=210$ y $\mathop{\text{lcm}}[a,b]=210^3$, sabemos que $ab = \gcd \cdot \text{lcm} = 210^4$.

Escribimos $a = 210x$ y $b = 210y$ con $\gcd(x,y)=1$. Entonces $xy = 210^2 = 2^2\cdot 3^2\cdot 5^2\cdot 7^2$.

Como $x$ e $y$ son coprimos, cada factor primo al cuadrado ($2^2, 3^2, 5^2, 7^2$) debe ir completo a $x$ o a $y$. Con 4 primos hay $2^4 = 16$ formas, es decir, 16 pares ordenados $(x,y)$. Ninguno cumple $x=y$, así que exactamente la mitad tiene $x<y$, lo que da $8$ valores posibles para $a$.

$$\boxed{8}$$