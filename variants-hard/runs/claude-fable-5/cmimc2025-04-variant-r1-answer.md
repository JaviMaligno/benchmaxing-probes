Planteo con las sustituciones $a=\log_x y$, $b=\log_y z$, $c=\log_z x$, que cumplen la identidad $abc=1$.

**Traducción de las tres condiciones:**

1. $a+b+c=10$, y como $c=\dfrac{1}{ab}$, esto es $a+b+\dfrac{1}{ab}=10$.
2. $\log_y x=\dfrac{1}{a}$, así que $\log_{1/a} z=-3$ significa $z=\left(\dfrac{1}{a}\right)^{-3}=a^3$.
3. $\log_z y=\dfrac{1}{b}$ y $\log_x z=\log_x y\cdot\log_y z=ab$, así que $\dfrac{1}{b}+ab=25$.

**Resolución del sistema en $a,b$:**

De la ecuación 3, multiplicando por $b$: $ab^2=25b-1$, es decir $a=\dfrac{25b-1}{b^2}$ y $ab=\dfrac{25b-1}{b}$.

Sustituyendo en la ecuación 1:
$$\frac{25b-1}{b^2}+b+\frac{b}{25b-1}=10.$$

Multiplicando por $b^2(25b-1)$ y expandiendo:
$$25b^4-250b^3+635b^2-50b+1=0,$$
que factoriza perfectamente como
$$(5b^2-25b+1)^2=0.$$

Por tanto $5b^2=25b-1$, lo que da directamente
$$a=\frac{25b-1}{b^2}=\frac{5b^2}{b^2}=5.$$

**Verificación:** con $a=5$ y $5b^2-25b+1=0$ (raíces positivas, válidas): $b+\dfrac{1}{5b}=\dfrac{5b^2+1}{5b}=\dfrac{25b}{5b}=5$, así que $a+b+c=5+5=10$ ✓; y $\dfrac{1}{b}+5b=\dfrac{1+5b^2}{b}=\dfrac{25b}{b}=25$ ✓.

Finalmente, de la condición 2:
$$z=a^3=5^3=125.$$

$$\boxed{125}$$