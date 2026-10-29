## Planteamiento

Con el filtro de raíces de la unidad ($\omega = e^{2\pi i/5}$):

$$q(k)=\frac{1}{5}\sum_{j=0}^{4}\omega^{-jk}\left(\frac{1+\omega^j}{2}\right)^{20}$$

Como $1+\omega^j = 2\cos(\pi j/5)\,e^{i\pi j/5}$, se tiene $\left(\frac{1+\omega^j}{2}\right)^{20}=\cos^{20}(\pi j/5)\,e^{i4\pi j}=\cos^{20}(\pi j/5)$, **real y positivo**.

Agrupando $j=1,4$ y $j=2,3$ (donde $c_1=\cos^{20}36^\circ$, $c_2=\cos^{20}72^\circ$):

$$q(k)-\tfrac15=\tfrac{2}{5}\Big[c_1\cos\tfrac{2\pi k}{5}+c_2\cos\tfrac{4\pi k}{5}\Big]$$

## Signos

Puesto que $c_1\approx 1.4426\cdot10^{-2}$ domina ampliamente a $c_2\approx 6.3\cdot10^{-11}$, el signo lo fija $\cos(2\pi k/5)$: positivo para $k=0,1,4$ y negativo para $k=2,3$. Sumando los valores absolutos:

$$S=\frac{2}{5}\Big[(1+2\cos72^\circ+2\cos36^\circ)c_1-(2\cos36^\circ+2\cos72^\circ-1)c_2\Big]=\frac{2}{5}\Big[(1+\sqrt5)c_1-(\sqrt5-1)c_2\Big]$$

## Cierre exacto

Con $\cos36^\circ=\frac{1+\sqrt5}{4}$, $\cos72^\circ=\frac{\sqrt5-1}{4}$ resulta $c_1=\varphi^{20}/2^{20}$, $c_2=\varphi^{-20}/2^{20}$, y usando $1+\sqrt5=2\varphi$, $\sqrt5-1=2/\varphi$:

$$S=\frac{4}{5\cdot 2^{20}}\left(\varphi^{21}-\varphi^{-21}\right)=\frac{4\,L_{21}}{5\cdot 2^{20}},\qquad L_{21}=24476$$

$$S=\frac{97904}{5242880}=\frac{6119}{327680}\approx 0.0186713$$

**Verificación directa** con los conteos $N_k$ (desviación respecto a $2^{20}/5=209715.2$):

| $k$ | $N_k$ | $N_k - 2^{20}/5$ |
|---|---|---|
| 0 | 215766 | $+6050.8$ |
| 1, 4 | 211585 | $+1869.8$ |
| 2, 3 | 204820 | $-4895.2$ |

Suma de valores absolutos: $19580.8 = \frac{97904}{5}$, y al dividir entre $2^{20}$ se obtiene $\frac{6119}{327680}$. ✓

$$\boxed{\dfrac{6119}{327680}}$$