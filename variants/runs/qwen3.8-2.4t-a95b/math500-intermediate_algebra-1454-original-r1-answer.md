

Sean

\[
S=\sqrt{x^2+400}+\sqrt{y^2+900}+\sqrt{x^2+y^2-80x-100y+4100}.
\]

Primero reescribimos el tercer término completando cuadrados:

\[
x^2+y^2-80x-100y+4100=(40-x)^2+(50-y)^2.
\]

Así,

\[
S=\sqrt{x^2+20^2}+\sqrt{y^2+30^2}+\sqrt{(40-x)^2+(50-y)^2}.
\]

Como \(0\le x\le 40\) y \(0\le y\le 50\), todos los números \(x,20,y,30,40-x,50-y\) son no negativos.

Usamos la desigualdad

\[
\sqrt{a^2+b^2}\ge \frac{a+b}{\sqrt2},
\]

válida para \(a,b\ge 0\), con igualdad si y solo si \(a=b\).

Aplicándola a cada término:

\[
\sqrt{x^2+20^2}\ge \frac{x+20}{\sqrt2},
\]

\[
\sqrt{y^2+30^2}\ge \frac{y+30}{\sqrt2},
\]

\[
\sqrt{(40-x)^2+(50-y)^2}\ge \frac{(40-x)+(50-y)}{\sqrt2}.
\]

Sumando,

\[
S\ge \frac{x+20+y+30+40-x+50-y}{\sqrt2}.
\]

Los términos \(x\) y \(y\) se cancelan:

\[
S\ge \frac{140}{\sqrt2}=70\sqrt2.
\]

La igualdad ocurre cuando

\[
x=20,\qquad y=30,\qquad 40-x=50-y,
\]

lo cual es consistente, pues \(40-20=50-30=20\). Además \((x,y)=(20,30)\) está dentro del dominio dado.

Por lo tanto, el valor mínimo es

\[
\boxed{70\sqrt2}
\]