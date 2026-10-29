Para determinar el área de la gráfica de $S$, analizamos la condición para que la ecuación cuártica tenga al menos una raíz real:
\[x^4 + ax^3 - bx^2 + ax + 1 = 0\]

Dado que $x = 0$ no es una solución (pues $1 \neq 0$), podemos dividir toda la ecuación entre $x^2$:
\[x^2 + ax - b + \frac{a}{x} + \frac{1}{x^2} = 0\]

Agrupando los términos simétricos, obtenemos:
\[\left(x^2 + \frac{1}{x^2}\right) + a\left(x + \frac{1}{x}\right) - b = 0\]

Realizamos el cambio de variable $t = x + \frac{1}{x}$. Sabemos que existe al menos un valor real $x \neq 0$ para un $t$ dado si y solo si $|t| \ge 2$ (es decir, $t \le -2$ o $t \ge 2$). 

Como $x^2 + \frac{1}{x^2} = t^2 - 2$, sustituimos en la ecuación:
\[f(t) = t^2 + at - b - 2 = 0\]

Por lo tanto, la ecuación original tiene al menos una raíz real $x$ si y solo si el polinomio cuadrático $f(t)$ tiene al menos una raíz real $t$ que cumpla $|t| \ge 2$.

Para $a, b \in [0, 1]$:
1. El producto de las raíces de $f(t)$ es $t_1 t_2 = -b - 2 < 0$, lo que implica que siempre existen dos raíces reales de signos opuestos: $t_1 < 0 < t_2$.
2. La suma de las raíces es $t_1 + t_2 = -a \le 0$, por lo que $|t_1| = -t_1 \ge t_2 = |t_2|$.

Esto significa que la raíz con mayor valor absoluto es siempre la raíz negativa $t_1$ (de hecho, para $t = 2$, $f(2) = 2 + 2a - b \ge 1 > 0$, por lo que $t_2 < 2$ siempre en el cuadrado unitario). En consecuencia, existe una raíz con $|t| \ge 2$ si y solo si $t_1 \le -2$.

Dado que $f(t)$ es una parábola que abre hacia arriba y $t_1 < 0 < t_2$, el número $-2$ se encuentra a la izquierda de $t_2$. Así, la condición $t_1 \le -2$ es equivalente a que $-2$ esté entre las dos raíces, es decir:
\[f(-2) \le 0\]

Evaluando en $t = -2$:
\[(-2)^2 + a(-2) - b - 2 \le 0 \implies 2 - 2a - b \le 0 \implies 2a + b \ge 2\]

Buscamos el área de la región definida por $2a + b \ge 2$ dentro del cuadrado unitario $0 \le a, b \le 1$. 
La recta $2a + b = 2$ interseca los lados del cuadrado en los puntos $(1, 0)$ y $\left(\frac{1}{2}, 1\right)$. La región $S$ es el triángulo rectángulo con vértices en $(1, 0)$, $(1, 1)$ y $\left(\frac{1}{2}, 1\right)$.

La base de este triángulo mide $1 - \frac{1}{2} = \frac{1}{2}$ y su altura mide $1 - 0 = 1$. Calculando su área:
\[\text{Área} = \frac{1}{2} \times \text{base} \times \text{altura} = \frac{1}{2} \times \frac{1}{2} \times 1 = \frac{1}{4}\]

\boxed{\frac{1}{4}}