Vamos a resolverlo.

Tenemos una cuadrícula de $3 \times 3$ de nenúfares. Kelvin está en la esquina inferior izquierda (posición $(3,1)$, si etiquetamos filas de arriba hacia abajo y columnas de izquierda a derecha), y su casa está en la celda central de la fila superior, es decir, la posición $(1,2)$.

Debemos quitar 4 nenúfares de los 7 restantes (ya que la casilla de inicio y la de la casa deben permanecer), de modo que Kelvin **no** pueda llegar a su casa usando saltos horizontales o verticales entre nenúfares que no hayan sido quitados.

Hay 9 casillas en total. Se mantienen la casilla de inicio $(3,1)$ y la casa $(1,2)$. Las otras 7 casillas son:

- $(1,1)$
- $(1,3)$
- $(2,1)$
- $(2,2)$
- $(2,3)$
- $(3,2)$
- $(3,3)$

Debemos elegir 4 de estas 7 para eliminar, es decir, mantener 3 de ellas además de las 2 fijas.

Queremos contar las selecciones en las que $(3,1)$ y $(1,2)$ quedan en componentes conexas distintas del grafo de la cuadrícula (considerando solo los nenúfares que permanecen).

Una forma de pensar: el grafo completo de la cuadrícula $3\times 3$ es:

```
(1,1) -- (1,2) -- (1,3)
  |       |        |
(2,1) -- (2,2) -- (2,3)
  |       |        |
(3,1) -- (3,2) -- (3,3)
```

Queremos que no exista camino entre $(3,1)$ y $(1,2)$.

Contemos el total de selecciones y restemos las que permiten el camino.

**Total de selecciones:**

Elegir 4 de las 7 casillas libres para quitar equivale a elegir las 3 que se mantienen además de las 2 fijas. Total:

$$
\binom{7}{4} = \binom{7}{3} = 35.
$$

**Selecciones que permiten el camino (casos malos):**

Para que sí exista camino entre $(3,1)$ y $(1,2)$, debe haber al menos un camino de casillas adyacentes que permanezcan.

Un camino posible desde $(3,1)$ hasta $(1,2)$ podría pasar por:

- $(3,1) \to (2,1) \to (1,1) \to (1,2)$
- $(3,1) \to (2,1) \to (2,2) \to (1,2)$
- $(3,1) \to (3,2) \to (2,2) \to (1,2)$
- $(3,1) \to (2,1) \to (2,2) \to (2,3) \to (1,3) \to (1,2)$, etc.

Es más cómodo contar por complemento o buscar los conjuntos de corte.

Como solo puede mantener 3 casillas adicionales, para que exista camino, en realidad necesita mantener al menos una de estas rutas.

Contemos cuántas elecciones de 3 casillas (a mantener) entre las 7 dejan conectadas la salida y la casa.

Vamos a enumerar. Etiquetemos las casillas así:

```
A = (1,1)
B = (1,2)  → casa (fija)
C = (1,3)

D = (2,1)
E = (2,2)
F = (2,3)

G = (3,1)  → salida (fija)
H = (3,2)
I = (3,3)
```

Las libres para mantener/quitar son: A, C, D, E, F, H, I.

Queremos elegir 3 de estas 7 para mantener (y quitar las otras 4), de modo que G y B estén conectados.

Para que exista conexión, al menos debe mantenerse un camino. Notemos que B solo está conectado a A y E. G solo está conectado a D y H.

Entonces, para conectar G con B:

- Si no se mantiene D ni H, G queda aislado (no conexo).
- Si no se mantiene A ni E, B queda aislado.

Por tanto, al menos se debe mantener una casilla vecina de G (D o H) y una vecina de B (A o E). Además, debe haber un camino intermedio.

Vamos a contar por casos.

**Caso 1: Se mantiene A (para conectar a B).**

Entonces B está conectado a A. Necesitamos conectar G con A. Para ello, G debe conectarse a A. Los vecinos de G son D y H; los vecinos de A son B y D.

- Si se mantiene D, entonces G–D–A–B conecta. En este caso, con A y D mantenidos, las 3 casillas mantenidas son A, D y una tercera cualquiera de las restantes {C, E, F, H, I} (5 opciones). Total: 5.

- Si no se mantiene D, la única alternativa para conectar G con A es G–H–E–D–A... pero D no está, entonces no; o G–H–E–? Hay que revisar.

  Si A se mantiene pero D no se mantiene, para conectar G al componente de A/B necesitamos que G se conecte vía H → E/H → ? 

  G está conectado solo a D y H. Sin D, G solo puede ir a H. H está conectado a G y E. De E, puede ir a H, D, F, B. Pero D no está. Entonces de E puede ir a B o a F. Para llegar a A/B, notemos que B ya es la casa, así que si llegamos a E y E está conectada a B, ya está.

  Pero A está mantenido. Entonces si A se mantiene y D no, y mantenemos H y E, tenemos camino G–H–E–B. Aquí las casillas mantenidas serían A, H, E (3 casillas). ¿Hay otras combinaciones?

  Veamos sistemáticamente: Con A mantenido y D quitado, elegimos 2 casillas más de {C, E, F, H, I} tal que haya camino de G a B.

  G necesita H (porque D está quitado). Entonces H debe ser mantenida. Ahora, desde H, llegar a B (o a A, pero A ya está conectado a B). Desde H solo se va a E. Entonces E debe mantenerse. Una vez en E, ya está conectada a B directamente. Por lo tanto, la segunda casilla además de A debe ser H y la tercera E.

  Entonces la única combinación en este subcaso es {A, H, E}. Total: 1.

  Sin D y sin H, G está aislado, no hay conexión. Sin E, no se puede pasar de H a B.

Entonces, con A mantenido, tenemos $5 + 1 = 6$ combinaciones válidas para conexión.

**Caso 2: No se mantiene A (entonces B solo está conectado a E).**

Para que B esté conectado, debe mantenerse E. Ahora necesitamos conectar G a E (y por tanto a B).

Vecinos de G: D y H. Vecinos de E: D, H, F, B.

- Si se mantiene D, entonces G–D–E–B conecta. Aquí B se conecta por E. Tenemos mantenidas E y D; la tercera puede ser cualquiera de {C, F, H, I} (4 opciones), recordando que A no se mantiene. También podría ser H (pero H es una de las opciones). Entonces total: 4.

  ¿Puede ser que D se mantenga, E se mantenga, y la tercera sea H? Sí, en ese caso G–D–E–B o G–H–E–B, ambas funcionan. Está contada en las 4.

- Si no se mantiene D, entonces G necesita H para conectar. Desde H, solo se va a G y E. Por tanto, E debe mantenerse (ya está) y H debe mantenerse. Entonces la única combinación con E, H y una tercera es: tercera puede ser cualquiera de las restantes que no sean A ni D: {C, F, I}. Entonces {E, H, C}, {E, H, F}, {E, H, I}: 3.

  Si D no está y H no está, G queda aislado.

  Notemos que F no conecta a G directamente, así que sin D y sin H no hay conexión.

Entonces, en el caso 2, total: $4 + 3 = 7$.

**Total de casos buenos (conexión):**

$$6 + 7 = 13.$$

**Total de casos malos (sin conexión):**

$$35 - 13 = 22.$$

Por lo tanto, el número de formas de quitar 4 nenúfares (manteniendo salida y casa) de modo que Kelvin no pueda llegar a casa es:

$$22.$$

Vamos a verificar rápidamente el conteo de los 13 casos buenos enumerando.

Casos buenos:

Con A mantenido:
- A, D, y una tercera de {C, E, F, H, I}: 5 → {A,D,C}, {A,D,E}, {A,D,F}, {A,D,H}, {A,D,I}
- A, H, E: 1 → {A,H,E}

Con E mantenido (A no):
- E, D, y una tercera de {C, F, H, I}: 4 → {E,D,C}, {E,D,F}, {E,D,H}, {E,D,I}
- E, H, y una tercera de {C, F, I}: 3 → {E,H,C}, {E,H,F}, {E,H,I}

Total: 5 + 1 + 4 + 3 = 13. ✔

Cada uno de estos 13 conjuntos de 3 casillas mantenidas corresponde a una selección mal (los 4 que se quitan son los otros).

Por lo tanto la respuesta es $35-13=22$.

Final:

\[
\boxed{22}
\]