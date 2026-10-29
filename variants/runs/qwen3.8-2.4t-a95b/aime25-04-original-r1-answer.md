Factorizamos la expresión:

\[
12x^2-xy-6y^2=(4x-3y)(3x+2y).
\]

Por lo tanto, necesitamos que

\[
(4x-3y)(3x+2y)=0.
\]

Así que las soluciones enteras provienen de dos rectas:

1. \(4x-3y=0 \Rightarrow 4x=3y\).  
   Como \(\gcd(4,3)=1\), las soluciones enteras son
   \[
   x=3t,\quad y=4t.
   \]
   Para que ambos estén entre \(-100\) y \(100\):
   \[
   |3t|\le 100 \Rightarrow |t|\le 33,
   \]
   \[
   |4t|\le 100 \Rightarrow |t|\le 25.
   \]
   Luego \(|t|\le 25\), dando \(51\) soluciones.

2. \(3x+2y=0 \Rightarrow 3x=-2y\).  
   Como \(\gcd(3,2)=1\), las soluciones enteras son
   \[
   x=2t,\quad y=-3t.
   \]
   Para que ambos estén entre \(-100\) y \(100\):
   \[
   |2t|\le 100 \Rightarrow |t|\le 50,
   \]
   \[
   |3t|\le 100 \Rightarrow |t|\le 33.
   \]
   Luego \(|t|\le 33\), dando \(67\) soluciones.

La única solución que pertenece a ambas familias es \((0,0)\), así que descontamos una repetición:

\[
51+67-1=117.
\]

\[
\boxed{117}
\]