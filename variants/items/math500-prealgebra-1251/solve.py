# Brute force: polygon with n sides, interior sum 180(n-2); one omitted angle x must satisfy 0 < x < 180 (convex).
def sides(partial):
    sols = [n for n in range(3, 1000) if 0 < 180*(n-2) - partial < 180]
    assert len(sols) == 1, sols
    return sols[0]

orig = sides(1070)
print("original:", orig)
assert orig == 8
var = sides(1550)
print("variant:", var, "missing angle:", 180*(var-2) - 1550)
