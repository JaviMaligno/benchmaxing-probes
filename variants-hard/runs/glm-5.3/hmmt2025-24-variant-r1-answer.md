# Planteamiento

Coloco $\omega_3$ con centro en el origen $O=(0,0)$, radio $12$, y diámetro $PQ$ sobre el eje $x$, con $P=(-12,0)$ y $Q=(12,0)$; la región es el semiplano $y\ge 0$.

**Paso 1: Parametrizar $\omega_2$.**

Sea $C=(t,r)$ el centro de $\omega_2$ y $r$ su radio. Como el arco de $\omega_2$ es tangente a $PQ$ (el eje $x$), la distancia de $C$ al eje es $r$, y el punto de tangencia es $T=(t,0)$.

El diámetro de $\omega_2$ es una cuerda $AB$ de $\omega_3$ con $C$ su punto medio y semilongitud $r$. Si $L$ es la distancia de $O$ a la cuerda, entonces $L^2 + r^2 = 144$; y como $|OC|^2 = t^2 + r^2 = L^2$:

$$t^2 + 2r^2 = 144, \qquad L^2 = 144 - r^2.$$

**Paso 2: Condiciones de $\omega_1$.**

El diámetro de $\omega_1$ es paralelo a $PQ$, es decir, horizontal; y es una cuerda de la circunferencia de centro $C$ y radio $r$. El punto medio de una cuerda horizontal de esa circunferencia está directamente encima o debajo de $C$, así que el centro de $\omega_1$ es $C_1=(t,b)$ para algún $b$, con semicuerda $3$:

$$(b-r)^2 = r^2 - 9.$$

La recta del diámetro $AB$ de $\omega_2$ pasa por $C$ y es perpendicular a $OC$, así que su ecuación es $tx + ry = t^2+r^2 = L^2$. El arco de $\omega_1$ es tangente a $AB$, con $C_1$ del lado del semicírculo interior, a distancia $3$:

$$\frac{|t^2 + rb - L^2|}{L} = 3, \qquad \text{con } t^2+rb-L^2 = -3L \ \text{(lado interior)}.$$

Usando $t^2 - L^2 = -r^2$ (de $t^2+2r^2=144$):

$$rb = r^2 - 3L \quad\Longrightarrow\quad b = r - \frac{3L}{r}.$$

**Paso 3: Resolver para $r$.**

Sustituyendo en $(b-r)^2 = r^2 - 9$:

$$\left(\frac{3L}{r}\right)^2 = r^2 - 9 \quad\Longrightarrow\quad 9L^2 = r^4 - 9r^2.$$

Con $L^2 = 144 - r^2$:

$$9(144 - r^2) = r^4 - 9r^2 \quad\Longrightarrow\quad r^4 = 1296 \quad\Longrightarrow\quad r = 6.$$

**Paso 4: Verificación de la configuración (con $t = 6\sqrt2$, $L=6\sqrt3$).**

- $t^2 = 144 - 72 = 72$, así que $T=(6\sqrt2, 0)$ está estrictamente entre $P$ y $Q$. ✓
- $b = 6 - 3\sqrt3 \approx 0.80$; el punto de tangencia del arco de $\omega_1$ con $AB$ es $C_1 + 3n = (6\sqrt2+\sqrt6,\ 6-2\sqrt3)$, que está dentro del segmento $AB$. ✓
- El semidisco de $\omega_1$ queda dentro de la circunferencia de $\omega_2$: para $z = C_1 + 3(\cos\theta,\sin\theta)$ con $\sin\theta \ge 0$, se tiene $|z - C|^2 = 36 - 18\sqrt3\sin\theta \le 36$. ✓
- El semidisco de $\omega_2$ (lado que contiene a $O$) queda dentro de $\omega_3$: en su frontera $|z|^2 = L^2 + r^2 = 144$ solo en $A,B$. ✓

**Paso 5: Calcular $PT\cdot TQ$.**

$$PT = t + 12, \qquad TQ = 12 - t,$$
$$PT \cdot TQ = 144 - t^2 = 144 - 72 = 72.$$

$$\boxed{72}$$