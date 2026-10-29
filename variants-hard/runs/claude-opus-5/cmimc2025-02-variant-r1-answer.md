## Planteamiento

Las parábolas son $y=(x-3j)^2$ con $j=0,1,\dots,11$, es decir **12 parábolas** (desplazamientos $0,3,6,\dots,33$).

**Cortes con $y=k$:**
- Si $k<0$: ningún punto.
- Si $k=0$: un punto por parábola → 12 puntos.
- Si $k>0$: dos puntos por parábola, $x=3j\pm\sqrt{k}$ → 24 puntos contados con repetición.

Como necesitamos 23, debe ser $k>0$ y ha de producirse **exactamente una coincidencia** entre puntos de parábolas distintas.

## Condición de coincidencia

Dos puntos coinciden cuando
$$3j+\sqrt{k}=3i-\sqrt{k}\quad\Longrightarrow\quad 2\sqrt{k}=3(i-j).$$

Escribiendo $i-j=m\ge 1$, se requiere $\sqrt{k}=\dfrac{3m}{2}$.

Para ese valor de $m$, las parejas de índices con $i-j=m$ dentro de $\{0,\dots,11\}$ son $12-m$. Cada pareja fusiona dos puntos en uno, reduciendo el total en $12-m$:
$$24-(12-m)=23\quad\Longrightarrow\quad 12-m=1\quad\Longrightarrow\quad m=11.$$

## Verificación

Con $m=11$: $\sqrt{k}=\frac{33}{2}=16{,}5$.

- Puntos derechos: $3j+16{,}5$ para $j=0,\dots,11$ → $16{,}5;\ 19{,}5;\ \dots;\ 49{,}5$.
- Puntos izquierdos: $3j-16{,}5$ → $-16{,}5;\ -13{,}5;\ \dots;\ 16{,}5$.

El único valor repetido es $x=16{,}5$ (derecho de $j=0$ e izquierdo de $j=11$). Total: $24-1=23$ puntos distintos. ✓

$$k=\left(\tfrac{33}{2}\right)^2=\frac{1089}{4}$$

\boxed{\dfrac{1089}{4}}