## Planteamiento

La ecuación $\log(kx)=2\log(x+2)$ exige $kx>0$ y $x+2>0$. Bajo esas condiciones equivale a

$$kx=(x+2)^2 \iff x^2+(4-k)x+4=0.$$

Sea $f(x)=x^2+(4-k)x+4$. Nota que el producto de las raíces es $4>0$ (mismo signo) y el discriminante es $(4-k)^2-16=k^2-8k=k(k-8)$.

**Caso $k=0$:** $\log(0)$ no está definido, no hay solución.

**Caso $k<0$:** se necesita $x<0$, junto con $x>-2$, es decir $x\in(-2,0)$. El discriminante $k(k-8)>0$, así que hay dos raíces reales distintas; la suma $k-4<0$ y el producto $4>0$, luego ambas son negativas. Como $f(-2)=4-2(4-k)+4=2k<0$ y $f(0)=4>0$, hay exactamente una raíz en $(-2,0)$ (la otra es menor que $-2$). Por tanto **todos** los $k$ de $-500$ a $-1$ sirven: $500$ valores.

**Caso $k>0$:** se necesita $x>0$. Como $f(0)=4>0$ y el producto de raíces es positivo, las raíces (si existen) son ambas positivas cuando $k-4>0$. 
- Si $0<k<8$: discriminante negativo, no hay soluciones.
- Si $k=8$: raíz doble $x=2$, exactamente **una** solución.
- Si $k>8$: dos raíces positivas distintas, ambas válidas → dos soluciones.

Así solo $k=8$ aporta: $1$ valor.

**Total:** $500+1=501$.

\boxed{501}