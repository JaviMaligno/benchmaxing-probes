Para hallar el perímetro del cuadrilátero $ABCD$, analizamos paso a paso las relaciones angulares y métricas de los cuatro triángulos que se forman alrededor del punto interior $P$.

### Paso 1: Relaciones entre los ángulos
Definimos los ángulos dados como:
$$\begin{aligned}
\alpha &= \angle PAB = \angle PDA, \\
\beta &= \angle PAD = \angle PDC, \\
\gamma &= \angle PBA = \angle PCB, \\
\delta &= \angle PBC = \angle PCD.
\end{aligned}$$

La suma de los ángulos interiores de los cuatro triángulos $\triangle PAB$, $\triangle PBC$, $\triangle PCD$ y $\triangle PDA$ nos permite expresar los ángulos alrededor de $P$:
$$\begin{aligned}
\angle APB &= 180^\circ - (\alpha + \gamma), \\
\angle BPC &= 180^\circ - (\gamma + \delta), \\
\angle CPD &= 180^\circ - (\beta + \delta), \\
\angle DPA &= 180^\circ - (\alpha + \beta).
\end{aligned}$$

Como la suma de los ángulos alrededor de $P$ es $360^\circ$:
$$[180^\circ - (\alpha + \gamma)] + [180^\circ - (\gamma + \delta)] + [180^\circ - (\beta + \delta)] + [180^\circ - (\alpha + \beta)] = 360^\circ$$
Simplificando, obtenemos:
$$\alpha + \beta + \gamma + \delta = 180^\circ.$$

De aquí se deduce que los ángulos opuestos alrededor de $P$ son suplementarios:
$$\angle APB + \angle CPD = 180^\circ \quad \text{y} \quad \angle BPC + \angle DPA = 180^\circ.$$

---

### Paso 2: Cálculo de $PD$ y razones trigonométricas
Aplicamos la ley de los senos en cada uno de los cuatro triángulos:
1. En $\triangle PAB$: $\frac{\sin \alpha}{\sin \gamma} = \frac{PB}{PA} = \frac{5}{4} \implies \sin \alpha = \frac{5}{4}\sin \gamma$.
2. En $\triangle PBC$: $\frac{\sin \delta}{\sin \gamma} = \frac{PC}{PB} = \frac{10}{5} = 2 \implies \sin \delta = 2\sin \gamma$.
3. En $\triangle PCD$: $\frac{\sin \beta}{\sin \delta} = \frac{PC}{PD} = \frac{10}{PD}$.
4. En $\triangle PDA$: $\frac{\sin \beta}{\sin \alpha} = \frac{PD}{PA} = \frac{PD}{4}$.

Igualando $\sin \beta$ de las ecuaciones (3) y (4):
$$\frac{10}{PD}\sin \delta = \frac{PD}{4}\sin \alpha \implies PD^2 = 40 \cdot \frac{\sin \delta}{\sin \alpha} = 40 \cdot \frac{2\sin \gamma}{\frac{5}{4}\sin \gamma} = 64 \implies PD = 8.$$

---

### Paso 3: Cálculo de los lados $AB$ y $CD$
Por la ley de los senos en $\triangle PAB$ y $\triangle PCD$, usando que $\sin \angle APB = \sin \angle CPD$ (ya que $\angle APB + \angle CPD = 180^\circ$):
$$AB = \frac{PA}{\sin \gamma}\sin \angle APB = \frac{4}{\sin \gamma}\sin \angle APB,$$
$$CD = \frac{PD}{\sin \delta}\sin \angle CPD = \frac{8}{2\sin \gamma}\sin \angle APB = \frac{4}{\sin \gamma}\sin \angle APB.$$
Por lo tanto, $AB = CD$.

Sea $\theta_1 = \angle APB$, de modo que $\angle CPD = 180^\circ - \theta_1$ y $\cos \angle CPD = -\cos \theta_1$. Aplicando la ley de los cosenos en $\triangle PAB$ y $\triangle PCD$:
$$\begin{aligned}
AB^2 &= 4^2 + 5^2 - 2(4)(5)\cos \theta_1 = 41 - 40\cos \theta_1, \\
CD^2 &= 8^2 + 10^2 - 2(8)(10)(-\cos \theta_1) = 4(41 + 40\cos \theta_1).
\end{aligned}$$
Como $AB^2 = CD^2$, dividimos la segunda ecuación por $4$ y la sumamos a la primera para eliminar $\cos \theta_1$:
$$AB^2 + \frac{1}{4}AB^2 = 82 \implies \frac{5}{4}AB^2 = 82 \implies AB^2 = \frac{328}{5}.$$
Por consiguiente:
$$AB = CD = \sqrt{\frac{328}{5}} = \frac{2\sqrt{410}}{5}.$$

---

### Paso 4: Cálculo de los lados $BC$ y $DA$
De manera análoga, por la ley de los senos en $\triangle PBC$ y $\triangle PDA$, usando que $\sin \angle BPC = \sin \angle DPA$:
$$BC = \frac{PB}{\sin \gamma}\sin \angle BPC = \frac{5}{\sin \gamma}\sin \angle BPC,$$
$$DA = \frac{PA}{\sin \alpha}\sin \angle DPA = \frac{4}{\frac{5}{4}\sin \gamma}\sin \angle BPC = \frac{16}{5\sin \gamma}\sin \angle BPC.$$
Esto implica que $DA = \frac{16}{25}BC$.

Sea $\theta_2 = \angle BPC$, de modo que $\angle DPA = 180^\circ - \theta_2$ y $\cos \angle DPA = -\cos \theta_2$. Aplicando la ley de los cosenos en $\triangle PBC$ y $\triangle PDA$:
$$\begin{aligned}
BC^2 &= 5^2 + 10^2 - 2(5)(10)\cos \theta_2 = 125 - 100\cos \theta_2, \\
DA^2 &= 4^2 + 8^2 - 2(4)(8)(-\cos \theta_2) = \frac{16}{25}(125 + 100\cos \theta_2).
\end{aligned}$$
Sustituyendo $DA^2 = \left(\frac{16}{25}\right)^2 BC^2$ en la segunda ecuación y dividiendo por $\frac{16}{25}$:
$$\frac{16}{25}BC^2 = 125 + 100\cos \theta_2.$$
Sumando esta ecuación con $BC^2 = 125 - 100\cos \theta_2$:
$$\left(1 + \frac{16}{25}\right)BC^2 = 250 \implies \frac{41}{25}BC^2 = 250 \implies BC^2 = \frac{6250}{41}.$$
Por lo tanto:
$$BC = \frac{25\sqrt{10}}{\sqrt{41}} = \frac{25\sqrt{410}}{41}, \quad DA = \frac{16}{25}BC = \frac{16\sqrt{410}}{41}.$$

---

### Paso 5: Perímetro de $ABCD$
Sumamos las longitudes de los cuatro lados:
$$\begin{aligned}
\text{Perímetro} &= (AB + CD) + (BC + DA) \\
&= \left(\frac{2\sqrt{410}}{5} + \frac{2\sqrt{410}}{5}\right) + \left(\frac{25\sqrt{410}}{41} + \frac{16\sqrt{410}}{41}\right) \\
&= \frac{4\sqrt{410}}{5} + \frac{41\sqrt{410}}{41} \\
&= \frac{4\sqrt{410}}{5} + \sqrt{410} \\
&= \frac{9\sqrt{410}}{5}.
\end{aligned}$$

\boxed{\frac{9\sqrt{410}}{5}}