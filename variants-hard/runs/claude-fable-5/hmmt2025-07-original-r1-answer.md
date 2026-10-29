## Solución

**Planteamiento.** Sea $k = 2(a^2+1) = 3(b^2+1) = 4(c^2+1)$. Entonces:
$$a^2 = \frac{k}{2}-1, \qquad b^2 = \frac{k}{3}-1, \qquad c^2 = \frac{k}{4}-1.$$

**Sustitución trigonométrica.** La condición $ab+bc+ca=1$ se satisface exactamente cuando $a=\tan\alpha$, $b=\tan\beta$, $c=\tan\gamma$ con $\alpha+\beta+\gamma=\frac{\pi}{2}$ (ángulos agudos positivos). Con esta sustitución, $a^2+1=\sec^2\alpha$, así que:
$$\cos^2\alpha = \frac{2}{k}, \qquad \cos^2\beta = \frac{3}{k}, \qquad \cos^2\gamma = \frac{4}{k}.$$

**Usando la restricción angular.** Como $\gamma = \frac{\pi}{2}-(\alpha+\beta)$, se tiene $\cos\gamma = \sin(\alpha+\beta)$, es decir:
$$\sin\alpha\cos\beta + \cos\alpha\sin\beta = \frac{2}{\sqrt{k}}.$$

Sustituyendo $\sin^2\alpha = 1-\frac{2}{k}$ y $\sin^2\beta = 1-\frac{3}{k}$:
$$\sqrt{1-\tfrac{2}{k}}\cdot\sqrt{\tfrac{3}{k}} + \sqrt{\tfrac{2}{k}}\cdot\sqrt{1-\tfrac{3}{k}} = \frac{2}{\sqrt{k}}.$$

Multiplicando por $\sqrt{k}$ y escribiendo $x = \frac{6}{k}$:
$$\sqrt{3-x} + \sqrt{2-x} = 2.$$

**Resolviendo.** Como $(3-x)-(2-x)=1$, al dividir se obtiene $\sqrt{3-x}-\sqrt{2-x} = \frac{1}{2}$. Sumando ambas ecuaciones: $\sqrt{3-x} = \frac{5}{4}$, de donde $3-x = \frac{25}{16}$, es decir $x = \frac{23}{16}$ y por tanto $k = \frac{96}{23}$.

**Cálculo final.**
$$a^2 = \frac{48}{23}-1 = \frac{25}{23}, \quad b^2 = \frac{32}{23}-1 = \frac{9}{23}, \quad c^2 = \frac{24}{23}-1 = \frac{1}{23},$$
$$a = \frac{5}{\sqrt{23}}, \quad b = \frac{3}{\sqrt{23}}, \quad c = \frac{1}{\sqrt{23}}.$$

**Verificación:** $ab+bc+ca = \frac{15+3+5}{23} = 1$. ✓

Por lo tanto:
$$a+b+c = \frac{5+3+1}{\sqrt{23}} = \frac{9}{\sqrt{23}} = \frac{9\sqrt{23}}{23}.$$

$$\boxed{\dfrac{9\sqrt{23}}{23}}$$