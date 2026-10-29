Para que un número sea divisible por \(22\), debe ser divisible por \(2\) y por \(11\).

1. **Divisibilidad por \(11\):**  
   Sea \(A\) la suma de los dígitos en las posiciones \(1,3,5,7,9\), y \(B\) la suma en las posiciones \(2,4,6,8\). Entonces
   \[
   A+B=45.
   \]
   La condición de divisibilidad por \(11\) exige que \(A-B\) sea múltiplo de \(11\). Como
   \[
   A-B=2A-45,
   \]
   y \(A\) está entre \(15\) y \(35\), los únicos múltiplos posibles son \(\pm 11\). Esto da
   \[
   A=17 \quad \text{o} \quad A=28.
   \]

2. **Divisibilidad por \(2\):**  
   El último dígito, que está en una posición impar del grupo \(A\), debe ser par.

   Para un conjunto fijo \(S\) de 5 dígitos en las posiciones impares, cada dígito par de \(S\) puede colocarse al final, y los demás se acomodan en
   \[
   4!\cdot 4! = 576
   \]
   formas.

3. **Conteo de conjuntos \(S\):**
   - Si \(A=17\), los conjuntos posibles son
     \[
     \{1,2,3,4,7\},\quad \{1,2,3,5,6\},
     \]
     con un total de \(4\) dígitos pares entre ambos.
   - Si \(A=28\), su complemento tiene 4 dígitos y suma \(17\). Enumerando estos complementos, los conjuntos \(S\) resultantes tienen un total de \(21\) dígitos pares.

   Por lo tanto,
   \[
   N=(4+21)\cdot 576=14400.
   \]

4. La diferencia pedida es
   \[
   14400-14025=375.
   \]

\[
\boxed{375}
\]