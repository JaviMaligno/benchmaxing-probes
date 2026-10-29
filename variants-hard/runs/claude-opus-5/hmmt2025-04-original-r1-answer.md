## Planteamiento

Escribo $j+0.5=\frac{2j+1}{2}$, de modo que

$$\left\lfloor\frac{2025}{j+0.5}\right\rfloor=\left\lfloor\frac{4050}{2j+1}\right\rfloor$$

Cuando $j$ recorre $-1000,\dots,1000$, el valor $n=2j+1$ recorre todos los **impares** desde $-1999$ hasta $2001$ (2001 términos en total).

## Emparejamiento

Separo el término extremo $n=2001$, que no tiene pareja:

$$\left\lfloor\frac{4050}{2001}\right\rfloor=2$$

Los restantes 2000 términos se agrupan en 1000 pares $\{n,-n\}$ con $n$ impar, $1\le n\le 1999$. Uso la identidad

$$\lfloor x\rfloor+\lfloor -x\rfloor=\begin{cases}0 & \text{si } x\in\mathbb{Z}\\ -1 & \text{en otro caso}\end{cases}$$

con $x=\dfrac{4050}{n}$.

## Contar los casos enteros

$4050=2\cdot 3^4\cdot 5^2$. Como $n$ es impar, $n\mid 4050 \iff n\mid 2025=3^4\cdot5^2$. Los divisores de 2025 son

$$1,\;3,\;5,\;9,\;15,\;25,\;27,\;45,\;75,\;81,\;135,\;225,\;405,\;675,\;2025$$

son 15 en total, pero $2025>1999$ queda fuera del rango, así que hay **14** valores de $n$ que dan cociente entero.

## Suma final

- 14 pares aportan $0$.
- Los $1000-14=986$ pares restantes aportan $-1$ cada uno.
- El término suelto aporta $+2$.

$$\text{Total}=-986+2=-984$$

\boxed{-984}