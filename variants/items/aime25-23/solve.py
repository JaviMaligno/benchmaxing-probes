# Brute force: greedy coin count vs optimal (DP) coin count.
def count_success(coins, M):
    coins = sorted(coins)
    INF = 10**9
    opt = [0] + [INF] * M
    for n in range(1, M + 1):
        opt[n] = min(opt[n - c] + 1 for c in coins if c <= n)
    succ = 0
    for n in range(1, M + 1):
        r, g = n, 0
        for c in reversed(coins):
            g += r // c
            r %= c
        succ += (g == opt[n])
    return succ

orig = count_success([1, 10, 25], 1000)
print("original (1,10,25; N<=1000):", orig)
assert orig == 610
var = count_success([1, 10, 24], 1000)
print("variant (1,10,24; N<=1000):", var)
