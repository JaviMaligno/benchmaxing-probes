## Planteamiento

Queremos minimizar $f(a,b,c) = a^4 + 6b^2 + 9c^4$ sujeta a la restricción $abc = 3$, con $a,b,c > 0$.

## Paso 1: Condición de punto crítico (Lagrange)

Usamos el multiplicador de Lagrange con la restricción en forma logarítmica, $\ln a + \ln b + \ln c = \ln 3$, ya que todas las variables son positivas.

Derivadas parciales de $f$:
- $\dfrac{\partial f}{\partial a} = 4a^3$
- $\dfrac{\partial f}{\partial b} = 12b$
- $\dfrac{\partial f}{\partial c} = 36c^3$

El sistema $\nabla f = \lambda \nabla g$ da:

$$4a^3 = \frac{\lambda}{a}, \qquad 12b = \frac{\lambda}{b}, \qquad 36c^3 = \frac{\lambda}{c}$$

Es decir:

$$4a^4 = 12b^2 = 36c^4 = \lambda$$

## Paso 2: Relacionar las variables

De $4a^4 = 12b^2$ obtenemos $a^4 = 3b^2$.

De $12b^2 = 36c^4$ obtenemos $b^2 = 3c^4$.

Combinando: $a^4 = 9c^4$, de donde $a^2 = 3c^2$, es decir, $a = \sqrt{3}\,c$.

También $b^2 = 3c^4$, es decir, $b = \sqrt{3}\,c^2$.

## Paso 3: Aplicar la restricción

Sustituyendo en $abc = 3$:

$$(\sqrt{3}\,c)(\sqrt{3}\,c^2)(c) = 3c^4 = 3 \quad\Longrightarrow\quad c = 1$$

Por lo tanto:
$$a = \sqrt{3}, \qquad b = \sqrt{3}, \qquad c = 1$$

## Paso 4: Evaluar y verificar

$$a^4 + 6b^2 + 9c^4 = (\sqrt{3})^4 + 6(\sqrt{3})^2 + 9(1)^4 = 9 + 18 + 9 = 36$$

Comprobación con AM-GM en el punto crítico: los tres sumandos $9$, $18$, $9$ satisfacen la proporción correcta y el crecimiento de $f$ hacia el infinito garantiza que este punto crítico es el mínimo global.

$$\boxed{36}$$