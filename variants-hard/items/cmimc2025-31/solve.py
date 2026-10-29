# Brute force: a day (m, d) is good if m | concat(m,d) and d | concat(m,d).
DAYS = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def good(m, d):
    c = int(f"{m}{d}")
    return c % m == 0 and c % d == 0

def count(months):
    return [(m, d) for m in months for d in range(1, DAYS[m] + 1) if good(m, d)]

# sanity checks from statement
assert good(3, 15) and not good(3, 9)
orig = count([3, 4, 5])
print("original (Mar, Apr, May):", len(orig))
assert len(orig) == 13
var = count([6, 7, 8])
print("variant days:", var)
print("variant (Jun, Jul, Aug):", len(var))
