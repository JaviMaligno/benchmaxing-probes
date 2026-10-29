Para hallar la suma de todos los valores posibles de $R^2$, establecemos un sistema de coordenadas cartesianas tridimensional con origen en el punto $X(0,0,0)$. Dado que los segmentos $\overline{AB}$, $\overline{CD}$ y $\overline{EF}$ son mutuamente perpendiculares y se intersecan en $X$, podemos hacer coincidir los ejes coordenados $x$, $y$ y $z$ con las rectas que contienen a $\overline{AB}$, $\overline{CD}$ y $\overline{EF}$, respectivamente.

Sin pérdida de generalidad, orientamos los semiejes positivos de modo que las coordenadas de los puntos $A$, $C$ y $E$ sean:
$$A = (1, 0, 0), \quad C = (0, \sqrt{2}, 0), \quad E = (0, 0, 2)$$

Sea $O = (x_0, y_0, z_0)$ el centro de la esfera de radio $R$. La ecuación de la esfera es:
$$(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = R^2$$

Además, sabemos que la distancia desde el centro $O$ hasta el origen $X$ es $OX = \frac{\sqrt{2}}{2}$, por lo que:
$$x_0^2 + y_0^2 + z_0^2 = OX^2 = \left(\frac{\sqrt{2}}{2}\right)^2 = \frac{1}{2}$$

Como los puntos $A$, $C$ y $E$ pertenecen a la esfera, sustituimos sus coordenadas en la ecuación de la esfera:
1. Para $A(1, 0, 0)$:
   $$(1 - x_0)^2 + y_0^2 + z_0^2 = R^2 \implies 1 - 2x_0 + (x_0^2 + y_0^2 + z_0^2) = R^2$$
2. Para $C(0, \sqrt{2}, 0)$:
   $$x_0^2 + (\sqrt{2} - y_0)^2 + z_0^2 = R^2 \implies 2 - 2\sqrt{2}y_0 + (x_0^2 + y_0^2 + z_0^2) = R^2$$
3. Para $E(0, 0, 2)$:
   $$x_0^2 + y_0^2 + (2 - z_0)^2 = R^2 \implies 4 - 4z_0 + (x_0^2 + y_0^2 + z_0^2) = R^2$$

Definamos $K = R^2 - OX^2 = R^2 - \frac{1}{2}$ (que corresponde a la potencia del punto $X$ respecto a la esfera; como $X$ está dentro de la esfera, se requiere $K > 0$). Despejando $x_0, y_0, z_0$ en términos de $K$:
$$x_0 = \frac{1 - K}{2}, \quad y_0 = \frac{2 - K}{2\sqrt{2}}, \quad z_0 = \frac{4 - K}{4}$$

Sustituimos estas expresiones en la condición $x_0^2 + y_0^2 + z_0^2 = \frac{1}{2}$:
$$\left(\frac{1 - K}{2}\right)^2 + \left(\frac{2 - K}{2\sqrt{2}}\right)^2 + \left(\frac{4 - K}{4}\right)^2 = \frac{1}{2}$$

Desarrollando cada término:
$$\frac{(K - 1)^2}{4} + \frac{(K - 2)^2}{8} + \frac{(K - 4)^2}{16} = \frac{1}{2}$$

Multiplicamos toda la ecuación por $16$:
$$4(K^2 - 2K + 1) + 2(K^2 - 4K + 4) + (K^2 - 8K + 16) = 8$$
$$7K^2 - 24K + 28 = 8$$
$$7K^2 - 24K + 20 = 0$$

Factorizamos la ecuación cuadrática:
$$(7K - 10)(K - 2) = 0$$

De aquí obtenemos dos soluciones reales y positivas para $K$:
$$K_1 = 2 \quad \text{y} \quad K_2 = \frac{10}{7}$$

Dado que ambos valores cumplen $K > 0$, en ambos casos el punto $X$ queda estrictamente en el interior de la esfera y, por tanto, dentro de las cuerdas $\overline{AB}$, $\overline{CD}$ y $\overline{EF}$.

Calculamos los valores correspondientes de $R^2 = K + \frac{1}{2}$:
$$R_1^2 = 2 + \frac{1}{2} = \frac{5}{2}$$
$$R_2^2 = \frac{10}{7} + \frac{1}{2} = \frac{27}{14}$$

Finalmente, la suma de todos los valores posibles de $R^2$ es:
$$R_1^2 + R_2^2 = \frac{5}{2} + \frac{27}{14} = \frac{35 + 27}{14} = \frac{62}{14} = \frac{31}{7}$$

\boxed{\frac{31}{7}}