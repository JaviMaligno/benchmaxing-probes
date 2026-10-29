Retomando en el punto donde $F(x) = (x-8)(x-50)(x-72)(x-k) - mx$ debe cumplir $F(x) = (x-x_1)^2(x-x_2)^2$ (pues $F \ge 0$ en $(0,\infty)$ con $F(0) = 28800k > 0$, así que $x_1, x_2$ son forzosamente raíces dobles de la cuártica).

**1. Sistema de coeficientes.** Con $s = x_1 + x_2$ y $p = x_1x_2$:
- constante: $p^2 = 28800k$
- coef. $x^3$: $2s = 130 + k$
- coef. $x^2$: $s^2 + 2p = 4576 + 130k$

(el coeficiente de $x$ solo determina $m = 2ps - 28800 - 4576k$, sin restricción adicional).

**2. Ecuación en $k$.** De lo anterior, $p = \sqrt{28800k} = 120\sqrt{2k}$ y $s = \frac{130+k}{2}$. Sustituyendo en la condición de $x^2$:

$$\frac{(130+k)^2}{4} + 240\sqrt{2k} = 4576 + 130k \iff k^2 - 260k + 960\sqrt{2k} - 1404 = 0.$$

**3. Substitución $t = \sqrt{2k}$** (con $t > 0$). Multiplicando por 4:

$$t^4 - 520t^2 + 3840t - 5616 = 0.$$

Racionales: $t = 2$ funciona ($16 - 2080 + 7680 - 5616 = 0$); dividiendo, $t^3 + 2t^2 - 516t + 2808$, y $t = 6$ funciona; queda $t^2 + 8t - 468$, con raíces $18$ y $-26$ (descartada). Verificación por expansión:

$$(t-2)(t-6)(t-18)(t+26) = t^4 - 520t^2 + 3840t - 5616. \checkmark$$

Entonces $k = t^2/2 \in \{2, 18, 162\}$.

**4. Comprobar que dan exactamente dos puntos de mínimo.** Hace falta $s^2 > 4p$ (raíces reales, distintas, positivas):

| $k$ | $s$ | $p$ | $s^2$ | $4p$ |
|---|---|---|---|---|
| $2$ | $66$ | $240$ | $4356$ | $960$ |
| $18$ | $74$ | $720$ | $5476$ | $2880$ |
| $162$ | $146$ | $2160$ | $21316$ | $8640$ |

En los tres casos $s^2 > 4p$. $\checkmark$ Y los coeficientes cuadran (p. ej. $k=18$: $s^2 + 2p = 6916 = 4576 + 130\cdot 18$, y $p^2 = 518400 = 28800\cdot 18$). Como entonces $F(x) = (x-x_1)^2(x-x_2)^2 \ge 0$, se tiene $g(x) \ge m$ con igualdad exactamente en $x_1$ y $x_2$.

**5. Suma.** $2 + 18 + 162 = 182$.

$$\boxed{182}$$