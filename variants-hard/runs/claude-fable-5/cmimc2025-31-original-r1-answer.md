## Planteamiento

Si el mes es $m$ y el día es $d$ (con $k$ dígitos), la concatenación vale $N = m \cdot 10^k + d$.

**Condición para $m$:** $m \mid N \iff m \mid d$ (pues $m \mid m\cdot 10^k$).

**Condición para $d$:** $d \mid N \iff d \mid m \cdot 10^k$ (pues $d \mid d$).

Así que un día es "bueno" si y solo si: $m \mid d$ **y** $d \mid m\cdot 10^k$, donde $k=1$ para días de un dígito y $k=2$ para días de dos dígitos.

## Marzo ($m=3$, días 1–31)

Candidatos: múltiplos de 3.
- Un dígito ($d \mid 30$): 3 ✓, 6 ✓, 9 ✗ (9∤30).
- Dos dígitos ($d \mid 300$): 12 ✓ (300/12=25), 15 ✓ (300/15=20), 18 ✗, 21 ✗, 24 ✗, 27 ✗, 30 ✓.

**Marzo: 5 días** (3, 6, 12, 15, 30).

## Abril ($m=4$, días 1–30)

Candidatos: múltiplos de 4.
- Un dígito ($d \mid 40$): 4 ✓, 8 ✓.
- Dos dígitos ($d \mid 400$): 12 ✗, 16 ✓ (400/16=25), 20 ✓, 24 ✗, 28 ✗.

**Abril: 4 días** (4, 8, 16, 20).

## Mayo ($m=5$, días 1–31)

Candidatos: múltiplos de 5.
- Un dígito ($d \mid 50$): 5 ✓.
- Dos dígitos ($d \mid 500$): 10 ✓, 15 ✗, 20 ✓ (500/20=25), 25 ✓ (500/25=20), 30 ✗.

**Mayo: 4 días** (5, 10, 20, 25).

## Total

$5 + 4 + 4 = 13$

$$\boxed{13}$$