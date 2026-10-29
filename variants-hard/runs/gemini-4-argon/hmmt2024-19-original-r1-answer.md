Para encontrar el número de ternas $(f, g, h)$ de permutaciones en el grupo simétrico $S_5$ que cumplen las condiciones dadas, trabajamos directamente con la composición de permutaciones en el grupo $S_5$:

$$\begin{aligned}
fgh &= hgf = g, \quad (1) \\
ghf &= fhg = h, \quad (2) \\
hfg &= gfh = f. \quad (3)
\end{aligned}$$

### Paso 1: Simplificación algebraica de las ecuaciones
De $fgh = g$, multiplicando por $f^{-1}$ por la izquierda obtenemos:
$$gh = f^{-1}g$$

Sustituyendo $gh$ en la ecuación $ghf = h$, resulta:
$$f^{-1}gf = h$$

Por otro lado, de la ecuación $gfh = f$, despejando $h$ al multiplicar por $(gf)^{-1} = f^{-1}g^{-1}$ por la izquierda, obtenemos:
$$h = f^{-1}g^{-1}f$$

Igualando ambas expresiones para $h$:
$$f^{-1}gf = f^{-1}g^{-1}f \implies g = g^{-1} \implies g^2 = e$$
donde $e$ es la permutación identidad.

Como el sistema de ecuaciones es completamente simétrico respecto a $f, g$ y $h$, se deduce de manera análoga que las tres permutaciones son involuciones:
$$f^2 = g^2 = h^2 = e$$

Usando que $f^{-1} = f$, la relación $h = f^{-1}gf$ se convierte en $h = fgf$. De igual manera, de $hgf = g$ y $ghf = h$ (o por simetría entre $f$ y $g$), tenemos que $h = gfg$. Igualando ambas expresiones para $h$:
$$fgf = gfg \iff (fg)^3 = e$$

Recíprocamente, si $f^2 = e$, $g^2 = e$ y $(fg)^3 = e$ (lo que equivale a $fgf = gfg$), al definir $h = fgf = gfg$ se cumple que $h^2 = (fgf)(fgf) = e$ y se satisfacen las seis igualdades originales:
- $fgh = fg(fgf) = f(gfg)f = f(fgf)f = f^2gf^2 = g$
- $hgf = (fgf)gf = f(gfg)f = g$
- $ghf = g(fgf)f = gfg = h$
- $fhg = f(gfg)g = fgf = h$
- $hfg = (gfg)fg = g(fgf)g = f$
- $gfh = gf(gfg) = g(fgf)g = f$

Por lo tanto, el número de ternas $(f, g, h)$ buscadas es igual al número de pares $(f, g) \in S_5 \times S_5$ tales que $f^2 = e$, $g^2 = e$ y $(fg)^3 = e$.

---

### Paso 2: Conteo de pares $(f, g)$ mediante el producto $u = fg$
Sea $u = fg$. Como $f^2 = e$, tenemos que $g = fu$.
Las condiciones sobre $(f, g)$ equivalen a las siguientes condiciones sobre el par $(u, f)$:
1. $u^3 = e$
2. $f^2 = e$
3. $g^2 = e \iff (fu)(fu) = e \iff fuf^{-1} = u^{-1}$ (ya que $f = f^{-1}$)

Analizamos los posibles elementos $u \in S_5$ tales que $u^3 = e$. En $S_5$, un elemento tiene orden divisor de $3$ si y solo si es la identidad o es un $3$-ciclo.

#### Caso 1: $u = e$
- Hay $1$ sola elección para $u = e$.
- La condición $fuf^{-1} = u^{-1}$ se cumple trivialmente, por lo que $f$ puede ser cualquier involución en $S_5$ ($f^2 = e$).
- Contamos las involuciones en $S_5$ según su estructura de ciclos:
  - Identidad (cero $2$-ciclos): $1$
  - Una transposición (un $2$-ciclo): $\binom{5}{2} = 10$
  - Dos transposiciones disjuntas (dos $2$-ciclos): $\frac{1}{2}\binom{5}{2}\binom{3}{2} = 15$
  - Total de involuciones: $1 + 10 + 15 = 26$.

Este caso aporta $1 \times 26 = 26$ soluciones.

#### Caso 2: $u$ es un $3$-ciclo
- El número de $3$-ciclos en $S_5$ es $\binom{5}{3} \times 2! = 10 \times 2 = 20$.
- Fijemos un $3$-ciclo, por ejemplo $u = (1\ 2\ 3)(4)(5)$, de modo que $u^{-1} = (1\ 3\ 2)(4)(5)$.
- Buscamos el número de involuciones $f \in S_5$ tales que $fuf^{-1} = (f(1)\ f(2)\ f(3))(f(4))(f(5)) = (1\ 3\ 2)(4)(5)$.
- Esto requiere que $f$ deje invariante el conjunto $\{1, 2, 3\}$ y el conjunto de puntos fijos $\{4, 5\}$:
  - En $\{1, 2, 3\}$, para que $(f(1)\ f(2)\ f(3)) = (1\ 3\ 2)$ y $f^2 = e$, $f$ debe restringirse a una de las $3$ transposiciones de $\{1, 2, 3\}$: $(1\ 2)$, $(2\ 3)$ o $(1\ 3)$. (Hay $3$ opciones).
  - En $\{4, 5\}$, $f$ puede actuar como la identidad $(4)(5)$ o como la transposición $(4\ 5)$, ambas de orden divisor de $2$. (Hay $2$ opciones).
- Así, para cada $3$-ciclo $u$, existen $3 \times 2 = 6$ involuciones $f$.

Este caso aporta $20 \times 6 = 120$ soluciones.

---

### Paso 3: Suma total
Sumando las soluciones de ambos casos obtenemos el total de ternas $(f, g, h)$:
$$26 + 120 = 146$$

\boxed{146}