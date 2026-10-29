# Resolución

**1. Planteamiento y coordenadas.**
Tomemos $PQ = QR = PR = 2$, con
$$P=(-1,0),\quad Q=(1,0),\quad R=(0,\sqrt3),\quad G=\left(0,\tfrac{\sqrt3}{3}\right).$$
Cada elipse tiene suma de distancias $\tfrac32\cdot 2 = 3$.

**2. Puntos de intersección de dos elipses.**
Si $X\in\mathcal E_{PQ}\cap\mathcal E_{QR}$, restando las ecuaciones $d(X,P)+d(X,Q)=3$ y $d(X,Q)+d(X,R)=3$ se obtiene $d(X,P)=d(X,R)$: es decir, $X$ está en la mediatriz de $PR$, que es la **mediana desde $Q$** (pasa por $Q$ y $G$). Lo mismo ocurre cíclicamente para los otros dos pares.

Sea $X$ un punto de esa mediana a distancia $t$ de $Q$ (hacia adentro). Entonces $d(X,Q)=t$ y, como la mediana forma $30^\circ$ con el lado $QP$,
$$d(X,P)^2 = t^2 + 4 - 4t\cos 30^\circ = t^2-2\sqrt3\,t+4.$$
La condición $d(X,P)+d(X,Q)=3$ da $\sqrt{t^2-2\sqrt3 t+4}=3-t$, es decir
$$6t-2\sqrt3\,t = 5 \quad\Longrightarrow\quad t_1=\frac{5(3+\sqrt3)}{12}\approx 1.972 .$$
Con $t<0$ (fuera, del lado de $Q$): $t_2=\frac{5(3-\sqrt3)}{12}\approx 0.528$ hacia afuera.

**3. Los seis puntos.** Cada par de elipses se corta en dos puntos:
- **Puntos "cercanos"**: a distancia $t_2\approx 0.528$ más allá de cada vértice, es decir a distancia del baricentro
$$R_n=\frac{2}{\sqrt3}+t_2=\frac{8\sqrt3+15-5\sqrt3}{12}=\frac{5+\sqrt3}{4}\approx 1.683.$$
Forman un triángulo equilátero **con la misma orientación** que $PQR$ y circunradio $1.683 > \tfrac{2}{\sqrt3}\approx 1.155$, así que **contiene estrictamente a $PQR$**: sus lados no cortan a los de $PQR$. ✓

- **Puntos "lejanos"**: más allá del punto medio de cada lado (p. ej. $(0,\sqrt3-t_1)\approx(0,-0.240)$, bajo el lado $PQ$). Forman un triángulo equilátero **invertido** con circunradio $t_1-\tfrac{2}{\sqrt3}=\tfrac{5-\sqrt3}{4}\approx 0.817$. Su lado opuesto al punto bajo $PQ$ es horizontal a altura $\tfrac{\sqrt3}{3}+\tfrac{5-\sqrt3}{8}\approx 0.986$; como los lados $PR$ y $QR$ de $PQR$ llegan hasta $y=\sqrt3\approx1.732$, ese lado **corta a $PR$ y a $QR$**. ✗ (Y todo triángulo con dos puntos lejanos contiene un lado así.) Los triángulos que mezclan dos puntos cercanos con el lejano intermedio son válidos, pero su lado mayor es el mismo lado cercano–cercano, así que el resultado no depende de la elección.

**4. Cálculo del lado mayor de $\triangle XYZ$.**
El triángulo $XYZ$ (puntos cercanos) es equilátero con circunradio $R_n=\tfrac{5+\sqrt3}{4}$, luego su lado es
$$XY=\sqrt3\,R_n=\frac{\sqrt3(5+\sqrt3)}{4}=\frac{5\sqrt3+3}{4}.$$

**5. Razón pedida.** Como el lado de $PQR$ es $2$:
$$\frac{XY}{PQ}=\frac{(5\sqrt3+3)/4}{2}=\frac{3+5\sqrt3}{8}\approx 1.4575.$$

$$\boxed{\dfrac{3+5\sqrt{3}}{8}}$$