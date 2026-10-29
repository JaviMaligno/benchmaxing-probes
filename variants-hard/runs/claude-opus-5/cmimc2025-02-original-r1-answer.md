## Planteamiento

Las parábolas son $y=(x-5j)^2$ con $j=0,1,\dots,9$ (diez parábolas, vértices en $0,5,\dots,45$).

**Intersecciones con $y=k$:**
- Si $k<0$: ningún punto.
- Si $k=0$: 10 puntos (los vértices).
- Si $k>0$: cada parábola aporta dos abscisas, $x=5j\pm\sqrt{k}$, es decir $20$ puntos contados con repetición.

## Cuándo se pierden puntos

Dos puntos coinciden cuando, para $i>j$,
$$5j+\sqrt{k}=5i-\sqrt{k}\quad\Longrightarrow\quad 5(i-j)=2\sqrt{k}.$$

Así que debe existir un entero $m=i-j\ge 1$ con $2\sqrt{k}=5m$, o sea $\sqrt{k}=\tfrac{5m}{2}$. Fijado ese $m$, las coincidencias ocurren para todos los pares $(j,j+m)$ con $j=0,\dots,9-m$: son $10-m$ fusiones, y cada fusión reduce el total en 1.

Para tener $19$ puntos distintos necesitamos exactamente una fusión:
$$10-m=1\quad\Longrightarrow\quad m=9.$$

## Valor de $k$

$$\sqrt{k}=\frac{5\cdot 9}{2}=\frac{45}{2}\qquad\Longrightarrow\qquad k=\frac{2025}{4}.$$

**Verificación:** con $\sqrt k = 22{,}5$, la rama derecha de $y=x^2$ da $x=22{,}5$ y la rama izquierda de $y=(x-45)^2$ da $x=45-22{,}5=22{,}5$: coinciden. Ningún otro par lo hace, porque $2\sqrt k=45=5\cdot 9$ sólo admite $m=9$. Total: $20-1=19$ puntos.

$$\boxed{\dfrac{2025}{4}}$$