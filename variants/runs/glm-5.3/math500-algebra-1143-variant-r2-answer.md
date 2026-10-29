## Planteamiento

La distancia desde el origen a un punto $(x, y)$ de la parábola es $d^2 = x^2 + y^2$. Queremos minimizarla sujeta a $y = \frac{1}{4}x^2 - 6$.

## Desarrollo

Sustituyendo la ecuación de la parábola:

$$d^2 = x^2 + \left(\frac{1}{4}x^2 - 6\right)^2$$

Sea $u = x^2$ (con $u \ge 0$):

$$d^2 = u + \left(\frac{u}{4} - 6\right)^2 = u + \frac{u^2}{16} - 3u + 36 = \frac{u^2}{16} - 2u + 36$$

Derivando e igualando a cero:

$$\frac{d(d^2)}{du} = \frac{u}{8} - 2 = 0 \quad\Rightarrow\quad u = 16$$

Evaluando en $u = 16$ (mínimo, pues es una parábola en $u$ con coeficiente principal positivo):

$$b^2 = \frac{16^2}{16} - 2(16) + 36 = 16 - 32 + 36 = 20$$

**Verificación:** el punto correspondiente es $(\pm 4, -2)$, efectivamente sobre la parábola ($\frac{16}{4} - 6 = -2$), con distancia al origen $\sqrt{16+4} = \sqrt{20}$. Comparado con el vértice $(0, -6)$, que da $d^2 = 36 > 20$, el mínimo es correcto.

## Resultado

$$\boxed{20}$$