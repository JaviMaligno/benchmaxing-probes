
<invoke name="Bash">
<parameter name="command">cd /tmp && python3 -I -c "
from itertools import permutations
c=0
for p in permutations(range(2,9)):
    a=(1,)+p
    if all(a[i]*a[(i+1)%8]<=24 for i in range(8)): c+=1
print(c*8)
"</parameter>
</invoke>


1536