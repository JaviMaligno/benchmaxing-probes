## Planteamiento

Los pares $(x,y)$ se distribuyen uniformemente en el cuadrado $(0,3)\times(0,3)$, de área $9$.

## Condiciones del triángulo

Para que exista un triángulo de lados $1$, $x$, $y$ se necesitan las tres desigualdades:

- $x + y > 1$
- $1 + x > y \iff y - x < 1$
- $1 + y > x \iff x - y < 1$

Es decir: $x+y>1$ y $|x-y|<1$.

## Cálculo del área favorable

**Región $|x-y|<1$:** se excluyen del cuadrado los dos triángulos $x-y\ge 1$ y $y-x\ge 1$. Cada uno tiene cateto $2$, con área $\tfrac{2\cdot 2}{2}=2$. Queda:

$$9 - 2 - 2 = 5$$

**Ahora se quita la parte con $x+y\le 1$:** es el triángulo de vértices $(0,0)$, $(1,0)$, $(0,1)$, de área $\tfrac12$. Todo ese triángulo cumple $|x-y|<1$, así que se descuenta por completo:

$$5 - \frac12 = \frac92$$

## Probabilidad

$$P = \frac{9/2}{9} = \frac12$$

\boxed{\dfrac{1}{2}}