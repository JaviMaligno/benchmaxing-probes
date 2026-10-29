Voy a razonar el problema y luego verificar con un cálculo.

**Planteamiento.** Sea $N = \overline{pqrs} = 1000p + 100q + 10r + s$ y su rotación $N' = \overline{qrsp} = 1000q + 100r + 10s + p$. Observemos que:

$$10N - 9999p = 10000p + 1000q + 100r + 10s - 9999p = p + 1000q + 100r + 10s = N'.$$

Entonces, si $m \mid N$, tenemos $N' \equiv -9999p \pmod{m}$. La condición del problema equivale a exigir que $m \mid 9999p$ para **cada** dígito inicial $p$ que aparezca en un múltiplo de cuatro cifras de $m$.

**Todos los dígitos aparecen.** Como $m \le 99 < 1000$, cada bloque $[1000p,\,1000p+999]$ (de longitud 1000) contiene al menos un múltiplo de $m$. Por lo tanto, para cada $p \in \{1,\dots,9\}$ existe un múltiplo de cuatro cifras de $m$ que empieza con $p$. En particular, existe uno que empieza con $p=1$, lo que fuerza $m \mid 9999$.

**Recíproco.** Si $m \mid 9999$, entonces $N' = 10N - 9999p \equiv 0 \pmod m$ para todo múltiplo $N$, así que la propiedad se cumple.

**Conclusión.** Los $m$ válidos son los divisores de dos cifras de $9999 = 3^2 \cdot 11 \cdot 101$, es decir: $11$, $33$ y $99$. Verifico con fuerza bruta:

```python
ans = []
for m in range(10, 100):
    if all(int(str(N)[1:] + str(N)[0]) % m == 0
           for N in range(1000, 10000) if N % m == 0):
        ans.append(m)
print(ans, sum(ans))
```

Esto imprime `[11, 33, 99] 143`, confirmando el análisis. La suma es $11 + 33 + 99 = 143$.

\boxed{143}