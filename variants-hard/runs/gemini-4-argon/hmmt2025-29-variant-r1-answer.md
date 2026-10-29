Para calcular la longitud del lado $PQ$, situemos el rectángulo $PQRS$ en un sistema de coordenadas cartesianas.

### 1. Planteamiento en coordenadas
Sea $x = PQ = RS$ la longitud buscada, y sabemos que $QR = PS = 30$. Ubicamos los vértices del rectángulo en:
$$P = (0, 0), \quad Q = (x, 0), \quad R = (x, 30), \quad S = (0, 30)$$

Sea $Y = (u, v)$ el punto en el interior del rectángulo, de modo que $0 < u < x$ y $0 < v < 30$.
Como $\angle PYQ = 90^\circ$, los vectores $\overrightarrow{YP} = (-u, -v)$ y $\overrightarrow{YQ} = (x - u, -v)$ son ortogonales, por lo que su producto escalar es cero:
$$\overrightarrow{YP} \cdot \overrightarrow{YQ} = -u(x - u) + v^2 = 0 \implies v^2 = u(x - u) \tag{1}$$

---

### 2. Análisis del triángulo $\triangle PYS$
En el triángulo $\triangle PYS$, el lado opuesto al ángulo $\angle PYS$ es $PS = 30$ y su circunradio es $R_1 = 17$. Por el teorema de los senos:
$$\sin \angle PYS = \frac{PS}{2 R_1} = \frac{30}{2 \cdot 17} = \frac{15}{17}$$
Dado que $\triangle PYS$ es acutángulo, $\angle PYS < 90^\circ$, de modo que:
$$\cos \angle PYS = \sqrt{1 - \left(\frac{15}{17}\right)^2} = \frac{8}{17} \implies \cot \angle PYS = \frac{8}{15}$$

Por otra parte, considerando los vectores $\overrightarrow{YP} = (-u, -v)$ y $\overrightarrow{YS} = (-u, 30 - v)$:
- El doble del área de $\triangle PYS$ es $PY \cdot SY \sin \angle PYS = PS \cdot u = 30u$.
- El producto escalar es $\overrightarrow{YP} \cdot \overrightarrow{YS} = PY \cdot SY \cos \angle PYS = u^2 + v^2 - 30v$.

Dividiendo ambas expresiones obtenemos:
$$\cot \angle PYS = \frac{u^2 + v^2 - 30v}{30u} = \frac{8}{15} \implies u^2 + v^2 - 30v = 16u$$
Usando la relación (1), sabemos que $u^2 + v^2 = u^2 + u(x - u) = ux$. Sustituyendo esto en la ecuación anterior:
$$ux - 30v = 16u \implies u(x - 16) = 30v \tag{2}$$

---

### 3. Análisis del triángulo $\triangle QYR$
De manera análoga, en el triángulo $\triangle QYR$, el lado opuesto a $\angle QYR$ es $QR = 30$ y su circunradio es $R_2 = 25$. Por el teorema de los senos:
$$\sin \angle QYR = \frac{QR}{2 R_2} = \frac{30}{2 \cdot 25} = \frac{3}{5}$$
Como $\triangle QYR$ también es acutángulo, $\angle QYR < 90^\circ$, por lo que:
$$\cos \angle QYR = \sqrt{1 - \left(\frac{3}{5}\right)^2} = \frac{4}{5} \implies \cot \angle QYR = \frac{4}{3}$$

Usando los vectores $\overrightarrow{YQ} = (x - u, -v)$ y $\overrightarrow{YR} = (x - u, 30 - v)$:
- El doble del área de $\triangle QYR$ es $QY \cdot RY \sin \angle QYR = QR \cdot (x - u) = 30(x - u)$.
- El producto escalar es $\overrightarrow{YQ} \cdot \overrightarrow{YR} = QY \cdot RY \cos \angle QYR = (x - u)^2 + v^2 - 30v$.

Dividiendo ambas expresiones:
$$\cot \angle QYR = \frac{(x - u)^2 + v^2 - 30v}{30(x - u)} = \frac{4}{3} \implies (x - u)^2 + v^2 - 30v = 40(x - u)$$
Usando nuevamente la relación (1), tenemos $(x - u)^2 + v^2 = (x - u)^2 + u(x - u) = x(x - u)$. Sustituyendo:
$$x(x - u) - 30v = 40(x - u) \implies (x - u)(x - 40) = 30v \tag{3}$$

---

### 4. Cálculo de $PQ = x$
De las ecuaciones (2) y (3), despejamos $u$ y $x - u$:
$$u = \frac{30v}{x - 16}, \qquad x - u = \frac{30v}{x - 40}$$
Como $u > 0$, $x - u > 0$ y $v > 0$, se debe cumplir que $x > 40$. Sustituyendo ambas expresiones en la ecuación (1), $u(x - u) = v^2$:
$$\left(\frac{30v}{x - 16}\right)\left(\frac{30v}{x - 40}\right) = v^2$$
Dividiendo entre $v^2 > 0$:
$$(x - 16)(x - 40) = 900$$
Expandiendo y resolviendo la ecuación cuadrática:
$$x^2 - 56x + 640 = 900 \implies x^2 - 56x - 260 = 0$$
$$x = 28 \pm \sqrt{28^2 + 260} = 28 \pm \sqrt{784 + 260} = 28 \pm \sqrt{1044} = 28 \pm 6\sqrt{29}$$

Dado que $x > 40$, descartamos la raíz negativa y tomamos únicamente la positiva.

\boxed{28 + 6\sqrt{29}}