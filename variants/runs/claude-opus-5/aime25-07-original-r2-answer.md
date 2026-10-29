## Planteamiento

Como las doce letras son distintas, las seis palabras tienen **primeras letras distintas**. Por tanto, la última palabra en orden alfabético es simplemente la que tiene la mayor primera letra. La condición pedida es: *la palabra que contiene a $G$ tiene la primera letra más grande*.

Total de emparejamientos: $11!! = 10395$.

## Caso 1: $G$ es la segunda letra (palabra $XG$ con $X<G$)

La primera letra es $X \in \{A,\dots,F\}$. Entonces $H,I,J,K,L$ (todas mayores que $X$) deben ser segundas letras, es decir, cada una emparejada con una letra menor. Las letras menores disponibles son las de $\{A,\dots,F\}\setminus\{X\}$, que son exactamente 5: encajan justo con $H,I,J,K,L$.

Luego las seis primeras letras son precisamente $A,B,C,D,E,F$, y para que $X$ sea la mayor hace falta $X=F$.

Fijado el par $FG$, hay $5!=120$ formas de emparejar $A,B,C,D,E$ con $H,I,J,K,L$.

$$\text{Caso 1} = 120$$

## Caso 2: $G$ es la primera letra (palabra $GX$ con $X>G$)

Hay 5 opciones para $X \in \{H,I,J,K,L\}$. Las 4 letras grandes restantes deben ser segundas letras, cada una emparejada con una letra de $\{A,\dots,F\}$: hay $6\cdot5\cdot4\cdot3 = 360$ inyecciones. Las 2 letras pequeñas sobrantes se emparejan entre sí (1 forma).

$$\text{Caso 2} = 5 \cdot 360 = 1800$$

## Resultado

$$P = \frac{120+1800}{10395} = \frac{1920}{10395} = \frac{128}{693}$$

Con $\gcd(128,693)=1$ (pues $128=2^7$ y $693=3^2\cdot7\cdot11$), se obtiene $m+n = 128+693$.

\boxed{821}