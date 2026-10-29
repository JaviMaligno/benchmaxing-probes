# Sum of all odd digit occurrences among positive multiples of m below N.
def odd_digit_sum(m, N):
    return sum(int(c) for k in range(m, N, m) for c in str(k) if int(c) % 2)

orig = odd_digit_sum(77, 1_000_000)
print("original (m=77):", orig)
assert orig == 194832
var = odd_digit_sum(91, 1_000_000)
print("variant (m=91):", var)
