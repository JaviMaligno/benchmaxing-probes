Para calcular $AC \cdot CB$, analicemos primero la relación geométrica general cuando un semicírculo $S$ de radio $r$ y centro $O$ está inscrito en un semicírculo mayor $S'$ de radio $R$ y centro $O'$.

1. **Relación de radios, distancias y ángulos en semicírculos inscritos:**
   Ubiquemos el centro $O'$ en el origen de coordenadas $(0,0)$ y el diámetro de $S'$ sobre el eje $x$, desde $(-R, 0)$ hasta $(R, 0)$.
   - Como el arco de $S$ es tangente al diámetro de $S'$, la distancia desde el centro $O$ hasta el diámetro de $S'$ es igual al radio $r$. Si $x_T$ es la coordenada en el eje $x$ del punto de tangencia $T$, entonces $O = (x_T, r)$, por lo que $|O'O|^2 = x_T^2 + r^2$.
   - Por otro lado, dado que el diámetro de $S$ (de longitud $2r$) es una cuerda del arco de $S'$ (de radio $R$) cuyo punto medio es $O$, el teorema de Pitágoras aplicado al triángulo rectángulo formado por $O'$, $O$ y un extremo del diámetro de $S$ nos da:
     $$|O'O|^2 + r^2 = R^2 \implies |O'O| = \sqrt{R^2 - r^2}.$$
   - Igualando ambas expresiones para $|O'O|^2$, obtenemos:
     $$x_T^2 + r^2 = R^2 - r^2 \implies R^2 - x_T^2 = 2r^2.$$
   - Además, el vector $\overrightarrow{O'O}$ es perpendicular a la cuerda (el diámetro de $S$), mientras que el vector normal al diámetro de $S'$ es vertical. Por lo tanto, el ángulo agudo $\theta$ entre el diámetro de $S$ y el diámetro de $S'$ es igual al ángulo que forma $\overrightarrow{O'O}$ con la vertical:
     $$\cos \theta = \frac{r}{|O'O|} = \frac{r}{\sqrt{R^2 - r^2}}.$$

2. **Aplicación a $S_1$, $S_2$ y $S_3$:**
   Sean $r_1 = 1$, $r_2$ y $r_3 = 10$ los radios de $S_1$, $S_2$ y $S_3$, respectivamente.
   - Como $S_2$ está inscrito en $S_3$ y es tangente a $AB$ en $C$, ubicando el centro de $S_3$ en el origen con $A = (-r_3, 0)$, $B = (r_3, 0)$ y $C = (x_C, 0)$, tenemos:
     $$AC \cdot CB = (r_3 + x_C)(r_3 - x_C) = r_3^2 - x_C^2 = 2r_2^2.$$
   - El ángulo agudo $\phi$ entre los diámetros de $S_2$ y $S_3$ cumple:
     $$\cos \phi = \frac{r_2}{\sqrt{r_3^2 - r_2^2}}.$$
   - Análogamente, como $S_1$ está inscrito en $S_2$, el ángulo agudo $\psi$ entre los diámetros de $S_1$ y $S_2$ cumple:
     $$\cos \psi = \frac{r_1}{\sqrt{r_2^2 - r_1^2}}.$$

3. **Condición de paralelismo:**
   Dado que los diámetros de $S_1$ y $S_3$ son paralelos, ambos forman el mismo ángulo agudo con el diámetro de $S_2$, es decir, $\phi = \psi$ y por tanto $\cos \phi = \cos \psi$:
   $$\frac{r_2}{\sqrt{r_3^2 - r_2^2}} = \frac{r_1}{\sqrt{r_2^2 - r_1^2}}.$$
   Elevando al cuadrado ambos lados e invirtiendo las fracciones:
   $$\frac{r_3^2 - r_2^2}{r_2^2} = \frac{r_2^2 - r_1^2}{r_1^2} \implies \frac{r_3^2}{r_2^2} - 1 = \frac{r_2^2}{r_1^2} - 1 \implies r_2^2 = r_1 r_3.$$
   Sustituyendo $r_1 = 1$ y $r_3 = 10$, obtenemos $r_2^2 = 10$.

Finalmente, sustituimos $r_2^2 = 10$ en la expresión para $AC \cdot CB$:
$$AC \cdot CB = 2r_2^2 = 2(10) = 20.$$

\boxed{20}