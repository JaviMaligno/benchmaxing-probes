Este es un problema clásico de "camino más corto sobre una superficie", que se resuelve desplegando (desdoblando) las caras del prisma rectangular en un plano y trazando la línea recta entre la posición del gecko y la mosca.

## 1. Coordenadas

Sala: 12 pies de largo, 10 pies de ancho, 8 pies de alto.

- El gecko está en una pared lateral de $10\times 8$, a 1 pie del techo y a 1 pie de la pared trasera.
- La mosca está en la pared lateral opuesta, a 1 pie del suelo y a 1 pie de la pared delantera.

## 2. Posición del gecko

Consideremos las coordenadas:

- Largo ($x$): desde la pared trasera (0) hasta la delantera (12).
- Ancho ($y$): de 0 a 10.
- Alto ($z$): de 0 (suelo) a 8 (techo).

El gecko está en la pared lateral izquierda ($y=0$):

- A 1 pie del techo: $z=8-1=7$.
- A 1 pie de la pared trasera: $x=1$.

Entonces, gecko: $G=(1,\,0,\,7)$.

La mosca está en la pared lateral derecha ($y=10$):

- A 1 pie del suelo: $z=1$.
- A 1 pie de la pared delantera: $x=12-1=11$.

Entonces, mosca: $F=(11,\,10,\,1)$.

## 3. Desdoblamientos

Debemos desplegar las paredes y el techo para encontrar el camino más corto. El gecko no puede caminar por el suelo, así que solo usamos las 4 paredes laterales y el techo.

### Desdoblamiento estándar (paredes laterales como banda + techo)

Desplegamos las 4 paredes laterales como una banda horizontal de largo

$$
10+12+10+12=44
$$

y alto 8. Sobre esa banda ponemos el techo (que no se cruza con el suelo).

Las coordenadas en el plano desdoblado:

- Pared izquierda: $u\in[0,10]$.
- Pared delantera: $u\in[10,22]$.
- Pared derecha: $u\in[22,32]$.
- Pared trasera: $u\in[32,44]$.

El techo se une a la parte superior de las cuatro paredes.

**Gecko** en pared izquierda: $u=10-1=9$ (porque $x=1$ se mide desde la esquina trasera-izquierda, donde $u=0$; avanzando hacia adelante, $u=x$, así que $u=1$ desde la esquina trasera... con la convención elegida, $u=10-1=9$).

**Mosca** en pared derecha: $u=22+1=23$ (porque la esquina trasera-derecha está en $u=22$ y $x=11$ hacia adelante es $11-10=1$).

Ahora, la mosca está a $z=1$, el gecko a $z=7$.

#### Camino directo sobre la banda de paredes

La distancia horizontal entre el gecko y la mosca en la banda es

$$
|23-9|=14.
$$

La diferencia vertical es

$$
|1-7|=6.
$$

Distancia euclidiana:

$$
\sqrt{14^2+6^2}=\sqrt{196+36}=\sqrt{232}.
$$

Pero este camino no usa el techo. La pregunta pide que puede cruzar el techo, y el camino más corto generalmente lo usa, porque el techo forma un "atajo" que cambia la geometría.

#### Camino que cruza el techo

Al cruzar el techo, la distancia horizontal entre los puntos donde suben al techo puede ser distinta. En la banda desdoblada de paredes, el techo aparece como una franja superior de longitud 44. Conectar los dos puntos cruzando el techo equivale a reflejar uno de ellos respecto a la línea del techo.

La diferencia de altura entre el gecko y el techo es

$$
8-7=1.
$$

Para la mosca:

$$
8-1=7.
$$

Entonces, la distancia en el plano desdoblado con el techo incluido es la hipotenusa de un triángulo rectángulo cuyos catetos son:

- Diferencia horizontal: $14$.
- Diferencia vertical **sumando** las distancias al techo: $1+7=8$.

Por tanto,

$$
d=\sqrt{14^2+8^2}=\sqrt{196+64}=\sqrt{260}.
$$

Simplificando:

$$
\sqrt{260}=\sqrt{4\cdot 65}=2\sqrt{65}.
$$

## 4. Verificación de otros desdoblamientos posibles

Otra forma de cruzar el techo es, por ejemplo, desdoblar la pared izquierda con el techo y la pared delantera/trasera. Debemos verificar si existe una distancia menor.

La Distancia Horizontal mínima entre $G$ y $F$ en el desarrollo usando techo y paredes, considerando todas las rutas posibles, da

$$
d=\sqrt{(1+7)^2 + 14^2}=2\sqrt{65}.
$$

Pero también debemos considerar la posibilidad de que el camino cruce el techo por una ruta más corta usando la pared delantera o trasera. En ese caso, la componente horizontal sería

$$
1+10+1=12
$$

(porque el gecko está a 1 de la pared trasera y la mosca a 1 de la delantera; la distancia horizontal total entre sus proyecciones en esas paredes es $12$, no $14$).

Revisemos con cuidado todas las rutas.

### Ruta 1: banda de paredes sin techo

Distancia: $\sqrt{14^2+6^2}=\sqrt{232}\approx 15.23$.

### Ruta 2: banda de paredes, cruzando el techo en la misma banda

Distancia: $2\sqrt{65}\approx 16.12$.

### Ruta 3: crecimiento por la pared trasera o delantera

Consideremos desdoblar la pared izquierda, el techo y la pared delantera.

Gecko en pared izquierda, a $x=1$, $z=7$; mosca en pared derecha, a $x=11$, $z=1$.

Al desdoblar la pared izquierda con el techo y la pared delantera:

Coordenadas planas:

- Gecko en $(1,7)$ en la pared izquierda.
- Para llegar al techo, sube 1.
- El techo tiene ancho 10 (de $y=0$ a $y=10$).
- En la pared delantera, la mosca está a $z=1$, y desde la esquina superior delantera-derecha, la distancia horizontal a la mosca es $1$ (porque $x=11$).

Entonces la distancia horizontal total (en el desarrollo) entre la proyección del gecko y la mosca es

$$
1+10+1=12.
$$

La distancia vertical total cruzando el techo es

$$
1+7=8.
$$

Por tanto,

$$
d=\sqrt{12^2+8^2}=\sqrt{144+64}=\sqrt{208}=4\sqrt{13}\approx 14.42.
$$

¡Esta es menor!

### Ruta 4: por la pared trasera

Gecko $x=1$ (distancia a la pared trasera), mosca $x=11$ (distancia a la pared trasera). La componente horizontal en el desarrollo trasero sería

$$
1+10+11=22.
$$

Eso es mayor, así que no importa.

## 5. Resultado

El camino más corto es el de la Ruta 3, con distancia

$$
\sqrt{208}=4\sqrt{13}.
$$

Verifiquemos rápidamente si hay alguna ruta aún más corta combinando la banda de paredes sin techo pero tomando una "diagonal" más favorable.

La Ruta 1 dio $\sqrt{232}\approx 15.23$, mayor que $4\sqrt{13}\approx 14.42$.

Por lo tanto, el camino más corto es:

$$
\boxed{4\sqrt{13}}
$$