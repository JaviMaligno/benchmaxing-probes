Voy a calcular el valor exacto por fuerza bruta sobre todas las secuencias de valores.

**Tool Call: Write**
```json
{
  "file_path": "<repo>/variants-hard/runs/pairs_expect.py",
  "content": "from itertools import permutations\nfrom fractions import Fraction\nfrom collections import Counter\n\nmulti = [5]*3 + [6]*3 + [7]*3 + [8]*3\n\nseen = set()\ntotal = 0\ncount = 0\nfor p in permutations(multi):\n    if p in seen:\n        continue\n    seen.add(p)\n    # simulate\n    n = 0\n    i = 0\n    start = 0\n    while i + 1 < len(p):\n        if p[i] == p[i+1]:\n            n += 1\n            i += 2\n            start = i\n        else:\n            i += 1\n    total += n\n    count += 1\n\nprint(count, total, Fraction(total, count))\n"
}
```

**Tool Result:**

```
File "<repo>/variants-hard/runs/pairs_expect.py" has been written successfully.
```