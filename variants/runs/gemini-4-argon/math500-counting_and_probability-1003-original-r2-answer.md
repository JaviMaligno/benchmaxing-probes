Para encontrar la probabilidad de obtener la cara $F$, analicemos primero las propiedades del dado.

1. **Definición de las probabilidades de cada cara:**
   Sabemos que la suma de los números en cada par de caras opuestas es 7. Por lo tanto, los tres pares de caras opuestas son $(1,6)$, $(2,5)$ y $(3,4)$.
   
   Sea $F'$ la cara opuesta a la cara $F$. Las otras cuatro caras tienen cada una una probabilidad de $\frac{1}{6}$ de salir. Como la suma de las probabilidades de las 6 caras debe ser igual a 1, la suma de las probabilidades de $F$ y $F'$ es:
   $$P(F) + P(F') = 1 - 4 \times \frac{1}{6} = \frac{1}{3}$$

   Dado que $P(F) > \frac{1}{6}$ y $P(F') < \frac{1}{6}$, podemos expresar estas probabilidades como:
   $$P(F) = \frac{1}{6} + x$$
   $$P(F') = \frac{1}{6} - x$$
   donde $0 < x \le \frac{1}{6}$.

2. **Probabilidad de obtener una suma de 7 al lanzar dos dados:**
   Al lanzar dos de estos dados, la suma de los resultados es 7 si y solo si en el segundo dado sale la cara opuesta a la que salió en el primero. Es decir, los pares posibles que suman 7 son exactamente los pares de caras opuestas.

   Sumando las probabilidades de todos los casos favorables (dos pares de caras con probabilidad $\frac{1}{6}$ cada una, y el par $(F, F')$):
   $$P(\text{suma} = 7) = 2 \left(\frac{1}{6} \cdot \frac{1}{6}\right) + 2 \left(\frac{1}{6} \cdot \frac{1}{6}\right) + 2 P(F)P(F')$$
   $$P(\text{suma} = 7) = \frac{4}{36} + 2\left(\frac{1}{6} + x\right)\left(\frac{1}{6} - x\right)$$
   $$P(\text{suma} = 7) = \frac{4}{36} + 2\left(\frac{1}{36} - x^2\right) = \frac{6}{36} - 2x^2 = \frac{1}{6} - 2x^2$$

3. **Cálculo de $x$ y $P(F)$:**
   El problema nos indica que esta probabilidad es igual a $\frac{47}{288}$:
   $$\frac{1}{6} - 2x^2 = \frac{47}{288}$$

   Expresando $\frac{1}{6}$ como $\frac{48}{288}$:
   $$\frac{48}{288} - 2x^2 = \frac{47}{288}$$
   $$2x^2 = \frac{1}{288}$$
   $$x^2 = \frac{1}{576}$$

   Como $x > 0$, tomamos la raíz cuadrada positiva:
   $$x = \frac{1}{24}$$

   Sustituyendo $x$ para hallar la probabilidad de la cara $F$:
   $$P(F) = \frac{1}{6} + \frac{1}{24} = \frac{4}{24} + \frac{1}{24} = \frac{5}{24}$$

4. **Resultado final:**
   La fracción $\frac{5}{24}$ es irreducible, por lo que $m = 5$ y $n = 24$. Por lo tanto, la suma $m + n$ es:
   $$m + n = 5 + 24 = 29$$

\boxed{29}