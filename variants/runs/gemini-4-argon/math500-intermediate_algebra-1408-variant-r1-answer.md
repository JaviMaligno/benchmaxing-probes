Para calcular $w^{95} + \frac{1}{w^{95}}$, podemos utilizar las propiedades trigonométricas de los números complejos o manipular la ecuación algebraicamente.

**Método 1: Forma trigonométrica**

Sea $w = e^{i\theta}$. Entonces, sabemos que:
\[w + \frac{1}{w} = 2\cos\theta\]

Sustituyendo en la ecuación dada:
\[2\cos\theta = \frac{\sqrt{5} - 1}{2} \implies \cos\theta = \frac{\sqrt{5} - 1}{4}\]

Recordemos que el valor exacto de $\cos\left(\frac{2\pi}{5}\right)$ (es decir, $\cos 72^\circ$) es precisamente $\frac{\sqrt{5} - 1}{4}$. Por lo tanto, podemos tomar $\theta = \pm\frac{2\pi}{5}$, lo que implica que $w$ es una raíz quinta primitiva de la unidad:
\[w = e^{\pm i\frac{2\pi}{5}}\]

Al elevar $w$ a la quinta potencia, obtenemos:
\[w^5 = \left(e^{\pm i\frac{2\pi}{5}}\right)^5 = e^{\pm i 2\pi} = 1\]

**Método 2: Manipulación algebraica**

Sea $x = w + \frac{1}{w} = \frac{\sqrt{5} - 1}{2}$. Notemos que $x$ satisface la ecuación cuadrática $x^2 + x - 1 = 0$, por lo que $x^2 = 1 - x$.

Calculamos las sumas de potencias $S_n = w^n + \frac{1}{w^n}$ usando la relación de recurrencia $S_n = x S_{n-1} - S_{n-2}$:
* $S_1 = x$
* $S_2 = x^2 - 2 = (1 - x) - 2 = -x - 1$
* $S_3 = x S_2 - S_1 = x(-x - 1) - x = -x^2 - 2x = -(1 - x) - 2x = -x - 1$
* $S_4 = x S_3 - S_2 = x(-x - 1) - (-x - 1) = -x^2 + 1 = -(1 - x) + 1 = x$
* $S_5 = x S_4 - S_3 = x(x) - (-x - 1) = x^2 + x + 1 = (1 - x) + x + 1 = 2$

Dado que $w^5 + \frac{1}{w^5} = 2$, multiplicando por $w^5$ y reordenando obtenemos $(w^5 - 1)^2 = 0$, de donde se deduce nuevamente que $w^5 = 1$.

---

**Cálculo final:**

Como $95$ es múltiplo de $5$ ($95 = 5 \times 19$), tenemos que:
\[w^{95} = (w^5)^{19} = 1^{19} = 1\]

Por lo tanto:
\[w^{95} + \frac{1}{w^{95}} = 1 + \frac{1}{1} = 2\]

\boxed{2}