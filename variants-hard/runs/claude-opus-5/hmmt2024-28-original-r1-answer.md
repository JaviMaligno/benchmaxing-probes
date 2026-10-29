## Planteamiento

Pongo $T$ en el origen con la **tangente común** en $T$ como eje $x$ (las dos circunferencias quedan del mismo lado: tangencia interna). Si una circunferencia pasa por $T$, es tangente al eje $x$ en $T$ y tiene diámetro $d$, entonces un punto $P$ suyo en el rayo de ángulo $\theta$ cumple $TP=d\sin\theta$.

Orden angular (convexidad, $\angle BTC=120^\circ$, $\angle ATD=90^\circ$): $\theta_B=\phi,\ \theta_A=\phi+x,\ \theta_D=\phi+x+90^\circ,\ \theta_C=\phi+120^\circ$, con $x+y=30^\circ$ ($y=\angle DTC$). Con $u,v$ los diámetros y $\phi'=60^\circ-\phi$:

$$TB=u\sin\phi=4,\quad TA=u\sin(\phi+x),\quad AB=u\sin x$$
$$TC=v\sin\phi'=5,\quad TD=v\sin(\phi'+y),\quad CD=v\sin y$$

Como $(\phi+x)+(\phi'+y)=90^\circ$, escribo $s=\phi+x$, $S=\sin s$, $C=\cos s$, de modo que $TA=uS$, $TD=vC$.

## Reducción

Sea $m=AB=CD$, $P=\cot\phi$, $Q=\cot\phi'$. De $\phi+\phi'=60^\circ$ sale $\sqrt3\,PQ=P+Q+\sqrt3$, y de $\cot\phi+\cot\phi'=\tfrac{\sin 60^\circ}{\sin\phi\sin\phi'}$ se obtiene
$$uv=\frac{20}{\sin\phi\sin\phi'}=40(PQ-1).$$

De $m=u\sin(s-\phi)$ y $m=v\sin\big((90^\circ-s)-\phi'\big)$:
$$P=\frac{m+4C}{4S},\qquad Q=\frac{m+5S}{5C}.$$

Con $X=mS$, $Y=mC$ (así $X^2+Y^2=m^2$) y $K=[TAD]=\tfrac12 uvSC=(m+4C)(m+5S)-20SC$:

$$K=X^2+Y^2+5X+4Y.$$

**Área del pentágono:** $[TAB]=\tfrac12 TA\cdot TB\sin x=2mS=2X$ … más precisamente $[TAB]=2mS$, $[TDC]=\tfrac52 mC$, luego
$$22=2X+\tfrac52 Y+K\ \Longrightarrow\ 4X+5Y=44-2K.$$

**Tangencia** ($\sqrt3PQ=P+Q+\sqrt3$), tras multiplicar por $20SC$ y cancelar $20\sqrt3\,SC$:
$$\sqrt3\,(m^2+5mS+4mC)=4mS+5mC+20\ \Longrightarrow\ \sqrt3\,K=4X+5Y+20.$$

## Conclusión

$$\sqrt3\,K=(44-2K)+20=64-2K\ \Longrightarrow\ K(2+\sqrt3)=64.$$

$$K=\frac{64}{2+\sqrt3}=128-64\sqrt3\approx 17{,}15.$$

(Verificación numérica: $\phi\approx58{,}2^\circ$, $s\approx87{,}4^\circ$, $m\approx2{,}29$ dan un pentágono convexo de área $22$ con $AB=CD$ y $[TAD]\approx17{,}15$.)

$$\boxed{128-64\sqrt{3}}$$