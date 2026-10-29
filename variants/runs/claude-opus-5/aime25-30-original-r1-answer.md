## Planteamiento

Si el mínimo $m$ se alcanza en exactamente dos puntos $a,b>0$, entonces el numerador de $f(x)-m$ tiene raíces dobles en $a$ y $b$:

$$(x-18)(x-72)(x-98)(x-k) - mx = (x-a)^2(x-b)^2$$

## Comparación de coeficientes

Con $e_1,e_2,e_3,e_4$ las simétricas elementales de $18,72,98,k$:

- $x^3$: $\;a+b = e_1/2$
- $x^2$: $\;(a+b)^2+2ab = e_2 \Rightarrow ab = \tfrac12\left(e_2-\tfrac{e_1^2}{4}\right)$
- $x^0$: $\;(ab)^2 = e_4 \Rightarrow ab = \sqrt{e_4}$ (pues $ab>0$)

El coeficiente de $x$ solo fija $m$, así que la condición es la compatibilidad de las dos expresiones de $ab$.

## Ecuación en $k$

$e_1 = 188+k$, $e_2 = 10116+188k$, $e_4 = 127008k$:

$$e_2-\frac{e_1^2}{4} = 1280+94k-\frac{k^2}{4}\quad\Longrightarrow\quad ab = 640+47k-\frac{k^2}{8}$$

y $\sqrt{e_4} = 252\sqrt{2}\sqrt{k}$. Igualando y multiplicando por 8:

$$k^2 - 376k + 2016\sqrt{2}\sqrt{k} - 5120 = 0$$

Con $\sqrt{k} = \sqrt{2}\,v$ (es decir $k=2v^2$) se obtiene:

$$v^4 - 188v^2 + 1008v - 1280 = 0$$

## Factorización

$$v^4-188v^2+1008v-1280 = (v-2)(v-4)(v-10)(v+16)$$

Las raíces positivas $v=2,4,10$ dan

$$k = 8,\quad 32,\quad 200$$

(la raíz $v=-16$ corresponde a la rama $ab=-\sqrt{e_4}$, inadmisible).

## Suma

$$8+32+200 = 240$$

\boxed{240}