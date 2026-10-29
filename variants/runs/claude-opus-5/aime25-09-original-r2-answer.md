## Planteamiento

Sea $Q=(x,y)$ el punto de intersección en el cuarto cuadrante. Como $Q$ está en la parábola original, $y=x^2-4$. Y como $Q$ también está en la imagen rotada, su **preimagen** (girar $Q$ en $-60^\circ$) debe estar sobre la parábola original.

Rotando $-60^\circ$:
$$x'=\tfrac{x}{2}+\tfrac{\sqrt3}{2}y,\qquad y'=-\tfrac{\sqrt3}{2}x+\tfrac{y}{2}$$

La condición es $y'=x'^2-4$:
$$-\tfrac{\sqrt3}{2}x+\tfrac{y}{2}=\left(\tfrac{x}{2}+\tfrac{\sqrt3}{2}y\right)^2-4$$

## Reducción

Desarrollando y usando $x^2=y+4$:
$$-\tfrac{\sqrt3}{2}x+\tfrac{y}{2}=\tfrac{y+4}{4}+\tfrac{\sqrt3}{2}xy+\tfrac34 y^2-4$$

Multiplicando por $4$ y agrupando:
$$-2\sqrt3\,x(1+y)=3y^2-y-12$$

Elevando al cuadrado con $x^2=y+4$:
$$12(y+4)(1+y)^2=(3y^2-y-12)^2$$
$$9y^4-18y^3-143y^2-84y+96=0$$

Esta cuártica factoriza como:
$$(y^2-3y-12)(9y^2+9y-8)=0$$

## Selección de la raíz

- $9y^2+9y-8=0$ da $y=\frac{-3-\sqrt{41}}{6}\approx-1.567$, que cumple la ecuación **con el signo opuesto** de $x$ (raíz extraña, corresponde al punto cuya imagen es la intersección, no a la intersección).
- $y^2-3y-12=0$ da $y=\frac{3-\sqrt{57}}{2}\approx-2.2749$, con $x=\sqrt{y+4}\approx1.3134>0$: está en el cuarto cuadrante y verifica $-2\sqrt3\,x(1+y)=3y^2-y-12$ (ambos lados positivos).

Comprobación: la preimagen es $(-1.3134,\,-2.2749)$, y en efecto $(-1.3134)^2-4=-2.2749$. ✓

Así $a=3$, $b=57$, $c=2$, con $\gcd(3,2)=1$, de donde $a+b+c=62$.

\boxed{62}