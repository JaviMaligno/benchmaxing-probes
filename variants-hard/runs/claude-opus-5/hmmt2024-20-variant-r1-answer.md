```bash
python3 -c "
from itertools import permutations
c=0
s=set(int(''.join(p)) for p in permutations('123456789'))
print(sum(1 for n in s if 2*n in s))
"
```