from itertools import product

def count(hair, brows, eyes, ears, lips, shoes):
    # hair optional: index -1 = bald; each other feature exactly one complete set
    opts = [list(range(-1, hair)), range(brows), range(eyes), range(ears), range(lips), range(shoes)]
    return sum(1 for _ in product(*opts))

orig = count(hair=3, brows=2, eyes=1, ears=2, lips=2, shoes=2)
print("original:", orig)
assert orig == 64
var = count(hair=4, brows=3, eyes=1, ears=2, lips=2, shoes=2)
print("variant:", var)
