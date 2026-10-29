Voy a calcularlo con un script rápido de Python.

**Herramienta: Bash**
```json
{
  "command": "python3 -c \"\nprint(sum(int(d) for k in range(91, 1000000, 91) for d in str(k) if int(d) % 2 == 1))\n\"",
  "description": "Sumar dígitos impares de los múltiplos de 91 menores a 1,000,000"
}
```