Para encontrar el área del triángulo $\triangle BGE$, primero determinamos las longitudes de los segmentos individuales sobre la recta que contiene a los puntos $A, B, C, D, E$ y $F$.

Sean las longitudes de los segmentos consecutivos:
- $x_1 = AB$
- $x_2 = BC$
- $x_3 = CD$
- $x_4 = DE$
- $x_5 = EF$

A partir de los datos del problema, tenemos el siguiente sistema de ecuaciones:
1. $AC = x_1 + x_2 = 26$
2. $BD = x_2 + x_3 = 22$
3. $CE = x_3 + x_4 = 31$
4. $DF = x_4 + x_5 = 33$
5. $AF = x_1 + x_2 + x_3 + x_4 + x_5 = 73$

Sumando $AC$ y $CE$, obtenemos la longitud de $AE$:
$$AE = x_1 + x_2 + x_3 + x_4 = 26 + 31 = 57$$

Restando esto de $AF$, hallamos $x_5$:
$$x_5 = AF - AE = 73 - 57 = 16$$

Sustituyendo hacia atrás en las demás ecuaciones, encontramos el resto de los segmentos:
- $x_4 = DF - x_5 = 33 - 16 = 17$
- $x_3 = CE - x_4 = 31 - 17 = 14$
- $x_2 = BD - x_3 = 22 - 14 = 8$
- $x_1 = AC - x_2 = 26 - 8 = 18$

De aquí obtenemos las longitudes de las bases $CD$ y $BE$:
- $CD = x_3 = 14$
- $BE = x_2 + x_3 + x_4 = 8 + 14 + 17 = 39$

Ahora calculamos el área del triángulo $\triangle CGD$, cuyos lados miden $CD = 14$, $CG = 40$ y $DG = 30$. Utilizando la fórmula de Herón, calculamos primero el semiperímetro $s$:
$$s = \frac{14 + 40 + 30}{2} = 42$$

El área de $\triangle CGD$ es:
$$\text{Área}(\triangle CGD) = \sqrt{s(s - CD)(s - CG)(s - DG)} = \sqrt{42(42 - 14)(42 - 40)(42 - 30)}$$
$$\text{Área}(\triangle CGD) = \sqrt{42 \cdot 28 \cdot 2 \cdot 12} = \sqrt{(6 \cdot 7) \cdot (4 \cdot 7) \cdot 2 \cdot (2 \cdot 6)} = 6 \cdot 7 \cdot 2 \cdot 2 = 168$$

Como los triángulos $\triangle BGE$ y $\triangle CGD$ comparten la misma altura trazada desde el vértice $G$ hacia la recta $AF$, la razón entre sus áreas es igual a la razón entre sus bases:
$$\frac{\text{Área}(\triangle BGE)}{\text{Área}(\triangle CGD)} = \frac{BE}{CD}$$

Sustituyendo los valores conocidos:
$$\text{Área}(\triangle BGE) = 168 \cdot \frac{39}{14} = 12 \cdot 39 = 468$$

\boxed{468}