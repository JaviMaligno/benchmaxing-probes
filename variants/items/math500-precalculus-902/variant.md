# math500-precalculus-902 — variant

**Problem.** A point $Q$ lies at distances 4, 8, 10, 11, and 13 from five of the six vertices of a regular octahedron. What is the distance from $Q$ to the remaining vertex?

**Answer.** $\sqrt{85}$

(Method: opposite vertices have equal sums of squared distances; $4^2+13^2 = 8^2+11^2 = 185$ is the only repeated pair sum, so the sixth distance is $\sqrt{185-10^2}=\sqrt{85}$. The configuration is realizable — solve.py constructs $Q$ and the octahedron explicitly.)
