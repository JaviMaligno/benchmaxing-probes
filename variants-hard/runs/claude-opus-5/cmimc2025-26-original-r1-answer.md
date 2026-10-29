## Planteamiento

Coloco $X$ en el origen con $AB$, $CD$, $EF$ sobre los ejes $x$, $y$, $z$. Sea $O=(p,q,r)$, con
$$p^2+q^2+r^2 = OX^2 = \tfrac12 .$$

**Potencia del punto.** Para cada cuerda, $XA\cdot XB = R^2-OX^2 \equiv k$. Entonces:
- eje $x$: $XA=1 \Rightarrow XB=k$
- eje $y$: $XC=\sqrt2 \Rightarrow XD=k/\sqrt2$
- eje $z$: $XE=2 \Rightarrow XF=k/2$

**Coordenadas del centro.** El pie de la perpendicular de $O$ a cada eje es el punto medio de la cuerda, y los dos extremos quedan en lados opuestos de $X$:
$$p=\frac{k-1}{2},\qquad q=\frac{k/\sqrt2-\sqrt2}{2}=\frac{k-2}{2\sqrt2},\qquad r=\frac{k/2-2}{2}=\frac{k-4}{4}$$
(los signos no importan, solo los cuadrados).

## Ecuación

$$\frac{(k-1)^2}{4}+\frac{(k-2)^2}{8}+\frac{(k-4)^2}{16}=\frac12$$

Multiplicando por 16:
$$4(k-1)^2+2(k-2)^2+(k-4)^2=8 \;\Longrightarrow\; 7k^2-24k+20=0$$
$$k=\frac{24\pm 4}{14}\quad\Longrightarrow\quad k=2 \ \ \text{o}\ \ k=\frac{10}{7}$$

Ambos son positivos y dan segundas intersecciones positivas ($k/\sqrt2$, $k/2>0$), así que ambas configuraciones existen realmente (verificado: para $k=2$, $O=(\pm\frac12,0,\pm\frac12)$ con $R^2=\frac52$; para $k=\frac{10}{7}$, $p^2+q^2+r^2=\frac{9+8+81}{196}=\frac12$ con $R^2=\frac{27}{14}$).

## Resultado

$R^2 = k+\tfrac12$, luego
$$R^2 \in \left\{\tfrac52,\ \tfrac{27}{14}\right\},\qquad \text{suma}=\frac{35+27}{14}=\frac{31}{7}$$

\boxed{\dfrac{31}{7}}