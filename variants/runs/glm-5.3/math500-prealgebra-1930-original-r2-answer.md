Razonemos paso a paso.

**Sumas de cada fila:**
- Fila superior: $(n-3) + 3 + (n+1) = 2n+1$
- Fila central: $(n+2) + (2n-9) + 1 = 3n-6$
- Fila inferior: $2 + n + (n-1) = 2n+1$

**Sumas de cada columna:**
- Columna izquierda: $(n-3) + (n+2) + 2 = 2n+1$
- Columna central: $3 + (2n-9) + n = 3n-6$
- Columna derecha: $(n+1) + 1 + (n-1) = 2n+1$

Como todas deben ser iguales, igualamos la fila central con la fila superior:
$$3n-6 = 2n+1 \implies n = 7$$

**Verificación con las diagonales** (con $n=7$, suma mágica $= 3(7)-6 = 15$):
- Diagonal principal: $(n-3) + (2n-9) + (n-1) = 4n-13 = 28-13 = 15$ ✓
- Diagonal secundaria: $2 + (2n-9) + (n+1) = 3n-6 = 15$ ✓

Todo es consistente.

\boxed{7}