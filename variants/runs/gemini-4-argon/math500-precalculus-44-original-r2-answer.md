Para encontrar la medida en grados del menor ángulo positivo $\theta$, simplificamos el numerador y el denominador de la fracción utilizando las identidades trigonométricas de suma de ángulos:
$$\cos(A + B) = \cos A \cos B - \sin A \sin B$$
$$\sin(A + B) = \sin A \cos B + \cos A \sin B$$

**Paso 1: Simplificar el numerador**
Agrupamos los términos del numerador:
$$\text{Numerador} = (\cos 5^\circ \cos 20^\circ - \sin 5^\circ \sin 20^\circ) + (\cos 35^\circ \cos 50^\circ - \sin 35^\circ \sin 50^\circ)$$
Aplicando la identidad del coseno de la suma:
$$\text{Numerador} = \cos(5^\circ + 20^\circ) + \cos(35^\circ + 50^\circ) = \cos 25^\circ + \cos 85^\circ$$

**Paso 2: Simplificar el denominador**
Agrupamos los términos del denominador:
$$\text{Denominador} = (\sin 5^\circ \cos 20^\circ + \cos 5^\circ \sin 20^\circ) - (\sin 35^\circ \cos 50^\circ + \cos 35^\circ \sin 50^\circ)$$
Aplicando la identidad del seno de la suma:
$$\text{Denominador} = \sin(5^\circ + 20^\circ) - \sin(35^\circ + 50^\circ) = \sin 25^\circ - \sin 85^\circ$$

**Paso 3: Aplicar las identidades de suma a producto**
Recordamos que:
$$\cos A + \cos B = 2 \cos\left(\frac{A+B}{2}\right) \cos\left(\frac{A-B}{2}\right)$$
$$\sin A - \sin B = 2 \cos\left(\frac{A+B}{2}\right) \sin\left(\frac{A-B}{2}\right)$$

Aplicando esto a nuestra fracción:
$$\tan \theta = \frac{\cos 25^\circ + \cos 85^\circ}{\sin 25^\circ - \sin 85^\circ} = \frac{2 \cos\left(\frac{25^\circ + 85^\circ}{2}\right) \cos\left(\frac{25^\circ - 85^\circ}{2}\right)}{2 \cos\left(\frac{25^\circ + 85^\circ}{2}\right) \sin\left(\frac{25^\circ - 85^\circ}{2}\right)}$$

$$\tan \theta = \frac{2 \cos 55^\circ \cos(-30^\circ)}{2 \cos 55^\circ \sin(-30^\circ)}$$

Cancelando el factor común $2 \cos 55^\circ$ y usando la paridad de las funciones ($\cos(-x) = \cos x$ y $\sin(-x) = -\sin x$):
$$\tan \theta = \frac{\cos 30^\circ}{-\sin 30^\circ} = -\cot 30^\circ$$

**Paso 4: Hallar el menor ángulo positivo $\theta$**
Como $\cot 30^\circ = \tan 60^\circ$, tenemos:
$$\tan \theta = -\tan 60^\circ = \tan(180^\circ - 60^\circ) = \tan 120^\circ$$

Por lo tanto, el menor ángulo positivo $\theta$ es $120^\circ$.

\boxed{120^\circ}