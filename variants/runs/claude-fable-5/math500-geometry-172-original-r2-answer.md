Voy a resolver con coordenadas.

**Planteamiento:** Sea $B=(0,0)$, $C=(1,0)$, $A=(a,b)$. Entonces:

- Centroide: $G=\left(\frac{a+1}{3}, \frac{b}{3}\right)$.
- $E$ es el punto medio de $AC$ (porque $BE$ es mediana): $E=\left(\frac{a+1}{2}, \frac{b}{2}\right)$.
- La recta por $G$ paralela a $BC$ es $y=\frac{b}{3}$. Corta a $AC$ en $N$: parametrizando $A+t(C-A)$, la coordenada $y$ es $b(1-t)=\frac{b}{3}$, así que $t=\frac{2}{3}$ y $N=\left(\frac{a+2}{3}, \frac{b}{3}\right)$.

**Área de $ENG$:** Como $N$ y $G$ están a la misma altura $y=\frac{b}{3}$, la base es
$$NG = \frac{a+2}{3}-\frac{a+1}{3} = \frac{1}{3},$$
y la altura desde $E$ es $\frac{b}{2}-\frac{b}{3}=\frac{b}{6}$. Entonces
$$[ENG] = \frac{1}{2}\cdot\frac{1}{3}\cdot\frac{b}{6} = \frac{b}{36}.$$

Como $[ABC]=\frac{1}{2}\cdot 1\cdot b = \frac{b}{2} = 144$, se tiene $b=288$, y por lo tanto
$$[ENG] = \frac{288}{36} = 8.$$

$$\boxed{8}$$