Sea \(f(c)=c^2-2\), y sean \(r,s\) las raíces, posiblemente iguales. La condición exige que \(f(r)\) y \(f(s)\) también pertenezcan a \(\{r,s\}\).

**1. Raíz doble (\(r=s\)).**  
Debe cumplirse \(f(r)=r\):
\[
r^2-2=r\implies r=2\quad\text{o}\quad r=-1.
\]
Esto da las ecuaciones
\[
(x-2)^2=0,\qquad (x+1)^2=0.
\]

**2. Dos raíces distintas, con al menos una fija.**  
Los puntos fijos son \(2\) y \(-1\). Pueden ser ambas raíces, dando
\[
(x-2)(x+1)=0.
\]
Si la otra raíz \(s\) se transforma en el punto fijo \(r\), entonces \(s^2-2=r\):

- Si \(r=2\), se obtiene \(s=-2\), dando \((x-2)(x+2)=0\).
- Si \(r=-1\), se obtiene \(s=1\), dando \((x+1)(x-1)=0\).

**3. Dos raíces distintas que se intercambian.**  
Se cumple
\[
r^2-2=s,\qquad s^2-2=r.
\]
Al restar y usar \(r\ne s\), resulta \(r+s=-1\). Por tanto,
\[
r^2-2=-1-r\implies r^2+r-1=0,
\]
y la ecuación cuadrática es \(x^2+x-1=0\).

En total hay \(2+1+2+1=\boxed{6}\).