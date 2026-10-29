## Planteamiento

**Paso 1: los triángulos laterales son 30‑60‑90.**

En $\triangle ABC$: $AC^2 = 14^2+7^2-2\cdot14\cdot7\cos 60^\circ = 147$, luego $AC = 7\sqrt3$. Como $7^2+147=14^2$, resulta $\angle ACB = 90^\circ$ y $\angle BAC = 30^\circ$.

En $\triangle AED$: $AD^2 = 26^2+13^2-2\cdot26\cdot13\cos 60^\circ = 507$, luego $AD = 13\sqrt3$, con $\angle ADE=90^\circ$ y $\angle DAE=30^\circ$.

**Paso 2: cota inferior.** Agrupando,
$$f(X) = (BX+EX) + (AX+CX+DX) \ge BE + \min_Y (AY+CY+DY).$$

En $\triangle ACD$: $\cos\angle CAD = \dfrac{147+507-576}{2\cdot7\sqrt3\cdot13\sqrt3} = \dfrac{78}{546}=\dfrac17$, así que $\sin\angle CAD = \dfrac{4\sqrt3}{7}$ y $[ACD] = \tfrac12\cdot7\sqrt3\cdot13\sqrt3\cdot\tfrac{4\sqrt3}{7} = 78\sqrt3$.

El punto de Fermat da
$$\min_Y(AY+CY+DY) = \sqrt{\tfrac{a^2+b^2+c^2}{2}+2\sqrt3\,[ACD]} = \sqrt{615+468} = \sqrt{1083}=19\sqrt3 .$$

Para $BE$: $\cos\angle BAE = \cos(60^\circ+\angle CAD) = \tfrac12\cdot\tfrac17-\tfrac{\sqrt3}{2}\cdot\tfrac{4\sqrt3}{7} = -\tfrac{11}{14}$, de donde
$$BE^2 = 196+676+2\cdot14\cdot26\cdot\tfrac{11}{14}=1444,\qquad BE=38.$$

**Paso 3: la igualdad se alcanza.** Sea $X$ el punto de Fermat de $\triangle ACD$, con $\angle AXC=\angle AXD=120^\circ$.

- Como $\angle ABC = 60^\circ$ y $\angle AXC = 120^\circ$ son suplementarios, $A,B,C,X$ son concíclicos; el radio es $\frac{7\sqrt3}{2\sin 120^\circ}=7$, luego $AB=14$ es diámetro y $\angle AXB = 90^\circ$.
- Análogamente, $\angle AED=60^\circ$ hace concíclicos a $A,E,D,X$, con $AE=26$ como diámetro, luego $\angle AXE = 90^\circ$.

Entonces $\angle BXE = 90^\circ+90^\circ = 180^\circ$: los puntos $B,X,E$ son colineales con $X$ entre $B$ y $E$, así que $BX+EX = BE$ exactamente en ese mismo punto.

Por tanto
$$f_{\min} = 38 + 19\sqrt3 \approx 70.909,$$
valor confirmado por minimización numérica directa con coordenadas (iteraciones de Weiszfeld convergen a $\approx 70.91$).

Así $m=38$, $n=19$, $p=3$ y $m+n+p = 60$.

\boxed{60}