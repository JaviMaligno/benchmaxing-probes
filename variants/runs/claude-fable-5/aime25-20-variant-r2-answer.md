## Planteamiento

El triángulo $DEF$ es el triángulo medial de $\triangle PQR$, así que su circuncírculo es la **circunferencia de los nueve puntos**. Esta circunferencia también pasa por los pies de las alturas, y las segundas intersecciones con las líneas $QD$ (lado $QR$), $PE$ (lado $PR$) y $PF$ (lado $PQ$) son precisamente esos pies: $G$ es el pie de la altura desde $P$, $H$ el pie desde $Q$, y $J$ el pie desde $R$.

## Cálculo con números complejos

Tomo el circuncírculo de $\triangle PQR$ como círculo unitario. Los arcos del circuncírculo son $\wideparen{QR}=2\angle P=160^\circ$, $\wideparen{PR}=2\angle Q=116^\circ$, $\wideparen{PQ}=2\angle R=84^\circ$. Coloco:

$$p = 0^\circ,\quad q = 84^\circ,\quad r = 244^\circ$$

Con centro de los nueve puntos $n=\tfrac{p+q+r}{2}$, los puntos sobre esa circunferencia tienen direcciones (respecto a $n$):

- Puntos medios: $D \sim -p$, $E \sim -q$, $F \sim -r$
- Pies de altura: $G \sim -\dfrac{qr}{p}$, $H \sim -\dfrac{pr}{q}$, $J \sim -\dfrac{pq}{r}$

Evaluando los argumentos (mód $360^\circ$):

| Punto | Dirección |
|---|---|
| $J$ | $180+0+84-244 = 20^\circ$ |
| $F$ | $244+180 = 64^\circ$ |
| $G$ | $180+84+244 = 148^\circ$ |
| $D$ | $180^\circ$ |
| $E$ | $264^\circ$ |
| $H$ | $180+0+244-84 = 340^\circ$ |

El orden cíclico es $G, D, E, H, J, F$, consistente con el enunciado. Los arcos pedidos son:

- $\wideparen{DE} = 264 - 180 = 84^\circ$
- $\wideparen{HJ} = 20 - 340 \equiv 40^\circ$
- $\wideparen{FG} = 148 - 64 = 84^\circ$

## Resultado

$$\wideparen{DE} + 2\,\wideparen{HJ} + 3\,\wideparen{FG} = 84 + 2(40) + 3(84) = 84 + 80 + 252 = \boxed{416}$$