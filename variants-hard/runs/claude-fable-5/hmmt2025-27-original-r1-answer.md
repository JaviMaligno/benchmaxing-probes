## Solución

**Planteamiento.** Sea $\angle ABP = \angle ACP = \theta$, $BP = x$, $PC = 2x$. Como $P$ está dentro del triángulo, $\angle PBC = B - \theta$ y $\angle PCB = C - \theta$.

**Datos del triángulo.** Con $a = BC = 7$, $b = AC = 8$, $c = AB = 6$, por ley de cosenos:

$$\cos A = \frac{64+36-49}{96} = \frac{17}{32}, \quad \cos B = \frac{49+36-64}{84} = \frac{1}{4}, \quad \cos C = \frac{49+64-36}{112} = \frac{11}{16}$$

De ahí: $\sin A = \frac{7\sqrt{15}}{32}$, $\sin B = \frac{\sqrt{15}}{4}$, $\sin C = \frac{3\sqrt{15}}{16}$.

**Hallar $\theta$.** En $\triangle BPC$, por ley de senos:
$$\frac{BP}{PC} = \frac{\sin(C-\theta)}{\sin(B-\theta)} = \frac{1}{2} \;\Longrightarrow\; 2\sin(C-\theta) = \sin(B-\theta)$$

Expandiendo y despejando:
$$\tan\theta = \frac{2\sin C - \sin B}{2\cos C - \cos B} = \frac{\frac{6\sqrt{15}}{16} - \frac{4\sqrt{15}}{16}}{\frac{22}{16} - \frac{4}{16}} = \frac{2\sqrt{15}}{18} = \frac{\sqrt{15}}{9}$$

Entonces $\sin\theta = \frac{\sqrt{15}}{4\sqrt{6}}$, $\cos\theta = \frac{9}{4\sqrt{6}}$. Calculando:
$$\sin(C-\theta) = \frac{3\sqrt{15}}{16}\cdot\frac{9}{4\sqrt{6}} - \frac{11}{16}\cdot\frac{\sqrt{15}}{4\sqrt{6}} = \frac{16\sqrt{15}}{64\sqrt{6}} = \sin\theta$$

Es decir, $\theta = \tfrac{C}{2}$, y por tanto $\angle BPC = \pi - (B-\theta) - (C-\theta) = A + 2\theta = A + C$, lo que da $\sin(\angle BPC) = \sin B$.

**Hallar $x$.** En $\triangle BPC$: $\dfrac{BP}{\sin(C-\theta)} = \dfrac{BC}{\sin(\angle BPC)}$, entonces
$$x = \frac{7\sin\theta}{\sin B} = \frac{7 \cdot \frac{\sqrt{15}}{4\sqrt{6}}}{\frac{\sqrt{15}}{4}} = \frac{7}{\sqrt{6}} \;\Longrightarrow\; x^2 = \frac{49}{6}$$

**Áreas.**
$$[BPC] = \tfrac{1}{2}\cdot x \cdot 2x \cdot \sin(\angle BPC) = \frac{49}{6}\cdot\frac{\sqrt{15}}{4} = \frac{49\sqrt{15}}{24}$$
$$[ABC] = \tfrac{1}{2}\cdot 6 \cdot 8 \cdot \sin A = 24\cdot\frac{7\sqrt{15}}{32} = \frac{21\sqrt{15}}{4}$$

$$\frac{[BPC]}{[ABC]} = \frac{49\sqrt{15}/24}{21\sqrt{15}/4} = \frac{49}{126} = \frac{7}{18}$$

$$\boxed{\dfrac{7}{18}}$$