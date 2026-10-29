Para determinar la mayor longitud de cuerda que se puede ahorrar, debemos encontrar la longitud mínima posible de la nueva cuerda $HP$, donde $P$ es un punto en el segmento $CD$.

**Paso 1: Analizar el triángulo $\triangle HCD$**
Conocemos las longitudes de los tres lados del triángulo formado por el globo en $H$ y los puntos de anclaje $C$ y $D$:
* $HC = 145\text{ m}$
* $HD = 125\text{ m}$
* $CD = 180\text{ m}$

Observamos que $HC^2 + HD^2 = 145^2 + 125^2 = 21025 + 15625 = 36650 > 180^2 = 32400$. Esto confirma que los ángulos en $C$ y $D$ del triángulo $\triangle HCD$ son agudos (y que la configuración tridimensional es geométricamente válida, dado que $2HO^2 = HC^2 + HD^2 - CD^2 = 4250 > 0$).

**Paso 2: Minimizar la longitud de $HP$**
La distancia mínima desde el punto $H$ hasta el segmento $CD$ corresponde a la altura del triángulo $\triangle HCD$ trazada desde el vértice $H$ hacia la base $CD$. Como los ángulos en $C$ y $D$ son agudos, el pie de esta altura $P$ cae dentro del segmento $CD$.

Calculamos el área $K$ del triángulo $\triangle HCD$ utilizando la fórmula de Herón. Primero hallamos el semiperímetro $s$:
$$s = \frac{145 + 125 + 180}{2} = \frac{450}{2} = 225\text{ m}$$

Sustituyendo en la fórmula de Herón:
$$K = \sqrt{s(s - HC)(s - HD)(s - CD)}$$
$$K = \sqrt{225(225 - 145)(225 - 125)(225 - 180)}$$
$$K = \sqrt{225 \times 80 \times 100 \times 45}$$
$$K = 15 \times 10 \times \sqrt{3600} = 150 \times 60 = 9000\text{ m}^2$$

Por otro lado, el área del triángulo también se expresa como $K = \frac{1}{2} \times CD \times HP$. Despejando la altura $HP$:
$$HP = \frac{2K}{CD} = \frac{2 \times 9000}{180} = 100\text{ m}$$

**Paso 3: Calcular la longitud de cuerda ahorrada**
La longitud combinada original de las cuerdas $HC$ y $HD$ es:
$$HC + HD = 145 + 125 = 270\text{ m}$$

Al reemplazarlas por la cuerda $HP$ de longitud mínima ($100\text{ m}$), el ahorro máximo de cuerda es:
$$270 - 100 = 170\text{ m}$$

\boxed{170}