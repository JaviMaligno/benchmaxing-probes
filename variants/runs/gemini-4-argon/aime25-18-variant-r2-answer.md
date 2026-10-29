Para encontrar el número de coloraciones válidas, podemos dividir los $12$ segmentos unitarios de la cuadrícula de $2 \times 2$ en dos grupos:
- **$4$ segmentos interiores:** cada uno de ellos es compartido por dos cuadrados unitarios adyacentes.
- **$8$ segmentos exteriores:** cada uno de los $4$ cuadrados unitarios tiene exactamente $2$ segmentos exteriores que no comparte con ningún otro cuadrado.

Como cada cuadrado unitario debe tener exactamente $1$ lado rojo y $3$ azules, ningún cuadrado puede tener $2$ lados interiores rojos. Analicemos por casos según la cantidad $k$ de segmentos interiores coloreados de rojo:

1. **Caso $k = 0$ (ningún segmento interior es rojo):**
   Todos los $4$ segmentos interiores son azules. Para que cada uno de los $4$ cuadrados tenga exactamente $1$ lado rojo, en cada cuadrado debemos elegir exactamente $1$ de sus $2$ segmentos exteriores para pintarlo de rojo (y el otro de azul). Como hay $2$ opciones por cada uno de los $4$ cuadrados de manera independiente, tenemos:
   $$2^4 = 16 \text{ formas.}$$

2. **Caso $k = 1$ (exactamente $1$ segmento interior es rojo):**
   Hay $4$ maneras de elegir cuál de los $4$ segmentos interiores es rojo. Una vez elegido, los $2$ cuadrados que comparten este segmento ya tienen su único lado rojo, por lo que sus segmentos exteriores deben ser todos azules ($1$ sola opción para cada uno). Los otros $2$ cuadrados no tocan ningún segmento interior rojo, por lo que cada uno tiene $2$ opciones para elegir cuál de sus $2$ lados exteriores será rojo. Esto nos da:
   $$4 \times (1 \times 1 \times 2 \times 2) = 16 \text{ formas.}$$

3. **Caso $k = 2$ (exactamente $2$ segmentos interiores son rojos):**
   Para que ningún cuadrado tenga $2$ lados rojos, los dos segmentos interiores rojos no pueden pertenecer al mismo cuadrado; es decir, deben ser segmentos opuestos (o ambos horizontales, o ambos verticales). Hay $2$ maneras de elegir este par de segmentos interiores. Con esto, cada uno de los $4$ cuadrados ya tiene exactamente $1$ lado interior rojo, por lo que los $8$ segmentos exteriores deben ser obligatoriamente azules ($1$ sola opción). Esto aporta:
   $$2 \times 1 = 2 \text{ formas.}$$

4. **Caso $k \ge 3$:**
   Por el principio del palomar, al menos un cuadrado tendría $2$ segmentos interiores rojos, lo cual es imposible. Hay $0$ formas en este caso.

Sumando todos los casos posibles, el número total de coloraciones es:
$$16 + 16 + 2 = 34$$

\boxed{34}