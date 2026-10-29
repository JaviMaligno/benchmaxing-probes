Para determinar de cuántas maneras se pueden ensamblar $2$ cubos unitarios rojos y $25$ cubos unitarios blancos en un cubo de $3 \times 3 \times 3$ de modo que el color rojo sea visible en exactamente $4$ caras, podemos representar las posiciones de los $27$ cubos unitarios mediante coordenadas $(x, y, z)$ donde $x, y, z \in \{-1, 0, 1\}$.

Las $6$ caras del cubo de $3 \times 3 \times 3$ corresponden a los planos $x = 1$, $x = -1$, $y = 1$, $y = -1$, $z = 1$ y $z = -1$. Un cubo unitario en la posición $(x, y, z)$ es visible en una cara si la coordenada correspondiente es $\pm 1$. Por lo tanto, el número de caras en las que es visible un cubo unitario es igual a su cantidad de coordenadas distintas de cero:
- **Cubo central** ($0$ coordenadas distintas de cero): $1$ cubo, visible en $0$ caras.
- **Centros de cara** ($1$ coordenada distinta de cero): $6$ cubos, cada uno visible en $1$ cara.
- **Centros de arista** ($2$ coordenadas distintas de cero): $12$ cubos, cada uno visible en $2$ caras.
- **Esquinas** ($3$ coordenadas distintas de cero): $8$ cubos, cada uno visible en $3$ caras.

Sea $F(c)$ el conjunto de caras en las que es visible un cubo ubicado en la posición $c$. Buscamos el número de pares no ordenados de posiciones distintas $\{c_1, c_2\}$ tales que:
$$|F(c_1) \cup F(c_2)| = |F(c_1)| + |F(c_2)| - |F(c_1) \cap F(c_2)| = 4$$

Sean $k_1 = |F(c_1)|$ y $k_2 = |F(c_2)|$, con $k_1 \ge k_2$. Como $k_1 + k_2 \ge 4$ y $k_1, k_2 \in \{0, 1, 2, 3\}$, analizamos los casos posibles para $(k_1, k_2)$:

1. **Caso $(k_1, k_2) = (3, 3)$ (dos cubos de esquina):**
   Necesitamos que $|F(c_1) \cap F(c_2)| = 3 + 3 - 4 = 2$.
   Dos esquinas comparten exactamente $2$ caras si y solo si coinciden en $2$ coordenadas y difieren en $1$ (es decir, están en los extremos de una misma arista del cubo grande). Como un cubo tiene $12$ aristas, hay **$12$** pares de este tipo.

2. **Caso $(k_1, k_2) = (3, 2)$ (un cubo de esquina y un centro de arista):**
   Necesitamos que $|F(c_1) \cap F(c_2)| = 3 + 2 - 4 = 1$.
   Hay $8$ opciones para elegir la esquina $c_1$. Para que un centro de arista $c_2$ (que tiene una coordenada igual a $0$ y dos coordenadas en $\{\pm 1\}$) comparta exactamente $1$ cara con $c_1$, podemos elegir cuál de sus tres coordenadas es $0$ ($3$ opciones) y luego, de las $2$ coordenadas restantes, una debe coincidir en signo con $c_1$ y la otra debe tener el signo opuesto ($2$ opciones).
   Así, por cada esquina hay $3 \times 2 = 6$ centros de arista válidos, lo que da $8 \times 6 =$ **$48$** pares.

3. **Caso $(k_1, k_2) = (3, 1)$ (un cubo de esquina y un centro de cara):**
   Necesitamos que $|F(c_1) \cap F(c_2)| = 3 + 1 - 4 = 0$.
   Hay $8$ opciones para la esquina $c_1$, la cual es visible en $3$ caras. El centro de cara $c_2$ debe ubicarse en una de las $3$ caras restantes donde $c_1$ no es visible.
   Esto nos da $8 \times 3 =$ **$24$** pares.

4. **Caso $(k_1, k_2) = (2, 2)$ (dos centros de arista):**
   Necesitamos que $|F(c_1) \cap F(c_2)| = 2 + 2 - 4 = 0$.
   Hay $12$ centros de arista. Fijado un centro de arista $c_1$, digamos $(1, 1, 0)$ (visible en $x=1$ e $y=1$), contamos cuántos centros de arista $c_2$ no comparten ninguna cara con $c_1$:
   - Si $c_2$ tiene $z = 0$, debe ser $(-1, -1, 0)$ ($1$ opción).
   - Si $c_2$ tiene $x = 0$, debe ser $(0, -1, 1)$ o $(0, -1, -1)$ ($2$ opciones).
   - Si $c_2$ tiene $y = 0$, debe ser $(-1, 0, 1)$ o $(-1, 0, -1)$ ($2$ opciones).
   
   Hay $1 + 2 + 2 = 5$ opciones para $c_2$ por cada $c_1$. Como el orden del par no importa, el número de pares es $\frac{12 \times 5}{2} =$ **$30$** pares.

Sumando todos los casos posibles, obtenemos el total de maneras:
$$12 + 48 + 24 + 30 = 114$$

\boxed{114}