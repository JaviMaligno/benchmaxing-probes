Sea \(f(t)=t^2-4t+6\). Los puntos fijos de \(f\) cumplen
\[
f(t)=t\iff t^2-5t+6=0\iff t=2\ \text{o}\ t=3.
\]

Analizamos las raíces, contando multiplicidad:

1. **Raíz doble:** debe ser un punto fijo, lo que da las ecuaciones
   \[
   (x-2)^2=0,\qquad (x-3)^2=0.
   \]

2. **Dos raíces distintas, ambas fijas:** son \(2\) y \(3\), dando
   \[
   (x-2)(x-3)=0.
   \]

3. **Exactamente una raíz fija:**
   - Si la raíz fija es \(2\), otra raíz \(r\) debería cumplir \(f(r)=2\), pero esto implica \((r-2)^2=0\), imposible por ser distinta.
   - Si la raíz fija es \(3\), entonces \(f(r)=3\) da \(r=1\) o \(r=3\). Así obtenemos
     \[
     (x-1)(x-3)=0.
     \]

4. **Ninguna raíz es fija:** las dos raíces \(r,s\) deben intercambiarse: \(f(r)=s\) y \(f(s)=r\). Restando estas igualdadades se obtiene \(r+s=3\), y sustituyendo \(s=3-r\) en \(f(r)=s\):
   \[
   r^2-3r+3=0.
   \]
   Por tanto, la ecuación buscada es
   \[
   x^2-3x+3=0.
   \]

En total hay \(2+1+1+1=5\) ecuaciones.

\[
\boxed{5}
\]