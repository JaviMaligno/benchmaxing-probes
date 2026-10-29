## Planteamiento

Sea $O$ el centro de $\Omega$ (radio $123$) y $P$ el centro de $\omega$ (radio $61$). Como $O$ está sobre $\omega$, tenemos $OP = 61$.

Sea la cuerda $AB$ de $\Omega$, que corta a $\omega$ en $X$ e $Y$, con
$$AX = t,\quad XY = 2t,\quad YB = 3t,$$
de modo que la cuerda mide $6t$.

## Coordenadas sobre la cuerda

Pongo una coordenada a lo largo de la recta: $A=0$, $X=t$, $Y=3t$, $B=6t$.

- El pie de la perpendicular desde $O$ es el punto medio de $AB$: coordenada $3t$, con distancia $d_1 = \sqrt{123^2 - 9t^2}$.
- El pie de la perpendicular desde $P$ es el punto medio de $XY$: coordenada $2t$, con distancia $d_2 = \sqrt{61^2 - t^2}$.

Entonces, según si $O$ y $P$ están del mismo lado de la recta o no:
$$OP^2 = 61^2 = t^2 + (d_1 \mp d_2)^2.$$

## Resolución

Con el signo menos (mismo lado):
$$61^2 = t^2 + d_1^2 + d_2^2 - 2d_1 d_2 = t^2 + (123^2 - 9t^2) + (61^2 - t^2) - 2d_1 d_2,$$
lo que da
$$2d_1 d_2 = 123^2 - 9t^2.$$

Elevando al cuadrado:
$$4(123^2 - 9t^2)(61^2 - t^2) = (123^2 - 9t^2)^2.$$

Si $123^2 = 9t^2$, entonces $6t = 2\cdot 123$ y la cuerda sería un diámetro, caso excluido. Por tanto:
$$4(61^2 - t^2) = 123^2 - 9t^2 \;\Longrightarrow\; 5t^2 = 123^2 - 4\cdot 61^2 = 15129 - 14884 = 245,$$
de donde $t^2 = 49$, es decir $t = 7$.

Verificación: $d_2^2 = 61^2 - 49 > 0$ y $d_1^2 = 123^2 - 441 > 0$, así que la configuración existe. (El caso con signo más lleva a $2d_1d_2 = -(123^2-9t^2) < 0$, imposible.)

La cuerda mide $6t = 42$.

$$\boxed{42}$$