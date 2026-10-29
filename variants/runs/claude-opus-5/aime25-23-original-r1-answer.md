
᠎{"command":"python3 -I -c \"\nres=0\nfails=[]\nfor N in range(1,1001):\n    q=N//25; r=N%25; g=q+r//10+r%10\n    best=min(a+ (N-25*a)//10 + (N-25*a)%10 for a in range(N//25+1))\n    if g==best: res+=1\n    else: fails.append(N)\nprint(res, len(fails), fails[:20])\n\"","description":"Contar N donde greedy es óptimo"}
᠎

Node use interrupted · Nodes do not run without permission