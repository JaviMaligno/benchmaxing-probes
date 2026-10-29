
<invoke name="Bash">
<parameter name="command">cd /tmp && cat > nu3.py <<'EOF'
b=0
total=0
for k in range(1,1081):
    b = b*10 + (k%10)
    n=b; e=0
    while n%3==0:
        n//=3; e+=1
    total+=e
print(total)
EOF
python3 -I nu3.py</parameter>
</invoke>


```
4336
```