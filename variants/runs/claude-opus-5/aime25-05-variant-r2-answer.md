
﹛"command": "python3 -I -c \"\nfrom itertools import permutations\nc=sum(1 for p in permutations('123456789') if int(''.join(p))%22==0)\nprint(c, c-14025)\n\"",
  "description": "Verificar por fuerza bruta el conteo"﹜

function_results{"stdout":"14400 375\n","is_error":false}