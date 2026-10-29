## Planteamiento

Sea $f(c)=c^2-2$. La condición dice que el conjunto de raíces $R$ (con $|R|\in\{1,2\}$) cumple $f(R)\subseteq R$.

**Caso 1: raíz doble $r$.** Entonces $f(r)=r$: $r^2-r-2=0\Rightarrow r=2$ o $r=-1$.
- $(x-2)^2 = x^2-4x+4$
- $(x+1)^2 = x^2+2x+1$

**Caso 2: raíces distintas $r\neq s$.**

*(a) Ambas fijas:* $r,s\in\{2,-1\}$, luego $\{2,-1\}$:
- $x^2-x-2$

*(b) Intercambio:* $r^2-2=s$, $s^2-2=r$. Restando: $(r-s)(r+s)=-(r-s)$, y como $r\neq s$, $r+s=-1$. Sustituyendo: $r^2+r-1=0$, cuyas dos soluciones son justamente $r$ y $s$, con $rs=-1$:
- $x^2+x-1$

*(c) Una fija y la otra va a ella:* $f(s)=s$ y $f(r)=s$ con $r\neq s$.
- $s=2$: $r^2=4\Rightarrow r=-2$, par $\{-2,2\}$: $x^2-4$
- $s=-1$: $r^2=1\Rightarrow r=1$, par $\{1,-1\}$: $x^2-1$

No hay soluciones con raíces no reales: un intercambio fuerza $r+s=-1$ y lleva a raíces reales, y una raíz fija debe ser real.

## Verificación

$x^2-4x+4$, $x^2+2x+1$, $x^2-x-2$, $x^2+x-1$, $x^2-4$, $x^2-1$ — las seis cumplen la condición (p. ej. en $x^2-4$: $(-2)^2-2=2$ y $2^2-2=2$).

\boxed{6}