## Planteamiento

Como $Q$ no tiene raíces reales, sus cuatro raíces forman dos pares conjugados. La forma pedida
$$z=\tfrac12\left(a+bi+\sqrt{c+di}\right)$$
es exactamente la fórmula cuadrática aplicada a un factor $x^2-(a+bi)x+w$ con coeficientes enteros de Gauss. Buscamos entonces una factorización
$$Q(x)=\big(x^2+Bx+C\big)\big(x^2+\bar Bx+\bar C\big),\qquad B,C\in\mathbb{Z}[i].$$

Desarrollando, las condiciones son:
$$B+\bar B=24,\quad |B|^2+C+\bar C=65,\quad 2\,\mathrm{Re}(B\bar C)=-900,\quad |C|^2=2500.$$

## Búsqueda de los factores

De $B+\bar B=24$ sale $\mathrm{Re}(B)=12$. Probando $B=12-i$ (es decir $|B|^2=145$), la segunda condición da $C+\bar C=65-145=-80$, o sea $\mathrm{Re}(C)=-40$; con $|C|^2=2500$ queda $\mathrm{Im}(C)=\pm 30$. Tomando $C=-40-30i$:
$$2\,\mathrm{Re}\big((12-i)(-40+30i)\big)=2\,\mathrm{Re}(-450+400i)=-900\ \checkmark$$

Por tanto
$$Q(x)=\big(x^2+(12-i)x-40-30i\big)\big(x^2+(12+i)x-40+30i\big),$$
y las cuatro condiciones se verifican ($24$, $65$, $-900$, $2500$).

## Raíz del primer cuadrante

Del primer factor, $x^2-(-12+i)x+(-40-30i)=0$:
$$z=\frac{(-12+i)\pm\sqrt{(-12+i)^2-4(-40-30i)}}{2}=\frac{-12+i+\sqrt{303+96i}}{2}.$$

Numéricamente $\sqrt{303+96i}\approx 17{,}619+2{,}724i$, luego
$$z\approx 2{,}809+1{,}861i,$$
que efectivamente está en el primer cuadrante (las demás raíces son $2{,}809-1{,}861i$ y $-14{,}809\pm0{,}860i$).

Así $a=-12$, $b=1$, $c=303$, $d=96$, y
$$a+b+c+d=-12+1+303+96=388.$$

\boxed{388}