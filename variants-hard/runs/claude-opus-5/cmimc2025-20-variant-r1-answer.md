
᠎
{"command":"mkdir -p /tmp/pw && cat > /tmp/pw/a.py <<'EOF'\nN = 3**11\npows = []\np = 1\nwhile p <= N:\n    pows.append(p)\n    p *= 3\n\na = [0]*(N+1)\na[0] = 1\nfor m in range(1, N+1):\n    s = 0\n    for q in pows:\n        if q > m: break\n        s += a[m-q]\n    a[m] = s % 3\n\nimport itertools\nrun = 0\nfor k in range(0, 12):\n    S = sum(a[1:3**k+1])\n    print(k, 3**k, S)\nEOF\npython3 -I /tmp/pw/a.py","description":"Compute remainders and partial sums"}

function_results
᠎
0 1 1
1 3 4
2 9 10
3 27 28
4 81 82
5 243 244
6 729 730
7 2187 2188
8 6561 6562
9 19683 19684
10 59049 59050
11 177147 177148