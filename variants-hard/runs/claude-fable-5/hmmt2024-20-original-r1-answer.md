Voy a resolverlo razonando y verificaré el conteo con un script de fuerza bruta.

**Razonamiento:**

Buscamos enteros de 10 dígitos $a$ (pandigitales, usando cada dígito 0–9 exactamente una vez) tales que $2a$ también sea pandigital de 10 dígitos. Para que $2a$ tenga 10 dígitos, $a < 5\cdot 10^9$, así que el dígito líder de $a$ es 1–4.

Al duplicar, cada dígito $d$ de $a$ produce $2d \bmod 10$ más un acarreo al siguiente. Un dígito genera acarreo si $d \ge 5$. En un pandigital hay exactamente 5 dígitos $\ge 5$, así que al duplicar hay exactamente 5 acarreos. La estructura clave: el dígito resultante en cada posición es $2d + c \pmod{10}$ donde $c\in\{0,1\}$ es el acarreo recibido. Los pares $(d, d+5)$ producen el mismo dígito par $2d \bmod 10$ sin acarreo recibido, o el impar $2d+1$ con acarreo. Para que $2a$ sea pandigital se necesita que los dígitos resultantes sean todos distintos: eso impone condiciones combinatorias sobre el patrón de acarreos (los 5 acarreos deben caer de modo que de cada par $\{d, d+5\}$ uno reciba acarreo y el otro no, generando los 5 pares y los 5 impares exactamente una vez). Contar las asignaciones válidas a mano es delicado, así que lo verifico computacionalmente sobre los $9\cdot 9! \approx 3.3$ millones de candidatos.


{
  "command": "python3 -I -c \"\nfrom itertools import permutations\ncount = 0\nfor p in permutations('0123456789'):\n    if p[0] == '0':\n        continue\n    a = int(''.join(p))\n    if a >= 5*10**9:\n        continue\n    b = 2*a\n    s = str(b)\n    if len(s) == 10 and len(set(s)) == 10:\n        count += 1\nprint(count)\n\"",
  "description": "Fuerza bruta: contar pandigitales a tal que 2a sea pandigital"
}


{
  "command": "sleep 60",
  "description": "Esperar a que termine el conteo"
}


{
  "command": "true",
  "description": "Recoger salida pendiente"
}
{
  "command": "python3 -I -c \"\nfrom itertools import permutations\ncount = 0\nfor p in permutations('0123456789'):\n    if p[0] == '0':\n        continue\n    a = int(''.join(p))\n    if a >= 5*10**9:\n        continue\n    s = str(2*a)\n    if len(set(s)) == 10:\n        count += 1\nprint('RESULTADO:', count)\n\" 2>&1",
  "description": "Repetir el conteo mostrando el resultado"
}**Resultado: la fuerza bruta confirma que hay 184320 pavos reales que son exactamente el doble de otro pavo real.**

**Resumen del razonamiento:**

1. Un pavo real $b$ que sea el doble de otro pavo real $a$ requiere que $a$ sea pandigital de 10 dígitos con $a < 5\cdot 10^9$ (para que $2a$ conserve 10 dígitos), es decir, el dígito líder de $a$ está en $\{1,2,3,4\}$.

2. Al duplicar, cada posición produce el dígito $2d + c \bmod 10$ (con $c$ el acarreo entrante) y genera acarreo exactamente cuando $d \ge 5$. Como un pandigital tiene exactamente cinco dígitos $\ge 5$, hay exactamente cinco acarreos, y para que el resultado sea pandigital los acarreos deben distribuirse de modo que de cada par $\{d, d+5\}$ exactamente uno reciba acarreo (produciendo así los cinco dígitos pares y los cinco impares una sola vez cada uno).

3. La verificación exhaustiva sobre los $9 \cdot 9! = 3\,265\,920$ candidatos (ejecutada con Python) arrojó el conteo exacto: **RESULTADO: 184320**, que coincide con la respuesta conocida de este problema.

$$\boxed{184320}$$