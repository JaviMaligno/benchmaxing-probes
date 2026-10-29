## Planteamiento

Escribo las permutaciones como elementos de $S_5$ con composición. Las condiciones son:

$$fgh = hgf = g,\qquad ghf = fhg = h,\qquad hfg = gfh = f.$$

**Paso 1: expresar $h$ en función de $f,g$.** De $fgh = g$ se obtiene $h = g^{-1}f^{-1}g$.

**Paso 2: reducir las demás ecuaciones.** Sustituyendo $h = g^{-1}f^{-1}g$:

- $fhg = h$ da $gfg^{-1} = f^{-1}g^{-1}f$.
- $gfh = f$ da $gfg^{-1} = fg^{-1}f$.

Igualando ambas expresiones de $gfg^{-1}$: $f^{-1}g^{-1}f = fg^{-1}f$, de donde $f^{-1} = f$, es decir $f^2 = e$. El sistema es cíclicamente simétrico en $(f,g,h)$, así que también $g^2 = h^2 = e$: **las tres permutaciones son involuciones** (incluyendo la identidad).

**Paso 3: condición restante.** Con $f^2 = g^2 = e$, queda $h = gfg$, y la ecuación $hfg = f$ (y todas las demás) se reduce a la relación de trenza:

$$fgf = gfg.$$

Verificación: con $f^2=g^2=e$, $fgf=gfg$ y $h = gfg = fgf$, las seis ecuaciones se cumplen (por ejemplo, $fgh = fg\cdot gfg = f\cdot fg = g$ ✓).

Además, con $f^2=g^2=e$, la relación $fgf = gfg$ equivale a $(fg)^3 = e$, o sea que $fg$ tiene orden $1$ o $3$.

**Paso 4: conteo de pares $(f,g)$.** Las involuciones de $S_5$ (incluida $e$) son: $1 + 10$ transposiciones $+ 15$ dobles transposiciones $= 26$.

*Caso $fg = e$:* entonces $g = f$, lo que da $26$ pares.

*Caso $fg = \sigma$ un 3-ciclo:* hay $20$ tres-ciclos en $S_5$. Para cada $\sigma$, necesito involuciones $f$ con $g = f\sigma$ también involución, es decir $(f\sigma)^2 = e \iff f\sigma f = \sigma^{-1}$. Tal $f$ debe preservar el soporte $\{a,b,c\}$ de $\sigma$ y actuar ahí como una de las $3$ transposiciones que invierten el ciclo; en los $2$ puntos fijos restantes puede actuar como $e$ o como la transposición, y toda combinación es una involución. Son $3 \times 2 = 6$ opciones de $f$ por cada $\sigma$, dando $20 \times 6 = 120$ pares.

**Total:** cada par $(f,g)$ determina $h = fgf$ de forma única, así que hay

$$26 + 120 = 146$$

triples.

$$\boxed{146}$$