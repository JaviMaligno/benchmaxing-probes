Para hallar la razón de áreas $\frac{[BPC]}{[ABC]}$, procedemos paso a paso utilizando trigonometría.

### Paso 1: Elementos del triángulo $\triangle ABC$
Sean $a = BC = 7$, $b = AC = 8$ y $c = AB = 6$ las longitudes de los lados de $\triangle ABC$, y sean $B = \angle ABC$ y $C = \angle ACB$.

Aplicando la ley de cosenos en $\triangle ABC$:
$$\cos B = \frac{a^2 + c^2 - b^2}{2ac} = \frac{7^2 + 6^2 - 8^2}{2 \cdot 7 \cdot 6} = \frac{49 + 36 - 64}{84} = \frac{21}{84} = \frac{1}{4}$$
$$\cos C = \frac{a^2 + b^2 - c^2}{2ab} = \frac{7^2 + 8^2 - 6^2}{2 \cdot 7 \cdot 8} = \frac{49 + 64 - 36}{112} = \frac{77}{112} = \frac{11}{16}$$

A partir de estos valores obtenemos los senos correspondientes:
$$\sin B = \sqrt{1 - \cos^2 B} = \sqrt{1 - \frac{1}{16}} = \frac{\sqrt{15}}{4}$$
$$\sin C = \frac{c}{b}\sin B = \frac{6}{8} \cdot \frac{\sqrt{15}}{4} = \frac{3\sqrt{15}}{16}$$

El área de $\triangle ABC$ es entonces:
$$[ABC] = \frac{1}{2} ac \sin B = \frac{1}{2} \cdot 7 \cdot 6 \cdot \frac{\sqrt{15}}{4} = \frac{21\sqrt{15}}{4}$$

---

### Paso 2: Cálculo del ángulo $\theta = \angle ABP = \angle ACP$
Como $P$ está en el interior de $\triangle ABC$, tenemos que $\angle PBC = B - \theta$ y $\angle PCB = C - \theta$.

Aplicando la ley de senos en $\triangle BPC$:
$$\frac{\sin(B - \theta)}{\sin(C - \theta)} = \frac{PC}{BP} = 2 \implies \sin(B - \theta) = 2\sin(C - \theta)$$

Desarrollando ambos miembros mediante la identidad del seno de la diferencia:
$$\sin B \cos\theta - \cos B \sin\theta = 2(\sin C \cos\theta - \cos C \sin\theta)$$

Sustituyendo los valores de $\sin B, \cos B, \sin C$ y $\cos C$:
$$\frac{\sqrt{15}}{4}\cos\theta - \frac{1}{4}\sin\theta = 2\left(\frac{3\sqrt{15}}{16}\cos\theta - \frac{11}{16}\sin\theta\right) = \frac{3\sqrt{15}}{8}\cos\theta - \frac{11}{8}\sin\theta$$

Multiplicando por $8$ y agrupando términos:
$$2\sqrt{15}\cos\theta - 2\sin\theta = 3\sqrt{15}\cos\theta - 11\sin\theta \implies 9\sin\theta = \sqrt{15}\cos\theta$$

De aquí obtenemos $\tan\theta = \frac{\sqrt{15}}{9}$. Como $0 < \theta < 180^\circ$, se sigue que:
$$\cos\theta = \frac{1}{\sqrt{1 + \tan^2\theta}} = \frac{1}{\sqrt{1 + \frac{15}{81}}} = \sqrt{\frac{81}{96}} = \frac{3\sqrt{6}}{8}$$
$$\sin\theta = \tan\theta \cos\theta = \frac{\sqrt{15}}{9} \cdot \frac{3\sqrt{6}}{8} = \frac{\sqrt{10}}{8}$$

---

### Paso 3: Elementos y área de $\triangle BPC$
Calculamos el seno y el coseno de $\angle PBC = B - \theta$:
$$\sin(B - \theta) = \sin B \cos\theta - \cos B \sin\theta = \frac{\sqrt{15}}{4} \cdot \frac{3\sqrt{6}}{8} - \frac{1}{4} \cdot \frac{\sqrt{10}}{8} = \frac{9\sqrt{10} - \sqrt{10}}{32} = \frac{\sqrt{10}}{4}$$
$$\cos(B - \theta) = \cos B \cos\theta + \sin B \sin\theta = \frac{1}{4} \cdot \frac{3\sqrt{6}}{8} + \frac{\sqrt{15}}{4} \cdot \frac{\sqrt{10}}{8} = \frac{3\sqrt{6} + 5\sqrt{6}}{32} = \frac{\sqrt{6}}{4}$$

Sea $BP = x$, de modo que $PC = 2x$. Por la ley de cosenos en $\triangle BPC$ y en los triángulos $\triangle ABP$ y $\triangle ACP$:
1. En $\triangle BPC$:
   $$(2x)^2 = x^2 + 7^2 - 2 \cdot 7 \cdot x \cos(B - \theta) \implies 3x^2 = 49 - 14x \cdot \frac{\sqrt{6}}{4} = 49 - \frac{7\sqrt{6}}{2}x$$
2. Igualando $AP^2$ por la ley de cosenos en $\triangle ABP$ y $\triangle ACP$:
   $$6^2 + x^2 - 12x\cos\theta = 8^2 + (2x)^2 - 32x\cos\theta \implies 3x^2 + 28 = 20x\cos\theta = 20x \cdot \frac{3\sqrt{6}}{8} = \frac{15\sqrt{6}}{2}x$$

Sustituyendo $3x^2$ de la primera ecuación en la segunda:
$$49 - \frac{7\sqrt{6}}{2}x + 28 = \frac{15\sqrt{6}}{2}x \implies 77 = 11\sqrt{6}x \implies x = \frac{7}{\sqrt{6}}$$

---

### Paso 4: Razón de áreas
Dado que $\triangle BPC$ y $\triangle ABC$ comparten la base $BC$, la razón de sus áreas es:
$$\frac{[BPC]}{[ABC]} = \frac{\frac{1}{2} \cdot BC \cdot BP \cdot \sin(B - \theta)}{\frac{1}{2} \cdot BC \cdot AB \cdot \sin B} = \frac{x \sin(B - \theta)}{6 \sin B}$$

Sustituyendo los valores hallados:
$$\frac{[BPC]}{[ABC]} = \frac{\frac{7}{\sqrt{6}} \cdot \frac{\sqrt{10}}{4}}{6 \cdot \frac{\sqrt{15}}{4}} = \frac{7\sqrt{10}}{6\sqrt{90}} = \frac{7\sqrt{10}}{6 \cdot 3\sqrt{10}} = \frac{7}{18}$$

\boxed{\frac{7}{18}}