
<invoke name="Bash">
<parameter name="command">python3 -I -c "
t=0
n=91
while n<1000000:
    t+=sum(int(c) for c in str(n) if int(c)%2==1)
    n+=91
print(t)
"</parameter>
</invoke>


```
250797
```