## Planteamiento con coordenadas

Coloco $A=(0,0)$, $C=(102,0)$ y busco $B$:

$$x^2+y^2=6400,\qquad (x-102)^2+y^2=676 \;\Rightarrow\; 204x=5724+10404 \;\Rightarrow\; x=\tfrac{1344}{17}$$

$$y^2=6400-\tfrac{1806336}{289}=\tfrac{43264}{289}\;\Rightarrow\; y=\tfrac{208}{17}$$

Luego $[ABC]=\tfrac12\cdot 102\cdot\tfrac{208}{17}=624$.

## Vértices de los cuadrados

Sea $J$ la rotación de $90^\circ$ antihoraria. Como $A\to B\to C$ es horario, la normal exterior de cada lado es $J$ aplicado al recorrido $A\to B\to C\to A$:

- $n_1=J(b-a)=\left(-\tfrac{208}{17},\tfrac{1344}{17}\right)$: $X=B+n_1$, $Y=A+n_1$
- $n_2=J(c-b)=\left(\tfrac{208}{17},\tfrac{390}{17}\right)$: $P=C+n_2$, $Q=B+n_2$
- $n_3=J(a-c)=(0,-102)$: $M=C+n_3=(102,-102)$, $N=A+n_3=(0,-102)$

## Los puntos medios

Como $n_1+n_2+n_3=J(0)=0$, resulta una simplificación notable:

$$L_1=\frac{M+P}{2}=c+\frac{n_2+n_3}{2}=c-\frac{n_1}{2},\quad L_2=b-\frac{n_3}{2},\quad L_3=a-\frac{n_2}{2}$$

Numéricamente:

$$L_1=\left(\tfrac{1838}{17},-\tfrac{672}{17}\right),\qquad L_2=\left(\tfrac{1344}{17},\tfrac{1075}{17}\right),\qquad L_3=\left(-\tfrac{104}{17},-\tfrac{195}{17}\right)$$

## Área

$$L_2-L_1=\tfrac{1}{17}(-494,\,1747),\qquad L_3-L_1=\tfrac{1}{17}(-1942,\,477)$$

$$\text{producto cruz}=\frac{(-494)(477)-(1747)(-1942)}{289}=\frac{-235638+3392674}{289}=\frac{3157036}{289}=10924$$

$$[L_1L_2L_3]=\tfrac12\cdot 10924=5462$$

**Verificación con la fórmula general:** desarrollando los mismos vectores en términos de $u=b-a$, $v=c-b$, $w=a-c$ se obtiene

$$[L_1L_2L_3]=\frac{7}{4}[ABC]+\frac{a^2+b^2+c^2}{4}=\frac{7\cdot 624}{4}+\frac{676+10404+6400}{4}=1092+4370=5462$$

\boxed{5462}