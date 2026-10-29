## Planteo del problema

Sea $ABC$ un triángulo rectángulo en $A$. Sobre la hipotenusa $BC$ se ubican tres puntos:

- $D$: pie de la **altura** desde $A$.
- $E$: pie de la **bisectriz** desde $A$.
- $F$: pie de la **mediana** desde $A$ (punto medio de $BC$).

Datos: $DE = 3$ y $EF = 5$.

## Razonamiento

**Paso 1: Posición de $F$ (mediana)**

En un triángulo rectángulo, la mediana a la hipotenusa mide la mitad de esta y $F$ es el punto medio de $BC$. Consideremos un sistema de coordenadas con $A = (0,0)$, $B = (b,0)$ y $C = (0,c)$. Entonces:

$$F = \left(\frac{b}{2}, \frac{c}{2}\right), \qquad BC = \sqrt{b^2 + c^2}$$

**Paso 2: Posición de $D$ (altura)**

La altura desde $A$ cae en la hipotenusa. La ecuación de $BC$ es $\frac{x}{b} + \frac{y}{c} = 1$, es decir $cx + by = bc$. La perpendicular desde $A$ tiene dirección $(c, b)$. El pie $D$ se obtiene proyectando $A$ sobre la recta $BC$:

$$D = \left(\frac{bc^2}{b^2+c^2}, \frac{b^2 c}{b^2+c^2}\right)$$

**Paso 3: Posición de $E$ (bisectriz)**

La bisectriz del ángulo recto forma $45^\circ$ con los ejes, de modo que está sobre la recta $y = x$. Su intersección con $BC$ ($cx + by = bc$) es:

$$E = \left(\frac{bc}{b+c}, \frac{bc}{b+c}\right)$$

**Paso 4: Relación entre los puntos sobre la hipotenusa**

Los puntos $D$, $E$, $F$ están alineados sobre $BC$. Podemos usar la distancia a lo largo de la recta. Parametricemos $BC$ con el parámetro $t \in [0, 1]$ tal que:

$$P(t) = (bt, c(1-t))$$

- Para $F$ (punto medio): $t_F = \frac{1}{2}$.

- Para $E$: resolviendo $bt = c(1-t)$, es decir $t = \frac{c}{b+c}$, y efectivamente $t_E = \frac{c}{b+c}$.

- Para $D$: el pie de la altura, en la proyección, corresponde al parámetro $t_D = \frac{c^2}{b^2 + c^2}$.

La longitud entre dos puntos $P(t_1)$ y $P(t_2)$ sobre $BC$ es:

$$\text{distancia} = |t_1 - t_2| \cdot BC$$

**Paso 5: Usar los datos**

$$DE = |t_D - t_E| \cdot BC = 3$$

$$EF = |t_E - t_F| \cdot BC = 5$$

Sabemos que:

$$t_E - t_D = \frac{c}{b+c} - \frac{c^2}{b^2+c^2}$$

Simplifiquemos. Llamemos $L = BC = \sqrt{b^2+c^2}$ y usemos $r = \frac{b}{c}$.

- $t_D = \dfrac{c^2}{b^2+c^2} = \dfrac{1}{r^2 + 1}$
- $t_E = \dfrac{c}{b+c} = \dfrac{1}{r+1}$
- $t_F = \dfrac{1}{2}$

Entonces:

$$t_E - t_D = \frac{1}{r+1} - \frac{1}{r^2+1} = \frac{(r^2+1) - (r+1)}{(r+1)(r^2+1)} = \frac{r^2 - r}{(r+1)(r^2+1)} = \frac{r(r-1)}{(r+1)(r^2+1)}$$

$$t_F - t_E = \frac{1}{2} - \frac{1}{r+1} = \frac{r+1-2}{2(r+1)} = \frac{r-1}{2(r+1)}$$

Ahora, al estar los tres puntos alineados y en el orden $D$–$E$–$F$ (para el caso típico), tenemos:

$$DE = \frac{r(r-1)}{(r+1)(r^2+1)} \cdot L = 3$$

$$EF = \frac{r-1}{2(r+1)} \cdot L = 5$$

**Paso 6: Dividir las ecuaciones**

$$\frac{DE}{EF} = \frac{3}{5}$$

Pero también:

$$\frac{DE}{EF} = \frac{\dfrac{r(r-1)}{(r+1)(r^2+1)} \cdot L}{\dfrac{r-1}{2(r+1)} \cdot L} = \frac{2r}{r^2+1}$$

Entonces:

$$\frac{2r}{r^2+1} = \frac{3}{5}$$

$$10r = 3r^2 + 3$$

$$3r^2 - 10r + 3 = 0$$

$$r = \frac{10 \pm \sqrt{100 - 36}}{6} = \frac{10 \pm 8}{6}$$

$$r = 3 \quad \text{o} \quad r = \frac{1}{3}$$

**Paso 7: Calcular $L = BC$**

Tomemos $r = 3$ (el otro valor corresponde al triángulo simétrico, con $b$ y $c$ intercambiados, que da el mismo resultado).

Para $r = 3$:

$$t_E - t_D = \frac{3 \cdot 2}{4 \cdot 10} = \frac{6}{40} = \frac{3}{20}$$

$$DE = \frac{3}{20} \cdot L = 3 \implies L = 20$$

Verificación con $EF$:

$$t_F - t_E = \frac{2}{2 \cdot 4} = \frac{1}{4}$$

$$EF = \frac{1}{4} \cdot L = \frac{1}{4} \cdot 20 = 5 \quad \checkmark$$

## Resultado final

$$\boxed{20}$$