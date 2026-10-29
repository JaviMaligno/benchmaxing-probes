## Resolución

**Configuración con coordenadas.** El pentágono es simétrico (PQ=TP=38, QR=ST=19), así que coloco P en el origen con el eje de simetría en el eje x.

En el triángulo PQR: con ∠Q=60°, por ley de cosenos
$$PR^2 = 38^2 + 19^2 - 2\cdot38\cdot19\cdot\tfrac12 = 1083 \Rightarrow PR = 19\sqrt3.$$
Igualmente PS = 19√3. Para el triángulo PRS (lados 19√3, 19√3, 48):
$$\cos\angle RPS = \frac{1083+1083-2304}{2\cdot1083} = -\frac{23}{361},$$
y con el semiángulo β respecto al eje: cos β = 13/19, sin β = 8√3/19.

Esto da las coordenadas:
- R = (13√3, 24), S = (13√3, −24)
- Como ∠QPR = 30° (el triángulo PQR es 30-60-90), Q queda en ángulo β+30°: **Q = (5√3, 37), T = (5√3, −37)**.

Verificación: QR = √((8√3)² + 13²) = √361 = 19 ✓.

**Minimización.** Por simetría y convexidad de g, el mínimo está en el eje x. Pruebo Y = (5√3, 0), el pie de la perpendicular desde Q. Los vectores unitarios desde Y hacia los cinco vértices son:

- Hacia P: (−1, 0)
- Hacia Q: (0, 1); hacia T: (0, −1) — se cancelan
- Hacia R: R−Y = (8√3, 24), con |R−Y| = √768 = 16√3, unitario (1/2, √3/2)
- Hacia S: (1/2, −√3/2)

Suma: (−1,0) + (0,1) + (0,−1) + (1/2, √3/2) + (1/2, −√3/2) = **(0,0)**.

El gradiente es cero y g es convexa, así que Y = (5√3, 0) es la mediana geométrica.

**Valor mínimo:**
$$g(Y) = \underbrace{5\sqrt3}_{PY} + \underbrace{37+37}_{QY+TY} + \underbrace{16\sqrt3+16\sqrt3}_{RY+SY} = 74 + 37\sqrt3.$$

Entonces m = 74, n = 37, p = 3, y m+n+p = 74+37+3.

$$\boxed{114}$$