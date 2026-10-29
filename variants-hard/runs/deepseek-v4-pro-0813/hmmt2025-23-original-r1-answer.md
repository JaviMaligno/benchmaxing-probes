Voy a razonar el problema paso a paso.

Sea el cuadrado $ABCD$, y $P$ un punto interior. Las áreas de los triángulos $\triangle PAB$, $\triangle PBC$, $\triangle PCD$, $\triangle PDA$ son $1,2,3,4$ en algún orden.

**Paso 1: Relación entre las áreas y las distancias de $P$ a los lados**

Si el lado del cuadrado mide $s$, entonces el área de un triángulo formado por $P$ y un lado es $\frac12 \cdot s \cdot d$, donde $d$ es la distancia de $P$ a ese lado.

Llamemos $x$ a la distancia de $P$ al lado $AB$, $y$ a la distancia de $P$ al lado $BC$, $z$ a la distancia de $P$ al lado $CD$, $w$ a la distancia de $P$ al lado $DA$. Las áreas correspondientes son $\frac12 sx$, $\frac12 sy$, $\frac12 sz$, $\frac12 sw$.

Como $AB$ y $CD$ son lados opuestos, $x+z=s$. Análogamente, $y+w=s$.

Las cuatro áreas son $1,2,3,4$, y su suma es $10$. Por otro lado, la suma de las cuatro áreas es:

$$\frac12 s(x+y+z+w)=\frac12 s(2s)=s^2.$$

Por tanto, $s^2=10$, así que $s=\sqrt{10}$.

**Paso 2: Determinar las distancias**

Las áreas son $\frac12 s d = 1,2,3,4$, con $s=\sqrt{10}$. Entonces las distancias correspondientes son:

$$d=\frac{2\cdot\text{área}}{s}=\frac{2A}{\sqrt{10}}.$$

Para áreas $1,2,3,4$:

- $A=1$: $d=\frac{2}{\sqrt{10}}$
- $A=2$: $d=\frac{4}{\sqrt{10}}$
- $A=3$: $d=\frac{6}{\sqrt{10}}$
- $A=4$: $d=\frac{8}{\sqrt{10}}$

Estas cuatro distancias deben agruparse en pares que suman $s=\sqrt{10}$. Como 

$$\frac{2}{\sqrt{10}}+\frac{8}{\sqrt{10}}=\sqrt{10},\qquad \frac{4}{\sqrt{10}}+\frac{6}{\sqrt{10}}=\sqrt{10},$$

las áreas correspondientes a lados opuestos son $\{1,4\}$ y $\{2,3\}$.

**Paso 3: Coordenadas de $P$**

Pongamos $A=(0,0)$, $B=(s,0)$, $C=(s,s)$, $D=(0,s)$.

Las áreas de $\triangle PAB$ y $\triangle PCD$ usan como base los lados horizontales $AB$ y $CD$, por lo que dependen de la coordenada $y$ de $P$: una es $\frac12 s y$ y la otra $\frac12 s(s-y)$. Como estas dos áreas suman $\frac12 s^2=5$, y deben ser el par $\{1,4\}$ o $\{2,3\}$.

Caso 1: $\triangle PAB$ y $\triangle PCD$ tienen áreas $1$ y $4$ (en algún orden). Entonces la distancia de $P$ a $AB$ es $\frac{2}{\sqrt{10}}$ o $\frac{8}{\sqrt{10}}$, es decir $y=\frac{2}{\sqrt{10}}$ o $y=\frac{8}{\sqrt{10}}$.

Las áreas de $\triangle PBC$ y $\triangle PDA$ son entonces $2$ y $3$. Sus distancias al lado derecho e izquierdo son $x$ y $s-x$, correspondientes a áreas $2$ y $3$. Para área $2$, $x=\frac{4}{\sqrt{10}}$; para área $3$, $x=\frac{6}{\sqrt{10}}$.

Entonces $P$ puede estar en una de estas posiciones (salvo permutaciones que reflejen el cuadrado):

$$P=\left(\frac{4}{\sqrt{10}},\frac{2}{\sqrt{10}}\right),\ \left(\frac{6}{\sqrt{10}},\frac{2}{\sqrt{10}}\right),\ \left(\frac{4}{\sqrt{10}},\frac{8}{\sqrt{10}}\right),\ \left(\frac{6}{\sqrt{10}},\frac{8}{\sqrt{10}}\right).$$

Caso 2: si $\triangle PAB$ y $\triangle PCD$ tienen áreas $2$ y $3$, se obtienen posiciones simétricas con los mismos valores absolutos de coordenadas, solo que intercambiados. En cualquier caso, los valores $\{x,s-x\}$ y $\{y,s-y\}$ son los mismos conjuntos, así que el producto que buscamos no cambia.

**Paso 4: Calcular el producto $PA\cdot PB\cdot PC\cdot PD$**

Tomemos por ejemplo

$$P=\left(\frac{4}{\sqrt{10}},\frac{2}{\sqrt{10}}\right).$$

Con $A=(0,0)$, $B=(\sqrt{10},0)$, $C=(\sqrt{10},\sqrt{10})$, $D=(0,\sqrt{10})$:

Sea $x=\frac{4}{\sqrt{10}}$, $y=\frac{2}{\sqrt{10}}$, y $s=\sqrt{10}$.

- $PA^2=x^2+y^2=\frac{16}{10}+\frac{4}{10}=\frac{20}{10}=2$, luego $PA=\sqrt2$.
- $PB^2=(s-x)^2+y^2=\left(\frac{6}{\sqrt{10}}\right)^2+\left(\frac{2}{\sqrt{10}}\right)^2=\frac{36}{10}+\frac{4}{10}=\frac{40}{10}=4$, luego $PB=2$.
- $PC^2=(s-x)^2+(s-y)^2=\left(\frac{6}{\sqrt{10}}\right)^2+\left(\frac{8}{\sqrt{10}}\right)^2=\frac{36}{10}+\frac{64}{10}=10$, luego $PC=\sqrt{10}$.
- $PD^2=x^2+(s-y)^2=\left(\frac{4}{\sqrt{10}}\right)^2+\left(\frac{8}{\sqrt{10}}\right)^2=\frac{16}{10}+\frac{64}{10}=8$, luego $PD=2\sqrt2$.

Entonces:

$$PA\cdot PB\cdot PC\cdot PD=\sqrt2\cdot 2\cdot\sqrt{10}\cdot 2\sqrt2=4\cdot 2\cdot\sqrt{10}\cdot\sqrt2\cdot\sqrt2?$$

Con más cuidado:

$$\sqrt2\cdot 2=2\sqrt2,\qquad \sqrt{10}\cdot 2\sqrt2=2\sqrt{20}=4\sqrt5.$$

Entonces el producto total es

$$(2\sqrt2)(4\sqrt5)=8\sqrt{10}.$$

Verifiquemos numéricamente multiplicando directamente:

$$PA^2\cdot PB^2\cdot PC^2\cdot PD^2=2\cdot 4\cdot 10\cdot 8=640.$$

Por tanto,

$$(PA\cdot PB\cdot PC\cdot PD)^2=640,$$

así que

$$PA\cdot PB\cdot PC\cdot PD=\sqrt{640}=\sqrt{64\cdot 10}=8\sqrt{10}.$$

Por lo tanto, el valor buscado es:

\boxed{8\sqrt{10}}