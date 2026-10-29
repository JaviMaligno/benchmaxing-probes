## Razonamiento

**Condición de divisibilidad por 11.** Sean $A$ la suma de los dígitos en posiciones impares y $B$ la de las pares. Entonces $A+B=36$ y se requiere $A-B\equiv 0 \pmod{11}$. Como $A-B$ es par y $|A-B|\le 26-10=16$, la única opción es $A-B=0$, es decir $A=B=18$.

**Subconjuntos de suma 18.** Hay que contar los subconjuntos de 4 elementos de $\{1,\dots,8\}$ con suma 18:

$$\{1,2,7,8\},\{1,3,6,8\},\{1,4,5,8\},\{1,4,6,7\},\{2,3,5,8\},\{2,3,6,7\},\{2,4,5,7\},\{3,4,5,6\}$$

Son **8** subconjuntos (se agrupan en 4 pares complementarios).

**Condición de divisibilidad por 2.** Nótese que cada uno de esos 8 subconjuntos contiene exactamente **2 dígitos pares**, y por tanto su complemento también contiene exactamente 2 pares.

Fijado el subconjunto de posiciones impares: hay $4!=24$ ordenaciones. Para las posiciones pares, la última cifra debe ser par, y hay 2 pares disponibles en ese complemento: $2\cdot 3!=12$ ordenaciones.

**Conteo total.**
$$N = 8 \cdot 24 \cdot 12 = 2304$$

(Comprobación: de los $8\cdot24\cdot24=4608$ múltiplos de 11, exactamente la mitad termina en cifra par.)

**Diferencia.**
$$N - 2025 = 2304 - 2025 = 279$$

\boxed{279}