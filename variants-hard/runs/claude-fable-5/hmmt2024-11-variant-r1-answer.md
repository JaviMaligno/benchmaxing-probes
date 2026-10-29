Voy a calcular esto con un programa de conteo exacto (programación dinámica por perfil), ya que un conteo manual sería inviable.

**Planteamiento:** Cada pieza de 4×5 tiene área 20, y el rectángulo de 20×28 tiene área 560, así que cualquier teselación usa 28 piezas, colocadas en orientación 4×5 o 5×4. Para contarlas, hago una recursión con memoización: tomo la celda vacía más baja y más a la izquierda, pruebo colocar ahí cada orientación de la pieza, y memoizo sobre el perfil de alturas de las 20 columnas. Así cada teselación se cuenta exactamente una vez.

**Tool use: Bash**

```json
{
  "command": "python3 -I - <<'EOF'\nimport sys\nfrom functools import lru_cache\nsys.setrecursionlimit(100000)\n\nW = 20   # ancho (columnas)\nH = 28   # altura objetivo\nTILES = [(4,5),(5,4)]  # (ancho, alto)\n\nfrom collections import defaultdict\nmemo = {}\n\ndef f(profile):\n    if all(h == H for h in profile):\n        return 1\n    key = profile\n    if key in memo:\n        return memo[key]\n    m = min(profile)\n    i = profile.index(m)  # columna más baja, más a la izquierda\n    total = 0\n    for tw, th in TILES:\n        if i + tw <= W and m + th <= H and all(profile[j] == m for j in range(i, i+tw)):\n            new = list(profile)\n            for j in range(i, i+tw):\n                new[j] = m + th\n            total += f(tuple(new))\n    memo[key] = total\n    return total\n\n# verificaciones con casos pequeños\ndef count(w, h):\n    global W, H, memo\n    W, H = w, h\n    memo = {}\n    return f(tuple([0]*w))\n\nprint(\"4x5:\", count(4,5))    # debe ser 1\nprint(\"5x4:\", count(5,4))    # debe ser 1\nprint(\"8x5:\", count(8,5))    # debe ser 1\nprint(\"4x10:\", count(4,10)) # debe ser 1\nprint(\"20x5:\", count(20,5)) # fila de 4x5: deberia dar algo pequeño\nprint(\"5x20:\", count(5,20))\nprint(\"20x28:\", count(20,28))\nprint(\"28x20:\", count(28,20))  # debe coincidir con 20x28\nprint(\"estados memoizados:\", len(memo))\nEOF",
  "description": "Contar teselaciones de 20×28 con piezas 4×5 por DP de perfil"
}
```