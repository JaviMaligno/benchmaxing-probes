```bash
python3 -c "
def greedy(N):
    a=N//24; r=N-24*a; b=r//10; return a+b+r-10*b
def opt(N):
    m=N
    for a in range(N//24+1):
        for b in range((N-24*a)//10+1):
            m=min(m,a+b+N-24*a-10*b)
    return m
print(sum(1 for N in range(1,1001) if greedy(N)==opt(N)))
"
```