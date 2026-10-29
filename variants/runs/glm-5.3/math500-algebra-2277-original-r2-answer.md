Para que exista $f^{-1}$ como función, verificamos que $f$ sea biyectiva:

- En $x\le 3$, $f(x)=3-x$ es estrictamente decreciente y toma valores $y\ge 0$.
- En $x>3$, $f(x)=-x^3+2x^2+3x$ tiene derivada
  \[
  f'(x)=-3x^2+4x+3,
  \]
  que es negativa para $x>3$, y además $f(x)<0$ en esa rama.

Por lo tanto, cada valor tiene exactamente una preimagen.

Para $f^{-1}(0)$:
\[
3-x=0 \implies x=3.
\]
Así, $f^{-1}(0)=3$.

Para $f^{-1}(6)$, como $6>0$, usamos la primera rama:
\[
3-x=6 \implies x=-3.
\]
Así, $f^{-1}(6)=-3$.

Entonces:
\[
f^{-1}(0)+f^{-1}(6)=3+(-3)=0.
\]

\[
\boxed{0}
\]