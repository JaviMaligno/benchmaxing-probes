
∧ Bash
 ⎿ {
     "command": "cd /tmp && mkdir -p lk && cd lk && cat > s.py << 'EOF'\nimport sys\nsys.setrecursionlimit(10000)\nN=7\nmoves=[(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]\nbest=[0]\nvis=[[False]*N for _ in range(N)]\nvis[0][0]=True\ndef dfs(r,c,n):\n    if n>best[0]:\n        best[0]=n\n        if n>=43: return True\n    for dr,dc in moves:\n        nr,nc=r+dr,c+dc\n        if 0<=nr<N and 0<=nc<N and not vis[nr][nc]:\n            vis[nr][nc]=True\n            if dfs(nr,nc,n+1): return True\n            vis[nr][nc]=False\n    return False\ndfs(0,0,1)\nprint(best[0])\nEOF\npython3 -I s.py",
     "description": "Buscar camino maximo del lame king"
   }

 ⎿ 43