## Planteamiento

Coloco el centro $P$ de $\omega_1$ en el origen. Como $\omega_1$ (radio 4) es tangente internamente a $\omega_2$ (radio 20) en $Q$, el centro $O$ de $\omega_2$ está a distancia $20-4=16$ de $P$, colineal con $Q$:
- $P = (0,0)$, $Q = (4, 0)$, $O = (-16, 0)$.

**Punto R:** $\overline{QR}$ es diámetro de $\omega_2$, así que $R = 2O - Q = (-36, 0)$. La recta $QR$ es el eje $x$.

**Punto S:** $\overline{PS} \perp \overline{QR}$ implica que $S$ está en la recta $x=0$. Sobre $\omega_2$: $16^2 + y^2 = 400 \Rightarrow y = \pm 12$.

**Rectángulo:** $\overline{KL} \perp \overline{QR}$ significa lados $KL$ y $MN$ verticales. Tomo
$$K=(a,b),\quad L=(a,-b),\quad M=(-a,-b),\quad N=(-a,b),\qquad a^2+b^2=16,\ a,b>0.$$

- $R=(-36,0)$ está más cerca de $MN$ (recta $x=-a$) que de $KL$ (recta $x=a$), pues $36-a < 36+a$. ✓
- Para que $S$ esté más cerca de $LM$ (recta $y=-b$) que de $KN$ (recta $y=b$), tomo $S=(0,-12)$: entonces $12-b < 12+b$. ✓

## Condición de áreas iguales

**$\triangle SML$:** base $ML = 2a$, altura $= 12 - b$, así que el área es $a(12-b)$.

**$\triangle RNM$:** base $NM = 2b$, altura $= 36 - a$, así que el área es $b(36-a)$.

Igualando:
$$12a - ab = 36b - ab \quad\Longrightarrow\quad 12a = 36b \quad\Longrightarrow\quad a = 3b.$$

## Cálculo del área

Sustituyendo en $a^2 + b^2 = 16$:
$$9b^2 + b^2 = 16 \quad\Longrightarrow\quad b^2 = \frac{8}{5}.$$

El área del rectángulo es
$$(2a)(2b) = 4ab = 4\cdot 3b^2 = 12 \cdot \frac{8}{5} = \frac{96}{5}.$$

Como $\gcd(96,5)=1$, tenemos $m=96$, $n=5$, y por tanto $m+n = 101$.

$$\boxed{101}$$