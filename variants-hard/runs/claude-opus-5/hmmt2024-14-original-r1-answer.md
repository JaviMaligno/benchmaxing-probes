Voy a calcular esto computacionalmente contando caminos hamiltonianos en la retícula 3×n.

```
¡Un momento!
```


■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
▐ Bash
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

{
  "command": "mkdir -p /tmp/snail && cat > /tmp/snail/ham.py <<'EOF'\nimport sys\nsys.setrecursionlimit(100000)\n\ndef count(n):\n    R, C = 3, n\n    N = R*C\n    def idx(i,j): return i*C+j\n    nbrs = [[] for _ in range(N)]\n    for i in range(R):\n        for j in range(C):\n            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):\n                a,b = i+di, j+dj\n                if 0<=a<R and 0<=b<C:\n                    nbrs[idx(i,j)].append(idx(a,b))\n    nmask = [0]*N\n    for v in range(N):\n        m = 0\n        for w in nbrs[v]: m |= 1<<w\n        nmask[v] = m\n    full = (1<<N)-1\n    start = idx(1,0)  # (2,1) -> row index 1, col index 0\n\n    def connected_ok(cur, visited):\n        rem = full & ~visited\n        if rem == 0: return True\n        # flood fill from a neighbour of cur within rem\n        startbits = nmask[cur] & rem\n        if startbits == 0: return False\n        s = startbits & -startbits\n        seen = s\n        stack = [s.bit_length()-1]\n        while stack:\n            v = stack.pop()\n            av = nmask[v] & rem & ~seen\n            while av:\n                b = av & -av\n                av ^= b\n                seen |= b\n                stack.append(b.bit_length()-1)\n        return seen == rem\n\n    total = 0\n    def dfs(cur, visited, cnt):\n        nonlocal total\n        if cnt == N:\n            total += 1\n            return\n        if not connected_ok(cur, visited):\n            return\n        # pruning: count unvisited cells with only one unvisited neighbour (dead ends)\n        rem = full & ~visited\n        dead = 0\n        t = rem\n        while t:\n            b = t & -t\n            t ^= b\n            v = b.bit_length()-1\n            deg = bin(nmask[v] & rem).count('1')\n            adj_cur = 1 if (nmask[v] >> cur) & 1 else 0\n            if deg + adj_cur == 0:\n                return\n            if deg + adj_cur == 1:\n                dead += 1\n                if dead > 1: return\n        av = nmask[cur] & rem\n        while av:\n            b = av & -av\n            av ^= b\n            v = b.bit_length()-1\n            dfs(v, visited | b, cnt+1)\n    dfs(start, 1<<start, 1)\n    return total\n\nfor n in range(1, 13):\n    print(n, count(n))\nEOF\npython3 -I /tmp/snail/ham.py"
}

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

{"stdout":"1 2\n2 4\n3 8\n4 16\n5 32\n6 64\n7 128\n8 256\n9 512\n10 1024\n11 2048\n12 4096\n","success":true}