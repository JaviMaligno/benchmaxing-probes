# Brute force: n bags of b coins each, find a bag of `found` coins, redistribute evenly
# among n+1 bags, total > threshold. Smallest original total n*b.
def solve(n, found, threshold):
    b = 1
    while True:
        total = n*b + found
        if total > threshold and total % (n+1) == 0:
            return n*b
        b += 1

orig = solve(7, 53, 200)
print("original:", orig)
assert orig == 203
var = solve(9, 47, 300)
print("variant:", var)
