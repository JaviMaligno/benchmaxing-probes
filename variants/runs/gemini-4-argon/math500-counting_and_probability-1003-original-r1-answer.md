Para resolver el problema paso a paso, definamos las probabilidades de las caras del dado:

1. **Planteamiento de las probabilidades:**
   En el dado, la suma de los números en cada par de caras opuestas es 7. Esto significa que los pares de caras opuestas son $(1,6)$, $(2,5)$ y $(3,4)$, y obtener una suma de 7 al lanzar dos dados equivale exactamente a obtener en el segundo dado la cara opuesta a la obtenida en el primero.

   Sabemos que cuatro de las caras tienen una probabilidad de $\frac{1}{6}$ cada una. Sea $F$ la cara con probabilidad mayor que $\frac{1}{6}$ y $F'$ su cara opuesta, con probabilidad menor que $\frac{1}{6}$.
   Como la suma de las probabilidades de las 6 caras debe ser igual a 1, podemos escribir la probabilidad de $F$ como:
   $$P(F) = \frac{1}{6} + x$$
   y la probabilidad de su cara opuesta $F'$ como:
   $$P(F') = \frac{1}{6} - x$$
   donde $x > 0$. Notemos que la suma de todas las probabilidades es $(\frac{1}{6} + x) + (\frac{1}{6} - x) + 4\left(\frac{1}{6}\right) = 1$.

2. **Probabilidad de obtener una suma de 7 con dos dados:**
   Para que la suma de los dos dados sea 7, debe salir un par de caras opuestas: $(F, F')$, $(F', F)$, o cualquiera de las otras 4 combinaciones de las caras restantes. La probabilidad total de obtener una suma de 7 es:
   $$P(\text{suma } 7) = 2 \cdot P(F)P(F') + 4 \cdot \left(\frac{1}{6} \cdot \frac{1}{6}\right)$$

   Sustituyendo las expresiones para $P(F)$ y $P(F')$:
   $$P(\text{suma } 7) = 2\left(\frac{1}{6} + x\right)\left(\frac{1}{6} - x\right) + \frac{4}{36}$$
   $$P(\text{suma } 7) = 2\left(\frac{1}{36} - x^2\right) + \frac{1}{9} = \frac{1}{18} - 2x^2 + \frac{2}{18} = \frac{1}{6} - 2x^2$$

3. **Cálculo de $x$:**
   El problema nos indica que esta probabilidad es igual a $\frac{47}{288}$:
   $$\frac{1}{6} - 2x^2 = \frac{47}{288}$$

   Convirtiendo $\frac{1}{6}$ a denominador 288 ($\frac{1}{6} = \frac{48}{288}$):
   $$\frac{48}{288} - 2x^2 = \frac{47}{288}$$
   $$2x^2 = \frac{1}{288}$$
   $$x^2 = \frac{1}{576}$$

   Dado que $x > 0$, tomamos la raíz cuadrada positiva:
   $$x = \frac{1}{24}$$

4. **Probabilidad de la cara $F$:**
   Sustituimos $x$ para hallar $P(F)$:
   $$P(F) = \frac{1}{6} + \frac{1}{24} = \frac{4}{24} + \frac{1}{24} = \frac{5}{24}$$

   Aquí $m = 5$ y $n = 24$, los cuales son enteros positivos primos entre sí. Por lo tanto, $m + n = 5 + 24 = 29$.

\boxed{29}