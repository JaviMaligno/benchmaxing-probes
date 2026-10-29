## Planteamiento

Sea $f(t) = t^2 - 4t + 6 = (t-2)^2 + 2$ y $S$ el conjunto de raíces de la ecuación. La condición exige que $f(S) \subseteq S$, es decir, que $f$ envíe raíces en raíces. Como la ecuación es cuadrática mónica, $|S| \le 2$ y la ecuación queda determinada por $S$.

**Puntos fijos:** $f(t) = t \iff t^2 - 5t + 6 = 0 \iff t \in \{2, 3\}$.

**Caso 1: raíz doble.** Si $S = \{t\}$, se necesita $f(t) = t$, luego $t = 2$ o $t = 3$:
- $x^2 - 4x + 4 = 0$ y $x^2 - 6x + 9 = 0$. *(2 ecuaciones)*

**Caso 2: raíces $a \neq b$.** Exigen $f(a), f(b) \in \{a, b\}$, con cuatro subcasos:

*(i) $f(a)=a,\ f(b)=b$:* ambas raíces son puntos fijos: $S = \{2,3\}$, es decir, $x^2 - 5x + 6 = 0$. *(1 ecuación)*

*(ii) $f(a)=b,\ f(b)=a$ (2-ciclo):* restando ambas igualdades,
$$f(a)-f(b) = (a-b)(a+b-4) = b-a = -(a-b) \implies a+b = 3.$$
Sustituyendo $b = 3-a$ en $a^2 - 4a + 6 = b$ resulta $a^2 - 3a + 3 = 0$, con soluciones complejas $a, b = \frac{3 \pm i\sqrt{3}}{2}$. La ecuación es $x^2 - 3x + 3 = 0$.
*Comprobación:* para $a = \frac{3+i\sqrt3}{2}$ se obtiene $f(a) = a^2 - 4a + 6 = \frac{3-i\sqrt3}{2} = b$, y simétricamente $f(b) = a$. ✔️ *(1 ecuación)*

*(iii) $f(a)=a,\ f(b)=a$ (y el caso simétrico):* $a \in \{2,3\}$. Si $a=2$: $f(b)=2 \iff (b-2)^2=0 \iff b=2$, imposible. Si $a=3$: $f(b)=3 \iff b \in \{1,3\}$, luego $b=1$: $S = \{1,3\}$, es decir, $x^2 - 4x + 3 = 0$.
*Comprobación:* $f(1) = 3$ ✔️, $f(3) = 3$ ✔️. *(1 ecuación)*

## Recuento y verificación

Las cinco ecuaciones encontradas (todas con coeficientes reales):

| Ecuación | Raíces | Verificación |
|---|---|---|
| $x^2-4x+4$ | $\{2\}$ | $f(2)=2$ ✔️ |
| $x^2-6x+9$ | $\{3\}$ | $f(3)=3$ ✔️ |
| $x^2-5x+6$ | $\{2,3\}$ | $f(2)=2,\ f(3)=3$ ✔️ |
| $x^2-4x+3$ | $\{1,3\}$ | $f(1)=3,\ f(3)=3$ ✔️ |
| $x^2-3x+3$ | $\{\tfrac{3\pm i\sqrt3}{2}\}$ | se intercambian ✔️ |

El análisis de casos es exhaustivo y las cinco son distintas, luego el total es $5$.

$\boxed{5}$