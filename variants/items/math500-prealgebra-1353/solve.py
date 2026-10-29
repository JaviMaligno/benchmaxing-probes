# Brute force: count x with x*y = N, x >= xmin, y >= ymin (positive integers)
def count(N, xmin, ymin):
    return sum(1 for x in range(1, N + 1) if N % x == 0 and x >= xmin and N // x >= ymin)

orig = count(54, 2, 5)
print("original:", orig)
assert orig == 4
var = count(48, 3, 4)
print("variant:", var, [x for x in range(1, 49) if 48 % x == 0 and x >= 3 and 48 // x >= 4])
