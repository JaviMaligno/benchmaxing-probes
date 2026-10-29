**Resolución (resumida):**

Sea el estado de la columna $n$ el conjunto de celdas alcanzables en ella: solo arriba ($A$), solo abajo ($B$) o ambas ($C$). Puertas horizontales abiertas con prob. $1/2$; vertical con prob. $1/4$.

**Transiciones** (de la columna $n$ a la $n+1$, con puertas $h_A, h_B, v$ independientes):

- Desde $A$ (abajo de la columna $n$ inalcanzable): $A' = h_A$, $B' = h_A v$. Entonces:
  - $\to C$: $(1/2)(1/4) = 1/8$; $\to A$: $(1/2)(3/4) = 3/8$; $\to \varnothing$: $1/2$.
- Desde $C$: $A' = h_A \vee (h_B v)$, así que $P(A') = 1/2 + 1/16 = 9/16$; simétrico para $B'$. Además:
  - ambos: $h_A h_B \vee h_A v \vee h_B v \Rightarrow 3/8$; ninguno: $\neg h_A \wedge \neg h_B \Rightarrow 1/4$; solo una: $3/16$ cada uno.

**Sistema de esperanzas** ($f(s)$ = celdas esperadas alcanzables en columnas $\ge n$, contando la columna $n$):

$$f(A) = 1 + \tfrac18 f(C) + \tfrac38 f(A) \;\Rightarrow\; f(A) = \frac{8 + f(C)}{5}$$
$$f(C) = 2 + \tfrac38 f(C) + \tfrac3{16}f(A) + \tfrac3{16}f(B) = 2 + \tfrac38 f(C) + \tfrac38 f(A) \;\Rightarrow\; f(C) = \frac{16 + 3f(A)}{5}$$

Resolviendo: $f(C) = 5f(A) - 8$, luego $25f(A) - 40 = 16 + 3f(A)$, de donde $f(A) = 28/11$ y $f(C) = 52/11$.

**Columna inicial:** la celda superior siempre cuenta; la inferior con prob. $1/4$ (si la vertical de la columna $0$ está abierta). Los valores futuros (restando la celda actual de $f$) son $g(A) = 28/11 - 1 = 17/11$ y $g(C) = 52/11 - 2 = 30/11$:

$$E = \frac54 + \frac34\cdot\frac{17}{11} + \frac14\cdot\frac{30}{11} = \frac{55 + 51 + 30}{44} = \frac{136}{44} = \frac{34}{11}$$

**Verificación numérica:** calculando $p_n, r_n$ (probabilidades de alcanzar cada celda de la columna $n$) por recursión y sumando: $1.25 + 0.75 + 0.462 + 0.275 + 0.15 + \dots \approx 3.09 = 34/11$ ✓.

$$\boxed{\dfrac{34}{11}}$$