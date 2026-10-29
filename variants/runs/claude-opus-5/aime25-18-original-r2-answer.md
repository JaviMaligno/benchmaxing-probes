**Enumeración rápida para confirmar:**


name: Bash
input:
command: python3 -Ic "
from itertools import product
c=0
for b in product([0,1],repeat=12):
    h=[[b[2*r+j] for j in range(2)] for r in range(3)]
    v=[[b[6+2*k+i] for i in range(2)] for k in range(3)]
    ok=all(h[r][k]+h[r+1][k]+v[k][r]+v[k+1][r]==2 for r in range(2) for k in range(2))
    c+=ok
print(c)
"
description: Brute force count of colorings
timeout: 60000

function_results
82