Para hallar la razón de áreas $\frac{[YQZ]}{[XYZ]}$, utilizaremos trigonometría en el triángulo $\triangle XYZ$.

### Paso 1: Elementos del triángulo $\triangle XYZ$
Los lados del triángulo son $XY = 5$, $XZ = 7$ y $YZ = 6$. 

Primero calculamos el área de $\triangle XYZ$ mediante la fórmula de Herón. El semiperímetro es:
$$s = \frac{5 + 6 + 7}{2} = 9$$
Por lo tanto, el área $[XYZ]$ es:
$$[XYZ] = \sqrt{9(9-5)(9-6)(9-7)} = \sqrt{9 \cdot 4 \cdot 3 \cdot 2} = 6\sqrt{6}$$

Aplicando la Ley de Cosenos en $\triangle XYZ$, obtenemos los cosenos y senos de los ángulos $Y = \angle XYZ$ y $Z = \angle XZY$:
$$\cos Y = \frac{XY^2 + YZ^2 - XZ^2}{2 \cdot XY \cdot YZ} = \frac{5^2 + 6^2 - 7^2}{2 \cdot 5 \cdot 6} = \frac{12}{60} = \frac{1}{5} \implies \sin Y = \sqrt{1 - \left(\frac{1}{5}\right)^2} = \frac{2\sqrt{6}}{5}$$

$$\cos Z = \frac{XZ^2 + YZ^2 - XY^2}{2 \cdot XZ \cdot YZ} = \frac{7^2 + 6^2 - 5^2}{2 \cdot 7 \cdot 6} = \frac{60}{84} = \frac{5}{7} \implies \sin Z = \sqrt{1 - \left(\frac{5}{7}\right)^2} = \frac{2\sqrt{6}}{7}$$

---

### Paso 2: Determinación del ángulo $\theta = \angle XYQ = \angle XZQ$
Sea $\theta = \angle XYQ = \angle XZQ$. Como el punto $Q$ se encuentra en el interior de $\triangle XYZ$, los ángulos en la base del triángulo $\triangle YQZ$ son:
$$\angle QYZ = Y - \theta \quad \text{y} \quad \angle QZY = Z - \theta$$

Por la Ley de Senos en $\triangle YQZ$:
$$\frac{\sin(Z - \theta)}{\sin(Y - \theta)} = \frac{YQ}{QZ} = \frac{1}{2} \implies 2\sin(Z - \theta) = \sin(Y - \theta)$$

Desarrollando con las fórmulas de resta de ángulos:
$$2(\sin Z \cos\theta - \cos Z \sin\theta) = \sin Y \cos\theta - \cos Y \sin\theta$$

Sustituimos los valores conocidos de $\sin Y, \cos Y, \sin Z, \cos Z$:
$$2\left(\frac{2\sqrt{6}}{7}\cos\theta - \frac{5}{7}\sin\theta\right) = \frac{2\sqrt{6}}{5}\cos\theta - \frac{1}{5}\sin\theta$$

Multiplicando ambos lados por $35$:
$$20\sqrt{6}\cos\theta - 50\sin\theta = 14\sqrt{6}\cos\theta - 7\sin\theta$$
$$6\sqrt{6}\cos\theta = 43\sin\theta \implies \tan\theta = \frac{6\sqrt{6}}{43}$$

Como $\theta$ es agudo y $(6\sqrt{6})^2 + 43^2 = 216 + 1849 = 2065$, tenemos:
$$\sin\theta = \frac{6\sqrt{6}}{\sqrt{2065}}, \qquad \cos\theta = \frac{43}{\sqrt{2065}}$$

---

### Paso 3: Cálculo de los ángulos en $\triangle YQZ$
Calculamos ahora el seno y coseno de $Y - \theta$ y $Z - \theta$:
$$\sin(Y - \theta) = \sin Y \cos\theta - \cos Y \sin\theta = \frac{2\sqrt{6}}{5}\cdot\frac{43}{\sqrt{2065}} - \frac{1}{5}\cdot\frac{6\sqrt{6}}{\sqrt{2065}} = \frac{80\sqrt{6}}{5\sqrt{2065}} = \frac{16\sqrt{6}}{\sqrt{2065}}$$
$$\cos(Y - \theta) = \cos Y \cos\theta + \sin Y \sin\theta = \frac{1}{5}\cdot\frac{43}{\sqrt{2065}} + \frac{2\sqrt{6}}{5}\cdot\frac{6\sqrt{6}}{\sqrt{2065}} = \frac{115}{5\sqrt{2065}} = \frac{23}{\sqrt{2065}}$$

Como $\sin(Z - \theta) = \frac{1}{2}\sin(Y - \theta)$, obtenemos directamente:
$$\sin(Z - \theta) = \frac{8\sqrt{6}}{\sqrt{2065}}$$
$$\cos(Z - \theta) = \cos Z \cos\theta + \sin Z \sin\theta = \frac{5}{7}\cdot\frac{43}{\sqrt{2065}} + \frac{2\sqrt{6}}{7}\cdot\frac{6\sqrt{6}}{\sqrt{2065}} = \frac{287}{7\sqrt{2065}} = \frac{41}{\sqrt{2065}}$$

Por lo tanto, para el ángulo $\angle YQZ = 180^\circ - ((Y - \theta) + (Z - \theta))$:
$$\sin(\angle YQZ) = \sin((Y - \theta) + (Z - \theta)) = \sin(Y - \theta)\cos(Z - \theta) + \cos(Y - \theta)\sin(Z - \theta)$$
$$\sin(\angle YQZ) = \frac{16\sqrt{6} \cdot 41 + 23 \cdot 8\sqrt{6}}{2065} = \frac{840\sqrt{6}}{2065}$$

---

### Paso 4: Área de $\triangle YQZ$ y razón de áreas
Por la Ley de Senos en $\triangle YQZ$, dado que $YZ = 6$:
$$YQ = \frac{YZ \cdot \sin(Z - \theta)}{\sin(\angle YQZ)}$$

El área de $\triangle YQZ$ es entonces:
$$[YQZ] = \frac{1}{2} \cdot YZ \cdot YQ \cdot \sin(Y - \theta) = \frac{YZ^2 \cdot \sin(Y - \theta)\sin(Z - \theta)}{2\sin(\angle YQZ)}$$

Sustituyendo los valores obtenidos:
$$[YQZ] = 18 \cdot \frac{\frac{16\sqrt{6}}{\sqrt{2065}} \cdot \frac{8\sqrt{6}}{\sqrt{2065}}}{\frac{840\sqrt{6}}{2065}} = 18 \cdot \frac{128 \cdot 6}{840\sqrt{6}} = \frac{18 \cdot 128\sqrt{6}}{840} = \frac{96\sqrt{6}}{35}$$

Finalmente, dividimos entre el área $[XYZ] = 6\sqrt{6}$:
$$\frac{[YQZ]}{[XYZ]} = \frac{\frac{96\sqrt{6}}{35}}{6\sqrt{6}} = \frac{16}{35}$$

\boxed{\frac{16}{35}}