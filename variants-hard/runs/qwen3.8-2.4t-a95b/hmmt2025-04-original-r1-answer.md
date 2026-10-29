Denotemos

$$S=\sum_{j=-1000}^{1000}\left\lfloor\frac{2025}{j+0.5}\right\rfloor.$$

**Paso 1: Reescribir con un divisor entero.** Como

$$\frac{2025}{j+0.5}=\frac{4050}{2j+1},$$

y cuando $j$ recorre $-1000,-999,\dots,1000$, el valor $n=2j+1$ recorre todos los enteros impares desde $-1999$ hasta $2001$. Así,

$$S=\sum_{\substack{n\text{ impar}\\ -1999\le n\le 2001}}\left\lfloor\frac{4050}{n}\right\rfloor.$$

**Paso 2: Agrupar en pares $(n,-n)$.** Hay $1000$ pares de la forma $(n,-n)$ con $n\in\{1,3,\dots,1999\}$, y queda sin pareja el término $n=2001$.

Para cada par, usamos la identidad $\lfloor x\rfloor+\lfloor -x\rfloor = 0$ si $x$ es entero, y $-1$ si no lo es. Aquí $x=4050/n$.

- Si $n\mid 4050$, el par contribuye $0$.
- Si $n\nmid 4050$, el par contribuye $-1$.

**Paso 3: Contar divisores impares de $4050$.** Factorizamos

$$4050=2\cdot 3^4\cdot 5^2,$$

cuyos divisores impares son los de $3^4\cdot 5^2$, en número $(4+1)(2+1)=15$. Estos son $1,3,5,9,15,25,27,45,75,81,135,225,405,675,2025$. De ellos, solo $2025$ supera a $1999$, así que hay $14$ divisores impares dentro de $\{1,3,\dots,1999\}$.

**Paso 4: Sumar.** Los $1000$ pares aportan

$$14\cdot 0+(1000-14)(-1)=-986.$$

El término suelto es

$$\left\lfloor\frac{4050}{2001}\right\rfloor=2.$$

Por lo tanto,

$$S=-986+2=-984.$$

$$\boxed{-984}$$