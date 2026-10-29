

Sea

\[
a=\log_x y,\qquad b=\log_y z.
\]

Entonces

\[
\log_y x=\frac1a,
\]

por lo que la segunda ecuación da

\[
\log_{1/a} z=-3 \implies z=\left(\frac1a\right)^{-3}=a^3.
\]

Así que basta encontrar \(a\).

Como

\[
\log_x z=\log_x y\cdot \log_y z=ab,
\qquad
\log_z y=\frac1b,
\qquad
\log_z x=\frac1{ab},
\]

la tercera ecuación es

\[
\frac1b+ab=16.
\]

La primera ecuación es

\[
a+b+\frac1{ab}=8.
\]

Sea \(u=ab\). De la tercera ecuación,

\[
\frac1b=16-u \implies b=\frac1{16-u}.
\]

Como \(u=ab\),

\[
a=\frac{u}{b}=u(16-u).
\]

Sustituyendo en la primera ecuación:

\[
u(16-u)+\frac1{16-u}+\frac1u=8.
\]

Multiplicando por \(u(16-u)\):

\[
u^2(16-u)^2+u+(16-u)=8u(16-u).
\]

Sea \(w=u(16-u)\). Entonces

\[
w^2+16=8w,
\]

\[
w^2-8w+16=0,
\]

\[
(w-4)^2=0 \implies w=4.
\]

Por tanto,

\[
a=u(16-u)=4.
\]

Finalmente,

\[
z=a^3=4^3=64.
\]

\[
\boxed{64}
\]