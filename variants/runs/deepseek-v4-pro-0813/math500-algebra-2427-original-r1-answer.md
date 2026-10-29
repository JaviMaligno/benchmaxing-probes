Vamos a razonar paso a paso.

El trabajador gana $20{,}000$ al año y deposita esa cantidad al final de cada año. Quiere que, justo al final del tercer año (después del tercer depósito), tenga al menos $66{,}200$.

Sea $r$ la tasa de interés compuesta anual (en forma decimal). El dinero depositado al final de cada año genera intereses en los años siguientes.

- Primer depósito ($20{,}000$) al final del año 1: genera intereses durante 2 años, así que vale
  \[
  20000(1+r)^2.
  \]
- Segundo depósito ($20{,}000$) al final del año 2: genera intereses durante 1 año, así que vale
  \[
  20000(1+r).
  \]
- Tercer depósito ($20{,}000$) al final del año 3: no genera intereses todavía, vale
  \[
  20000.
  \]

Por lo tanto, al final del tercer año, el saldo total es

\[
20000(1+r)^2 + 20000(1+r) + 20000 \ge 66200.
\]

Dividimos todo entre $20000$:

\[
(1+r)^2 + (1+r) + 1 \ge 3{,}31.
\]

Sea $x = 1+r$. Entonces

\[
x^2 + x + 1 \ge 3{,}31.
\]

Restamos $3{,}31$:

\[
x^2 + x - 2{,}31 \ge 0.
\]

Resolvemos la ecuación

\[
x^2 + x - 2{,}31 = 0.
\]

Aplicamos la fórmula cuadrática:

\[
x = \frac{-1 \pm \sqrt{1 + 4 \cdot 2{,}31}}{2}
   = \frac{-1 \pm \sqrt{1 + 9{,}24}}{2}
   = \frac{-1 \pm \sqrt{10{,}24}}{2}.
\]

Como $\sqrt{10{,}24} = 3{,}2$,

\[
x = \frac{-1 \pm 3{,}2}{2}.
\]

La solución positiva es

\[
x = \frac{-1 + 3{,}2}{2} = \frac{2{,}2}{2} = 1{,}1.
\]

Por lo tanto,

\[
1 + r = 1{,}1 \implies r = 0{,}1 = 10\%.
\]

El saldo correspondiente sería

\[
20000(1{,}1)^2 + 20000(1{,}1) + 20000
= 24200 + 22000 + 20000
= 66200,
\]

que cumple exactamente el requisito.

La tasa de interés compuesta mínima es $10\%$.

\[
\boxed{10}
\]