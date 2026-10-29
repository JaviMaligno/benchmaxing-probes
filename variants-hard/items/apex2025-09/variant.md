# apex2025-09 — variant

**Problem.** Let $S$ be the region in the complex plane enclosed by the curve
$$g(t)=e^{it}+\tfrac{3}{2}e^{2it}+e^{3it}+\tfrac{1}{4}e^{4it},\qquad 0\le t\le 2\pi .$$
Compute the perimeter of $S$.

**Answer.** $\dfrac{40\sqrt{2}}{3}$ (≈ 18.856)

Method (same as original): $g'(t)=i\,w(1+w)^3$ with $w=e^{it}$, so $|g'(t)|=8\cos^3(t/2)$; cusp at $t=\pi$,
self-intersection on the real axis where $\operatorname{Im} g=2\sin t\cos t(1+\cos t)^2=0$, i.e. $t=\pm\pi/2$;
the small loop $t\in[\pi/2,3\pi/2]$ lies inside, so the perimeter is $\int_{-\pi/2}^{\pi/2}8\cos^3(t/2)\,dt=40\sqrt2/3$.
Verified by solve.py (exact sympy + independent numeric boundary/winding check; original reproduces $2\sqrt3+8\pi/3$).
