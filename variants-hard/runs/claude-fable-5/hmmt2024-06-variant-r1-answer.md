Voy a verificar el razonamiento con un cálculo rápido en Python antes de dar el resultado.

**Razonamiento:** Sea $m = 2n+3$ (impar, así que $\gcd(2,m)=1$). Entonces $m \mid 2^{n!}-1 \iff \operatorname{ord}_m(2) \mid n!$. Como $\operatorname{ord}_m(2) \le m-1 = 2n+2$, la única obstrucción posible es que el orden tenga un factor primo $p > n$. Si $m$ es compuesto, todos los factores primos de $\lambda(m)$ son $< n$ (pues cada factor primo de $m$ es $\le m/3 < n$ para $n \ge 60$), así que siempre divide. Si $m$ es primo, el orden divide $2(n+1)$, y solo falla si $n+1$ es primo (entonces el orden es $n+1$ o $2(n+1)$, no divide a $n!$). Es decir: falla exactamente cuando $p = n+1$ es un **primo de Sophie Germain** ($p$ y $2p+1$ primos).

**Bash**

```json
{
  "command": "python3 -I -c \"\nfrom sympy import n_order, isprime\nbad=[]\nfor n in range(60,121):\n    m=2*n+3\n    d=n_order(2,m)\n    # n! mod d\n    f=1\n    for k in range(2,n+1): f=f*k%d\n    if f%d!=0: bad.append(n)\nprint(bad, sum(bad))\n\"",
  "description": "Verificar qué n no cumplen la divisibilidad"
}
```