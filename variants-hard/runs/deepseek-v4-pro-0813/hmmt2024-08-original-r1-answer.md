

<tool_calls>
<tool_calls>
<invoke name="exec_command">
<parameter name="cmd" string="true">python3 - <<'PY'
import itertools, cmath, math
n=13
z=0
vals={}
for comb in itertools.combinations(range(n),4):
    s=sum(cmath.exp(2j*math.pi*k/n) for k in comb)
    m2=abs(s)**2
    # check near 3
    if abs(m2-3)<1e-9:
        print(comb, m2, s)
PY</parameter>
<parameter name="reason" string="true">Enumerate 4 distinct residues mod 13 whose sum has magnitude sqrt(3).</parameter>
</invoke>
</tool_calls>