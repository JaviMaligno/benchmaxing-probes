Para encontrar la medida en grados del menor ángulo positivo $\theta$, simplificamos el numerador y el denominador de la fracción utilizando las identidades trigonométricas para el coseno y el seno de la suma de dos ángulos:
\[\cos(A + B) = \cos A \cos B - \sin A \sin B\]
\[\sin(A + B) = \sin A \cos B + \cos A \sin B\]

**Paso 1: Simplificar el numerador**

Agrupamos los términos del numerador:
\[\text{Numerador} = (\cos 10^\circ \cos 5^\circ - \sin 10^\circ \sin 5^\circ) + (\cos 55^\circ \cos 80^\circ - \sin 55^\circ \sin 80^\circ)\]
Aplicando la identidad de la suma para el coseno:
\[\text{Numerador} = \cos(10^\circ + 5^\circ) + \cos(55^\circ + 80^\circ) = \cos 15^\circ + \cos 135^\circ\]

**Paso 2: Simplificar el denominador**

Agrupamos los términos del denominador:
\[\text{Denominador} = (\sin 10^\circ \cos 5^\circ + \cos 10^\circ \sin 5^\circ) - (\sin 55^\circ \cos 80^\circ + \cos 55^\circ \sin 80^\circ)\]
Aplicando la identidad de la suma para el seno:
\[\text{Denominador} = \sin(10^\circ + 5^\circ) - \sin(55^\circ + 80^\circ) = \sin 15^\circ - \sin 135^\circ\]

**Paso 3: Transformar sumas en productos**

Usamos las identidades de suma a producto:
\[\cos X + \cos Y = 2 \cos\left(\frac{X+Y}{2}\right) \cos\left(\frac{X-Y}{2}\right)\]
\[\sin X - \sin Y = 2 \cos\left(\frac{X+Y}{2}\right) \sin\left(\frac{X-Y}{2}\right)\]

Sustituyendo $X = 15^\circ$ y $Y = 135^\circ$:
\[\text{Numerador} = 2 \cos\left(\frac{15^\circ + 135^\circ}{2}\right) \cos\left(\frac{15^\circ - 135^\circ}{2}\right) = 2 \cos 75^\circ \cos(-60^\circ) = 2 \cos 75^\circ \cos 60^\circ\]
\[\text{Denominador} = 2 \cos\left(\frac{15^\circ + 135^\circ}{2}\right) \sin\left(\frac{15^\circ - 135^\circ}{2}\right) = 2 \cos 75^\circ \sin(-60^\circ) = -2 \cos 75^\circ \sin 60^\circ\]

**Paso 4: Calcular $\tan \theta$**

Dividiendo el numerador entre el denominador (observando que $\cos 75^\circ \neq 0$):
\[\tan \theta = \frac{2 \cos 75^\circ \cos 60^\circ}{-2 \cos 75^\circ \sin 60^\circ} = -\frac{\cos 60^\circ}{\sin 60^\circ} = -\cot 60^\circ = -\tan 30^\circ\]

Como $-\tan 30^\circ = \tan(180^\circ - 30^\circ) = \tan 150^\circ$ y la función tangente tiene un período de $180^\circ$, el menor ángulo positivo $\theta$ que cumple la ecuación es $150^\circ$.

\boxed{150}