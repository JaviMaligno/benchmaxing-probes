## Planteamiento

**Suma de Isabella:** llena con $1,2,\dots,ab$, así que

$$S_I = \frac{ab(ab+1)}{2}$$

**Suma de Vidur:** la tabla de multiplicar se factoriza

$$S_V = \sum_{i=1}^{a}\sum_{j=1}^{b} ij = \left(\frac{a(a+1)}{2}\right)\left(\frac{b(b+1)}{2}\right)$$

## Diferencia

$$\frac{ab(ab+1)}{2} - \frac{a(a+1)b(b+1)}{4} = 1200$$

Multiplicando por $4$ y sacando factor común $ab$:

$$ab\big[2(ab+1) - (a+1)(b+1)\big] = 4800$$

$$ab\big[2ab+2 - ab - a - b - 1\big] = 4800$$

$$ab(ab - a - b + 1) = 4800 \quad\Longrightarrow\quad ab(a-1)(b-1) = 4800$$

## Búsqueda de soluciones

Con $a(a-1)\cdot b(b-1) = 4800$, basta recorrer valores:

- $a=2$: $b(b-1)=2400$ — no ($49\cdot48=2352$, $50\cdot49=2450$)
- $a=3$: $b(b-1)=800$ — no ($28\cdot27=756$, $29\cdot28=812$)
- $a=4$: $b(b-1)=400$ — no ($20\cdot19=380$, $21\cdot20=420$)
- $a=5$: $b(b-1)=240 = 16\cdot 15$ ✓ → $b=16$
- $a=6$: $b(b-1)=160$ — no; y para $a\ge 7$ no aparecen más productos de consecutivos (salvo el simétrico $a=16,\ b=5$)

**Verificación** con $a=5$, $b=16$: $S_I = \frac{80\cdot 81}{2} = 3240$, $S_V = 15\cdot 136 = 2040$, diferencia $= 1200$ ✓

$$\boxed{21}$$