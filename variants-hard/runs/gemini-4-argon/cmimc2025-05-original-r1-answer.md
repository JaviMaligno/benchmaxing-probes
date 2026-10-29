Para hallar la suma de todos los dígitos impares que aparecen en los múltiplos positivos de $77$ menores que $1,000,000$, podemos aprovechar las propiedades de divisibilidad y simetría cíclica.

### Paso 1: Cantidad de múltiplos de $77$
Observemos que:
$$1,000,000 - 1 = 999,999 = 999 \times 1001 = 999 \times 13 \times 77 = 12,987 \times 77$$
Por lo tanto, los múltiplos positivos de $77$ menores que $1,000,000$ son exactamente los números de la forma $77k$ para $k \in \{1, 2, \dots, 12,987\}$.

Si incluimos el $0$ ($k = 0$) y representamos cada múltiplo como una cadena de $6$ dígitos rellenando con ceros a la izquierda (desde $000000$ hasta $999999$), la suma de los dígitos impares no se altera, ya que el dígito $0$ es par.

### Paso 2: Simetría por desplazamiento cíclico
Sea $S = \{0, 77, 154, \dots, 999999\}$ el conjunto de todos los múltiplos de $77$ de hasta $6$ dígitos. Si escribimos un número $x \in \{0, 1, \dots, 999999\}$ en base $10$ con $6$ dígitos como $x = \overline{d_5 d_4 d_3 d_2 d_1 d_0}$, una rotación cíclica hacia la izquierda de sus dígitos produce el número:
$$\sigma(x) = \overline{d_4 d_3 d_2 d_1 d_0 d_5} = 10x - 999,999 \cdot d_5$$
Como $999,999$ es múltiplo de $77$ y $\operatorname{mcd}(10, 77) = 1$, se cumple que:
$$77 \mid x \iff 77 \mid \sigma(x)$$
Esto significa que la rotación cíclica $\sigma$ es una biyección del conjunto $S$ en sí mismo. En consecuencia, la distribución (el multiconjunto) de los dígitos que aparecen en cualquiera de las $6$ posiciones decimales es exactamente idéntica a la distribución de los dígitos que aparecen en la posición de las unidades ($d_0$).

### Paso 3: Suma de los dígitos impares en la posición de las unidades
Para $x = 77k$, el dígito de las unidades depende únicamente de $7k \bmod 10$.
Dividimos el rango $k \in \{1, 2, \dots, 12,987\}$ en bloques de $10$:
$$12,987 = 1,298 \times 10 + 7$$

1. **En cada bloque completo de $10$ valores consecutivos de $k$:**
   Como $\operatorname{mcd}(7, 10) = 1$, el dígito de las unidades recorre todos los dígitos $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$ exactamente una vez. Los dígitos impares suman:
   $$1 + 3 + 5 + 7 + 9 = 25$$
   En los $1,298$ bloques completos, la suma de los dígitos impares en las unidades es:
   $$1,298 \times 25 = 32,450$$

2. **En los $7$ valores restantes ($k \equiv 1, 2, 3, 4, 5, 6, 7 \pmod{10}$):**
   Los dígitos de las unidades de $77k$ son respectivamente:
   - $k \equiv 1 \implies 7$ (impar)
   - $k \equiv 2 \implies 4$ (par)
   - $k \equiv 3 \implies 1$ (impar)
   - $k \equiv 4 \implies 8$ (par)
   - $k \equiv 5 \implies 5$ (impar)
   - $k \equiv 6 \implies 2$ (par)
   - $k \equiv 7 \implies 9$ (impar)

   La suma de los dígitos impares en estos $7$ casos es:
   $$7 + 1 + 5 + 9 = 22$$

Sumando ambos resultados, la suma total de los dígitos impares en la posición de las unidades es:
$$32,450 + 22 = 32,472$$

### Paso 4: Suma total en las $6$ posiciones
Dado que las $6$ posiciones tienen exactamente la misma distribución de dígitos, la suma total de todos los dígitos impares es:
$$6 \times 32,472 = 194,832$$

\boxed{194832}