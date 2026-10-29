def rem(a, e1, b, e2, m):
    # exact big-integer arithmetic plus modular pow cross-check
    exact = (a**e1 + b**e2) % m
    assert exact == (pow(a, e1, m) + pow(b, e2, m)) % m
    return exact

orig = rem(129, 34, 96, 38, 11)
print("original:", orig)
assert orig == 9
var = rem(117, 36, 194, 38, 11)
print("variant:", var)
