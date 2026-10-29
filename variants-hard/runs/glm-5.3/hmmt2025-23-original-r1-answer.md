## Planteamiento

Pongo el cuadrado en coordenadas: $A=(0,0)$, $B=(s,0)$, $C=(s,s)$, $D=(0,s)$, con $P=(x,y)$ en el interior. Las áreas de los cuatro triángulos son

$$[PAB]=\frac{s\,y}{2},\qquad [PBC]=\frac{s\,(s-x)}{2},\qquad [PCD]=\frac{s\,(s-y)}{2},\qquad [PDA]=\frac{s\,x}{2}.$$

**Paso 1 — El lado del cuadrado.** Al sumar las cuatro áreas, los términos en $x$ e $y$ se cancelan, así que la suma es $s^2$. Como las áreas son $1,2,3,4$ en algún orden:

$$s^2 = 1+2+3+4 = 10,\qquad s=\sqrt{10}.$$

**Paso 2 — Triángulos opuestos.** Los triángulos opuestos suman

$$[PAB]+[PCD]=\frac{s}{2}\big(y+(s-y)\big)=\frac{s^2}{2}=5,$$

e igual $[PBC]+[PDA]=5$. Por tanto los pares de áreas opuestas son necesariamente $\{1,4\}$ y $\{2,3\}$. Escribo $\alpha=[PAB]$, $\beta=[PBC]$, $\gamma=[PCD]$, $\delta=[PDA]$, con $\{\alpha,\gamma\}=\{1,4\}$ y $\{\beta,\delta\}=\{2,3\}$ (o al revés).

**Paso 3 — Las distancias.** De las áreas: $y=\frac{2\alpha}{s}$, $s-y=\frac{2\gamma}{s}$, $x=\frac{2\delta}{s}$, $s-x=\frac{2\beta}{s}$. Entonces

$$PA^2=\frac{4}{s^2}\big(\delta^2+\alpha^2\big),\quad PB^2=\frac{4}{s^2}\big(\alpha^2+\beta^2\big),\quad PC^2=\frac{4}{s^2}\big(\beta^2+\gamma^2\big),\quad PD^2=\frac{4}{s^2}\big(\gamma^2+\delta^2\big).$$

Es decir, cada distancia al cuadrado es (salvo el factor $4/s^2$) la suma de los cuadrados de las áreas de los dos triángulos que tocan esa esquina. Como $\{\alpha,\gamma\}$ y $\{\beta,\delta\}$ son los dos pares $\{1,4\}$ y $\{2,3\}$, las cuatro sumas recorren exactamente todas las combinaciones:

$$\{1^2+2^2,\ 1^2+3^2,\ 4^2+2^2,\ 4^2+3^2\}=\{5,\,10,\,20,\,25\},$$

que **no depende del orden** de las áreas.

**Paso 4 — El producto.** Con $s^2=10$:

$$\{PA^2,\,PB^2,\,PC^2,\,PD^2\}=\frac{4}{10}\{5,\,10,\,20,\,25\}=\{2,\,4,\,8,\,10\}.$$

(Comprobación: con áreas $\alpha=1,\beta=2,\gamma=4,\delta=3$ queda $P=(6/\sqrt{10},\,2/\sqrt{10})$ y las distancias son $2,\ \sqrt2,\ 2\sqrt2,\ \sqrt{10}$.)

Por lo tanto,

$$PA\cdot PB\cdot PC\cdot PD=\sqrt{2\cdot 4\cdot 8\cdot 10}=\sqrt{640}=8\sqrt{10}.$$

$\boxed{8\sqrt{10}}$