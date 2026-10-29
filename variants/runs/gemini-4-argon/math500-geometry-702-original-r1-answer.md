Para determinar la mayor longitud de cuerda que se puede ahorrar, debemos minimizar la longitud de la nueva cuerda $HP$, donde $P$ es un punto en el segmento de recta $CD$.

1. **Análisis del triángulo $\triangle HCD$:**
   Conocemos las longitudes de los tres lados del triángulo formado por el globo en $H$ y los puntos de anclaje $C$ y $D$:
   - $HC = 150\text{ m}$
   - $HD = 130\text{ m}$
   - $CD = 140\text{ m}$

   (Podemos verificar que esta configuración tridimensional es geométricamente válida: dado que $\angle COD = \angle HOC = \angle HOD = 90^\circ$, tenemos $OC^2 + OD^2 = 140^2$, $OC^2 + OH^2 = 150^2$ y $OD^2 + OH^2 = 130^2$, lo cual da $OH^2 = 9900 > 0$, $OD^2 = 7000 > 0$ y $OC^2 = 12600 > 0$).

2. **Minimización de la longitud $HP$:**
   La distancia más corta desde el punto $H$ hasta la línea recta que une $C$ y $D$ es la altura del triángulo $\triangle HCD$ trazada desde el vértice $H$ hacia la base $CD$, de modo que $HP \perp CD$.

   Observamos que los lados del triángulo $\triangle HCD$ ($130, 140, 150$) son proporcionales al clásico triángulo de Herón con lados $13, 14, 15$ multiplicados por un factor de $10$.
   Usando la fórmula de Herón para calcular el área del triángulo $\triangle HCD$:
   - El semiperímetro es $s = \frac{130 + 140 + 150}{2} = 210\text{ m}$.
   - El área es:
     $$\text{Área} = \sqrt{210(210 - 130)(210 - 140)(210 - 150)} = \sqrt{210 \cdot 80 \cdot 70 \cdot 60} = 8400\text{ m}^2$$

   Por otro lado, el área del triángulo también se expresa como $\frac{1}{2} \cdot CD \cdot HP$:
   $$\frac{1}{2} \cdot 140 \cdot HP = 8400 \implies 70 \cdot HP = 8400 \implies HP = 120\text{ m}$$

   Como el triángulo es acutángulo ($130^2 + 140^2 > 150^2$), el pie de la altura $P$ se encuentra efectivamente entre $C$ y $D$ (a $90\text{ m}$ de $C$ y a $50\text{ m}$ de $D$).

3. **Cálculo de la cuerda ahorrada:**
   - Longitud original de las dos cuerdas: $HC + HD = 150 + 130 = 280\text{ m}$.
   - Longitud mínima de la nueva cuerda: $HP = 120\text{ m}$.
   - Ahorro máximo de cuerda: $280 - 120 = 160\text{ m}$.

\boxed{160}