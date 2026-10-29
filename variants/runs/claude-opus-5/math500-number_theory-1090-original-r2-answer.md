## Razonamiento

**Total de casos:** los enteros impares positivos menores que 2010 son $1, 3, 5, \dots, 2009$, es decir
$$\frac{2009-1}{2}+1 = 1005 \text{ números}.$$

**Casos favorables:** $\frac{1}{n}$ es un decimal finito si y solo si $n$ solo tiene factores primos 2 y 5. Como $n$ es impar, no puede tener el factor 2, así que $n$ debe ser una potencia de 5:
$$5^0=1,\quad 5^1=5,\quad 5^2=25,\quad 5^3=125,\quad 5^4=625,$$
y $5^5=3125 > 2009$. Son **5** valores.

**Probabilidad:**
$$\frac{5}{1005} = \frac{1}{201}$$

Con $a=1$ y $b=201$ coprimos, $a+b = 202$.

\boxed{202}