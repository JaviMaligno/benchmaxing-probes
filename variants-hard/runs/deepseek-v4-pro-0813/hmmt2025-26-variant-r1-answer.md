Voy a resolver el problema paso a paso.

**Paso 1: Determinar la altura del trapecio.**

Trapecio $PQRS$ con $PQ \parallel RS$, $PQ = 10$, $RS = 18$, lados $QR = 7$, $SP = 5$.

Dado que $PQ$ y $RS$ son paralelas, la diferencia de longitudes es $18 - 10 = 8$. Si proyectamos los lados sobre la base mayor, obtenemos un desplazamiento horizontal total de 8.

Consideremos un sistema de coordenadas: colocamos $P=(0,0)$, $Q=(10,0)$. Como $PQ \parallel RS$, tenemos $R$ y $S$ a cierta altura $h$ con $RS=18$. Podemos escribir $S=(x,h)$ y $R=(x+18,h)$.

Usamos las longitudes $PS=5$ y $QR=7$:
- $PS^2 = x^2 + h^2 = 25$
- $QR^2 = (x+18-10)^2 + h^2 = (x+8)^2 + h^2 = 49$

Restando:
$$
(x+8)^2 - x^2 = 49 - 25 = 24
$$
$$
x^2 + 16x + 64 - x^2 = 24
$$
$$
16x = -40 \implies x = -\frac{5}{2}
$$

Entonces:
$$
h^2 = 25 - x^2 = 25 - \frac{25}{4} = \frac{75}{4} \implies h = \frac{5\sqrt{3}}{2}
$$

Así que:
- $P=(0,0)$
- $Q=(10,0)$
- $R=\left(x+18,h\right) = \left(\frac{31}{2}, \frac{5\sqrt{3}}{2}\right)$
- $S=\left(x,h\right) = \left(-\frac{5}{2}, \frac{5\sqrt{3}}{2}\right)$

**Paso 2: Calcular los circuncentros.**

El circuncentro de un triángulo es el punto de intersección de las mediatrices de sus lados.

- **Circuncentro de $\triangle PQR$**: $P=(0,0)$, $Q=(10,0)$, $R=(31/2, 5\sqrt{3}/2)$.

  La mediatriz de $PQ$ es $x=5$. La mediatriz de $PR$: punto medio de $PR$ es $\left(31/4, 5\sqrt{3}/4\right)$, y la pendiente de $PR$ es:
  $$
  m_{PR} = \frac{5\sqrt{3}/2}{31/2} = \frac{5\sqrt{3}}{31}
  $$
  La mediatriz tiene pendiente $-31/(5\sqrt{3})$. Una manera más directa es usar la condición de equidistancia. Sean $O_1=(5,y)$. Debe cumplir $O_1P^2=O_1R^2$:
  $$
  5^2 + y^2 = \left(\frac{31}{2}-5\right)^2 + \left(\frac{5\sqrt{3}}{2}-y\right)^2
  $$
  $$
  25 + y^2 = \left(\frac{21}{2}\right)^2 + \left(\frac{5\sqrt{3}}{2}-y\right)^2
  $$
  $$
  25 + y^2 = \frac{441}{4} + \frac{75}{4} - 5\sqrt{3}\,y + y^2
  $$
  $$
  25 = \frac{516}{4} - 5\sqrt{3}\,y = 129 - 5\sqrt{3}\, y
  $$
  $$
  5\sqrt{3}\,y = 104 \implies y = \frac{104}{5\sqrt{3}}
  $$

  Entonces $O_1 = \left(5, \frac{104}{5\sqrt{3}}\right)$.

- **Circuncentro de $\triangle QRS$**: $Q=(10,0)$, $R=(31/2, 5\sqrt{3}/2)$, $S=(-5/2, 5\sqrt{3}/2)$.

  Dado que $Q$, $R$, $S$ — observemos que $RS$ es horizontal ($y$ iguales), su mediatriz es vertical en el punto medio de $RS$: $x = \frac{31/2 + (-5/2)}{2} = \frac{26/2}{2} = \frac{13}{2}$.

  Sea $O_2 = (13/2, y)$. Debemos tener $O_2Q^2 = O_2R^2$:
  $$
  \left(\frac{13}{2}-10\right)^2 + y^2 = \left(\frac{13}{2}-\frac{31}{2}\right)^2 + \left(\frac{5\sqrt{3}}{2}-y\right)^2
  $$
  $$
  \left(-\frac{7}{2}\right)^2 + y^2 = (-9)^2 + \left(\frac{5\sqrt{3}}{2}-y\right)^2
  $$
  $$
  \frac{49}{4} + y^2 = 81 + \frac{75}{4} - 5\sqrt{3}\,y + y^2
  $$
  $$
  \frac{49}{4} = 81 + \frac{75}{4} - 5\sqrt{3}\,y
  $$
  $$
  \frac{49}{4} = \frac{324}{4} + \frac{75}{4} - 5\sqrt{3}\,y = \frac{399}{4} - 5\sqrt{3}\,y
  $$
  $$
  5\sqrt{3}\,y = \frac{350}{4} = \frac{175}{2} \implies y = \frac{175}{10\sqrt{3}} = \frac{35}{2\sqrt{3}}
  $$

  Entonces $O_2 = \left(\frac{13}{2}, \frac{35}{2\sqrt{3}}\right)$.

- **Circuncentro de $\triangle RSP$**: $R=(31/2, 5\sqrt{3}/2)$, $S=(-5/2, 5\sqrt{3}/2)$, $P=(0,0)$.

  La mediatriz de $RS$ es $x=13/2$. Sea $O_3=(13/2, y)$. Igualamos $O_3P^2=O_3R^2$:
  $$
  \left(\frac{13}{2}\right)^2 + y^2 = \left(\frac{13}{2}-\frac{31}{2}\right)^2 + \left(\frac{5\sqrt{3}}{2}-y\right)^2
  $$
  $$
  \frac{169}{4} + y^2 = 81 + \frac{75}{4} - 5\sqrt{3}\,y + y^2
  $$
  $$
  \frac{169}{4} = \frac{399}{4} - 5\sqrt{3}\,y
  $$
  $$
  5\sqrt{3}\,y = \frac{230}{4} = \frac{115}{2} \implies y = \frac{115}{10\sqrt{3}} = \frac{23}{2\sqrt{3}}
  $$

  Entonces $O_3 = \left(\frac{13}{2}, \frac{23}{2\sqrt{3}}\right)$.

- **Circuncentro de $\triangle SPQ$**: $S=(-5/2, 5\sqrt{3}/2)$, $P=(0,0)$, $Q=(10,0)$.

  La mediatriz de $PQ$ es $x=5$. Sea $O_4=(5,y)$. Igualamos $O_4P^2=O_4S^2$:
  $$
  25 + y^2 = \left(-5 - \frac{5}{2}\right)^2 + \left(\frac{5\sqrt{3}}{2}-y\right)^2
  $$
  
  Cuidado: la coordenada $x$ de $S$ es $-5/2$, así que $x_S - 0 = -5/2$, y $x_S - 5 = -5/2 - 5 = -15/2$.
  $$
  25 + y^2 = \left(5+\frac{5}{2}\right)^2 + \left(\frac{5\sqrt{3}}{2}-y\right)^2
  $$
  Espera, $x_S - 5 = -5/2 - 5 = -15/2$, al cuadrado da $225/4$. Veamos:
  $$
  (x_S - 5)^2 = \left(-\frac{5}{2}-5\right)^2 = \left(-\frac{15}{2}\right)^2 = \frac{225}{4}
  $$
  $$
  25 + y^2 = \frac{225}{4} + \frac{75}{4} - 5\sqrt{3}\,y + y^2
  $$
  $$
  25 = \frac{300}{4} - 5\sqrt{3}\,y = 75 - 5\sqrt{3}\,y
  $$
  $$
  5\sqrt{3}\,y = 50 \implies y = \frac{50}{5\sqrt{3}} = \frac{10}{\sqrt{3}}
  $$

  Entonces $O_4 = \left(5, \frac{10}{\sqrt{3}}\right)$.

**Paso 3: Calcular el área del cuadrilátero $O_1O_2O_3O_4$.**

Los puntos son:
- $O_1 = \left(5, \frac{104}{5\sqrt{3}}\right)$
- $O_2 = \left(\frac{13}{2}, \frac{35}{2\sqrt{3}}\right)$
- $O_3 = \left(\frac{13}{2}, \frac{23}{2\sqrt{3}}\right)$
- $O_4 = \left(5, \frac{10}{\sqrt{3}}\right)$

Observemos que $O_2$ y $O_3$ comparten la misma coordenada $x = 13/2$, y $O_1$ y $O_4$ comparten $x = 5$. Esto sugiere que $O_1O_2O_3O_4$ es un trapecio con bases verticales.

El orden de los vértices según el enunciado es $O_1 \to O_2 \to O_3 \to O_4$ (circuncentros de $\triangle PQR$, $\triangle QRS$, $\triangle RSP$, $\triangle SPQ$). Verifiquemos que este orden da un polígono convexo.

Coordenadas $y$:
- $O_1$: $y_1 = 104/(5\sqrt{3}) \approx 12.008$
- $O_2$: $y_2 = 35/(2\sqrt{3}) \approx 10.104$
- $O_3$: $y_3 = 23/(2\sqrt{3}) \approx 6.640$
- $O_4$: $y_4 = 10/\sqrt{3} \approx 5.774$

Las coordenadas $x$: $x_{O_1}=5$, $x_{O_2}=6.5$, $x_{O_3}=6.5$, $x_{O_4}=5$.

El orden es $O_1(5, 12.008) \to O_2(6.5, 10.104) \to O_3(6.5, 6.640) \to O_4(5, 5.774)$, formando un trapecio convexo con lados verticales $O_2O_3$ y $O_4O_1$ y lados inclinados $O_1O_2$ y $O_3O_4$.

Podemos calcular el área con la fórmula del zapatero (shoelace):

$$
\text{Área} = \frac{1}{2}\left| \sum x_i y_{i+1} - \sum x_{i+1} y_i \right|
$$

Puntos en orden: $O_1$, $O_2$, $O_3$, $O_4$.

$$
\sum x_i y_{i+1} = x_1 y_2 + x_2 y_3 + x_3 y_4 + x_4 y_1
$$
$$
= 5 \cdot \frac{35}{2\sqrt{3}} + \frac{13}{2} \cdot \frac{23}{2\sqrt{3}} + \frac{13}{2} \cdot \frac{10}{\sqrt{3}} + 5 \cdot \frac{104}{5\sqrt{3}}
$$
$$
= \frac{175}{2\sqrt{3}} + \frac{299}{4\sqrt{3}} + \frac{65}{\sqrt{3}} + \frac{104}{\sqrt{3}}
$$

Convertimos todo a denominador $4\sqrt{3}$:
$$
\frac{350}{4\sqrt{3}} + \frac{299}{4\sqrt{3}} + \frac{260}{4\sqrt{3}} + \frac{416}{4\sqrt{3}} = \frac{1325}{4\sqrt{3}}
$$

$$
\sum x_{i+1} y_i = x_2 y_1 + x_3 y_2 + x_4 y_3 + x_1 y_4
$$
$$
= \frac{13}{2} \cdot \frac{104}{5\sqrt{3}} + \frac{13}{2} \cdot \frac{35}{2\sqrt{3}} + 5 \cdot \frac{23}{2\sqrt{3}} + 5 \cdot \frac{10}{\sqrt{3}}
$$
$$
= \frac{676}{5\sqrt{3}} + \frac{455}{4\sqrt{3}} + \frac{115}{2\sqrt{3}} + \frac{50}{\sqrt{3}}
$$

Convertimos a denominador $20\sqrt{3}$:
- $\frac{676}{5\sqrt{3}} = \frac{2704}{20\sqrt{3}}$
- $\frac{455}{4\sqrt{3}} = \frac{2275}{20\sqrt{3}}$
- $\frac{115}{2\sqrt{3}} = \frac{1150}{20\sqrt{3}}$
- $\frac{50}{\sqrt{3}} = \frac{1000}{20\sqrt{3}}$

Suma: $\frac{2704 + 2275 + 1150 + 1000}{20\sqrt{3}} = \frac{7129}{20\sqrt{3}}$.

Ahora resta:
$$
\sum x_i y_{i+1} - \sum x_{i+1} y_i = \frac{1325}{4\sqrt{3}} - \frac{7129}{20\sqrt{3}}
$$

Denominador común $20\sqrt{3}$:
$$
\frac{6625}{20\sqrt{3}} - \frac{7129}{20\sqrt{3}} = \frac{-504}{20\sqrt{3}} = -\frac{126}{5\sqrt{3}}
$$

El área:
$$
\text{Área} = \frac{1}{2}\left|\frac{-126}{5\sqrt{3}}\right| = \frac{126}{10\sqrt{3}} = \frac{63}{5\sqrt{3}} = \frac{21\sqrt{3}}{5}
$$

**Paso 4: Verificación alternativa.**

Como $O_1O_2O_3O_4$ es un trapecio con bases verticales $O_2O_3$ y $O_4O_1$ (paralelas entre sí), su área se puede calcular como:

$$
\text{Área} = \frac{1}{2} (h_1 + h_2) \cdot d
$$

donde $h_1$ y $h_2$ son las longitudes de las bases verticales y $d$ la distancia horizontal entre ellas.

- Base superior: $O_2 \to O_3$: $|y_2 - y_3| = \left|\frac{35}{2\sqrt{3}} - \frac{23}{2\sqrt{3}}\right| = \frac{12}{2\sqrt{3}} = \frac{6}{\sqrt{3}} = 2\sqrt{3}$.
- Base inferior: $O_1 \to O_4$: $|y_1 - y_4| = \left|\frac{104}{5\sqrt{3}} - \frac{10}{\sqrt{3}}\right| = \left|\frac{104}{5\sqrt{3}} - \frac{50}{5\sqrt{3}}\right| = \frac{54}{5\sqrt{3}}$.
- Distancia horizontal: $d = \frac{13}{2} - 5 = \frac{3}{2}$.

$$
\text{Área} = \frac{1}{2}\left(\frac{6}{\sqrt{3}} + \frac{54}{5\sqrt{3}}\right) \cdot \frac{3}{2}
= \frac{1}{2} \cdot \frac{30 + 54}{5\sqrt{3}} \cdot \frac{3}{2}
= \frac{1}{2} \cdot \frac{84}{5\sqrt{3}} \cdot \frac{3}{2}
= \frac{84 \cdot 3}{20\sqrt{3}} = \frac{252}{20\sqrt{3}} = \frac{63}{5\sqrt{3}} = \frac{21\sqrt{3}}{5}
$$

Coincide con el cálculo anterior.

---

$$\boxed{\frac{21\sqrt{3}}{5}}$$