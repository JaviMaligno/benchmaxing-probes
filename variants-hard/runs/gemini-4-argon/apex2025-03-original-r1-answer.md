Para hallar la suma de todas las posibles longitudes del inradio del triángulo $\triangle ABC$, procedemos paso a paso utilizando las propiedades geométricas de las circunferencias tangentes y el teorema de Thébault.

### Paso 1: Relación entre los centros de $\omega_2$ y $\omega_3$
Sean $O_2$ y $O_3$ los centros de las circunferencias $\omega_2$ y $\omega_3$, con radios $r_2 = 5$ y $r_3 = 7$, respectivamente.
Sea $\angle ADB = 2\theta$. Como $D$ se encuentra sobre el segmento $BC$, los ángulos $\angle ADB$ y $\angle ADC$ son suplementarios, por lo que $\angle ADC = \pi - 2\theta$.

- Dado que $\omega_2$ es tangente a los segmentos $AD$ y $BD$, su centro $O_2$ se encuentra sobre la bisectriz interior de $\angle ADB$. Por lo tanto, $\angle O_2DA = \theta$ y la distancia de $D$ a $O_2$ es:
  $$DO_2 = \frac{r_2}{\sin\theta} = \frac{5}{\sin\theta}$$

- Análogamente, como $\omega_3$ es tangente a los segmentos $AD$ y $CD$, su centro $O_3$ se encuentra sobre la bisectriz interior de $\angle ADC$. Así, $\angle O_3DA = \frac{\pi}{2} - \theta$ y la distancia de $D$ a $O_3$ es:
  $$DO_3 = \frac{r_3}{\sin\left(\frac{\pi}{2} - \theta\right)} = \frac{7}{\cos\theta}$$

Como las bisectrices de dos ángulos adyacentes suplementarios son perpendiculares, tenemos que:
$$\angle O_2DO_3 = \theta + \left(\frac{\pi}{2} - \theta\right) = \frac{\pi}{2}$$

Por el teorema de Pitágoras en el triángulo rectángulo $\triangle O_2DO_3$, sabiendo que $O_2O_3 = 13$:
$$DO_2^2 + DO_3^2 = O_2O_3^2 \implies \frac{25}{\sin^2\theta} + \frac{49}{\cos^2\theta} = 13^2 = 169$$

### Paso 2: Ecuación cuadrática para $\sin^2\theta$
Sea $t = \sin^2\theta$, de modo que $\cos^2\theta = 1 - t$ con $0 < t < 1$. Sustituyendo en la ecuación anterior:
$$\frac{25}{t} + \frac{49}{1-t} = 169$$

Multiplicando ambos lados por $t(1-t)$:
$$25(1 - t) + 49t = 169t(1 - t)$$
$$25 + 24t = 169t - 169t^2$$
$$169t^2 - 145t + 25 = 0$$

El discriminante es $\Delta = (-145)^2 - 4(169)(25) = 21025 - 16900 = 4125 > 0$, lo cual produce dos soluciones reales positivas $t_1, t_2 \in (0, 1)$. Por las fórmulas de Vieta, la suma de las dos raíces es:
$$t_1 + t_2 = \frac{145}{169}$$

### Paso 3: Aplicación del teorema de Thébault
Por el teorema de Sawayama-Thébault, el inradio $r$ del triángulo $\triangle ABC$ está relacionado con los radios $r_2$ y $r_3$ y el ángulo $\angle ADB = 2\theta$ mediante la fórmula:
$$r = r_2\cos^2\theta + r_3\sin^2\theta$$

Sustituyendo $r_2 = 5$, $r_3 = 7$, $\cos^2\theta = 1 - t$ y $\sin^2\theta = t$:
$$r = 5(1 - t) + 7t = 5 + 2t$$

Sumando los dos valores posibles del inradio correspondientes a $t_1$ y $t_2$:
$$r_a + r_b = (5 + 2t_1) + (5 + 2t_2) = 10 + 2(t_1 + t_2) = 10 + 2\left(\frac{145}{169}\right) = \frac{1690 + 290}{169} = \frac{1980}{169}$$

\boxed{\frac{1980}{169}}