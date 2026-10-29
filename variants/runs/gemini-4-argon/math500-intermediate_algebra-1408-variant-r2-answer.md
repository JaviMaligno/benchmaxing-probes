Para calcular $w^{95} + \frac{1}{w^{95}}$, podemos utilizar propiedades trigonométricas o algebraicas a partir de la ecuación dada:
\[w + \frac{1}{w} = \frac{\sqrt{5} - 1}{2}.\]

**Método 1: Forma trigonométrica**

Recordemos que el valor exacto de $\cos\left(\frac{2\pi}{5}\right)$ (es decir, $\cos 72^\circ$) es:
\[\cos\left(\frac{2\pi}{5}\right) = \frac{\sqrt{5} - 1}{4}.\]

Por lo tanto, podemos reescribir la condición dada como:
\[w + \frac{1}{w} = 2\cos\left(\frac{2\pi}{5}\right).\]

Esta ecuación se satisface cuando $w = e^{\pm i \frac{2\pi}{5}} = \cos\left(\frac{2\pi}{5}\right) \pm i\sin\left(\frac{2\pi}{5}\right)$. 

Al elevar $w$ a la quinta potencia usando la fórmula de De Moivre, obtenemos:
\[w^5 = \left(e^{\pm i \frac{2\pi}{5}}\right)^5 = e^{\pm i 2\pi} = 1.\]

Dado que $95$ es un múltiplo de $5$ ($95 = 5 \times 19$), tenemos que:
\[w^{95} = (w^5)^{19} = 1^{19} = 1.\]

Sustituyendo este valor en la expresión que queremos calcular:
\[w^{95} + \frac{1}{w^{95}} = 1 + \frac{1}{1} = 2.\]

---

**Método 2: Enfoque algebraico**

Sea $x = w + \frac{1}{w} = \frac{\sqrt{5} - 1}{2}$. Notemos que $x$ es raíz del polinomio $x^2 + x - 1 = 0$, por lo que $x^2 = 1 - x$.

Calculamos las potencias sucesivas $x_n = w^n + \frac{1}{w^n}$:
- $w^2 + \frac{1}{w^2} = x^2 - 2 = (1 - x) - 2 = -x - 1$.
- $w^3 + \frac{1}{w^3} = x(w^2 + \frac{1}{w^2}) - x = x(-x - 1) - x = -x^2 - 2x = -(1 - x) - 2x = -x - 1$.
- $w^5 + \frac{1}{w^5} = \left(w^2 + \frac{1}{w^2}\right)\left(w^3 + \frac{1}{w^3}\right) - \left(w + \frac{1}{w}\right) = (-x - 1)^2 - x = x^2 + 2x + 1 - x = (1 - x) + x + 1 = 2$.

Como $w^5 + \frac{1}{w^5} = 2$, multiplicando por $w^5$ llegamos a $(w^5 - 1)^2 = 0$, lo que implica que $w^5 = 1$. 
Por consiguiente, $w^{95} = (w^5)^{19} = 1$, y finalmente:
\[w^{95} + \frac{1}{w^{95}} = 1 + 1 = 2.\]

\boxed{2}