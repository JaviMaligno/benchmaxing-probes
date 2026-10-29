## Planteamiento

Como $\overline{PQ}$ es diámetro, $\angle PRQ=\angle PSQ=90^\circ$, luego
$$PR=\sqrt{20^2-12^2}=16,\qquad QS=\sqrt{20^2-8^2}=4\sqrt{21}.$$

Esto dice que, en el triángulo $TPQ$, los puntos $R$ y $S$ son los pies de las alturas desde $P$ y desde $Q$ ($PR\perp TQ$, $QS\perp TP$).

**Coordenadas.** Con $O=(0,0)$, $P=(-10,0)$, $Q=(10,0)$ y $k=\sqrt{21}$:
- $\cos\angle RPQ=\tfrac{16}{20}$ da $R=\left(\tfrac{14}{5},\tfrac{48}{5}\right)$,
- $\cos\angle SPQ=\tfrac{8}{20}$ da $S=\left(-\tfrac{34}{5},\tfrac{8k}{5}\right)$.

**Punto $T$.** La recta $QR$ es $(10-3t,\,4t)$ y la recta $PS$ es $(-10+2s,\,ks)$. Resolviendo, con $D=3k+8$:
$$T=\left(\frac{80-30k}{D},\ \frac{80k}{D}\right),\qquad TP=\frac{400}{D},\qquad TQ=\frac{100k}{D}.$$

**Lados de $TRS$.** Como $R\in \overline{TQ}$ y $S\in\overline{TP}$:
$$TR=TQ-12=\frac{64k-96}{D},\qquad TS=TP-8=\frac{336-24k}{D},\qquad \cos T=\frac{TR}{TP}=\frac{4k-6}{25},$$
y por la semejanza $TRS\sim TPQ$ (razón $\cos T$): $RS=20\cos T=\frac{16k-24}{5}$.

## Exincentro

Con $a=RS$, $b=TS$, $c=TR$, el exincentro opuesto a $T$ es
$$J=\frac{-a\,T+b\,R+c\,S}{-a+b+c}.$$

El denominador se simplifica notablemente: $b+c=\frac{40(k+6)}{D}$ y
$$-a+b+c=\frac{200(k+6)-8(2k-3)D}{5D}=\frac{144k+384}{5D}=\frac{48}{5}.$$

Para la ordenada, con denominador común $5D$:
$$5(384k-5376)+(16128-1152k)+(10752-768k)=0\cdot k+0=0,$$
así que $y_J=0$: **el exincentro está sobre la recta $PQ$.**

Para la abscisa:
$$-aT_x+bR_x+cS_x=\frac{19968-4512k}{5D}\ \Longrightarrow\ x_J=\frac{19968-4512k}{48D}=\frac{416-94k}{3k+8}.$$

Racionalizando (con $(3k)^2-64=125$):
$$x_J=\frac{(416-94k)(3k-8)}{125}=\frac{2000k-9250}{125}=16\sqrt{21}-74.$$

## Resultado

$$OJ=|x_J|=74-16\sqrt{21}\approx 0{,}6788.$$

(Verificación numérica: las distancias de $J\approx(-0{,}6788,\,0)$ a las rectas $TP$, $TQ$ y $RS$ valen todas $\approx 8{,}5430$, y $J$ queda al otro lado de $RS$ respecto de $T$.)

$$\boxed{74-16\sqrt{21}}$$