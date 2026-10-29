Voy a razonar y verificar la estructura con fuerza bruta.

**Paso 1 (progresiones aritméticas).** Si las ocurrencias de una letra $x$ están en $a_1<a_2<a_3$, entre $a_1,a_2$ no hay otras $x$, así que el total de letras en ese hueco es $\sum_{y\neq x}\#y$, y la condición obliga a que ese total coincida con el del segundo hueco: $a_2-a_1=a_3-a_2$.

**Paso 2 (estructura).** Las concatenaciones de bloques con alfabetos disjuntos siempre sirven (los huecos de cada letra solo contienen letras de su bloque), y los bloques indescomponibles parecen ser exactamente las repeticiones triples $PPP$ de una permutación. Lo verifico computacionalmente.


� Bash
{
  "command": "mkdir -p /tmp/greek && cat > /tmp/greek/bf.py <<'EOF'\nfrom itertools import permutations\nfrom math import factorial\n\ndef valid(w):\n    letters = set(w)\n    pos = {c: [i for i,ch in enumerate(w) if ch==c] for c in letters}\n    for x in letters:\n        a1,a2,a3 = pos[x]\n        for y in letters:\n            if y==x: continue\n            c1 = sum(1 for p in pos[y] if a1<p<a2)\n            c2 = sum(1 for p in pos[y] if a2<p<a3)\n            if c1!=c2: return False\n    return True\n\ndef count(n):\n    letters = ''.join(chr(97+i) for i in range(n))\n    seen=set()\n    tot=0\n    for p in set(permutations(letters*3)):\n        if valid(p): tot+=1\n    return tot\n\nfor n in (1,2,3,4):\n    print(n, count(n), 2**(n-1)*factorial(n))\nEOF\npython3 -I /tmp/greek/bf.py"
}
� 1 1 1
2 4 4
3 24 24
4 192 192