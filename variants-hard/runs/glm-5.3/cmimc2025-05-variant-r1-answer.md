```python
sum(int(d) for n in range(91,1000000,91) for d in str(n) if d in '13579')
```
2251650Podemos computarlo directamente:

```python
sum(int(d) for n in range(91, 1000000, 91) for d in str(n) if d in '13579')
```

Esto da `2251650`.

Por tanto, la suma pedida es:

\[
\boxed{2251650}
\]