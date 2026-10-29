## Planteamiento

Sea $h$ la altura de la cueva. Las puntas tienen alturas:

- estalactitas: $h-16$ y $h-36$
- estalagmitas: $25$ y $49$

En un cuadrado, las diagonales se bisecan mutuamente, así que las dos parejas de vértices opuestos tienen la misma suma de ordenadas. Las estalactitas no pueden ser opuestas entre sí (si lo fueran, las estalagmitas también, y entonces $(h-16)+(h-36)=25+49$ daría $h=63$... conviene probar los emparejamientos).

Probemos el emparejamiento en que cada diagonal une una estalactita con una estalagmita. Suponiendo $h-16$ opuesta a $25$ y $h-36$ opuesta a $49$:
$$(h-16)+25=(h-36)+49 \;\Rightarrow\; 9=13,$$
imposible. Con el otro cruce, $(h-16)+49=(h-36)+25$ da $33=-11$, también imposible.

Queda entonces que las estalactitas sean vértices opuestos y las estalagmitas también:
$$(h-16)+(h-36)=25+49 \;\Rightarrow\; 2h-52=74 \;\Rightarrow\; h=63.$$

## Verificación

Con $h=63$ las alturas son $47,\,27,\,25,\,49$, con centro en $y=37$. Tomando el centro como origen, los vértices son
$$(a,12),\;(-a,-12)\quad\text{(diagonal }49\text{–}25),\qquad (b,10),\;(-b,-10)\quad\text{(diagonal }47\text{–}27).$$

Diagonales perpendiculares: $ab+120=0$. Diagonales iguales: $a^2+144=b^2+100$, es decir $b^2-a^2=44$. Sustituyendo $b=-120/a$ y $u=a^2$:
$$\frac{14400}{u}-u=44 \;\Rightarrow\; u^2+44u-14400=0 \;\Rightarrow\; u=\frac{-44+244}{2}=100.$$

Luego $a=10$, $b=-12$: los vértices son $(10,49),(-12,47),(-10,25),(12,27)$, un cuadrado genuino de lado $\sqrt{22^2+2^2}=\sqrt{488}$ y diagonal $\sqrt{244}\cdot 2$. Todo consistente.

\boxed{63}