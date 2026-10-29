## Planteamiento

Sean $A=\arccos x$, $B=\arccos 2x$, $C=\arccos 4x$. De $A+B+C=\pi$ se sigue $A+B=\pi-C$, luego

$$\cos(A+B)=-\cos C=-4x.$$

## Desarrollo

$$\cos A\cos B-\sin A\sin B=-4x$$
$$2x^2-\sqrt{1-x^2}\sqrt{1-4x^2}=-4x$$
$$\sqrt{1-x^2}\sqrt{1-4x^2}=2x^2+4x$$

Elevando al cuadrado:

$$(1-x^2)(1-4x^2)=4x^4+16x^3+16x^2$$
$$4x^4-5x^2+1=4x^4+16x^3+16x^2$$
$$0=16x^3+21x^2-1$$

El polinomio $16x^3+21x^2-1$ no tiene raíces racionales (los candidatos $\pm 1,\pm\tfrac12,\pm\tfrac14,\pm\tfrac18,\pm\tfrac1{16}$ fallan), así que es irreducible sobre $\mathbb{Q}$ y cualquier cúbica entera con esta raíz es un múltiplo entero de él. El mínimo se alcanza con los coeficientes $a=16$, $b=21$, $c=0$, $d=-1$:

$$|a|+|b|+|c|+|d|=16+21+0+1=38.$$

\boxed{38}