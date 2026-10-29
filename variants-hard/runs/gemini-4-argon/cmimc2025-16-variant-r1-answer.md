Para determinar de cuántas maneras se pueden colocar las fichas en una cuadrícula de $4 \times 5$ cumpliendo las condiciones dadas, podemos analizar la cuadrícula columna por columna (cada una de altura $4$) utilizando programación dinámica.

### Paso 1: Estados válidos para una sola columna
Representemos cada columna de $4$ casillas como una cadena binaria $u = u_1u_2u_3u_4 \in \{0,1\}^4$, donde $1$ indica la presencia de una ficha y $0$ indica una casilla vacía.

Como dos fichas no pueden ser ortogonalmente adyacentes, una columna válida no puede contener dos $1$ consecutivos (`11`). Existen $F_6 = 8$ configuraciones válidas para una columna:
- $Z = \text{0000}$
- $A_1 = \text{0001}, \quad A_2 = \text{1000}$
- $B_1 = \text{0010}, \quad B_2 = \text{0100}$
- $C_1 = \text{0101}, \quad C_2 = \text{1010}$
- $D = \text{1001}$

---

### Paso 2: Transiciones válidas entre columnas adyacentes
Dos columnas válidas adyacentes $u$ y $v$ cumplen las condiciones del problema si y solo si:
1. **Sin adyacencia horizontal:** No tienen fichas en la misma fila, es decir, $u_i \cdot v_i = 0$ para todo $i \in \{1,2,3,4\}$.
2. **Todo bloque de $2 \times 2$ tiene al menos una ficha:** Para cada $i \in \{1,2,3\}$, se cumple $u_i + u_{i+1} + v_i + v_{i+1} \ge 1$. Esto equivale a decir que el vector suma $w = u + v \in \{0,1\}^4$ no contiene dos ceros consecutivos (`00`).

Analicemos qué columnas $v$ pueden seguir a cada columna $u$:
- **$u = Z = \text{0000}$:** Necesitamos que $v$ no tenga `00` ni `11`. Las únicas opciones son $C_1 = \text{0101}$ y $C_2 = \text{1010}$.
  $$Z \sim \{C_1, C_2\}$$
- **$u = A_1 = \text{0001}$:** Requiere $v_4 = 0$ y que $v_1v_2v_3$ no contenga `00`. Las opciones para $v$ son $B_2 = \text{0100}$ y $C_2 = \text{1010}$. Por simetría vertical, se obtiene también la vecindad de $A_2$:
  $$A_1 \sim \{B_2, C_2\}, \qquad A_2 \sim \{B_1, C_1\}$$
- **$u = B_1 = \text{0010}$:** Como $u_3 = 1$, los bloques de las filas $(2,3)$ y $(3,4)$ ya están cubiertos. Solo necesitamos $v_3 = 0$ y $v_1 + v_2 \ge 1$. Las opciones son $A_2 = \text{1000}$, $B_2 = \text{0100}$, $C_1 = \text{0101}$ y $D = \text{1001}$. Por simetría:
  $$B_1 \sim \{A_2, B_2, C_1, D\}, \qquad B_2 \sim \{A_1, B_1, C_2, D\}$$
- **$u = C_1 = \text{0101}$:** Como $u$ ya cubre todos los bloques de $2 \times 2$, solo se requiere que $v_2 = v_4 = 0$. Las opciones son $Z = \text{0000}$, $A_2 = \text{1000}$, $B_1 = \text{0010}$ y $C_2 = \text{1010}$. Por simetría:
  $$C_1 \sim \{Z, A_2, B_1, C_2\}, \qquad C_2 \sim \{Z, A_1, B_2, C_1\}$$
- **$u = D = \text{1001}$:** Requiere $v_1 = v_4 = 0$ y $v_2 + v_3 \ge 1$. Las opciones son $B_1 = \text{0010}$ y $B_2 = \text{0100}$.
  $$D \sim \{B_1, B_2\}$$

---

### Paso 3: Recurrencia por simetría
Para una cuadrícula de $4 \times k$, por simetría el número de configuraciones válidas que terminan en los estados dentro de cada grupo $\{Z, A_1, A_2, D\}$ y $\{B_1, B_2, C_1, C_2\}$ evoluciona de forma uniforme:
- Cada estado en $X = \{Z, A_1, A_2, D\}$ tiene exactamente $2$ vecinos en $Y = \{B_1, B_2, C_1, C_2\}$ y $0$ vecinos en $X$.
- Cada estado en $Y = \{B_1, B_2, C_1, C_2\}$ tiene exactamente $2$ vecinos en $X$ y $2$ vecinos en $Y$.

Sea $x_k$ el número de configuraciones válidas para $k$ columnas que terminan en un estado fijo de $X$, y $y_k$ el número de configuraciones que terminan en un estado fijo de $Y$. Entonces:
$$x_1 = 1, \qquad y_1 = 1$$
y para $k \ge 1$:
$$\begin{aligned}
x_{k+1} &= 2y_k \\
y_{k+1} &= 2x_k + 2y_k
\end{aligned}$$
El total de configuraciones para $k$ columnas es $T_k = 4x_k + 4y_k$.

---

### Paso 4: Cálculo hasta $k = 5$
Calculamos iterativamente para cada columna:
- **$k = 1$:**
  $$x_1 = 1, \quad y_1 = 1 \implies T_1 = 4(1) + 4(1) = 8$$
- **$k = 2$:**
  $$x_2 = 2(1) = 2, \quad y_2 = 2(1) + 2(1) = 4 \implies T_2 = 4(2) + 4(4) = 24$$
- **$k = 3$:**
  $$x_3 = 2(4) = 8, \quad y_3 = 2(2) + 2(4) = 12 \implies T_3 = 4(8) + 4(12) = 80$$
- **$k = 4$:**
  $$x_4 = 2(12) = 24, \quad y_4 = 2(8) + 2(12) = 40 \implies T_4 = 4(24) + 4(40) = 256$$
- **$k = 5$:**
  $$x_5 = 2(40) = 80, \quad y_5 = 2(24) + 2(40) = 128$$
  $$T_5 = 4(80) + 4(128) = 320 + 512 = 832$$

\boxed{832}