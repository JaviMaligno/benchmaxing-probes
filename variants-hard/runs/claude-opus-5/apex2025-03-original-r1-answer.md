## Planteamiento

Sea $\theta = \angle ADB$. Como $\omega_2$ está inscrita en el ángulo $\angle ADB$ y $\omega_3$ en el ángulo $\angle ADC = \pi - \theta$, sus centros están sobre las bisectrices de dos ángulos adyacentes suplementarios, que son **perpendiculares**.

**Distancias al punto $D$:**
$$DO_2 = \frac{r_2}{\sin(\theta/2)}, \qquad DO_3 = \frac{r_3}{\sin\!\big(\tfrac{\pi-\theta}{2}\big)} = \frac{r_3}{\cos(\theta/2)}$$

Por el teorema de Pitágoras en el triángulo rectángulo $O_2DO_3$:
$$O_2O_3^2 = \frac{r_2^2}{\sin^2(\theta/2)} + \frac{r_3^2}{\cos^2(\theta/2)}$$

## Ecuación

Con $r_2=5$, $r_3=7$, $O_2O_3=13$ y $x=\sin^2(\theta/2)$:
$$\frac{25}{x} + \frac{49}{1-x} = 169 \;\Longrightarrow\; 25(1-x) + 49x = 169x(1-x)$$
$$169x^2 - 145x + 25 = 0$$

El discriminante es $145^2 - 4\cdot169\cdot25 = 21025 - 16900 = 4125 > 0$, y como $f(0)=25>0$, $f(1)=49>0$ con vértice en $x=\tfrac{145}{338}\in(0,1)$, **ambas raíces** son válidas (están en $(0,1)$). Por Vieta:
$$x_1 + x_2 = \frac{145}{169}$$

Numéricamente $x_1\approx 0{,}619$ ($\theta\approx 103{,}7^\circ$) y $x_2\approx 0{,}239$ ($\theta\approx 58{,}5^\circ$); ambos valores de $\theta$ son compatibles con un triángulo acutángulo, pues $\theta$ recorre $(C,\;\pi-B)$ cuando $D$ recorre $BC$.

## Teorema de Thébault (Sawayama)

El incentro de $\triangle ABC$ yace en $O_2O_3$ y el inradio cumple:
$$r = r_2\cos^2(\theta/2) + r_3\sin^2(\theta/2) = 5(1-x) + 7x = 5 + 2x$$

(verificado numéricamente con configuraciones explícitas: p. ej. $\theta=60^\circ$ da $r_2\approx0{,}5277$, $r_3\approx0{,}3167$, y la media ponderada $0{,}4749$ coincide con el inradio calculado directamente).

## Suma

$$r_1 + r_2 = 10 + 2(x_1+x_2) = 10 + \frac{290}{169} = \frac{1980}{169}$$

$$\boxed{\dfrac{1980}{169}}$$