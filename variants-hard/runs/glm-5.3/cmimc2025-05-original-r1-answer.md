Voy a razonarlo paso a paso y verificar con un cálculo directo.

**Planteamiento:** Los múltiplos positivos de 77 menores que 1 000 000 son $77k$ para $k = 1, \dots, 12987$ (ya que $77 \times 12987 = 999\,999$). Necesito sumar, sobre todos estos múltiplos, la suma de sus dígitos impares (1, 3, 5, 7, 9).

Lo verifico con un script:

```python
s = 0
for k in range(1, 12988):
    for c in str(77*k):
        if c in '13579':
            s += int(c)
print(s)
```bash
python3 -c "
s = 0
for k in range(1, 12988):
    for c in str(77*k):
        if c in '13579':
            s += int(c)
print(s)
"\boxed{234302}