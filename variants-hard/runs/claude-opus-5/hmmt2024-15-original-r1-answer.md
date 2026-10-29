
≈
{
  "command": "cd /tmp && cat > count_graphs.py <<'EOF'\nfrom itertools import combinations\n\nn = 8\nverts = range(n)\nedges = list(combinations(verts, 2))\n\ncount = 0\nfound = {}\n\ndef ok(adj):\n    for u, v in combinations(verts, 2):\n        c = bin(adj[u] & adj[v]).count('1')\n        if c not in (0, 2):\n            return False\n    return True\n\n# busqueda recursiva: completar vecindades grado 3\ndef search(v, adj, deg):\n    global count\n    if v == n:\n        if ok(adj):\n            count += 1\n        return\n    need = 3 - deg[v]\n    if need < 0:\n        return\n    cand = [u for u in range(v+1, n) if deg[u] < 3]\n    if len(cand) < need:\n        return\n    for extra in combinations(cand, need):\n        for u in extra:\n            adj[v] |= 1 << u; adj[u] |= 1 << v\n            deg[v] += 1; deg[u] += 1\n        search(v+1, adj, deg)\n        for u in extra:\n            adj[v] &= ~(1 << u); adj[u] &= ~(1 << v)\n            deg[v] -= 1; deg[u] -= 1\n\nsearch(0, [0]*n, [0]*n)\nprint(count)\nEOF\npython3 -I count_graphs.py"
}


≈
875