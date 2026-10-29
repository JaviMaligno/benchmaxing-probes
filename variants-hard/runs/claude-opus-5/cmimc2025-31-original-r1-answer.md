## Planteamiento

Para el mes $m$ y el día $d$, la concatenación es:
- $N = 10m + d$ si $d$ tiene un dígito
- $N = 100m + d$ si $d$ tiene dos dígitos

**Condición sobre el mes:** $m \mid N$ equivale en ambos casos a $m \mid d$ (pues $m$ divide a $10m$ y a $100m$).

**Condición sobre el día:** $d \mid N$ equivale a $d \mid 10m$ (un dígito) o $d \mid 100m$ (dos dígitos).

## Marzo ($m=3$, 31 días)

- $d\in\{1..9\}$: $3\mid d$ y $d\mid 30$ → $d = 3, 6$ (el $9$ no divide a $30$).
- $d\in\{10..31\}$: $3\mid d$ y $d\mid 300$ → divisores de $300$ en rango: $10,12,15,20,25,30$; múltiplos de $3$: $12, 15, 30$.

Días: $3, 6, 12, 15, 30$ → **5**

## Abril ($m=4$, 30 días)

- $d\in\{1..9\}$: $4\mid d$ y $d\mid 40$ → $d = 4, 8$.
- $d\in\{10..30\}$: $4\mid d$ y $d\mid 400$ → divisores de $400$ en rango: $10,16,20,25$; múltiplos de $4$: $16, 20$.

Días: $4, 8, 16, 20$ → **4**

## Mayo ($m=5$, 31 días)

- $d\in\{1..9\}$: $5\mid d$ y $d\mid 50$ → $d = 5$.
- $d\in\{10..31\}$: $5\mid d$ y $d\mid 500$ → divisores de $500$ en rango: $10, 20, 25$, todos múltiplos de $5$.

Días: $5, 10, 20, 25$ → **4**

## Total

$5 + 4 + 4 = 13$

\boxed{13}