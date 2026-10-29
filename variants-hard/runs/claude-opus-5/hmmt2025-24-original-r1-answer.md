## Planteamiento

Coloco $AB$ sobre el eje $x$ con centro $O=(0,0)$, radio $R=10$, y $C=(c,0)$.

**Lema (semicírculo inscrito).** Si un semicírculo de radio $r$ está inscrito en otro de centro $O'$ y radio $R'$, su centro $O_r$ está a distancia $r$ del diámetro mayor (tangencia) y, como el diámetro menor es una cuerda cuyo punto medio es $O_r$, se cumple $|O'O_r|^2 + r^2 = R'^2$, con el diámetro menor perpendicular a $O'O_r$.

## $S_2$ dentro de $S_3$

La tangencia en $C$ da $O_2=(c,r_2)$, luego
$$|OO_2|^2 + r_2^2 = R^2 \implies c^2 + 2r_2^2 = 100 .$$

Por tanto
$$AC\cdot CB = (10+c)(10-c) = 100 - c^2 = 2r_2^2 .$$

## $S_1$ dentro de $S_2$

Aplicando el lema: $|O_2O_1|^2 + r_1^2 = r_2^2$, con $r_1=1$, así que $h:=|O_2O_1|=\sqrt{r_2^2-1}$, y el diámetro de $S_1$ es perpendicular a $O_2O_1$.

Como el diámetro de $S_1$ es paralelo a $AB$, el segmento $O_2O_1$ es **vertical**: $O_1-O_2=(0,\pm h)$.

La recta del diámetro de $S_2$ pasa por $O_2$ con normal $OO_2=(c,r_2)$, y $O_1$ debe estar a distancia $r_1=1$ de ella:
$$\frac{|(0,\pm h)\cdot(c,r_2)|}{|OO_2|} = \frac{h\,r_2}{\sqrt{c^2+r_2^2}} = 1 .$$

Usando $c^2+r_2^2 = 100 - r_2^2$:
$$r_2^2(r_2^2-1) = 100 - r_2^2 \implies r_2^4 = 100 \implies r_2^2 = 10 .$$

## Resultado

$$AC\cdot CB = 2r_2^2 = 20 .$$

\boxed{20}