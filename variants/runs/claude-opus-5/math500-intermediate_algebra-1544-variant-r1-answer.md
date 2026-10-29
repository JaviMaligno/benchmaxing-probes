## Planteamiento

Sea $f(t) = t^2 - 4t + 6$. Si $S$ es el conjunto de raíces distintas de $x^2+px+q=0$, la condición es $f(S) \subseteq S$, con $|S| \in \{1,2\}$.

**Puntos fijos de $f$:** $f(t)=t \iff t^2-5t+6=0 \iff t\in\{2,3\}$.

**Preimágenes útiles:**
- $f(t)=2 \iff t^2-4t+4=0 \iff t=2$
- $f(t)=3 \iff t^2-4t+3=0 \iff t\in\{1,3\}$
- $f(t)=1 \iff t^2-4t+5=0 \iff t=2\pm i$

## Caso $|S|=1$ (raíz doble)

Se necesita $f(t)=t$, luego $t=2$ o $t=3$:
$$(x-2)^2 = x^2-4x+4, \qquad (x-3)^2 = x^2-6x+9$$

## Caso $|S|=2$, $S=\{a,b\}$

**(i) Ambas fijas:** $S=\{2,3\}$ → $x^2-5x+6$.

**(ii) Una fija, la otra va hacia ella:** $f(b)=a$, $f(a)=a$ con $b \ne a$.
- $a=2$: $f^{-1}(2)=\{2\}$, no hay $b$ válido.
- $a=3$: $f^{-1}(3)=\{1,3\}$, luego $b=1$ → $S=\{1,3\}$ → $x^2-4x+3$.

Verificación: $f(1)=3$ ✓, $f(3)=3$ ✓.

**(iii) Ciclo de longitud 2:** $f(a)=b$, $f(b)=a$, $a\ne b$. Restando las ecuaciones:
$$(a-b)(a+b) - 4(a-b) = b-a \implies (a-b)(a+b-3)=0 \implies a+b=3$$
Sumándolas: $a^2+b^2 - 4\cdot 3 + 12 = 3$, es decir $a^2+b^2=3$, y con $a+b=3$: $ab = \frac{9-3}{2}=3$.

Esto da $x^2-3x+3=0$, con raíces $\frac{3\pm i\sqrt3}{2}$. Verificación: si $t^2=3t-3$, entonces $f(t)=3t-3-4t+6=3-t$, que es la otra raíz ✓.

(Un intento con $a=2+i$ falla: $f(2+i)=1$, pero $f(1)=3\notin S$.)

## Conteo

$$x^2-4x+4,\quad x^2-6x+9,\quad x^2-5x+6,\quad x^2-4x+3,\quad x^2-3x+3$$

\boxed{5}