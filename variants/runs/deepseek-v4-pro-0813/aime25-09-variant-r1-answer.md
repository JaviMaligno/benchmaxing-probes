Voy a resolver el problema paso a paso.

**Paso 1: Plantear la rotación de la parábola.**

La parábola original es $y = x^2 - 5$. Un punto $(x, y)$ de la parábola original, tras rotarlo $60^\circ$ en sentido antihorario respecto al origen, se transforma en:

$$(x', y') = \left( \frac{x}{2} - \frac{\sqrt{3}}{2}\, y,\; \frac{\sqrt{3}}{2}\, x + \frac{y}{2} \right).$$

**Paso 2: Condición de que un punto rotado esté sobre la parábola original.**

Como buscamos puntos donde la parábola original y su imagen se cortan, el punto rotado $(x', y')$ debe cumplir la ecuación de la parábola original:

$$y' = (x')^2 - 5.$$

Sustituyendo:

$$\frac{\sqrt{3}}{2}x + \frac{y}{2} = \left( \frac{x}{2} - \frac{\sqrt{3}}{2}y \right)^2 - 5.$$

**Paso 3: Sistema con la condición de que $(x,y)$ está en la parábola original.**

Además, $y = x^2 - 5$. Sustituimos esto en la ecuación anterior.

Primero, desarrollamos el miembro derecho:

$$\left( \frac{x}{2} - \frac{\sqrt{3}}{2}y \right)^2 = \frac{x^2}{4} - \frac{\sqrt{3}}{2}xy + \frac{3y^2}{4}.$$

Entonces:

$$\frac{\sqrt{3}}{2}x + \frac{y}{2} = \frac{x^2}{4} - \frac{\sqrt{3}}{2}xy + \frac{3y^2}{4} - 5.$$

**Paso 4: Eliminar $y$ usando $y = x^2 - 5$.**

Sustituimos $y = x^2 - 5$:

Miembro izquierdo:

$$L = \frac{\sqrt{3}}{2}x + \frac{x^2 - 5}{2}.$$

Miembro derecho:

$$R = \frac{x^2}{4} - \frac{\sqrt{3}}{2}x(x^2 - 5) + \frac{3(x^2 - 5)^2}{4} - 5.$$

Los puntos de intersección cumplen $L = R$.

**Paso 5: Alternativa usando la transformación inversa.**

En lugar de rotar la parábola original y luego igualar, podemos rotar la parábola original y plantear la intersección. Sin embargo, hay un enfoque más cómodo: buscamos puntos $(X, Y)$ que estén simultáneamente sobre la parábola original y sobre la parábola rotada. Es decir:

- $Y = X^2 - 5$ (parábola original),
- Y además, el punto $(X, Y)$ debe ser la imagen de algún punto $(x, y)$ de la parábola original bajo la rotación.

Equivalentemente, el punto $(X, Y)$ rotado $-60^\circ$ (o sea, $60^\circ$ en sentido horario) debe estar sobre la parábola original.

La rotación horaria de $60^\circ$ es:

$$x = \frac{X}{2} + \frac{\sqrt{3}}{2}Y, \qquad y = -\frac{\sqrt{3}}{2}X + \frac{Y}{2}.$$

Como $(x, y)$ está sobre la parábola original:

$$y = x^2 - 5,$$

sustituimos:

$$-\frac{\sqrt{3}}{2}X + \frac{Y}{2} = \left( \frac{X}{2} + \frac{\sqrt{3}}{2}Y \right)^2 - 5.$$

Y además $Y = X^2 - 5$.

**Paso 6: Resolver el sistema.**

Sustituimos $Y = X^2 - 5$ en la ecuación:

$$-\frac{\sqrt{3}}{2}X + \frac{X^2 - 5}{2} = \left( \frac{X}{2} + \frac{\sqrt{3}}{2}(X^2 - 5) \right)^2 - 5.$$

Desarrollamos el cuadrado:

$$\left( \frac{X}{2} + \frac{\sqrt{3}}{2}(X^2 - 5) \right)^2 = \frac{X^2}{4} + \frac{\sqrt{3}}{2}X(X^2 - 5) + \frac{3(X^2 - 5)^2}{4}.$$

Entonces la ecuación queda:

$$-\frac{\sqrt{3}}{2}X + \frac{X^2 - 5}{2} = \frac{X^2}{4} + \frac{\sqrt{3}}{2}X(X^2 - 5) + \frac{3(X^2 - 5)^2}{4} - 5.$$

**Paso 7: Simplificar.**

Multiplicamos todo por $4$ para eliminar denominadores:

$$-2\sqrt{3}\,X + 2(X^2 - 5) = X^2 + 2\sqrt{3}\,X(X^2 - 5) + 3(X^2 - 5)^2 - 20.$$

Desarrollamos:

Lado izquierdo:

$$2X^2 - 10 - 2\sqrt{3}\,X.$$

Lado derecho:

$$X^2 + 2\sqrt{3}\,X^3 - 10\sqrt{3}\,X + 3(X^4 - 10X^2 + 25) - 20.$$

Es decir:

$$X^2 + 2\sqrt{3}\,X^3 - 10\sqrt{3}\,X + 3X^4 - 30X^2 + 75 - 20.$$

Simplificamos:

$$3X^4 + 2\sqrt{3}\,X^3 + X^2 - 30X^2 - 10\sqrt{3}\,X + 55.$$

$$= 3X^4 + 2\sqrt{3}\,X^3 - 29X^2 - 10\sqrt{3}\,X + 55.$$

**Paso 8: Ecuación completa.**

Igualamos ambos lados:

$$2X^2 - 10 - 2\sqrt{3}\,X = 3X^4 + 2\sqrt{3}\,X^3 - 29X^2 - 10\sqrt{3}\,X + 55.$$

Pasamos todo a un lado:

$$0 = 3X^4 + 2\sqrt{3}\,X^3 - 29X^2 - 10\sqrt{3}\,X + 55 - 2X^2 + 10 + 2\sqrt{3}\,X.$$

Observamos que $-10\sqrt{3}\,X$ y $+2\sqrt{3}\,X$ se combinan:

$$-10\sqrt{3}\,X + 2\sqrt{3}\,X = -8\sqrt{3}\,X.$$

Entonces:

$$0 = 3X^4 + 2\sqrt{3}\,X^3 - 31X^2 - 8\sqrt{3}\,X + 65.$$

**Paso 9: Resolver la ecuación cuártica.**

Tenemos:

$$3X^4 + 2\sqrt{3}\,X^3 - 31X^2 - 8\sqrt{3}\,X + 65 = 0.$$

Separamos los términos con $\sqrt{3}$ y sin $\sqrt{3}$:

Términos sin $\sqrt{3}$:

$$3X^4 - 31X^2 + 65.$$

Términos con $\sqrt{3}$:

$$2\sqrt{3}\,X^3 - 8\sqrt{3}\,X = 2\sqrt{3}\,X(X^2 - 4).$$

Así que la ecuación es:

$$3X^4 - 31X^2 + 65 + 2\sqrt{3}\,X(X^2 - 4) = 0.$$

**Paso 10: Buscar soluciones racionales con $\sqrt{3}$.**

Para que una solución $X$ tenga la propiedad de que su $y$-coordenada sea de la forma $\frac{a - \sqrt{b}}{c}$, es natural que $X$ contenga $\sqrt{3}$. Probamos soluciones de la forma $X = k\sqrt{3}$.

Sustituimos $X = k\sqrt{3}$:

$$X^2 = 3k^2, \quad X^3 = 3k^3\sqrt{3}, \quad X^4 = 9k^4.$$

La ecuación queda:

$$3(9k^4) - 31(3k^2) + 65 + 2\sqrt{3}\,(k\sqrt{3})(3k^2 - 4) = 0.$$

Es decir:

$$27k^4 - 93k^2 + 65 + 2\cdot 3k(3k^2 - 4) = 0.$$

Simplificamos el último término:

$$2\sqrt{3} \cdot k\sqrt{3} \cdot (3k^2 - 4) = 6k(3k^2 - 4) = 18k^3 - 24k.$$

Entonces:

$$27k^4 + 18k^3 - 93k^2 - 24k + 65 = 0.$$

**Paso 11: Buscar raíces racionales de esta cuártica en $k$.**

Probamos $k = 1$:

$$27 + 18 - 93 - 24 + 65 = 110 - 117 = -7 \neq 0.$$

Probamos $k = -1$:

$$27 - 18 - 93 + 24 + 65 = 116 - 111 = 5 \neq 0.$$

Probamos $k = 5/3$:

$$27\left(\frac{125}{27}\right) + 18\left(\frac{125}{27}\right)?$$

Mejor probamos de forma ordenada. La ecuación:

$$27k^4 + 18k^3 - 93k^2 - 24k + 65 = 0.$$

Probamos $k = 5/3$:

$$k^2 = \frac{25}{9}, \quad k^3 = \frac{125}{27}, \quad k^4 = \frac{625}{81}.$$

$$27\cdot \frac{625}{81} = \frac{625}{3}.$$

$$18\cdot \frac{125}{27} = \frac{250}{3}.$$

Suma: $\frac{625}{3} + \frac{250}{3} = \frac{875}{3}$.

$$-93\cdot \frac{25}{9} = -\frac{2325}{9} = -\frac{775}{3}.$$

Sumamos hasta ahora: $\frac{875}{3} - \frac{775}{3} = \frac{100}{3}$.

$$-24\cdot \frac{5}{3} = -40 = -\frac{120}{3}.$$

Sumamos: $\frac{100}{3} - \frac{120}{3} = -\frac{20}{3}$.

Sumamos $65 = \frac{195}{3}$:

$$-\frac{20}{3} + \frac{195}{3} = \frac{175}{3} \neq 0.$$

Probamos $k = 1/3$:

$$27\cdot \frac{1}{81} = \frac{1}{3}.$$

$$18\cdot \frac{1}{27} = \frac{2}{3}.$$

Suma: $1$.

$$-93\cdot \frac{1}{9} = -\frac{31}{3}.$$

Sumamos: $1 - \frac{31}{3} = -\frac{28}{3}$.

$$-24\cdot \frac{1}{3} = -8 = -\frac{24}{3}.$$

Sumamos: $-\frac{28}{3} - \frac{24}{3} = -\frac{52}{3}$.

Sumamos $65 = \frac{195}{3}$:

$$-\frac{52}{3} + \frac{195}{3} = \frac{143}{3} \neq 0.$$

Probamos $k = -5/3$:

Ya calculamos para $k=5/3$ y no dio cero. Probemos factorizar.

**Paso 12: Factorizar la cuártica en $k$.**

Intentamos factorizar como producto de dos cuadráticas con coeficientes enteros:

$$27k^4 + 18k^3 - 93k^2 - 24k + 65 = (Ak^2 + Bk + C)(Dk^2 + Ek + F).$$

Como el coeficiente principal es $27$, probamos $A = 3$, $D = 9$, o $A = 1$, $D = 27$, etc.

Probemos $A = 3$, $D = 9$:

- $AD = 27$. Bien.
- $CF = 65$. Posibilidades: $(1, 65)$, $(5, 13)$, $(-1, -65)$, $(-5, -13)$, etc.

Probamos $C = 5$, $F = 13$:

$$(3k^2 + Bk + 5)(9k^2 + Ek + 13).$$

Coeficiente de $k^3$: $3E + 9B = 18$, es decir, $3E + 9B = 18 \Rightarrow E + 3B = 6$.

Coeficiente de $k$: $13B + 5E = -24$.

Coeficiente de $k^2$: $39 + BE + 45 = -93$, es decir, $BE + 84 = -93 \Rightarrow BE = -177$.

Resolvemos el sistema:

$$E = 6 - 3B.$$

Sustituimos en $13B + 5E = -24$:

$$13B + 5(6 - 3B) = -24,$$

$$13B + 30 - 15B = -24,$$

$$-2B = -54,$$

$$B = 27.$$

Entonces $E = 6 - 81 = -75$.

Verificamos $BE = 27 \cdot (-75) = -2025 \neq -177$. No sirve.

Probamos $C = 13$, $F = 5$:

$$(3k^2 + Bk + 13)(9k^2 + Ek + 5).$$

Coeficiente de $k^3$: $3E + 9B = 18 \Rightarrow E + 3B = 6$.

Coeficiente de $k$: $5B + 13E = -24$.

Coeficiente de $k^2$: $15 + BE + 117 = -93 \Rightarrow BE + 132 = -93 \Rightarrow BE = -225$.

Resolvemos:

$$E = 6 - 3B.$$

$$5B + 13(6 - 3B) = -24.$$

$$5B + 78 - 39B = -24.$$

$$-34B = -102.$$

$$B = 3.$$

Entonces $E = 6 - 9 = -3$.

Verificamos $BE = 3 \cdot (-3) = -9 \neq -225$. No sirve.

Probamos $C = -5$, $F = -13$:

El término constante $CF = 65$, correcto.

$$(3k^2 + Bk - 5)(9k^2 + Ek - 13).$$

Coeficiente de $k^2$: $-39 + BE - 45 = -93 \Rightarrow BE - 84 = -93 \Rightarrow BE = -9$.

Coeficiente de $k$: $-13B - 5E = -24$.

Coeficiente de $k^3$: $3E + 9B = 18 \Rightarrow E + 3B = 6$.

Resolvemos:

$$E = 6 - 3B.$$

$$-13B - 5(6 - 3B) = -24.$$

$$-13B - 30 + 15B = -24.$$

$$2B = 6.$$

$$B = 3.$$

Entonces $E = 6 - 9 = -3$.

Verificamos $BE = 3 \cdot (-3) = -9$. ¡Correcto!

Entonces la factorización es:

$$27k^4 + 18k^3 - 93k^2 - 24k + 65 = (3k^2 + 3k - 5)(9k^2 - 3k - 13).$$

**Paso 13: Resolver las cuadráticas en $k$.**

Primera cuadrática:

$$3k^2 + 3k - 5 = 0.$$

$$k = \frac{-3 \pm \sqrt{9 + 60}}{6} = \frac{-3 \pm \sqrt{69}}{6}.$$

Segunda cuadrática:

$$9k^2 - 3k - 13 = 0.$$

$$k = \frac{3 \pm \sqrt{9 + 468}}{18} = \frac{3 \pm \sqrt{477}}{18} = \frac{3 \pm 3\sqrt{53}}{18} = \frac{1 \pm \sqrt{53}}{6}.$$

**Paso 14: Encontrar la solución en el cuarto cuadrante.**

Recordemos que $X = k\sqrt{3}$ y $Y = X^2 - 5 = 3k^2 - 5$.

El cuarto cuadrante corresponde a $X > 0$ e $Y < 0$.

Para la primera cuadrática:

$$k_1 = \frac{-3 + \sqrt{69}}{6} \approx \frac{-3 + 8.3066}{6} = \frac{5.3066}{6} \approx 0.8844 > 0.$$

$$Y_1 = 3k_1^2 - 5.$$

$$k_1^2 = \left( \frac{-3 + \sqrt{69}}{6} \right)^2 = \frac{9 - 6\sqrt{69} + 69}{36} = \frac{78 - 6\sqrt{69}}{36} = \frac{13 - \sqrt{69}}{6}.$$

Entonces:

$$Y_1 = 3\cdot \frac{13 - \sqrt{69}}{6} - 5 = \frac{13 - \sqrt{69}}{2} - 5 = \frac{13 - \sqrt{69} - 10}{2} = \frac{3 - \sqrt{69}}{2}.$$

Como $\sqrt{69} \approx 8.3066$, tenemos:

$$Y_1 \approx \frac{3 - 8.3066}{2} = \frac{-5.3066}{2} \approx -2.6533 < 0.$$

Y $X_1 = k_1\sqrt{3} \approx 0.8844 \times 1.732 \approx 1.532 > 0$.

Entonces $(X_1, Y_1)$ está en el cuarto cuadrante.

Para la otra raíz de la primera cuadrática:

$$k_2 = \frac{-3 - \sqrt{69}}{6} < 0.$$

Entonces $X_2 < 0$, no está en el cuarto cuadrante.

Para la segunda cuadrática:

$$k_3 = \frac{1 + \sqrt{53}}{6} \approx \frac{1 + 7.2801}{6} = \frac{8.2801}{6} \approx 1.38 > 0.$$

$$Y_3 = 3k_3^2 - 5.$$

$$k_3^2 = \left( \frac{1 + \sqrt{53}}{6} \right)^2 = \frac{1 + 2\sqrt{53} + 53}{36} = \frac{54 + 2\sqrt{53}}{36} = \frac{27 + \sqrt{53}}{18}.$$

$$Y_3 = 3\cdot \frac{27 + \sqrt{53}}{18} - 5 = \frac{27 + \sqrt{53}}{6} - 5 = \frac{27 + \sqrt{53} - 30}{6} = \frac{\sqrt{53} - 3}{6}.$$

Como $\sqrt{53} \approx 7.2801$, tenemos:

$$Y_3 \approx \frac{7.2801 - 3}{6} = \frac{4.2801}{6} \approx 0.7134 > 0.$$

Entonces $(X_3, Y_3)$ está en el primer cuadrante, no en el cuarto.

Para la otra raíz de la segunda cuadrática:

$$k_4 = \frac{1 - \sqrt{53}}{6} < 0.$$

Entonces $X_4 < 0$, y además:

$$Y_4 = 3k_4^2 - 5.$$

$$k_4^2 = \left( \frac{1 - \sqrt{53}}{6} \right)^2 = \frac{1 - 2\sqrt{53} + 53}{36} = \frac{54 - 2\sqrt{53}}{36} = \frac{27 - \sqrt{53}}{18}.$$

$$Y_4 = 3\cdot \frac{27 - \sqrt{53}}{18} - 5 = \frac{27 - \sqrt{53}}{6} - 5 = \frac{27 - \sqrt{53} - 30}{6} = \frac{-3 - \sqrt{53}}{6} < 0.$$

Entonces $(X_4, Y_4)$ tiene $X_4 < 0$ e $Y_4 < 0$, es decir, está en el tercer cuadrante.

**Paso 15: Conclusión sobre el cuarto cuadrante.**

El único punto de intersección en el cuarto cuadrante corresponde a $k_1 = \frac{-3 + \sqrt{69}}{6}$, con:

$$Y_1 = \frac{3 - \sqrt{69}}{2}.$$

Aquí $Y_1 = \frac{a - \sqrt{b}}{c}$ con $a = 3$, $b = 69$ y $c = 2$.

Verificamos que $a$ y $c$ son relativamente primos: $\gcd(3, 2) = 1$. Correcto.

**Paso 16: Calcular $a + b + c$.**

$$a + b + c = 3 + 69 + 2 = 74.$$

Por lo tanto, la respuesta final es:

$$\boxed{74}$$