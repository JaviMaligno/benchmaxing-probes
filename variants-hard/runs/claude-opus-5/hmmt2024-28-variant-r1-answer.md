## Planteamiento

Coloco $X$ en el origen. En el pentágono convexo $PQXRS$ el ángulo interior en $X$ es $\angle QXR=120^\circ$, y las diagonales $XP$, $XS$ quedan dentro de él:

$$\angle QXP=a,\qquad \angle PXS=90^\circ,\qquad \angle SXR=b,\qquad a+b=30^\circ .$$

**Uso de la tangencia.** Las circunferencias de $XPQ$ y $XRS$ son tangentes internamente en $X$, luego comparten la recta tangente $\ell$ en $X$. Midiendo ángulos desde $\ell$, todos los rayos caen del mismo lado, y por el ángulo semiinscrito cada cuerda desde $X$ vale $2R\sin(\text{ángulo con }\ell)$. Si $\varphi$ es el ángulo de $XP$ con $\ell$ y $L=PQ=RS$, se obtiene:

- Triángulo $XPQ$: $XP=m$ con $m^2=9+L^2+6L\cos\varphi$, y $m\sin a=L\sin\varphi$.
- Triángulo $XRS$: $XS=n$ con $n^2=36+L^2+12L\sin\varphi$, y $n\sin b=L\cos\varphi$.

## Modelo vectorial

Sea $W=(X,Y)=L(\cos\varphi,\sin\varphi)$, $A=(3,0)$, $B=(0,6)$ (perpendiculares, longitudes $QX$ y $RX$). Entonces
$$m=|W+A|,\qquad n=|W+B|,$$
y $a$ es el ángulo entre $A$ y $W+A$, $b$ el ángulo entre $B$ y $W+B$. Como $\angle(A,B)=90^\circ$ y $a+b=30^\circ$:
$$\angle(W+A,\;W+B)=60^\circ .$$

Con $A'=-A$, $B'=-B$ esto es el ángulo en $W$ del triángulo $A'WB'$, con $|A'B'|^2=45$. Por el teorema del coseno:
$$45=m^2+n^2-mn\;\Longrightarrow\; mn=2(X^2+Y^2)+6X+12Y,$$
es decir, siendo $[XPS]=\tfrac12 mn\sin 90^\circ=S$:
$$\boxed{\,}\quad S=X^2+Y^2+3X+6Y .$$

Equivalentemente, de $\tan(a+b)=\tfrac{1}{\sqrt3}$ sale $\sqrt3\,(X^2+Y^2+3X+6Y)=18+6X+3Y$, o sea
$$S=\sqrt3\,(6+2X+Y).$$

## Área del pentágono

$$[XPQ]=\tfrac12\cdot 3\cdot m\sin a=\tfrac32 Y,\qquad [XSR]=\tfrac12\cdot 6\cdot n\sin b=3X,$$
$$27=[XPQ]+[XPS]+[XSR]=\tfrac32 Y+3X+S\;\Longrightarrow\; S=27-\tfrac32(2X+Y).$$

## Resolución

Con $k=2X+Y$:
$$\sqrt3(6+k)=27-\tfrac32 k\;\Longrightarrow\;k=\frac{54-12\sqrt3}{3+2\sqrt3}=48\sqrt3-78 .$$

$$S=27-\tfrac32(48\sqrt3-78)=27+117-72\sqrt3=144-72\sqrt3 .$$

(Comprobación: $X\approx1.885$, $Y\approx1.369$ dan $X,Y>0$, $a\approx15.7^\circ$, $b\approx14.3^\circ$, y área total $27$.)

$$\boxed{144-72\sqrt{3}}$$