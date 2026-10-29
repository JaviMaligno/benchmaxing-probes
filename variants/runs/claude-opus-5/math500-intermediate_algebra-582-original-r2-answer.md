## Planteamiento

Como $x=0$ no es raíz, divido entre $x^{10}$:

$$\left(\frac{13x-1}{x}\right)^{10} = -1$$

Defino $y = \dfrac{13x-1}{x} = 13 - \dfrac{1}{x}$, de modo que $y^{10} = -1$.

Las diez soluciones son $y_k = e^{i\pi(2k+1)/10}$, $k=0,\dots,9$, y de cada una se recupera

$$\frac{1}{x} = 13 - y.$$

## Cálculo de los productos

Si $r$ corresponde a $y$, entonces $\bar r$ corresponde a $\bar y$ (los coeficientes son reales), luego

$$\frac{1}{r\bar r} = (13-y)(13-\bar y) = 169 - 13(y+\bar y) + |y|^2 = 170 - 26\,\mathrm{Re}(y),$$

usando $|y| = 1$.

## Suma sobre los cinco pares

Los cinco representantes con parte imaginaria positiva tienen argumentos $18^\circ, 54^\circ, 90^\circ, 126^\circ, 162^\circ$, y sus partes reales se cancelan por simetría:

$$\cos 18^\circ + \cos 162^\circ = 0,\qquad \cos 54^\circ + \cos 126^\circ = 0,\qquad \cos 90^\circ = 0.$$

Por tanto $\sum \mathrm{Re}(y) = 0$ y

$$\sum_{j=1}^{5} \frac{1}{r_j \bar r_j} = 5 \cdot 170 - 26 \cdot 0 = 850.$$

\boxed{850}