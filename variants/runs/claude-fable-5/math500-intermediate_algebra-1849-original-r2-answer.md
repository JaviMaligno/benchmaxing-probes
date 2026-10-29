**Planteamiento.** La ecuación $\log(kx)=2\log(x+2)$ exige $kx>0$ y $x+2>0$, y equivale a
$$kx=(x+2)^2 \quad\Longleftrightarrow\quad x^2+(4-k)x+4=0,\qquad x>-2.$$
Nótese que si $x>-2$ y $x\neq -2$, entonces $kx=(x+2)^2>0$ se cumple automáticamente, así que solo hay que contar raíces de la cuadrática con $x>-2$.

**Discriminante:** $(4-k)^2-16=k(k-8)$.

- **$0<k<8$:** discriminante negativo, sin soluciones reales.
- **$k=8$:** raíz doble $x=\frac{k-4}{2}=2>-2$. Exactamente una solución. ✓
- **$k=0$:** $\log(0)$ no está definido; no sirve.
- **$k>8$:** dos raíces distintas con suma $k-4>0$ y producto $4>0$, es decir, ambas positivas y por tanto ambas válidas. Son **dos** soluciones, no una.
- **$k<0$:** sea $f(x)=x^2+(4-k)x+4$. Entonces $f(-2)=4-2(4-k)+4=2k<0$, de modo que $-2$ queda estrictamente entre las dos raíces: exactamente una raíz satisface $x>-2$ (y está en $(-2,0)$, donde $kx>0$). ✓

**Conteo.** Funcionan todos los $k$ enteros con $-500\le k\le -1$ (son $500$ valores) más $k=8$, lo que da $500+1=501$.

$$\boxed{501}$$