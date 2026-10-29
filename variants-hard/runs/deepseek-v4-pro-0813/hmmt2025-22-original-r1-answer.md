Voy a razonar el problema paso a paso.

**Planteamiento del modelo**

Tenemos una cueva de altura $H$ (desconocida). Podemos imaginar un sistema de coordenadas:

- El techo está en la recta $y = H$.
- El suelo está en la recta $y = 0$.
- Dos estalactitas cuelgan perpendicularmente del techo, con longitudes $16$ y $36$. Por tanto, sus puntas están en las alturas $H - 16$ y $H - 36$.
- Dos estalagmitas crecen perpendicularmente desde el suelo, con alturas $25$ y $49$. Sus puntas están en las alturas $25$ y $49$.

Sea $x$ la coordenada horizontal. Coloquemos las cuatro puntas (los vértices del cuadrado) así:

- $A$: punta de la estalactita de longitud $16$, en altura $H - 16$.
- $B$: punta de la estalactita de longitud $36$, en altura $H - 36$.
- $C$: punta de la estalagmita de altura $25$, en altura $25$.
- $D$: punta de la estalagmita de altura $49$, en altura $49$.

Las alturas (coordenadas $y$) de las cuatro puntas son:

$$
H-36,\quad H-16,\quad 25,\quad 49.
$$

**Condición geométrica: los cuatro puntos forman un cuadrado**

Las puntas del techo tienen alturas altas (si $H$ es grande) y las del suelo, altitudes bajas. Para que formen un cuadrado, en algún orden.

Trabajemos con la idea clave: en un cuadrado, los vértices pueden agruparse en dos pares opuestos; la suma de las alturas de los vértices opuestos debe ser constante (el centro tiene altura $(y_1+y_3)/2 = (y_2+y_4)/2$). En realidad, el centro de un cuadrado es el punto medio de cada diagonal, y también es el promedio de los cuatro vértices. Por tanto, si $y_1,y_2,y_3,y_4$ son las alturas de los cuatro vértices, debe cumplirse que una suma de dos de ellas iguale a la suma de las otras dos.

Esto nos da una ecuación entre las alturas, y nos permitirá despejar $H$.

**Buscar el emparejamiento correcto**

Las cuatro alturas son:

$$
a = H-32 \quad \text{(la más baja de las estalactitas)},
$$

Perdón, organicemos con calma:

- Estalactita larga: $36$, punta en $H-36$.
- Estalactita corta: $16$, punta en $H-16$.
- Estalagmita corta: $25$, punta en $25$.
- Estalagmita larga: $49$, punta en $49$.

Las ordenamos de menor a mayor suponiendo $H$ suficientemente grande:

$$
H-36 < H-16 < 25 < 49.
$$

Para que haya una relación diagonal válida, las sumas deben emparejarse. La única manera natural de que dos sumas de alturas sean iguales es:

Opción 1:

$$
(H-36) + 49 = (H-16) + 25.
$$

Veamos si esto funciona:

Lado izquierdo: $H - 36 + 49 = H + 13$.

Lado derecho: $H - 16 + 25 = H + 9$.

No son iguales. Descartamos.

Opción 2:

$$
(H-36) + (H-16) = 25 + 49.
$$

Lado izquierdo: $2H - 52$.

Lado derecho: $74$.

Entonces:

$$
2H - 52 = 74 \implies 2H = 126 \implies H = 63.
$$

Con $H=63$, las alturas son:

- Estalactita larga: $63 - 36 = 27$.
- Estalactita corta: $63 - 16 = 47$.
- Estalagmita corta: $25$.
- Estalagmita larga: $49$.

Es decir: $25, 27, 47, 49$. Ordenadas: $25 < 27 < 47 < 49$.

La suma de los extremos: $25 + 49 = 74$.

La suma de los medios: $27 + 47 = 74$.

Por tanto, en el cuadrado, los vértices opuestos tendrían alturas $(25,49)$ y $(27,47)$; el centro tendría altura $(25+49)/2 = 37$ y también $(27+47)/2 = 37$. Esto es consistente con un cuadrado centrado en altura $37$.

**Verificación geométrica completa**

Además de las alturas, las distancias horizontales deben cuadrar. Coloquemos las puntas con coordenadas $x$ adecuadas. Como forman un cuadrado de centro en altura $37$, la distancia vertical entre $25$ y $49$ es $24$; la distancia vertical entre $27$ y $47$ es $20$.

Si las diagonales se cruzan en el centro, los cuatro vértices podrían ordenarse, por ejemplo, así:

- $P_1 = (x_0, 25)$,
- $P_2 = (x_0 + s, 27)$,
- $P_3 = (x_0, 49)$,
- $P_4 = (x_0 + s, 47)$.

Aquí $P_1P_3$ es vertical de longitud $24$ y $P_2P_4$ es vertical de longitud $20$. Para que ambas diagonales se corten en su punto medio y tengan la misma longitud, necesitaríamos que las diagonales tuvieran igual longitud, pero en un cuadrado las dos diagonales miden lo mismo. La diagonal $P_1P_3$ mide $24$ y la $P_2P_4$ mide $20$, lo cual no puede ser.

Entonces ese orden concreto no es válido; hay que elegir el orden de los vértices de modo que las distancias cuadren. La condición de las alturas sólo nos da que el centro está a altura $37$.

Vamos a construir un cuadrado real.

Tomemos $H=63$. Las cuatro alturas son $27, 47, 25, 49$.

Etiquetemos:

- $A$: altura $27$ (estalactita larga, punta en $63-36=27$).
- $B$: altura $47$ (estalactita corta, punta en $63-16=47$).
- $C$: altura $25$ (estalagmita corta).
- $D$: altura $49$ (estalagmita larga).

Queremos que $A,B,C,D$ sean los cuatro vértices de un cuadrado en algún orden. Una manera de lograrlo es elegir como diagonal la pareja $(C,D)$, es decir, la vertical entre $25$ y $49$. Su punto medio está en altura $37$. La otra diagonal debe unir $A$ y $B$, y su punto medio también debe estar en altura $37$. Como las alturas de $A$ y $B$ son $27$ y $47$, en efecto su promedio es $37$.

Ahora, para que $AB$ sea perpendicular a $CD$ y ambas se bisequen:

- $CD$ es vertical, longitud $24$.
- Entonces $AB$ debe ser horizontal y medir $24$.

Como las alturas de $A$ y $B$ no son iguales ($27 \neq 47$), $AB$ no puede ser horizontal. Por tanto, este emparejamiento de diagonales no da un cuadrado con una diagonal estrictamente vertical.

Probemos otro emparejamiento: que la diagonal sea $(A,D)$, alturas $27$ y $49$, promedio $38$; la otra diagonal $(B,C)$, alturas $47$ y $25$, promedio $36$. No coinciden. Descartamos.

Diagonal $(A,C)$: alturas $27$ y $25$, promedio $26$; diagonal $(B,D)$: alturas $47$ y $49$, promedio $48$. No coinciden.

Parece que el único emparejamiento con promedios iguales de alturas es $(A,B)$ y $(C,D)$:

- Alturas $A,B$: $27,47$, promedio $37$.
- Alturas $C,D$: $25,49$, promedio $37$.

Para que $AB$ y $CD$ sean diagonales que se bisecan, sus puntos medios deben coincidir. El punto medio de $AB$ tiene altura $37$; el de $CD$ tiene altura $37$. Elegimos sus coordenadas $x$ de modo que los puntos medios también tengan la misma coordenada $x$. Eso siempre es posible: colocamos $A$ y $B$ simétricamente respecto a una vertical $x=m$, y $C$ y $D$ también simétricos respecto a $x=m$.

Falta que las dos diagonales sean perpendiculares y de igual longitud.

Como las alturas de $A$ y $B$ difieren en $20$, la diagonal $AB$ tiene desnivel $20$. Para que sea perpendicular a $CD$, su pendiente debe ser el recíproco negativo de la pendiente de $CD$. $CD$ tiene desnivel $24$. Si ponemos $CD$ con cierta separación horizontal $p$ y $AB$ con separación horizontal $q$, la perpendicularidad exige:

$$
\frac{20}{q} \cdot \frac{24}{p} = -1.
$$

(Esto si una pendiente es positiva y la otra negativa.)

Para un cuadrado, además, las diagonales miden lo mismo y se bisecan. La condición suficiente es que las longitudes proyectadas cumplan $|AB|=|CD|$, es decir:

$$
q^2 + 20^2 = p^2 + 24^2.
$$

Y la perpendicularidad entre vectores $AB=(q,20)$ y $CD=(p,24)$ (eligiendo orientaciones adecuadas) es:

$$
q p + 20\cdot 24 = 0.
$$

De aquí:

$$
q p = -480.
$$

Tomemos $q>0$ y $p<0$, de modo que:

$$
p = -\frac{480}{q}.
$$

Sustituimos en la igualdad de longitudes:

$$
q^2 + 400 = p^2 + 576.
$$

Es decir:

$$
q^2 = p^2 + 176.
$$

Sustituyendo $p$:

$$
q^2 = \frac{480^2}{q^2} + 176.
$$

Multiplicamos por $q^2$:

$$
q^4 = 480^2 + 176 q^2.
$$

Sea $u=q^2$. Entonces:

$$
u^2 - 176u - 230400 = 0.
$$

Resolvemos:

$$
\Delta = 176^2 + 4\cdot 230400 = 30976 + 921600 = 952576.
$$

Calculamos $\sqrt{952576}$. Notemos que:

$$
976^2 = 952576,
$$

porque $976^2 = (1000-24)^2 = 1000000 - 48000 + 576 = 952576$. Exacto.

Entonces:

$$
u = \frac{176 \pm 976}{2}.
$$

La raíz positiva es:

$$
u = \frac{176+976}{2} = \frac{1152}{2} = 576.
$$

Por tanto:

$$
q^2 = 576 \implies q = 24.
$$

Y:

$$
p = -\frac{480}{24} = -20.
$$

Verificamos la longitud de las diagonales:

- $|AB| = \sqrt{24^2 + 20^2} = \sqrt{576+400} = \sqrt{976}$.
- $|CD| = \sqrt{(-20)^2 + 24^2} = \sqrt{400+576} = \sqrt{976}$.

Iguales. Perpendicularidad:

$$
AB\cdot CD = 24\cdot(-20) + 20\cdot 24 = -480 + 480 = 0.
$$

Por tanto, efectivamente $A,B,C,D$ pueden disponerse como los vértices de un cuadrado con $H=63$.

**Conclusión**

La altura de la cueva es:

\[
\boxed{63}
\]