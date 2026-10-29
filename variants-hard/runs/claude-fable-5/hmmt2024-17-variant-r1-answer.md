Voy a resolver este problema de percolación en una escalera 2×∞ con un argumento de matriz de transferencia, y luego verificaré el resultado con una simulación rápida.

**Planteamiento.** Las puertas horizontales están abiertas con probabilidad 1/2 y las verticales con probabilidad 3/4. Proceso columna por columna. Tras procesar la columna $n$, el estado de la frontera (conectividad de las dos celdas de la columna $n$ con la fuente usando solo aristas de las columnas $\le n$) es:

- **A**: ambas celdas conectadas; **T**: solo la de arriba; **B**: solo la de abajo; **D**: ninguna (muerto, nada más a la derecha es alcanzable).

Sutileza clave: en estado T, la celda inferior tiene un "clúster colgante" a la izquierda que puede rescatarse más adelante mediante un lazo por la derecha (abajo→derecha→arriba por la vertical de la columna $n{+}1$). Hay que llevar el tamaño esperado de ese clúster.

Transiciones (con $h_t,h_b$ abiertas con prob. 1/2 y $v$ con 3/4):
- Desde A: →A con 5/8 (+2 celdas), →T con 1/16 (+1, clúster nuevo de peso 1), →B con 1/16 (+1, peso 1), →D con 1/4.
- Desde T: si $h_t,v,h_b$ (3/16) →A, +2 y **se rescata el clúster** $w$; si $h_t,v,\neg h_b$ (3/16) →A, +2, clúster perdido; si $h_t,\neg v,h_b$ (1/16) →T, +1, $w{\to}w{+}1$; si $h_t,\neg v,\neg h_b$ (1/16) →T, +1, $w{\to}1$; si $\neg h_t$ (1/2) →D. (B es simétrico.)

Con $a_n, s_n = t_n+b_n$, $W_n$ = peso colgante esperado, y condiciones iniciales $a_1=3/4$, $s_1=1/4$, $W_1=1/4$, $C_1=7/4$:

$$a_{n+1}=\tfrac58 a_n+\tfrac38 s_n,\quad s_{n+1}=\tfrac18(a_n+s_n),\quad W_{n+1}=\tfrac18(a_n+s_n)+\tfrac1{16}W_n$$

Sumando las series: $A=\sum a_n=8/3$, $S=\sum s_n=2/3$, $W=\sum W_n=32/45$. El total esperado es

$$E = \tfrac74 + \tfrac{11}8 A + \tfrac78 S + \tfrac3{16}W = \tfrac74+\tfrac{11}3+\tfrac7{12}+\tfrac2{15}=\tfrac{368}{60}=\tfrac{92}{15}\approx 6.1333.$$

Verifico con una simulación Monte Carlo:


{
  "command": "cd /tmp && python3 -I -c \"\nimport random\nrandom.seed(1)\nN=60  # columnas (la probabilidad de llegar tan lejos es despreciable)\ntrials=400000\ntot=0\nfor _ in range(trials):\n    ht=[random.random()<0.5 for _ in range(N-1)]\n    hb=[random.random()<0.5 for _ in range(N-1)]\n    vv=[random.random()<0.75 for _ in range(N)]\n    # BFS desde (0,0): celdas (fila,col), fila 0=arriba\n    from collections import deque\n    seen={(0,0)}\n    q=deque([(0,0)])\n    while q:\n        r,c=q.popleft()\n        # vertical\n        if vv[c] and (1-r,c) not in seen:\n            seen.add((1-r,c)); q.append((1-r,c))\n        h = ht if r==0 else hb\n        if c+1<N and h[c] and (r,c+1) not in seen:\n            seen.add((r,c+1)); q.append((r,c+1))\n        if c-1>=0 and h[c-1] and (r,c-1) not in seen:\n            seen.add((r,c-1)); q.append((r,c-1))\n    tot+=len(seen)\nprint(tot/trials, 92/15)\n\"",
  "description": "Simulación Monte Carlo del problema de percolación"
}


{
  "command": "cd /tmp && python3 -I -c \"\nimport random\nfrom collections import deque\nrandom.seed(1)\nN=60\ntrials=400000\ntot=0\nfor _ in range(trials):\n    ht=[random.random()<0.5 for _ in range(N-1)]\n    hb=[random.random()<0.5 for _ in range(N-1)]\n    vv=[random.random()<0.75 for _ in range(N)]\n    seen={(0,0)}\n    q=deque([(0,0)])\n    while q:\n        r,c=q.popleft()\n        if vv[c] and (1-r,c) not in seen:\n            seen.add((1-r,c)); q.append((1-r,c))\n        h = ht if r==0 else hb\n        if c+1<N and h[c] and (r,c+1) not in seen:\n            seen.add((r,c+1)); q.append((r,c+1))\n        if c-1>=0 and h[c-1] and (r,c-1) not in seen:\n            seen.add((r,c-1)); q.append((r,c-1))\n    tot+=len(seen)\nprint('simulado:', tot/trials, ' teorico:', 92/15)\n\"",
  "description": "Simulación Monte Carlo del problema de percolación"
}


{
  "command": "python3 -I -c \"\nimport random\nfrom collections import deque\nrandom.seed(1)\nN=60\ntrials=400000\ntot=0\nfor _ in range(trials):\n    ht=[random.random()<0.5 for _ in range(N-1)]\n    hb=[random.random()<0.5 for _ in range(N-1)]\n    vv=[random.random()<0.75 for _ in range(N)]\n    seen={(0,0)}\n    q=deque([(0,0)])\n    while q:\n        r,c=q.popleft()\n        if vv[c] and (1-r,c) not in seen:\n            seen.add((1-r,c)); q.append((1-r,c))\n        h = ht if r==0 else hb\n        if c+1<N and h[c] and (r,c+1) not in seen:\n            seen.add((r,c+1)); q.append((r,c+1))\n        if c-1>=0 and h[c-1] and (r,c-1) not in seen:\n            seen.add((r,c-1)); q.append((r,c-1))\n    tot+=len(seen)\nprint('simulado:', tot/trials, ' teorico:', 92/15)\n\" 2>&1",
  "description": "Simulación Monte Carlo (reintento)"
}


{
  "command": "cat > /tmp/sim_hallway.py <<'EOF'\nimport random\nfrom collections import deque\nrandom.seed(1)\nN = 60\ntrials = 400000\ntot = 0\nfor _ in range(trials):\n    ht = [random.random() < 0.5 for _ in range(N - 1)]\n    hb = [random.random() < 0.5 for _ in range(N - 1)]\n    vv = [random.random() < 0.75 for _ in range(N)]\n    seen = {(0, 0)}\n    q = deque([(0, 0)])\n    while q:\n        r, c = q.popleft()\n        if vv[c] and (1 - r, c) not in seen:\n            seen.add((1 - r, c)); q.append((1 - r, c))\n        h = ht if r == 0 else hb\n        if c + 1 < N and h[c] and (r, c + 1) not in seen:\n            seen.add((r, c + 1)); q.append((r, c + 1))\n        if c - 1 >= 0 and h[c - 1] and (r, c - 1) not in seen:\n            seen.add((r, c - 1)); q.append((r, c - 1))\n    tot += len(seen)\nprint('simulado:', tot / trials, ' teorico:', 92 / 15)\nEOF\npython3 -I /tmp/sim_hallway.py",
  "description": "Simulación Monte Carlo vía archivo"
}


{
  "exitCode": 0,
  "stdout": "simulado: 6.1334025  teorico: 6.133333333333334",
  "stderr": ""
}La simulación con 400 000 muestras da **6.1334**, que coincide con el valor teórico $92/15 \approx 6.1333$.

**Resumen de la solución.** Modelé el pasillo como percolación en una escalera 2×∞ (aristas horizontales abiertas con probabilidad 1/2, verticales con 3/4) y lo procesé columna por columna con estados de frontera: ambas celdas conectadas a Mira (A), solo la de arriba (T), solo la de abajo (B), o ninguna (D, absorbente). El punto delicado es que en los estados T/B la celda desconectada arrastra un "clúster colgante" que puede rescatarse mediante un lazo por la derecha (ocurre con probabilidad 3/16 en cada paso), así que llevé también su tamaño esperado $W_n$. Sumando las series de las recurrencias lineales: $\sum a_n = 8/3$, $\sum s_n = 2/3$, $\sum W_n = 32/45$, y el conteo esperado total resulta

$$E = \frac74 + \frac{11}{8}\cdot\frac83 + \frac78\cdot\frac23 + \frac3{16}\cdot\frac{32}{45} = \frac{92}{15}.$$

$$\boxed{\dfrac{92}{15}}$$