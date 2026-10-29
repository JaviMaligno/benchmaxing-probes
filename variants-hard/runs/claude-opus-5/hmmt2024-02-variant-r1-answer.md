## Planteamiento

**Suma de Priya:** escribe $1,2,\dots,mn$, así que

$$P=\frac{mn(mn+1)}{2}.$$

**Suma de Tomás:** la tabla de multiplicar se factoriza,

$$T=\sum_{i=1}^{m}\sum_{j=1}^{n} ij=\left(\frac{m(m+1)}{2}\right)\left(\frac{n(n+1)}{2}\right).$$

## Diferencia

$$4(P-T)=2mn(mn+1)-mn(m+1)(n+1)=mn\big[2mn+2-(mn+m+n+1)\big]=mn(mn-m-n+1),$$

y como $mn-m-n+1=(m-1)(n-1)$:

$$P-T=\frac{mn(m-1)(n-1)}{4}=\frac{\big[m(m-1)\big]\big[n(n-1)\big]}{4}\ \ge 0.$$

Por tanto la condición es

$$m(m-1)\cdot n(n-1)=4\cdot 2100=8400.$$

## Búsqueda

Hay que factorizar $8400$ como producto de dos números pronicos ($2,6,12,20,30,42,56,72,90,110,132,156,182,210,240,\dots$):

- $8400/2=4200$, $8400/6=1400$, $8400/12=700$ — ninguno pronico.
- $8400/20=420=20\cdot 21$ ✓

Así $m(m-1)=20\Rightarrow m=5$ y $n(n-1)=420\Rightarrow n=21$ (o al revés). Revisando el resto de divisores pronicos ($30,42,56,210,420,\dots$) no aparece otra solución.

**Verificación** con $m=5$, $n=21$: $mn=105$, $P=\frac{105\cdot106}{2}=5565$ y $T=15\cdot231=3465$; la diferencia es $5565-3465=2100$ ✓

$$\boxed{26}$$