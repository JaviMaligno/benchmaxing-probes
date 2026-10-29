## Solución paso a paso

**Paso 1: Simplificar el numerador**

Agrupando los términos y usando la identidad del coseno de una suma, $\cos A\cos B - \sin A \sin B = \cos(A+B)$:

$$\cos 5° \cos 20° - \sin 5° \sin 20° + \cos 35° \cos 50° - \sin 35° \sin 50°$$
$$= \cos(5°+20°) + \cos(35°+50°) = \cos 25° + \cos 85°.$$

**Paso 2: Simplificar el denominador**

Usando la identidad del seno de una suma, $\sin A\cos B + \cos A \sin B = \sin(A+B)$:

$$\sin 5° \cos 20° + \cos 5° \sin 20° - \sin 35° \cos 50° - \cos 35° \sin 50°$$
$$= \sin 25° - \sin 85°.$$

**Paso 3: Aplicar fórmulas de suma a producto**

- $\cos 25° + \cos 85° = 2\cos 55° \cos\left(-\frac{30°}{2}\cdot 1\right)$... más precisamente:
$$\cos A + \cos B = 2\cos\frac{A+B}{2}\cos\frac{A-B}{2} \implies \cos 25° + \cos 85° = 2\cos 55° \cos 30°.$$
- $$\sin A - \sin B = 2\cos\frac{A+B}{2}\sin\frac{A-B}{2} \implies \sin 25° - \sin 85° = 2\cos 55° \sin(-30°) = -2\cos 55° \sin 30°.$$

**Paso 4: Calcular la tangente**

$$\tan\theta = \frac{2\cos 55° \cos 30°}{-2\cos 55° \sin 30°} = -\frac{\cos 30°}{\sin 30°} = -\frac{\frac{\sqrt{3}}{2}}{\frac{1}{2}} = -\sqrt{3}.$$

**Paso 5: Encontrar el menor ángulo positivo**

Como $\tan\theta = -\sqrt{3} < 0$, $\theta$ está en el segundo cuadrante (para el menor ángulo positivo). El ángulo de referencia es $60°$, por lo que:

$$\theta = 180° - 60° = 120°.$$

$$\boxed{120}$$