## Planteamiento

**Fórmula del área.** Para un paralelogramo delimitado por $y=px+a$, $y=px+b$, $y=qx+a$, $y=qx+b$, los vértices se obtienen de la fórmula general: el área es

$$A=\frac{(b-a)^2}{|p-q|}.$$

*(Verificación: con vectores desde la intersección $(0,a)$, el determinante da exactamente ese valor.)*

**Primer paralelogramo:** separación vertical entre las rectas de pendiente $p$ es $s-r$, así que

$$\frac{(s-r)^2}{|p-q|}=8.$$

**Segundo paralelogramo:** las rectas $y=px+r$ y $y=px-s$ están separadas verticalmente por $r+s$, así que

$$\frac{(r+s)^2}{|p-q|}=50.$$

## Resolución de ecuaciones

Sea $d=|p-q|\ge 1$, $k=|s-r|$, $m=r+s$. Entonces:

$$k^2=8d,\qquad m^2=50d.$$

Dividiendo: $\dfrac{m^2}{k^2}=\dfrac{50}{8}=\dfrac{25}{4}$, así que $m=5u$ y $k=2u$ para algún entero positivo $u$. Sustituyendo:

$$d=\frac{u^2}{2}.$$

Como $d$ debe ser entero, $u$ debe ser par. Además, $r=\frac{m-k}{2}$ y $s=\frac{m+k}{2}$ deben ser enteros, lo cual también exige que $m=5u$ y $k=2u$ tengan la misma paridad, es decir, $u$ par. ✓

Escribamos $u=2v$. Entonces:

$$d=2v^2,\qquad r=3v,\quad s=7v \quad (\text{o al revés}),\qquad r+s=10v.$$

## Minimización

Con $|p-q|=2v^2$ y $p,q\ge 1$, la suma mínima es $p+q=1+(1+2v^2)=2+2v^2$. Por lo tanto:

$$p+q+r+s = 2+2v^2+10v.$$

Para $v=1$: $2+2+10=14$. Para $v=2$: $2+8+20=30$. El mínimo se alcanza con $v=1$.

**Configuración óptima:** $\{p,q\}=\{1,3\}$, $\{r,s\}=\{3,7\}$.

**Verificación:**
- Primer paralelogramo: $\frac{(7-3)^2}{|1-3|}=\frac{16}{2}=8$ ✓
- Segundo: $\frac{(3+7)^2}{2}=\frac{100}{2}=50$ ✓
- $p+q+r+s=1+3+3+7=14$

(Cota inferior confirmada: $m^2=50d\ge 50$ con $m=5u$, $u$ par $\Rightarrow r+s\ge 10$; y $d\ge 2 \Rightarrow p+q\ge 4$; total $\ge 14$.)

$$\boxed{14}$$