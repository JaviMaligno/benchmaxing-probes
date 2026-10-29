## Planteamiento

Sea $f(c) = c^2 - 2$. La condición dice: si $c$ es raíz, entonces $f(c)$ también es raíz. Es decir, el conjunto $S$ de raíces debe cumplir $f(S) \subseteq S$. Como la ecuación es cuadrática mónica, $S$ tiene 1 o 2 elementos, y cada $S$ admisible determina exactamente una ecuación.

## Caso 1: raíz doble, $S = \{c\}$

Se necesita $f(c) = c$:
$$c^2 - 2 = c \iff (c-2)(c+1) = 0 \implies c = 2 \ \text{o} \ c = -1.$$
- $c = 2$: $(x-2)^2 = x^2 - 4x + 4$
- $c = -1$: $(x+1)^2 = x^2 + 2x + 1$

→ **2 ecuaciones.**

## Caso 2: dos raíces distintas $r \neq s$

Cada imagen debe caer en $\{r,s\}$; hay cuatro sub-casos:

**(a) Ambas fijas:** $f(r)=r$, $f(s)=s$ obliga a $\{r,s\} = \{2,-1\}$:
$$x^2 - x - 2.$$

**(b) Se intercambian:** $f(r)=s$, $f(s)=r$. Entonces $f(f(r)) = r$ con $f(r) \neq r$:
$$f(f(x)) - x = (x^2-2)^2 - 2 - x = x^4 - 4x^2 - x + 2 = (x^2 - x - 2)(x^2 + x - 1).$$
El primer factor son los puntos fijos; el ciclo de período 2 son las raíces de $x^2 + x - 1$, es decir $\frac{-1 \pm \sqrt{5}}{2}$, y en efecto $f$ las intercambia:
$$x^2 + x - 1.$$

**(c) Una fija y la otra se mapea a ella:** $f(s) = s$ (luego $s \in \{2,-1\}$) y $r^2 = s+2$ con $r \neq s$:
- $s = 2$: $r = -2$ → raíces $\{2,-2\}$ → $x^2 - 4$
- $s = -1$: $r = 1$ → raíces $\{1,-1\}$ → $x^2 - 1$

**(d)** El caso simétrico $f(r)=r$, $f(s)=r$ reproduce los mismos conjuntos del sub-caso (c).

## Verificación de las seis

| Ecuación | Raíces | Acción de $f(c)=c^2-2$ |
|---|---|---|
| $x^2-4x+4$ | $2$ | $2 \mapsto 2$ ✓ |
| $x^2+2x+1$ | $-1$ | $-1 \mapsto -1$ ✓ |
| $x^2-x-2$ | $2,-1$ | ambos fijos ✓ |
| $x^2+x-1$ | $\frac{-1\pm\sqrt5}{2}$ | se intercambian ✓ |
| $x^2-4$ | $\pm 2$ | $-2 \mapsto 2$, $2 \mapsto 2$ ✓ |
| $x^2-1$ | $\pm 1$ | $1 \mapsto -1$, $-1 \mapsto -1$ ✓ |

(Todas tienen coeficientes reales —de hecho enteros—, así que el resultado no depende del dominio de $a,b$.)

## Total

$$2 + 1 + 1 + 2 = \boxed{6}$$