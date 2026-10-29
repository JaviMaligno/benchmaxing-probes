## Planteamiento

Como las 12 letras son distintas, las seis palabras tienen **primeras letras distintas**, así que la última palabra en orden alfabético es simplemente la que tiene la primera letra mayor.

Total de emparejamientos: $11!! = 10395$.

## Caso 1: $G$ es la segunda letra

La palabra es $XG$ con $X < G$, y debe ser la última. Entonces $H,I,J,K,L$ (5 letras) deben estar emparejadas con letras menores que $X$. Las letras menores que $G$ son $A,\dots,F$ (6), una de ellas es $X$; las otras 5 deben ser todas menores que $X$, lo que fuerza $X=F$.

Así: pareja $FG$, y $A,B,C,D,E$ emparejadas biyectivamente con $H,I,J,K,L$:
$$5! = 120 \text{ casos}$$

## Caso 2: $G$ es la primera letra

La palabra es $GY$ con $Y>G$, y todas las demás palabras empiezan con letra menor que $G$. Las 4 letras restantes de $\{H,\dots,L\}$ deben emparejarse con letras de $\{A,\dots,F\}$, y las 2 letras pequeñas sobrantes se emparejan entre sí.

- Elegir $Y$: $5$ formas
- Emparejar las 4 letras grandes con 4 de las 6 pequeñas: $\binom{6}{4}\cdot 4! = 15\cdot 24 = 360$
- Las 2 pequeñas restantes: $1$ forma

$$5 \cdot 360 = 1800 \text{ casos}$$

## Resultado

$$P = \frac{120+1800}{10395} = \frac{1920}{10395} = \frac{128}{693}$$

Como $693$ es impar, $\gcd(128,693)=1$, luego $m+n = 128+693 = 821$.

\boxed{821}