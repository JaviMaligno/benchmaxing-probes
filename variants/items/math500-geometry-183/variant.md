# math500-geometry-183 — variant

A hexagon is inscribed in a circle:

[asy]
pair pA, pB, pC, pD, pE, pF, pO;
pO = (0, 0);
pA = pO + dir(-10);
pB = pO + dir(55);
pC = pO + dir(120);
pD = pO + dir(175);
pE = pO + dir(-120);
pF = pO + dir(-60);
draw(pA--pB--pC--pD--pE--pF--pA);
label("$125^\circ$", pF, N * 2);
label("$115^\circ$", pB, SW * 1.5);
label("$\theta$", pD, E);
draw(circle(pO, 1));
[/asy]

The interior angle of the hexagon at the vertex marked $115^\circ$ is $115^\circ$, the interior angle at the vertex marked $125^\circ$ is $125^\circ$, and these two vertices are separated by one vertex on each side from the vertex marked $\theta$ (the hexagon is $ABCDEF$ with $\angle ABC = 115^\circ$, $\angle EFA = 125^\circ$, $\angle CDE = \theta$). What is the measure of $\theta$, in degrees?

**Answer:** $120^\circ$
