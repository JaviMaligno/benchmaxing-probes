Sea
\[
E=\frac{(a+b+c)\left[(a+b)^2+(a+b+4c)^2\right]}{abc}.
\]

Ponemos \(x=a+b\). Para \(x,c\) fijos, el numerador solo depende de \(x\) y \(c\), mientras que
\[
ab\le \left(\frac{a+b}{2}\right)^2=\frac{x^2}{4},
\]
con igualdad cuando \(a=b\). Por tanto,
\[
E\ge \frac{4(x+c)\left[x^2+(x+4c)^2\right]}{x^2c}.
\]

Como la expresión es homogénea, sea \(t=\frac{x}{c}>0\). Entonces
\[
E\ge 4\cdot \frac{(t+1)\left[t^2+(t+4)^2\right]}{t^2}
=8\cdot \frac{(t+1)(t^2+4t+8)}{t^2}.
\]
Expandimos:
\[
8\cdot \frac{(t+1)(t^2+4t+8)}{t^2}
=8t+40+\frac{96}{t}+\frac{64}{t^2}.
\]
Llamemos
\[
f(t)=8t+40+\frac{96}{t}+\frac{64}{t^2}.
\]
Derivamos:
\[
f'(t)=8-\frac{96}{t^2}-\frac{128}{t^3}.
\]
Igualando a cero:
\[
8-\frac{96}{t^2}-\frac{128}{t^3}=0
\]
\[
t^3-12t-16=0
\]
\[
(t-4)(t+2)^2=0.
\]
La única solución positiva es \(t=4\), y da el mínimo global.

Evaluamos:
\[
f(4)=8(4)+40+\frac{96}{4}+\frac{64}{16}
=32+40+24+4=100.
\]

La igualdad se alcanza cuando \(a=b\) y \(a+b=4c\), es decir, \(a=b=2c\). Por ejemplo, con \((a,b,c)=(2,2,1)\).

\[
\boxed{100}
\]