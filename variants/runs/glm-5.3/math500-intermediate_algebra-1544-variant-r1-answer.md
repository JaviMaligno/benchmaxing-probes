# Solución

Denotemos $g(t) = t^2 - 4t + 6 = (t-2)^2 + 2$.

## Puntos fijos y preimágenes

**Puntos fijos** ($g(t) = t$): $t^2 - 5t + 6 = 0$, es decir $(t-2)(t-3) = 0$, así que $t = 2$ o $t = 3$.

**Preimágenes:**
- De $2$: $(t-2)^2 = 0 \Rightarrow t = 2$ (única).
- De $3$: $(t-2)^2 = 1 \Rightarrow t = 1$ o $t = 3$.

## Caso 1: Raíz doble $r$

La única raíz es $r$, así que se necesita $g(r) = r$, es decir $r \in \{2, 3\}$:

1. $x^2 - 4x + 4 = 0$ (raíz doble $2$: $g(2)=2$ ✓)
2. $x^2 - 6x + 9 = 0$ (raíz doble $3$: $g(3)=3$ ✓)

## Caso 2: Raíces distintas $a, b$

Se necesita $g(a), g(b) \in \{a, b\}$. Cuatro sub-casos:

**(i) Ambas fijas:** $\{a,b\} = \{2,3\}$:

3. $x^2 - 5x + 6 = 0$ ✓

**(ii) Ciclo de longitud 2** ($g(a)=b$, $g(b)=a$, $a \neq b$):
Restando las ecuaciones $a^2-4a+6=b$ y $b^2-4b+6=a$: $(b-a)(a+b-4) = a-b$, y como $a \neq b$: $a+b = 3$. Sumándolas: $a^2+b^2 = 3$, de donde $ab = \frac{9-3}{2} = 3$. Así $\{a,b\}$ son las raíces de $x^2-3x+3=0$ (números complejos $\frac{3\pm i\sqrt{3}}{2}$). Verificación: si $a^2 = 3a-3$, entonces $g(a) = 3a-3-4a+6 = 3-a = b$ ✓:

4. $x^2 - 3x + 3 = 0$ ✓

**(iii) Una fija, la otra apunta hacia ella:** la fija es $2$ o $3$.
- Fija en $2$: la otra raíz $t$ cumple $g(t)=2 \Rightarrow t=2$, contradicción. No hay solución.
- Fija en $3$: la otra raíz cumple $g(t)=3 \Rightarrow t \in \{1, 3\}$, y como es distinta, $t = 1$:

5. $x^2 - 4x + 3 = 0$ (raíces $1, 3$: $g(1)=3$ ✓, $g(3)=3$ ✓)

**(iv)** Es simétrico a (iii) y da la misma ecuación 5.

## Verificación completa

| Ecuación | Raíces | Comportamiento de $g$ |
|---|---|---|
| $x^2-4x+4$ | $2$ (doble) | $g(2)=2$ ✓ |
| $x^2-6x+9$ | $3$ (doble) | $g(3)=3$ ✓ |
| $x^2-5x+6$ | $2, 3$ | ambas fijas ✓ |
| $x^2-4x+3$ | $1, 3$ | $g(1)=3$, $g(3)=3$ ✓ |
| $x^2-3x+3$ | $\frac{3\pm i\sqrt3}{2}$ | se intercambian ✓ |

No hay más posibilidades: todo otro par de raíces falla la condición de cierre bajo $g$.

El número de ecuaciones es $\boxed{5}$.