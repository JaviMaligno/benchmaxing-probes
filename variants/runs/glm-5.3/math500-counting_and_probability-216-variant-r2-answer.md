**Paso 1: Total de personas y elecciones sin restricción**

Hay \(9 + 6 = 15\) personas en total. El número de formas de elegir 5 miembros es:
\[
\binom{15}{5} = \frac{15 \cdot 14 \cdot 13 \cdot 12 \cdot 11}{120} = 3003
\]

**Paso 2: Restar los casos inválidos (complemento)**

- **Solo ingenieros** (sin diseñadores): \(\binom{9}{5} = 126\)
- **Solo diseñadores** (sin ingenieros): \(\binom{6}{5} = 6\)

**Paso 3: Cálculo final**

\[
3003 - 126 - 6 = 2871
\]

**Verificación** (suma directa por composición): \((1,4):\ 9\binom{6}{4}=135\); \((2,3):\ \binom{9}{2}\binom{6}{3}=720\); \((3,2):\ \binom{9}{3}\binom{6}{2}=1260\); \((4,1):\ \binom{9}{4}\binom{6}{1}=756\). Suma: \(135+720+1260+756=2871\). ✓

\[
\boxed{2871}
\]