Las dos rectas son paralelas porque sus vectores directores son proporcionales: $(2,-9,-2)$ y $(4,-18,-4)=2(2,-9,-2)$.

Para hallar la distancia entre dos rectas paralelas, tomamos un punto de cada una:

- $P_1 = (3,-10,1)$ está en la primera recta.
- $P_2 = (-5,-3,6)$ está en la segunda recta.

La distancia entre rectas paralelas se calcula como:

\[
d=\frac{\|\overrightarrow{P_1P_2}\times \mathbf{v}\|}{\|\mathbf{v}\|},
\]

donde $\mathbf{v}=(2,-9,-2)$ es el vector director de las rectas.

Primero calculamos:

\[
\overrightarrow{P_1P_2}=P_2-P_1=(-5-3,\,-3-(-10),\,6-1)=(-8,\,7,\,5).
\]

Ahora el producto cruz:

\[
\overrightarrow{P_1P_2}\times \mathbf{v}
=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k}\\
-8 & 7 & 5\\
2 & -9 & -2
\end{vmatrix}.
\]

Calculamos las componentes:

- Componente $\mathbf{i}$:

\[
7(-2)-5(-9)=-14+45=31.
\]

- Componente $\mathbf{j}$ (con signo negativo):

\[
-\left[(-8)(-2)-5(2)\right]=-\left[16-10\right]=-6.
\]

- Componente $\mathbf{k}$:

\[
(-8)(-9)-7(2)=72-14=58.
\]

Por lo tanto,

\[
\overrightarrow{P_1P_2}\times \mathbf{v}=(31,-6,58).
\]

Su norma es:

\[
\|(31,-6,58)\|=\sqrt{31^2+(-6)^2+58^2}
=\sqrt{961+36+3364}
=\sqrt{4361}.
\]

Y la norma de $\mathbf{v}$ es:

\[
\|(2,-9,-2)\|=\sqrt{2^2+(-9)^2+(-2)^2}
=\sqrt{4+81+4}
=\sqrt{89}.
\]

Entonces la distancia es:

\[
d=\frac{\sqrt{4361}}{\sqrt{89}}
=\sqrt{\frac{4361}{89}}.
\]

Como $4361=89\cdot 49$, tenemos:

\[
\frac{4361}{89}=49.
\]

Por lo tanto,

\[
d=\sqrt{49}=7.
\]

\[
\boxed{7}
\]