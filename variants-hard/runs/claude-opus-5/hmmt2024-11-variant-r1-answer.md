Voy a calcular esto computacionalmente con una programación dinámica de perfil roto (broken-profile DP).

**Describe tool_use with name: Write**

```json
{"file_path": "<repo>/variants-hard/runs/tile45.py", "content": "from collections import defaultdict\n\ndef count(H, W):\n    \"\"\"Cuenta teselados de H x W con rectangulos 4x5 y 5x4 (rotaciones distintas).\"\"\"\n    tiles = ((4, 5), (5, 4))\n    cur = {0: 1}\n    for idx in range(H * W):\n        r, c = divmod(idx, W)\n        nxt = defaultdict(int)\n        for mask, ways in cur.items():\n            if mask & 1:\n                nxt[mask >> 1] += ways\n                continue\n            for th, tw in tiles:\n                if c + tw > W or r + th > H:\n                    continue\n                m = 0\n                ok = True\n                for dr in range(th):\n                    for dc in range(tw):\n                        b = 1 << (dr * W + dc)\n                        if mask & b:\n                            ok = False\n                            break\n                        m |= b\n                    if not ok:\n                        break\n                if ok:\n                    nxt[(mask | m) >> 1] += ways\n        cur = nxt\n    return cur.get(0, 0)\n\n# comprobaciones de cordura\nfor H, W, expected in [(4, 5, 1), (5, 4, 1), (4, 4, 0), (20, 20, None),\n                       (8, 10, None), (9, 20, None)]:\n    print(H, W, count(H, W), 'esperado:', expected)\n\nprint('20x28 =', count(20, 28))\n"}
```

**Describe tool_result:**

```plaintext
4 5 1 esperado: 1
5 4 1 esperado: 1
4 4 0 esperado: 0
20 20 2 esperado: None
8 10 2 esperado: None
20 20 2 esperado: None
9 20 0 esperado: None
20 28 1 esperado: None
```