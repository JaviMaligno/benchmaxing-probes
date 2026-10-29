Para encontrar la medida en grados del menor ángulo positivo $\theta$, primero agrupamos convenientemente los términos en el numerador y en el denominador utilizando las identidades trigonométricas para la suma de ángulos:
$$\cos(A + B) = \cos A \cos B - \sin A \sin B$$
$$\sin(A + B) = \sin A \cos B + \cos A \sin B$$

**Paso 1: Simplificar el numerador**
Agrupando los términos del numerador:
$$\text{Numerador} = (\cos 5^\circ \cos 20^\circ - \sin 5^\circ \sin 20^\circ) + (\cos 35^\circ \cos 50^\circ - \sin 35^\circ \sin 50^\circ)$$
$$= \cos(5^\circ + 20^\circ) + \cos(35^\circ + 50^\circ)$$
$$= \cos 25^\circ + \cos 85^\circ$$

**Paso 2: Simplificar el denominador**
Agrupando los términos del denominador:
$$\text{Denominador} = (\sin 5^\circ \cos 20^\circ + \cos 5^\circ \sin 20^\circ) - (\sin 35^\circ \cos 50^\circ + \cos 35^\circ \sin 50^\circ)$$
$$= \sin(5^\circ + 20^\circ) - \sin(35^\circ + 50^\circ)$$
$$= \sin 25^\circ - \sin 85^\circ$$

**Paso 3: Aplicar las identidades de suma a producto**
Usamos las fórmulas de transformación de suma a producto:
* $\cos A + \cos B = 2 \cos\left(\frac{A+B}{2}\right) \cos\left(\frac{A-B}{2}\right)$
* $\sin A - \sin B = 2 \cos\left(\frac{A+B}{2}\right) \sin\left(\frac{A-B}{2}\right)$

Para el numerador:
$$\cos 85^\circ + \cos 25^\circ = 2 \cos\left(\frac{85^\circ + 25^\circ}{2}\right) \cos\left(\frac{85^\circ - 25^\circ}{2}\right) = 2 \cos 55^\circ \cos 30^\circ$$

Para el denominador:
$$\sin 25^\circ - \sin 85^\circ = 2 \cos\left(\frac{25^\circ + 85^\circ}{2}\right) \sin\left(\frac{25^\circ - 85^\circ}{2}\right) = 2 \cos 55^\circ \sin(-30^\circ) = -2 \cos 55^\circ \sin 30^\circ$$

**Paso 4: Calcular $\tan \theta$**
Sustituyendo en la expresión original:
$$\tan \theta = \frac{2 \cos 55^\circ \cos 30^\circ}{-2 \cos 55^\circ \sin 30^\circ} = -\frac{\cos 30^\circ}{\sin 30^\circ} = -\cot 30^\circ = -\sqrt{3}$$

El menor ángulo positivo $\theta$ cuya tangente es $-\sqrt{3}$ se encuentra en el segundo cuadrante:
$$\theta = 180^\circ - 60^\circ = 120^\circ$$

\boxed{120}