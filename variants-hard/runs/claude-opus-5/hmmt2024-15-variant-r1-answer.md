## Análisis

Sea $G$ el grafo 3-regular con 12 vértices (ciudades), donde cada par de vértices distintos tiene 0 o 2 vecinos comunes.

**Aristas en triángulos.** Si $u\sim v$ tienen 2 vecinos comunes $a,b$, entonces $u$ tiene vecinos $\{v,a,b\}$ y $v$ tiene $\{u,a,b\}$. El vértice $a$ es vecino de $u,v$ y de un tercero $x$. Los vecinos comunes de $u$ y $a$ son $\{v\}\cup(\{b\}\cap\{x\})$; para que sean 2 hace falta $x=b$. Igual con $b$, luego $\{u,v,a,b\}=K_4$, una componente completa. En $K_4$ todo par adyacente tiene exactamente 2 vecinos comunes ✓.

Como no se admite "1 vecino común", cada arista está en 0 o 2 triángulos: **toda componente es $K_4$ o es libre de triángulos**.

**Componentes libres de triángulos.** Sea $u$ con vecinos $a,b,c$ (no adyacentes entre sí). Cada par, p. ej. $a,b$, ya comparte $u$, así que debe tener exactamente otro vecino común. Llamemos $w_c$ al segundo vecino común de $a,b$; análogamente $w_b$ (de $a,c$) y $w_a$ (de $b,c$). Son distintos (si no, algún vértice tendría grado $<3$), y así:
$$a\sim u,w_b,w_c\qquad b\sim u,w_a,w_c\qquad c\sim u,w_a,w_b$$
Cada $w$ tiene aún grado 2. $w_a$ y $w_b$ comparten $c$ y necesitan otro vecino común: no puede ser que $w_a\sim w_b$ (daría triángulo con $c$), ni un vértice de $\{a,b,c\}$ (daría 3 vecinos comunes con $u$). Luego los terceros vecinos de $w_a,w_b,w_c$ coinciden en un único vértice nuevo $v$.

Resultan 8 vértices y el grafo es exactamente el **cubo $Q_3$** (pares antipodales: $u\!-\!v$, $a\!-\!w_a$, etc.). Se verifica: distancia 2 → 2 vecinos comunes; distancia 3 → 0 ✓. Nótese que $K_{3,3}$ **no** sirve (dos vértices del mismo lado tienen 3 vecinos comunes).

**Conclusión:** toda componente es $K_4$ (4 vértices) o $Q_3$ (8 vértices). Con 12 ciudades: $4+4+4$ o $4+8$.

**Conteo.**

- $4+4+4$: $\dfrac{12!}{(4!)^3\,3!}=5775$.
- $4+8$: elegir el $K_4$: $\binom{12}{4}=495$; etiquetados de $Q_3$ sobre 8 vértices: $\dfrac{8!}{|\mathrm{Aut}(Q_3)|}=\dfrac{40320}{48}=840$. Total $495\cdot 840=415800$.

$$5775+415800=421575$$

\boxed{421575}