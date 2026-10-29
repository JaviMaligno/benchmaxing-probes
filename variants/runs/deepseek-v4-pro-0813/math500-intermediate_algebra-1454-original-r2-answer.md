Razonemos paso a paso.

Tenemos que minimizar

\[
F(x,y)=\sqrt{x^2+400}+\sqrt{y^2+900}+\sqrt{x^2+y^2-80x-100y+4100},
\]

donde \(0\le x\le 40\), \(0\le y\le 50\).

Primero completamos cuadrados en el tercer radicando:

\[
x^2+y^2-80x-100y+4100
=(x-40)^2+(y-50)^2+4100-1600-2500
=(x-40)^2+(y-50)^2.
\]

Por lo tanto,

\[
F(x,y)=\sqrt{x^2+20^2}+\sqrt{y^2+30^2}+\sqrt{(x-40)^2+(y-50)^2}.
\]

Interpretación geométrica. Sean:

- \(A=(0,-20)\), \(B=(0,0)\), \(C=(40,50)\),
- y un punto \(P=(x,y)\) con \(0\le x\le 40\), \(0\le y\le 50\).

Entonces:

\[
\sqrt{x^2+20^2}=\sqrt{(x-0)^2+(y-(-20))^2}=|PA|,
\]

\[
\sqrt{y^2+30^2}=\sqrt{(x-0)^2+(y-(-30))^2}=|PB|,
\]

y

\[
\sqrt{(x-40)^2+(y-50)^2}=|PC|.
\]

Así que queremos minimizar

\[
|PA|+|PB|+|PC|.
\]

Sin embargo, conviene notar que \(A\) y \(B\) están ambos sobre la vertical \(x=0\), uno en \(y=-20\) y el otro en \(y=-30\). La suma

\[
|PA|+|PB|
\]

es la suma de distancias desde \(P\) a dos puntos fijos en una misma recta vertical.

Para un \(x\) fijo, la suma

\[
\sqrt{x^2+20^2}+\sqrt{x^2+30^2}
\]

depende solo de \(x\), no de \(y\). Para minimizar la suma respecto a \(x\), por convexidad y simetría, el mínimo se puede buscar derivando:

Sea

\[
f(x)=\sqrt{x^2+400}+\sqrt{x^2+900}.
\]

Entonces

\[
f'(x)=\frac{x}{\sqrt{x^2+400}}+\frac{x}{\sqrt{x^2+900}}.
\]

Como \(x\ge 0\), se tiene \(f'(x)>0\) para \(x>0\), y \(f'(0)=0\). Por tanto, \(f(x)\) es creciente y su mínimo en \([0,40]\) ocurre en \(x=0\).

Así que parece óptimo tomar \(x=0\). Con \(x=0\),

\[
F(0,y)=\sqrt{400}+\sqrt{y^2+900}+\sqrt{(y-50)^2+1600}.
\]

Es decir,

\[
F(0,y)=20+\sqrt{y^2+900}+\sqrt{(y-50)^2+40^2}.
\]

Ahora minimizamos

\[
g(y)=\sqrt{y^2+900}+\sqrt{(y-50)^2+1600}
\]

para \(0\le y\le 50\).

Geométricamente, esto es la suma de distancias desde el punto \(Q=(0,y)\) a los puntos \((-30,0)\) y \((40,50)\), pero en la forma anterior es más fácil derivar:

\[
g'(y)=\frac{y}{\sqrt{y^2+900}}+\frac{y-50}{\sqrt{(y-50)^2+1600}}.
\]

Igualamos a cero:

\[
\frac{y}{\sqrt{y^2+900}}=\frac{50-y}{\sqrt{(y-50)^2+1600}}.
\]

Elevamos al cuadrado:

\[
\frac{y^2}{y^2+900}=\frac{(50-y)^2}{(50-y)^2+1600}.
\]

Multiplicamos en cruz:

\[
y^2\bigl((50-y)^2+1600\bigr)=(50-y)^2(y^2+900).
\]

Desarrollando,

\[
y^2(50-y)^2+1600y^2=y^2(50-y)^2+900(50-y)^2.
\]

Cancelamos \(y^2(50-y)^2\):

\[
1600y^2=900(50-y)^2.
\]

Dividiendo entre \(100\):

\[
16y^2=9(50-y)^2.
\]

Tomando raíz cuadrada no negativa,

\[
4y=3(50-y).
\]

Por tanto,

\[
4y=150-3y,
\]

\[
7y=150,
\]

\[
y=\frac{150}{7}.
\]

Este valor está dentro del intervalo \([0,50]\). Sustituimos:

\[
50-y=50-\frac{150}{7}=\frac{350-150}{7}=\frac{200}{7}.
\]

Entonces:

\[
\sqrt{y^2+900}
=\sqrt{\left(\frac{150}{7}\right)^2+900}
=\sqrt{\frac{22500}{49}+\frac{44100}{49}}
=\sqrt{\frac{66600}{49}}
=\frac{\sqrt{66600}}{7}.
\]

Observamos

\[
66600=900\cdot 74=900\cdot 74,
\]

luego

\[
\sqrt{66600}=30\sqrt{74}.
\]

Así,

\[
\sqrt{y^2+900}=\frac{30\sqrt{74}}{7}.
\]

Por otro lado,

\[
\sqrt{(50-y)^2+1600}
=\sqrt{\left(\frac{200}{7}\right)^2+1600}
=\sqrt{\frac{40000}{49}+\frac{78400}{49}}
=\sqrt{\frac{118400}{49}}
=\frac{\sqrt{118400}}{7}.
\]

Como

\[
118400=1600\cdot 74,
\]

tenemos

\[
\sqrt{118400}=40\sqrt{74}.
\]

Por lo tanto,

\[
\sqrt{(50-y)^2+1600}=\frac{40\sqrt{74}}{7}.
\]

Así,

\[
g\left(\frac{150}{7}\right)
=\frac{30\sqrt{74}}{7}+\frac{40\sqrt{74}}{7}
=\frac{70\sqrt{74}}{7}
=10\sqrt{74}.
\]

Finalmente,

\[
F_{\min}=20+g_{\min}=20+10\sqrt{74}.
\]

Por lo tanto, el mínimo pedido es

\[
\boxed{20+10\sqrt{74}}.
\]