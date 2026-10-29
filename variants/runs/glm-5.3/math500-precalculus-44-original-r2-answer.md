# Resolución paso a paso

## Simplificación del numerador

Agrupando los términos con la identidad $\cos A \cos B - \sin A \sin B = \cos(A+B)$:

- $\cos 5^\circ \cos 20^\circ - \sin 5^\circ \sin 20^\circ = \cos(5^\circ + 20^\circ) = \cos 25^\circ$
- $\cos 35^\circ \cos 50^\circ - \sin 35^\circ \sin 50^\circ = \cos(35^\circ + 50^\circ) = \cos 85^\circ$

**Numerador** $= \cos 25^\circ + \cos 85^\circ$.

Aplicando la identidad de suma a producto $\cos A + \cos B = 2\cos\frac{A+B}{2}\cos\frac{A-B}{2}$:

$$\cos 25^\circ + \cos 85^\circ = 2\cos 55^\circ \cos 30^\circ = 2\cos 55^\circ \cdot \frac{\sqrt{3}}{2} = \sqrt{3}\cos 55^\circ$$

## Simplificación del denominador

Agrupando los términos con la identidad $\sin A \cos B + \cos A \sin B = \sin(A+B)$:

- $\sin 5^\circ \cos 20^\circ + \cos 5^\circ \sin 20^\circ = \sin 25^\circ$
- $\sin 35^\circ \cos 50^\circ + \cos 35^\circ \sin 50^\circ = \sin 85^\circ$

**Denominador** $= \sin 25^\circ - \sin 85^\circ$.

Aplicando $\sin A - \sin B = 2\cos\frac{A+B}{2}\sin\frac{A-B}{2}$:

$$\sin 25^\circ - \sin 85^\circ = 2\cos 55^\circ \sin(-30^\circ) = 2\cos 55^\circ \cdot \left(-\frac{1}{2}\right) = -\cos 55^\circ$$

## Cálculo de la fracción

$$\tan\theta = \frac{\sqrt{3}\cos 55^\circ}{-\cos 55^\circ} = -\sqrt{3}$$

## Conclusión

Buscamos el menor ángulo positivo con $\tan\theta = -\sqrt{3}$. Como $\tan 60^\circ = \sqrt{3}$, el ángulo con tangente $-\sqrt{3}$ en $(0^\circ, 180^\circ)$ es:

$$\theta = 120^\circ$$

$$\boxed{120}$$