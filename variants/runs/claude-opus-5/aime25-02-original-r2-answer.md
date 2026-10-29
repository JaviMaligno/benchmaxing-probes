## Planteamiento

**Longitudes de los lados:**
- $AB = 4 + 16 + 8 = 28$
- $AC = 13 + 52 + 26 = 91$

**Cálculo de $[ABC]$ a partir de $[DEGF]$:**

Como $DEGF = \triangle AEG \setminus \triangle ADF$ (ambos triángulos comparten el ángulo $A$):

$$[ADF] = \frac{AD\cdot AF}{AB\cdot AC}[ABC] = \frac{4\cdot 13}{28\cdot 91}[ABC] = \frac{1}{49}[ABC]$$

$$[AEG] = \frac{AE\cdot AG}{AB\cdot AC}[ABC] = \frac{20\cdot 65}{28\cdot 91}[ABC] = \frac{25}{49}[ABC]$$

Entonces $288 = \frac{24}{49}[ABC]$, de donde $[ABC] = 588$.

## Verificación con coordenadas

Tomando $A=(0,0)$, $B=(28,0)$, $C=(0,42)$ (se conservan las razones sobre los lados, y $[ABC]=588$):

$D=(4,0)$, $E=(20,0)$, $F=(0,6)$, $G=(0,30)$.

Comprobación: shoelace de $D,E,G,F$ da $\tfrac{1}{2}|600-24| = 288$ ✓

Reflexiones: $M = 2F - D = (-4,12)$, $N = 2E - G = (40,-30)$.

Shoelace del heptágono $A(0,0), F(0,6), N(40,-30), B(28,0), C(0,42), E(20,0), M(-4,12)$:

$$0 - 240 + 840 + 1176 - 840 + 240 + 0 = 1176 \implies \text{Área} = 588$$

*(Razón estructural: $[AFM]=[AFD]=12$, el cuadrilátero $FMEN$ equivale a $[DFE]+[GEF]=288$, y el resto completa el triángulo.)*

\boxed{588}