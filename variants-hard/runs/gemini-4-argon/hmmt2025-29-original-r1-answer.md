Para encontrar la longitud del lado $AB$, planteamos las relaciones trigonométricas y geométricas de los triángulos dentro del rectángulo $ABCD$.

**Paso 1: Parametrización en el triángulo rectángulo $\triangle AXB$**
Sea $c = AB$ la longitud que deseamos calcular y sea $\theta = \angle XAB$. 
Dado que $\angle AXB = 90^\circ$ y el punto $X$ está en el interior del rectángulo, se tiene que $0^\circ < \theta < 90^\circ$ y $\angle XBA = 90^\circ - \theta$. A partir de esto, podemos expresar los lados $AX$ y $BX$ como:
$$AX = c \cos\theta$$
$$BX = c \sin\theta$$

Como los ángulos del rectángulo son rectos ($\angle DAB = \angle CBA = 90^\circ$), los ángulos adyacentes en los vértices $A$ y $B$ son:
$$\angle XAD = 90^\circ - \theta$$
$$\angle XBC = 90^\circ - (90^\circ - \theta) = \theta$$

---

**Paso 2: Análisis del triángulo acutángulo $\triangle AXD$**
Sabemos que $AD = BC = 24$ y que el circunradio de $\triangle AXD$ es $R_1 = 13$.
Sea $\alpha = \angle AXD$. Por la Ley de los Senos en $\triangle AXD$:
$$\sin\alpha = \frac{AD}{2R_1} = \frac{24}{2(13)} = \frac{12}{13}$$

Como $\triangle AXD$ es acutángulo, $\alpha < 90^\circ$, por lo que su coseno es positivo:
$$\cos\alpha = \sqrt{1 - \sin^2\alpha} = \frac{5}{13}$$

La suma de los ángulos internos en $\triangle AXD$ es $180^\circ$, por lo que el ángulo $\angle XDA$ es:
$$\angle XDA = 180^\circ - \alpha - \angle XAD = 180^\circ - \alpha - (90^\circ - \theta) = 90^\circ - (\alpha - \theta)$$

Aplicando nuevamente la Ley de los Senos para el lado $AX$:
$$AX = 2R_1 \sin(\angle XDA) = 26 \sin(90^\circ - (\alpha - \theta)) = 26 \cos(\alpha - \theta)$$

Sustituyendo $AX = c \cos\theta$ y desarrollando el coseno de la diferencia:
$$c \cos\theta = 26 (\cos\alpha \cos\theta + \sin\alpha \sin\theta)$$
$$c \cos\theta = 26 \left(\frac{5}{13}\cos\theta + \frac{12}{13}\sin\theta\right) = 10\cos\theta + 24\sin\theta$$

Dividiendo ambos lados entre $\cos\theta$:
$$c = 10 + 24\tan\theta \implies c - 10 = 24\tan\theta \quad \text{(Ecuación 1)}$$

---

**Paso 3: Análisis del triángulo acutángulo $\triangle BXC$**
Sabemos que $BC = 24$ y que el circunradio de $\triangle BXC$ es $R_2 = 15$.
Sea $\beta = \angle BXC$. Por la Ley de los Senos en $\triangle BXC$:
$$\sin\beta = \frac{BC}{2R_2} = \frac{24}{2(15)} = \frac{4}{5}$$

Como $\triangle BXC$ es acutángulo, $\beta < 90^\circ$, lo que implica:
$$\cos\beta = \sqrt{1 - \sin^2\beta} = \frac{3}{5}$$

El tercer ángulo del triángulo es $\angle XCB = 180^\circ - (\beta + \theta)$. Aplicando la Ley de los Senos para el lado $BX$:
$$BX = 2R_2 \sin(\angle XCB) = 30 \sin(180^\circ - (\beta + \theta)) = 30 \sin(\beta + \theta)$$

Sustituyendo $BX = c \sin\theta$ y desarrollando el seno de la suma:
$$c \sin\theta = 30 (\sin\beta \cos\theta + \cos\beta \sin\theta)$$
$$c \sin\theta = 30 \left(\frac{4}{5}\cos\theta + \frac{3}{5}\sin\theta\right) = 24\cos\theta + 18\sin\theta$$

Dividiendo ambos lados entre $\sin\theta$:
$$c = 24\cot\theta + 18 \implies c - 18 = 24\cot\theta \quad \text{(Ecuación 2)}$$

---

**Paso 4: Resolución para $c = AB$**
Multiplicamos la Ecuación 1 y la Ecuación 2 para eliminar $\theta$:
$$(c - 10)(c - 18) = (24\tan\theta)(24\cot\theta)$$
$$(c - 10)(c - 18) = 576$$

Sea $u = c - 14$. La ecuación se transforma en:
$$(u + 4)(u - 4) = 576$$
$$u^2 - 16 = 576 \implies u^2 = 592$$

Dado que $\cot\theta > 0$, se cumple que $c > 18$, por lo que tomamos la raíz positiva:
$$u = \sqrt{592} = \sqrt{16 \times 37} = 4\sqrt{37}$$

Finalmente, despejamos $c$:
$$c = 14 + 4\sqrt{37}$$

\boxed{14 + 4\sqrt{37}}