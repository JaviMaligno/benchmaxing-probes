# Venn-region solver: brute-force over |P| = x, chemistry = 2x.
def solve(total, all3, none, calc, cc, pc, pcal):
    sols = []
    for x in range(0, total + 1):
        chem = 2 * x
        only_pcal = pcal - all3
        only_cc = cc - all3
        only_pc = pc - all3
        only_c = calc - all3 - only_pcal - only_cc
        only_p = x - all3 - only_pcal - only_pc
        only_ch = chem - all3 - only_cc - only_pc
        regions = [only_p, only_ch, only_c, only_pcal, only_cc, only_pc, all3, none]
        if min(regions) < 0:
            continue
        if sum(regions) == total:
            # independent check via inclusion-exclusion
            assert x + chem + calc - pcal - cc - pc + all3 + none == total
            sols.append(x)
    return sols

orig = solve(360, 15, 15, 180, 75, 75, 30)
print("original:", orig)
assert orig == [110]
var = solve(390, 20, 20, 200, 80, 80, 35)
print("variant:", var)
assert len(var) == 1
