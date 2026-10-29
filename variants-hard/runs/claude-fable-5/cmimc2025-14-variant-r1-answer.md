Voy a verificar mi razonamiento teórico con una comprobación rápida por fuerza bruta en Python.

**Razonamiento:** $H_{n,k}$ es un grafo de Cayley sobre $\mathbb{F}_2^n$ con conjunto de conexión los vectores de peso $k$; sus componentes son las clases laterales del subgrupo generado por esos vectores. Para $k<n$, sumando dos vectores de peso $k$ que se solapan en $k-1$ posiciones se obtienen todos los vectores de peso 2, que generan el código de peso par. Así: si $k<n$ y $k$ impar, el subgrupo es todo $\mathbb{F}_2^n$ y $d_{n,k}=1$; si $k<n$ y $k$ par, el subgrupo es el código de peso par y $d_{n,k}=2$; si $k=n$, el subgrupo es $\{0,\mathbf{1}\}$ y $d_{n,n}=2^{n-1}$.

**Tool use without permission: Bash**