# Resolución paso a paso

**Planteamiento.** Como $x>0$ y el grado del numerador es 3 más que el del denominador, $f(x)\to+\infty$ cuando $x\to 0^+$ y cuando $x\to+\infty$, así que el mínimo existe. Si el mínimo $m$ se alcanza en exactamente dos puntos $a<b$, entonces
$$f(x)-m=\frac{(x-18)(x-72)(x-98)(x-k)-mx}{x}\ge 0 \quad (x>0),$$
con igualdad exactamente en $x=a,b$. Por lo tanto el polinomio cuártico
$$g(x)=(x-18)(x-72)(x-98)(x-k)-mx$$
debe ser $g(x)=(x-a)^2(x-b)^2$ (raíces dobles obligatorias).

**Comparación de coeficientes.** Con $s=a+b$, $p=ab$:
$$x^4-(188+k)x^3+(10116+188k)x^2-(127008+10116k+m)x+127008k=(x-a)^2(x-b)^2.$$

Nota: $188=18+72+98$, $10116=18\cdot72+18\cdot98+72\cdot98$, $127008=18\cdot72\cdot98$. Igualando:

- $2s=188+k \Rightarrow s=\tfrac{k+188}{2}$
- $s^2+2p=10116+188k$
- $p^2=127008k$

**Ecuación en $k$.** Despejando $2p$ y usando $p=\sqrt{127008k}=252\sqrt{2k}$:
$$2\sqrt{127008k}=10116+188k-\frac{(k+188)^2}{4}=-\frac{k^2}{2}+94k+1280\cdot\tfrac{...}{}$$
multiplicando por 4:
$$8\sqrt{127008\,k}=-k^2+376k+5120.$$
Elevando al cuadrado y simplificando:
$$k^4-752k^3+131136k^2-4278272k+26214400=0.$$

**Raíces.** Probando divisores: $k=32$ es raíz, y también $k=8$. Factorizando:
$$(k-32)(k-8)(k^2-712k+102400)=0,$$
y el cuadrático da $k=\frac{712\pm 312}{2}$, es decir $k=200$ y $k=512$.

**Descarte de la raíz extraña.** Como $8\sqrt{127008k}>0$, se necesita $-k^2+376k+5120>0$, es decir $k\lesssim 389$. El valor $k=512$ da $-64512<0$: se descarta (apareció al elevar al cuadrado).

**Verificación de los tres valores** ($s^2>4p$ para que $a,b$ sean reales, distintos y positivos):

- $k=8$: $s=98$, $p=1008$, puntos $49\pm\sqrt{1393}>0$ ✓
- $k=32$: $s=110$, $p=2016$, puntos $55\pm\sqrt{1009}>0$ ✓
- $k=200$: $s=194$, $p=5040$, puntos $97\pm\sqrt{4369}>0$ ✓

En cada caso $f(x)\ge m$ con igualdad exactamente en dos puntos.

**Suma:** $8+32+200=240$.

$$\boxed{240}$$