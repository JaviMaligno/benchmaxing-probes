## Razonamiento

**Enteros impares positivos menores que 2010:** son 1, 3, 5, …, 2009, es decir $\frac{2009+1}{2} = 1005$ números.

**Condición de decimal finito:** $\frac{1}{n}$ tiene expansión decimal finita si y solo si $n$ es de la forma $2^a 5^b$. Como $n$ debe ser impar, no puede tener factores de 2, así que $n$ debe ser una potencia de 5:

$$5^0 = 1,\quad 5^1 = 5,\quad 5^2 = 25,\quad 5^3 = 125,\quad 5^4 = 625$$

La siguiente, $5^5 = 3125$, excede 2010. Hay **5** casos favorables.

**Probabilidad:**
$$\frac{5}{1005} = \frac{1}{201}$$

Como $\gcd(1,201)=1$, tenemos $a=1$, $b=201$, por lo que $a+b = 202$.

\boxed{202}