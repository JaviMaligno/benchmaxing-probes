Vamos a resolverlo paso a paso.

**Paso 1: Condición para un trapecio tangencial**

Un trapecio isósceles tiene un círculo inscrito tangente a sus cuatro lados si y solo si la suma de sus lados paralelos es igual a la suma de los otros dos lados (lados no paralelos).

Llamemos a los lados paralelos \(r\) y \(s\) (con \(r > s\)), y a cada lado no paralelo \(l\). Para un trapecio tangencial:

\[
r + s = 2l \quad \Rightarrow \quad l = \frac{r+s}{2}.
\]

**Paso 2: Relación entre el área y el radio de la circunferencia inscrita**

Para un polígono tangencial, el área es:

\[
A = r_{\text{inc}} \cdot s_{\text{semi}},
\]

donde \(s_{\text{semi}}\) es el semiperímetro.

El semiperímetro del trapecio es:

\[
s_{\text{semi}} = \frac{r + s + 2l}{2} = \frac{r + s + (r+s)}{2} = r+s.
\]

El área es \(72\) y el radio es \(3\), así que:

\[
72 = 3(r+s) \quad \Rightarrow \quad r+s = 24.
\]

**Paso 3: Relación entre la altura y el radio**

En un trapecio isósceles tangencial, la altura es \(2 \times\) el radio de la circunferencia inscrita:

\[
h = 2R = 6.
\]

**Paso 4: Relación de los lados no paralelos con la altura**

En un trapecio isósceles, cada lado no paralelo \(l\) forma un triángulo rectángulo con la altura \(h\) y la mitad de la diferencia de las bases:

\[
l^2 = h^2 + \left(\frac{r-s}{2}\right)^2.
\]

Ya tenemos \(l = \frac{r+s}{2} = \frac{24}{2} = 12\), y \(h = 6\). Entonces:

\[
12^2 = 6^2 + \left(\frac{r-s}{2}\right)^2,
\]

\[
144 = 36 + \left(\frac{r-s}{2}\right)^2,
\]

\[
\left(\frac{r-s}{2}\right)^2 = 108,
\]

\[
\frac{r-s}{2} = 6\sqrt{3} \quad \Rightarrow \quad r-s = 12\sqrt{3}.
\]

**Paso 5: Calcular \(r\) y \(s\)**

Tenemos:

\[
r+s = 24, \quad r-s = 12\sqrt{3}.
\]

Sumando:

\[
2r = 24 + 12\sqrt{3} \quad \Rightarrow \quad r = 12 + 6\sqrt{3}.
\]

Restando:

\[
2s = 24 - 12\sqrt{3} \quad \Rightarrow \quad s = 12 - 6\sqrt{3}.
\]

**Paso 6: Calcular \(r^2 + s^2\)**

\[
r^2 + s^2 = (12 + 6\sqrt{3})^2 + (12 - 6\sqrt{3})^2.
\]

\[
= (144 + 144\sqrt{3} + 108) + (144 - 144\sqrt{3} + 108).
\]

Los términos con \(\sqrt{3}\) se cancelan:

\[
= 144 + 108 + 144 + 108 = 504.
\]

Por lo tanto:

\[
\boxed{504}
\]