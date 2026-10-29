# hmmt2025-30 — variant

**Problem.** A plane $\mathcal{Q}$ cuts a rectangular box, and the cross-section is a hexagon whose side lengths, in order around the hexagon, are $44, 60, 54, 52, 50$, and $66$. Find the distance from the center of the box to $\mathcal{Q}$.

**Answer.** $\sqrt{\tfrac{27}{14}} = \tfrac{3\sqrt{42}}{14} \approx 1.38873$

(Original: sides 45, 66, 63, 55, 54, 77; answer $\sqrt{95/24}$.) Verified by `solve.py`: exact closed form, forward construction of a box and plane realising these sides, and a numeric inverse solve that finds a single distance.
