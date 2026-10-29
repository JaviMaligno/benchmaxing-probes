## Planteamiento

**Reformulación clave.** El procedimiento registra el valor de la raíz en los tiempos $t = 0, 1, 2, \dots$ (siendo $t$ el número de intercambios realizados) y se detiene en
$$T = \min\{t : \text{el } 6 \text{ está en la raíz}\}.$$
Como la raíz contiene $4$ en $t=0$ y $6$ en $t=T$, para $a \in \{1,2,3,5,7\}$:
$$q(a) = P(a \text{ visita la raíz en algún } t < T) = P(T_a < T_6),$$
es decir, $q(a)$ es la probabilidad de que **$a$ llegue a la raíz antes que el 6** (una "carrera" entre dos partículas).

**Cadena de dos partículas.** El par $(x,y) = (\text{posición del } 6, \text{posición de } a)$ es markoviano: se elige una arista uniformemente entre las 6; el 6 se mueve si la arista toca $x$, $a$ se mueve si toca $y$, y si la arista es $\{x,y\}$ se intercambian. Frontera: si $x = R$ el valor es $0$ (el proceso termina); si $y = R$ (con $x \ne R$) el valor es $1$.

**Simetrías del árbol.** Los automorfismos $(C\,D)$, $(E\,F)$ y $(A\,B)(C\,E)(D\,F)$ hacen a $h$ constante en órbitas de pares. Con el 6 empezando en $B$:
- $q(2) = h(B,A) =: \alpha$
- $q(1) = q(3) = h(B,C) =: \gamma$ (1 y 3 en hijos de $A$)
- $q(5) = q(7) = h(B,E) =: \beta$ (5 y 7 en hijos de $B$)

Defino además $\delta = h(C,A)$ ($a$ es padre del 6), $\varepsilon = h(C,B)$ ($a$ es tío), $\phi = h(C,D)$ (hojas hermanas), $\psi = h(C,E)$ (hojas primas).

## Sistema de ecuaciones (análisis del primer paso, aristas $(R,A),(R,B),(A,C),(A,D),(B,E),(B,F)$)

$$\alpha = \tfrac{1 + 2\gamma + 2\varepsilon}{6}, \qquad
\gamma = \tfrac{\alpha + 2\gamma + 2\psi}{6}, \qquad
\varepsilon = \tfrac{1 + \alpha + 2\varepsilon + 2\psi}{6}, \qquad
\psi = \tfrac{2\gamma + 2\varepsilon + 2\psi}{6}$$

$$\beta = \tfrac{3\beta + \delta + \phi}{6}, \qquad
\delta = \tfrac{1 + \beta + \phi + 3\delta}{6}, \qquad
\phi = \tfrac{4\phi## Resolución del sistema

**Subsistema $\beta, \delta, \phi$:**
- $3\beta = \delta + \phi$
- $3\delta = 1 + \beta + \phi$
- $2\phi = \beta + \delta$

De la 1.ª y 3.ª: $\delta = 3\beta - \phi$ y $\delta = 2\phi - \beta$, luego $3\beta - \phi = 2\phi - \beta \Rightarrow 4\beta = 3\phi$, es decir $\phi = \frac{4\beta}{3}$, $\delta = \frac{5\beta}{3}$. Sustituyendo en la 2.ª: $5\beta = 1 + \beta + \frac{4\beta}{3} \Rightarrow 8\beta = 3$, luego:
$$\beta = \tfrac{3}{8}, \quad \delta = \tfrac{5}{8}, \quad \phi = \tfrac{1}{2}.$$

**Subsistema $\alpha, \gamma, \varepsilon, \psi$:** restando la ecuación de $\gamma$ de la de $\varepsilon$: $4(\varepsilon - \gamma) = 1$, es decir $\varepsilon = \gamma + \tfrac14$. Además $\psi = \tfrac{\gamma + \varepsilon}{2}$, y la ecuación de $\gamma$ da $\alpha = 4\gamma - 2\psi = 3\gamma - \varepsilon = 2\gamma - \tfrac14$. Sustituyendo en la de $\alpha$:
$$6(2\gamma - \tfrac14) = 1 + 2\gamma + 2(\gamma + \tfrac14) \Rightarrow 12\gamma - \tfrac32 = \tfrac32 + 4\gamma \Rightarrow 8\gamma = 3,$$
luego:
$$\gamma = \tfrac{3}{8}, \quad \varepsilon = \tfrac{5}{8}, \quad \alpha = \tfrac{1}{2}, \quad \psi = \tfrac{1}{2}.$$

**Comprobación de $\alpha = \tfrac12$ por simetría pura:** componer la reflexión del árbol (intercambio de subárboles izquierdo y derecho, que manda $(B,A) \mapsto (A,B)$) con el intercambio de los papeles de las partículas 6 y 2 deja la configuración inicial invariante y transforma el evento "el 2 llega antes" en su complementario; por tanto $\alpha = 1 - \alpha$.

**Verificación numérica** (p. ej.): $6\alpha = 3$ y $1 + 2\gamma + 2\varepsilon = 1 + \tfrac34 + \tfrac54 = 3$ ✓; $3\delta = \tfrac{15}{8}$ y $1 + \beta + \phi = 1 + \tfrac38 + \tfrac48 = \tfrac{15}{8}$ ✓; $4\gamma = \tfrac32$ y $\alpha + 2\psi = \tfrac12 + 1 = \tfrac32$ ✓.

## Resultado

$$q(2) = \tfrac{1}{2}, \qquad q(1) = q(3) = q(5) = q(7) = \tfrac{3}{8}.$$

Por tanto:
$$q(1)+q(2)+q(3)+q(5)+q(7) = \tfrac{3}{8} + \tfrac{1}{2} + \tfrac{3}{8} + \tfrac{3}{8} + \tfrac{3}{8} = \tfrac{3+4+3+3+3}{8} = \tfrac{16}{8} = 2.$$

$\boxed{2}$