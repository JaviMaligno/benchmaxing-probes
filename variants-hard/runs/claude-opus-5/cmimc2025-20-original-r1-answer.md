
<invoke name="Bash">
<parameter name="command">cd /tmp && cat > comp.py <<'EOF'
N = 3**9
pw = [1]
while pw[-1]*3 <= N: pw.append(pw[-1]*3)
a = [0]*(N+1)
a[0]=1
for n in range(1,N+1):
    s=0
    for p in pw:
        if p>n: break
        s+=a[n-p]
    a[n]=s%3
for m in range(0,10):
    M=3**m
    print(m, M, sum(a[1:M+1]))
EOF
python3 -I comp.py</parameter>
</invoke>


Rendered interactively for the user:
0 1 1
1 3 3
2 9 8
3 27 22
4 81 60
5 243 164
6 729 448
7 2187 1224
8 6561 3344
9 19683 9136