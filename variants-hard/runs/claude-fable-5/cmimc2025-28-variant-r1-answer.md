## Planteamiento con coordenadas

Coloco $O$ en el origen, con $P=(-10,0)$ y $Q=(10,0)$, de modo que $\Gamma: x^2+y^2=100$.

**Puntos R y S.** Como $PQ$ es diámetro, los ángulos $\angle PRQ$ y $\angle PSQ$ son rectos.

- $R$: de $x^2+y^2=100$ y $(x-10)^2+y^2=144$ sale $x=\tfrac{14}{5}$, $y=\tfrac{48}{5}$, es decir $R=(2.8,\,9.6)$ (y de paso $PR=16$).
- $S$: de $x^2+y^2=100$ y $(x+10)^2+y^2=64$ sale $x=-\tfrac{34}{5}$, $y=\tfrac{8\sqrt{21}}{5}$, es decir $S=(-6.8,\,1.6\sqrt{21})$.

**Punto T.** La recta $QR$ es $(10-3t,\,4t)$ y la recta $PS$ es $(-10+2s,\,\sqrt{21}\,s)$. Igualando:
$$t_T=\frac{252-32\sqrt{21}}{25},\qquad T=\left(\frac{96\sqrt{21}-506}{25},\ \frac{1008-128\sqrt{21}}{25}\right).$$

## Lados del triángulo $TRS$

Usando que cada parámetro avanza 5 unidades de longitud:

$$TR = 5t_T-12=\frac{192-32\sqrt{21}}{5},\qquad TS = 5s_T-8=\frac{48\sqrt{21}-168}{5}.$$

Para $RS$: $RS^2 = 9.6^2+\left(9.6-1.6\sqrt{21}\right)^2 = \tfrac{192(31-4\sqrt{21})}{25}$, y como $31-4\sqrt{21}=(2\sqrt7-\sqrt3)^2$,
$$RS=\frac{16\sqrt{21}-24}{5}.$$

## Excentro opuesto a $T$

Con $a=RS$, $b=TS$, $c=TR$, el excentro opuesto a $T$ es
$$J=\frac{-a\,T+b\,R+c\,S}{-a+b+c},\qquad -a+b+c=\frac{48}{5}.$$

**Coordenada $y$:** el numerador da
$$\frac{(67200-19200\sqrt{21})+(11520\sqrt{21}-40320)+(7680\sqrt{21}-26880)}{125}=0,$$
así que $J$ cae exactamente sobre la recta $PQ$ (¡el excentro queda en el diámetro!).

**Coordenada $x$:** el numerador da
$$\frac{(10400\sqrt{21}-44400)+(3360\sqrt{21}-11760)+(5440\sqrt{21}-32640)}{125}=\frac{19200\sqrt{21}-88800}{125},$$
y dividiendo entre $\tfrac{48}{5}$:
$$J_x = \frac{19200\sqrt{21}-88800}{1200}=16\sqrt{21}-74\approx -0.6788.$$

Por lo tanto, como $O$ es el origen:
$$OJ=|16\sqrt{21}-74| = 74-16\sqrt{21}\approx 0.679.$$

$$\boxed{74-16\sqrt{21}}$$