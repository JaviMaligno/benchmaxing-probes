Para determinar la mayor longitud de cuerda que se puede ahorrar, debemos encontrar la longitud mínima posible de la nueva cuerda $HP$ y restarla de la longitud total original de las cuerdas $HC$ y $HD$.

### Paso 1: Analizar el triángulo $\triangle HCD$
Consideremos el triángulo formado en el espacio por los puntos $H$, $C$ y $D$. Conocemos las longitudes de sus tres lados:
- $HC = 150\text{ m}$
- $HD = 130\text{ m}$
- $CD = 140\text{ m}$

La longitud combinada original de las dos cuerdas que se van a reemplazar es:
$$HC + HD = 150\text{ m} + 130\text{ m} = 280\text{ m}$$

### Paso 2: Minimizar la longitud de $HP$
Para ahorrar la mayor cantidad posible de cuerda, necesitamos que la longitud del segmento $HP$ (donde $P$ está en el segmento de recta $CD$) sea lo más pequeña posible. La distancia más corta desde el punto $H$ hasta la recta $CD$ se obtiene cuando $HP$ es perpendicular a $CD$, es decir, cuando $HP$ es la altura del triángulo $\triangle HCD$ correspondiente a la base $CD$.

Observamos que las longitudes de los lados de $\triangle HCD$ ($130$, $140$, $150$) son proporcionales al conocido triángulo de lados $13$, $14$ y $15$ multiplicados por $10$.

Podemos calcular el área del triángulo $\triangle HCD$ utilizando la fórmula de Herón. Primero hallamos el semiperímetro $s$:
$$s = \frac{130 + 140 + 150}{2} = 210\text{ m}$$

El área $K$ del triángulo $\triangle HCD$ es:
$$K = \sqrt{s(s - HC)(s - HD)(s - CD)}$$
$$K = \sqrt{210(210 - 150)(210 - 130)(210 - 140)} = \sqrt{210 \cdot 60 \cdot 80 \cdot 70} = 8400\text{ m}^2$$

Por otro lado, el área del triángulo también se expresa como $\frac{1}{2} \cdot CD \cdot HP_{\text{mín}}$:
$$8400 = \frac{1}{2} \cdot 140 \cdot HP_{\text{mín}} \implies 8400 = 70 \cdot HP_{\text{mín}} \implies HP_{\text{mín}} = 120\text{ m}$$

*(Nota: Al ser $PC = \sqrt{150^2 - 120^2} = 90\text{ m}$ y $PD = \sqrt{130^2 - 120^2} = 50\text{ m}$, se cumple que $PC + PD = 140\text{ m}$, lo que confirma que el pie de la altura $P$ se encuentra efectivamente entre $C$ y $D$).*

### Paso 3: Calcular el ahorro máximo de cuerda
Restamos la longitud mínima de la cuerda $HP$ de la suma original de las longitudes de $HC$ y $HD$:
$$\text{Ahorro máximo} = (150 + 130) - 120 = 280 - 120 = 160\text{ m}$$

\boxed{160}