## Solución paso a paso

**1. Dominio de la ecuación.**
Se requiere $kx>0$ y $x+2>0$, es decir $x>-2$ (y $k\neq 0$).

**2. Eliminar los logaritmos.**
Como $\log$ es inyectiva, con $x>-2$:
$$kx=(x+2)^2 \iff x^2+(4-k)x+4=0.$$
Nótese que si $x>-2$, entonces $kx=(x+2)^2>0$ automáticamente, así que la única restricción real es $x>-2$.

**3. Análisis de la parábola.** Producto de raíces $=4>0$, suma $=k-4$, discriminante $D=k(k-8)$. Además $f(-2)=2k$.

- **$k<0$:** ambas raíces son negativas (suma y producto negativos/positivos correspondientes) y $f(-2)=2k<0$, con lo cual $-2$ queda **estrictamente entre** las dos raíces: $r_1<-2<r_2<0$. Exactamente **una** raíz ($r_2$) cumple $x>-2$, y para ella $kx=(x+2)^2>0$. ✓ **Exactamente una solución.**
- **$k=0$:** $\log(0\cdot x)$ no está definido (y la raíz sería $x=-2$, inválida). Cero soluciones.
- **$0<k<8$:** $D<0$, no hay raíces reales. Cero soluciones.
- **$k=8$:** $D=0$, raíz doble $x=2>-2$, válida ($\log 16=\log 16$). ✓ **Exactamente una solución.**
- **$k>8$:** $D>0$, suma $=k-4>4>0$, producto $4>0$: ambas raíces positivas, ambas $>-2$. **Dos** soluciones (ej. $k=9$ da $x=1$ y $x=4$, ambas válidas).

**4. Conteo en $[-500,500]$.**
- Todos los enteros $k\in\{-500,-499,\dots,-1\}$: $500$ valores.
- Más $k=8$: $1$ valor.

Total: $500+1=501$.

$$\boxed{501}$$