
<invoke_parameter name="command">python3 -I -c "
INF=float('inf')
best=[0]+[INF]*1000
for n in range(1,1001):
    for c in (1,10,25):
        if n>=c and best[n-c]+1<best[n]: best[n]=best[n-c]+1
def greedy(n):
    k=0
    for c in (25,10,1):
        k+=n//c; n%=c
    return k
print(sum(1 for n in range(1,1001) if greedy(n)==best[n]))
"</invoke_parameter>
<invoke_parameter name="description">Contar N donde greedy es óptimo</invoke_parameter>
</invoke>


_results715