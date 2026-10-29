Para hallar la medida en grados del menor ángulo positivo $\theta$, primero agrupamos los términos del numerador y del denominador para aplicar las identidades trigonométricas de la suma de ángulos:

$$\cos(A + B) = \cos A \cos B - \sin A \sin B$$
$$\sin(A + B) = \sin A \cos B + \cos A \sin B$$

**1. Simplificación del numerador ($N$):**
$$N = (\cos 10^\circ \cos 5^\circ - \sin 10^\circ \sin 5^\circ) + (\cos 55^\circ \cos 80^\circ - \sin 55^\circ \sin 80^\circ)$$
$$N = \cos(10^\circ + 5^\circ) + \cos(55^\circ + 80^\circ) = \cos 15^\circ + \cos 135^\circ$$

Usando la identidad de suma a producto $\cos X + \cos Y = 2 \cos\left(\frac{X+Y}{2}\right)\cos\left(\frac{X-Y}{2}\right)$:
$$N = 2 \cos\left(\frac{15^\circ + 135^\circ}{2}\right) \cos\left(\frac{15^\circ - 135^\circ}{2}\right) = 2 \cos 75^\circ \cos(-60^\circ) = 2 \cos 75^\circ \cos 60^\circ$$

**2. Simplificación del denominador ($D$):**
$$D = (\sin 10^\circ \cos 5^\circ + \cos 10^\circ \sin 5^\circ) - (\sin 55^\circ \cos 80^\circ + \cos 55^\circ \sin 80^\circ)$$
$$D = \sin(10^\circ + 5^\circ) - \sin(55^\circ + 80^\circ) = \sin 15^\circ - \sin 135^\circ$$

Usando la identidad de diferencia a producto $\sin X - \sin Y = 2 \cos\left(\frac{X+Y}{2}\right)\sin\left(\frac{X-Y}{2}\right)$:
$$D = 2 \cos\left(\frac{15^\circ + 135^\circ}{2}\right) \sin\left(\frac{15^\circ - 135^\circ}{2}\right) = 2 \cos 75^\circ \sin(-60^\circ) = -2 \cos 75^\circ \sin 60^\circ$$

**3. Cálculo de $\tan \theta$:**
Dividiendo el numerador entre el denominador:
$$\tan \theta = \frac{2 \cos 75^\circ \cos 60^\circ}{-2 \cos 75^\circ \sin 60^\circ} = -\frac{\cos 60^\circ}{\sin 60^\circ} = -\cot 60^\circ = -\tan 30^\circ$$

Usando la propiedad $\tan(180^\circ - \alpha) = -\tan \alpha$, obtenemos:
$$\tan \theta = \tan(180^\circ - 30^\circ) = \tan 150^\circ$$

Por lo tanto, el menor ángulo positivo $\theta$ mide $150^\circ$.

\boxed{150}