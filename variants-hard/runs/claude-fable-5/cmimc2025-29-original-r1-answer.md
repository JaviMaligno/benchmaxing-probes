## Planteamiento

Coloco coordenadas: $D=(0,0)$, $C=(130,0)$, $A=(0,33)$, $B=(18,33)$.

Toda cónica que pasa por los 4 puntos pertenece al haz generado por dos cónicas degeneradas: el par de rectas $AB\cdot DC$ y el par $AD\cdot BC$:

- $DC: y=0$, $AB: y=33$, así que una degenerada es $y(y-33)=0$.
- $AD: x=0$, $BC: 33x+112y-4290=0$, así que la otra es $x(33x+112y-4290)=0$.

El haz (con parámetro $t$):
$$33t\,x^2 + 112t\,xy + y^2 - 4290t\,x - 33y = 0$$

con parte cuadrática $A=33t$, $B=112t$, $C=1$.

## Condición de elipse y razón de ejes

Es elipse cuando $B^2-4AC<0$, es decir $12544t^2 - 132t < 0$, o sea $0 < t < \tfrac{33}{3136}$.

La razón de ejes $r$ satisface, con $k=r^2$ (cociente de autovalores de la matriz cuadrática):
$$k + 2 + \frac{1}{k} = \frac{(A+C)^2}{AC - B^2/4} = \frac{(1+33t)^2}{33t - 3136t^2} =: f(t)$$

Minimizar $r$ equivale a minimizar $f$.

## Minimización

Derivando e igualando a cero:
$$66(33t-3136t^2) = (1+33t)(33-6272t) \;\Rightarrow\; 2178t = 33 - 5183t \;\Rightarrow\; t=\frac{33}{7361}$$

Evaluando: $1+33t = \frac{8450}{7361}$ y $33t-3136t^2 = \frac{1089\cdot 4225}{7361^2}$, luego
$$f = \frac{8450^2}{1089\cdot 4225} = \frac{4\cdot 4225}{1089} = \frac{16900}{1089}$$

Entonces $k + \frac1k = \frac{16900}{1089} - 2 = \frac{14722}{1089}$, y resolviendo:
$$k = \frac{14722 + \sqrt{14722^2 - 4\cdot 1089^2}}{2\cdot 1089} = \frac{14722 + \sqrt{12544\cdot 16900}}{2178} = \frac{14722+14560}{2178} = \frac{14641}{1089} = \left(\frac{11}{3}\right)^2$$

En los extremos del intervalo la elipse degenera (razón $\to\infty$), así que este mínimo interior es global.

$$r = \sqrt{k} = \boxed{\dfrac{11}{3}}$$