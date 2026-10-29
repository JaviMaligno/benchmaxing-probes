## Factorización de 12!

Calculamos los exponentes de cada primo en 12!:

- **2**: ⌊12/2⌋ + ⌊12/4⌋ + ⌊12/8⌋ = 6 + 3 + 1 = **10**
- **3**: ⌊12/3⌋ + ⌊12/9⌋ = 4 + 1 = **5**
- **5**: ⌊12/5⌋ = **2**
- **7**: **1**
- **11**: **1**

Es decir, 12! = 2¹⁰ · 3⁵ · 5² · 7 · 11.

## Condición sobre y

Si $y = 2^a 3^b 5^c 7^d 11^e$, entonces $y^3 = 2^{3a} 3^{3b} 5^{3c} 7^{3d} 11^{3e}$, y para que divida a 12! hace falta:

- $3a \le 10 \Rightarrow a \le 3$ → 4 valores (0, 1, 2, 3)
- $3b \le 5 \Rightarrow b \le 1$ → 2 valores (0, 1)
- $3c \le 2 \Rightarrow c = 0$ → 1 valor
- $3d \le 1 \Rightarrow d = 0$ → 1 valor
- $3e \le 1 \Rightarrow e = 0$ → 1 valor

## Conteo

$4 \times 2 \times 1 \times 1 \times 1 = 8$

Los valores son: 1, 2, 3, 4, 6, 8, 12, 24.

\boxed{8}