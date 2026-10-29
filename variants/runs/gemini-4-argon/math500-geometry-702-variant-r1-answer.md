Para determinar la mayor longitud de cuerda que se puede ahorrar, debemos minimizar la longitud de la nueva cuerda $HP$, donde $P$ es un punto en el segmento $CD$.

Consideremos el triángulo $\triangle HCD$ en el espacio. Conocemos las longitudes de sus tres lados:
- $HC = 145\text{ m}$
- $HD = 125\text{ m}$
- $CD = 180\text{ m}$

La longitud total de las dos cuerdas que se van a reemplazar es:
$$HC + HD = 145 + 125 = 270\text{ m}$$

Al reemplazar ambas cuerdas por una sola cuerda $HP$ con $P$ sobre el segmento $CD$, el ahorro de cuerda es $(HC + HD) - HP = 270 - HP$. Este ahorro es máximo cuando la longitud $HP$ es mínima, lo cual ocurre cuando $HP$ es la altura del triángulo $\triangle HCD$ trazada desde el vértice $H$ hacia el lado $CD$ (siempre que el pie de la altura caiga dentro del segmento $CD$).

Podemos simplificar los cálculos dividiendo las longitudes de los lados de $\triangle HCD$ entre su máximo común divisor, que es $5$:
$$a = \frac{125}{5} = 25, \quad b = \frac{145}{5} = 29, \quad c = \frac{180}{5} = 36$$

Calculamos el área $K$ de este triángulo reducido utilizando la fórmula de Herón. El semiperímetro $s$ es:
$$s = \frac{25 + 29 + 36}{2} = 45$$

El área $K$ es:
$$K = \sqrt{s(s-a)(s-b)(s-c)} = \sqrt{45(45-25)(45-29)(45-36)} = \sqrt{45 \cdot 20 \cdot 16 \cdot 9} = \sqrt{900 \cdot 144} = 30 \cdot 12 = 360$$

La altura $h_c$ correspondiente al lado $c = 36$ en el triángulo reducido es:
$$h_c = \frac{2K}{c} = \frac{2 \cdot 360}{36} = 20$$

Multiplicando nuevamente por el factor de escala $5$, obtenemos la longitud mínima de la cuerda $HP$:
$$HP_{\text{mín}} = 5 \cdot 20 = 100\text{ m}$$

(Notemos que las proyecciones sobre $CD$ miden $\sqrt{145^2 - 100^2} = 105\text{ m}$ y $\sqrt{125^2 - 100^2} = 75\text{ m}$, cuya suma es $180\text{ m}$, confirmando que $P$ se encuentra efectivamente dentro del segmento $CD$).

Por lo tanto, la mayor longitud de cuerda que se puede ahorrar es:
$$270 - 100 = 170\text{ m}$$

\boxed{170}