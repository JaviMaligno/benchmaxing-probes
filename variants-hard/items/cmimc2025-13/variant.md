# cmimc2025-13 variant

**Problem.** There are $45$ friends sitting in a circle playing the following game. Every round, five of them are chosen at random and have a dance-off. The winner of the dance-off stays in the circle and the other four leave. This continues until one player remains. Everyone dances equally well, i.e. every person in a dance-off has equal probability of winning it. What is the probability that Priya and Tomas end up dancing in the same round?

**Answer.** $\frac{1}{9}$

(Method: 11 rounds, each containing $\binom{5}{2}=10$ pairs, no pair meets twice, so by symmetry $P = 110/\binom{45}{2} = 1/9$. Verified by exact round-by-round Fraction DP and Monte Carlo in solve.py; same code gives 2/17 on the original 34 players / battles of 4.)
