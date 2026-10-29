Para encontrar la raíz $z$ del polinomio $Q(x) = x^{4}+24x^{3}+65x^{2}-900x+2500$ en el primer cuadrante, primero expresamos $Q(x)$ como una suma de cuadrados.

Observamos que los términos de mayor grado $x^4 + 24x^3$ provienen del desarrollo de $(x^2 + 12x + q)^2$. Desarrollando esta expresión para un parámetro $q$:
$$(x^2 + 12x + q)^2 = x^4 + 24x^3 + (144 + 2q)x^2 + 24qx + q^2$$

Restando esto de $Q(x)$, obtenemos:
$$Q(x) - (x^2 + 12x + q)^2 = (65 - 144 - 2q)x^2 - (900 + 24q)x + (2500 - q^2)$$
$$= (-79 - 2q)x^2 - (900 + 24q)x + (2500 - q^2)$$

Buscamos un valor de $q$ tal que el resto sea un cuadrado perfecto. Probando $q = -40$:
- El coeficiente de $x^2$ es $-79 - 2(-40) = 1$.
- El coeficiente de $x$ es $-900 - 24(-40) = 60$.
- El término independiente es $2500 - (-40)^2 = 900$.

El polinomio restante es $x^2 + 60x + 900 = (x + 30)^2$. Por lo tanto, podemos reescribir $Q(x)$ como:
$$Q(x) = (x^2 + 12x - 40)^2 + (x + 30)^2$$

Para hallar las raíces de $Q(x) = 0$, igualamos:
$$(x^2 + 12x - 40)^2 = -(x + 30)^2 \implies x^2 + 12x - 40 = \pm i(x + 30)$$

Esto nos da dos ecuaciones cuadráticas:

1. **Caso 1:** $x^2 + (12 - i)x - (40 + 30i) = 0$
   Aplicando la fórmula cuadrática:
   $$x = \frac{-(12 - i) \pm \sqrt{(12 - i)^2 + 4(40 + 30i)}}{2} = \frac{-12 + i \pm \sqrt{144 - 24i - 1 + 160 + 120i}}{2} = \frac{-12 + i \pm \sqrt{303 + 96i}}{2}$$

2. **Caso 2:** $x^2 + (12 + i)x - (40 - 30i) = 0$
    Sus raíces son las conjugadas del Caso 1:
   $$x = \frac{-12 - i \pm \sqrt{303 - 96i}}{2}$$

Ahora identificamos cuál de las cuatro raíces se encuentra en el primer cuadrante (donde tanto la parte real como la imaginaria son positivas). Sea $\sqrt{303 + 96i} = u + vi$ la raíz cuadrada principal con $u, v > 0$. Entonces:
$$u = \sqrt{\frac{\sqrt{303^2 + 96^2} + 303}{2}} = \sqrt{\frac{\sqrt{101025} + 303}{2}} \approx \sqrt{\frac{317.84 + 303}{2}} \approx 17.62$$
$$v = \frac{96}{2u} \approx 2.72$$

Evaluando los signos de las partes real e imaginaria de las cuatro raíces, vemos que la única con parte real $\frac{-12 + u}{2} > 0$ y parte imaginaria $\frac{1 + v}{2} > 0$ es:
$$z = \frac{1}{2}\left(-12 + i + \sqrt{303 + 96i}\right)$$

Comparando con la forma $z = \frac{1}{2}\left(a + bi + \sqrt{c + di}\right)$, identificamos los enteros:
- $a = -12$
- $b = 1$
- $c = 303$
- $d = 96$

Finalmente, calculamos la suma pedida:
$$a + b + c + d = -12 + 1 + 303 + 96 = 388$$

\boxed{388}