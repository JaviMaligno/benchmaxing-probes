# Solución

**Planteamiento.** Cada día el total acumulado de peces aumenta en $1$ (con probabilidad $\tfrac23$) o en $2$ (con probabilidad $\tfrac13$). Las plumas se vuelven naranjas el primer día en que el total llega a $\geq 8$; ese mismo día Coral se enferma si el total llega a $\geq 9$.

Como los saltos son de tamaño $1$ o $2$, la primera entrada al conjunto $\{8, 9, 10, \dots\}$ solo puede ocurrir de tres formas:

- desde $6$ comiendo $2$ peces $\to$ total $8$,
- desde $7$ comiendo $1$ pez $\to$ total $8$,
- desde $7$ comiendo $2$ peces $\to$ total $9$.

Por lo tanto, **Coral no se enferma el día en que se vuelve naranja si y solo si la caminata visits exactamente el estado $8$** (es decir, la primera vez que el total alcanza $\geq 8$, este es exactamente $8$, y no "salta" de $7$ a $9$).

**Recurrencia.** Sea $a_n$ la probabilidad de que el total acumulado pase alguna vez exactamente por $n$. Entonces:

$$a_0 = 1, \qquad a_1 = \tfrac23, \qquad a_n = \tfrac23\, a_{n-1} + \tfrac13\, a_{n-2} \quad (n \geq 2),$$

pues para visitar $n$ hay que venir de $n-1$ (comiendo $1$) o de $n-2$ (comiendo $2$).

**Cálculo.**

| $n$ | $a_n$ |
|---|---|
| $0$ | $1$ |
| $1$ | $\tfrac{2}{3} = \tfrac{2}{3}$ |
| $2$ | $\tfrac{4}{9} + \tfrac{3}{9} = \tfrac{7}{9}$ |
| $3$ | $\tfrac{14}{27} + \tfrac{6}{27} = \tfrac{20}{27}$ |
| $4$ | $\tfrac{40}{81} + \tfrac{21}{81} = \tfrac{61}{81}$ |
| $5$ | $\tfrac{122}{243} + \tfrac{60}{243} = \tfrac{182}{243}$ |
| $6$ | $\tfrac{364}{729} + \tfrac{183}{729} = \tfrac{547}{729}$ |
| $7$ | $\tfrac{1094}{2187} + \tfrac{546}{2187} = \tfrac{1640}{2187}$ |
| $8$ | $\tfrac{3280}{6561} + \tfrac{1641}{6561} = \tfrac{4921}{6561}$ |

**Verificación con forma cerrada.** La recurrencia $3a_n = 2a_{n-1} + a_{n-2}$ tiene raíces características $x = 1$ y $x = -\tfrac13$, así que $a_n = \tfrac34 + \tfrac14\left(-\tfrac13\right)^n$. Para $n = 8$:

$$a_8 = \frac34 + \frac{1}{4 \cdot 3^8} = \frac34 + \frac{1}{26244} = \frac{19683 + 1}{26244} = \frac{4921}{6561}. \checkmark$$

Como $4921 = 7 \cdot 19 \cdot 37$ y $6561 = 3^8$, la fracción es irreducible.

$$\boxed{\dfrac{4921}{6561}}$$