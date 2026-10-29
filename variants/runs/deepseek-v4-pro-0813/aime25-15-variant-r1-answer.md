Let $N=3^7$ y $m=3^8$.

Analizamos los residuos de $x^3 \pmod{3^8}$ según si $3\mid x$.

- Si $3\nmid x$, entonces $x^3$ es una unidad, y $x^3\equiv \pm 1 \pmod 9$.
- Si $3\mid x$, entonces $x^3\equiv 0 \pmod 9$.

Por tanto, para que $x^3+y^3+z^3\equiv 0\pmod{3^8}$, en particular debe ser divisible por $9$. Las únicas posibilidades módulo $9$ son:

1. $x,y,z$ son todos divisibles por $3$;
2. exactamente uno de $x,y,z$ es divisible por $3$, y los otros dos tienen cubos $\equiv 1$ y $\equiv -1 \pmod 9$.

**Caso 1: exactamente uno divisible por $3$.**  
Fijamos cuál de las tres variables es divisible por $3$: $3$ opciones. Hay $3^6=729$ múltiplos de $3$ entre $1$ y $3^7$.

Para un $z$ divisible por $3$ fijo, necesitamos contar pares ordenados $(x,y)$ con $3\nmid x,y$ y
\[
x^3+y^3\equiv -z^3 \pmod{3^8}.
\]
Los cubos de las unidades forman exactamente los residuos $\equiv \pm1 \pmod 9$, cada uno una vez. Como $-z^3\equiv0\pmod9$, si $x^3\equiv1\pmod9$ entonces $y^3\equiv-1\pmod9$ y viceversa. Hay $729$ residuos $\equiv1\pmod9$ y $729$ residuos $\equiv-1\pmod9$, de modo que hay $729+729=1458$ pares.

Entonces este caso aporta:
\[
3\cdot 729\cdot 1458 = 3\,188\,646.
\]

**Caso 2: $x,y,z$ todos divisibles por $3$.**  
Escribimos $x=3u,\ y=3v,\ z=3w$, con $1\le u,v,w\le 3^6$. Entonces
\[
x^3+y^3+z^3=27(u^3+v^3+w^3),
\]
y necesitamos
\[
u^3+v^3+w^3\equiv 0\pmod{3^5}.
\]
Como $1\le u,v,w\le 3^6$, cada residuo módulo $3^5$ aparece exactamente $3$ veces, así que este caso vale $27$ veces el número de soluciones de
\[
r^3+s^3+t^3\equiv0\pmod{3^5}
\]
con $r,s,t$ recorriendo todos los residuos módulo $3^5$.

Para el módulo $3^5$, recortemos el conteo completo $A_5$. Separamos en el mismo esquema:

- Soluciones con exactamente uno divisible por $3$: $3\cdot 3^4\cdot (2\cdot 3^5)=2\cdot 3^{10}=118098$.
- Soluciones con los tres divisibles por $3$: tras factorizar, cada residuo módulo $3^2$ aparece $9$ veces, y el número de soluciones módulo $3^2$ es $189$. Aportan
\[
9^3\cdot 189 = 137\,781.
\]

Por lo tanto,
\[
A_5 = 118098 + 137781 = 255879.
\]

Entonces el caso con los tres divisibles por $3$ aporta:
\[
27A_5 = 27\cdot 255879 = 6\,908\,733.
\]

Sumando ambos casos:
\[
M = 6\,908\,733 + 3\,188\,646 = 10\,097\,379.
\]

Finalmente,
\[
M \equiv 379 \pmod{1000}.
\]

\[
\boxed{379}
\]