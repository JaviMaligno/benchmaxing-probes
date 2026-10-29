

<tool_calls>
<invoke name="Bash">
<parameter name="command">python3 -c "
import itertools
digits = '0123456789'
count = 0
results = []
for p in itertools.permutations(digits):
    if p[0] == '0':
        continue
    n = int(''.join(p))
    m = 2*n
    s = str(m)
    if len(s) == 10 and len(set(s)) == 10:
        count += 1
        results.append((n, m))
print('count =', count)
print('first few:', results[:10])
"
</parameter>
</invoke>
</tool_calls>