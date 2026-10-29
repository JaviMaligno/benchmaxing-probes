## Planteamiento

Tomo $P$ como origen y los vectores $\vec q = \vec{PQ}$, $\vec r = \vec{PR}$. Con $PQ = 3+9+6 = 18$ y $PR = 5+15+10 = 30$:

- $D = \tfrac{3}{18}\vec q = \tfrac16 \vec q$, $\quad E = \tfrac{12}{18}\vec q = \tfrac23 \vec q$
- $F = \tfrac{5}{30}\vec r = \tfrac16 \vec r$, $\quad G = \tfrac{20}{30}\vec r = \tfrac23 \vec r$

Sea $T = [PQR] = \tfrac12|\vec q \times \vec r|$.

## Área de $DEGF$ para hallar $T$

Shoelace con coordenadas en la base $(\vec q, \vec r)$: $D(\tfrac16,0)$, $E(\tfrac23,0)$, $G(0,\tfrac23)$, $F(0,\tfrac16)$.

$$\sum = \underbrace{0}_{D\to E} + \underbrace{\tfrac23\cdot\tfrac23}_{E\to G} + \underbrace{0}_{G\to F} + \underbrace{-\tfrac16\cdot\tfrac16}_{F\to D} = \tfrac49 - \tfrac1{36} = \tfrac{5}{12}$$

Luego $[DEGF] = \tfrac{5}{12}\,T = 300 \Rightarrow T = 720$.

## Reflexiones

$$M = 2F - D = -\tfrac16\vec q + \tfrac13\vec r, \qquad N = 2E - G = \tfrac43\vec q - \tfrac23\vec r$$

## Área del heptágono $PFNQREM$

Vértices: $P(0,0)$, $F(0,\tfrac16)$, $N(\tfrac43,-\tfrac23)$, $Q(1,0)$, $R(0,1)$, $E(\tfrac23,0)$, $M(-\tfrac16,\tfrac13)$.

Términos del shoelace:

$$0 \;-\; \tfrac29 \;+\; \tfrac23 \;+\; 1 \;-\; \tfrac23 \;+\; \tfrac29 \;+\; 0 \;=\; 1$$

Los términos de $F\to N$ y $E\to M$ se cancelan (efecto de las reflexiones), igual que los de $N\to Q$ y $R\to E$, porque $E$ y $G$ dividen sus lados en la misma razón $\tfrac23$.

Por tanto el heptágono tiene área $1\cdot T = T$:

$$[PFNQREM] = 720$$

\boxed{720}