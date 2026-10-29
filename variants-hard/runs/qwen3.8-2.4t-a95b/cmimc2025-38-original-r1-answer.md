

Sean  
\[
a=-1+2i,\qquad b=-1-2i
\]
las raíces de \(x^2+2x+5\), y sean \(c,d\) las raíces de \(x^2-2mx+25\). Entonces
\[
c+d=2m,\qquad cd=25,\qquad d=\frac{25}{c}.
\]

Todo círculo que pasa por \(a\) y \(b\) tiene centro sobre el eje real. Si su centro es \(h\in\mathbb R\), su ecuación es
\[
|z-h|^2=(h+1)^2+4
\]
o, equivalentemente,
\[
|z|^2-h(z+\bar z)-2h-5=0. \tag{1}
\]

Para que \(c,d\) estén en el mismo círculo que \(a,b\), deben satisfacer (1). Escribiendo \(t=|c|^2\) y \(s=c+\bar c\), y usando \(d=25/c\), las dos ecuaciones dan, al restarlas,
\[
\frac{t-25}{t}\bigl(t+25-hs\bigr)=0.
\]

### Caso 1: \(t=25\)

Entonces \(|c|=5\), luego \(d=25/c=\bar c\), y
\[
m=\frac{c+d}{2}=\operatorname{Re}(c).
\]
Al recorrer \(c\) la circunferencia \(|c|=5\), \(m\) recorre el segmento real
\[
[-5,5].
\]
El punto \(m=-1\) corresponde a cuatro puntos colineales; se incluya o no, no afecta la longitud. La longitud de este segmento es
\[
10.
\]

### Caso 2: \(t\neq 25\)

Entonces \(hs=t+25\). Sustituyendo en (1):
\[
t-(t+25)-2h-5=0 \implies h=-15.
\]
Luego
\[
t+25=-15s \iff |c+15|^2=200.
\]
Así, \(c\) y \(d\) están en la circunferencia
\[
\Gamma:\ |z+15|=10\sqrt2,
\]
la cual también contiene a \(a,b\).

Ahora,
\[
|(c+15)(d+15)|=(10\sqrt2)^2=200.
\]
Pero
\[
(c+15)(d+15)=cd+15(c+d)+225=25+30m+225=10(3m+25).
\]
Por tanto,
\[
|3m+25|=20
\]
o
\[
\left|m+\frac{25}{3}\right|=\frac{20}{3}.
\]
Esto es una circunferencia de radio \(20/3\). Recíprocamente, todo punto de esa circunferencia produce raíces sobre \(\Gamma\), de modo que aporta la circunferencia completa.

Su longitud es
\[
2\pi\cdot \frac{20}{3}=\frac{40\pi}{3}.
\]

El segmento y la circunferencia solo se intersectan en un punto, \(m=-5/3\), por lo que las longitudes se suman.

\[
\boxed{10+\frac{40\pi}{3}}
\]