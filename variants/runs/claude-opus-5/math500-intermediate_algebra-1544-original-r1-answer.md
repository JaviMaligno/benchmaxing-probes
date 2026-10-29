## Planteamiento

Sea $f(c)=c^2-2$. Si $r,s$ son las raíces (con multiplicidad), la condición dice que $f$ envía el conjunto de raíces dentro de sí mismo.

**Caso 1: raíz doble $r$.** Entonces $f(r)=r$, es decir $r^2-r-2=0$, luego $r=2$ o $r=-1$:
- $(x-2)^2 = x^2-4x+4$
- $(x+1)^2 = x^2+2x+1$

**Caso 2: raíces distintas $r\neq s$.**

*2a) Ambas fijas:* $f(r)=r$, $f(s)=s$ obliga a $\{r,s\}=\{2,-1\}$:
- $x^2-x-2$

*2b) Intercambio:* $r^2-2=s$, $s^2-2=r$. Restando: $(r-s)(r+s)=-(r-s)$, así $r+s=-1$. Sumando: $r^2+s^2=r+s+4=3$, y de $(r+s)^2-2rs=3$ sale $rs=-1$:
- $x^2+x-1$ (discriminante $5>0$, raíces reales distintas ✓)

*2c) Una fija, la otra cae en ella:* $f(s)=s$ con $s=2$ o $s=-1$, y $r^2-2=s$ con $r\neq s$:
- $s=2$: $r=-2$ → $x^2-4$
- $s=-1$: $r=1$ → $x^2-1$

**Raíces complejas:** si fueran conjugadas no reales, $f(r)=r$ daría $r$ real, y $f(r)=\bar r$ lleva al caso 2b, cuyas raíces son reales. No aportan soluciones nuevas.

## Conteo

$$x^2-4x+4,\quad x^2+2x+1,\quad x^2-x-2,\quad x^2+x-1,\quad x^2-4,\quad x^2-1$$

\boxed{6}