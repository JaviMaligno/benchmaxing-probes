Modelo el museo como un grafo: las habitaciones son vértices y las puertas son aristas.

1. **Total de puertas:**
   \[
   9(13-1)+(9-1)13=108+104=212.
   \]

2. **Condición de paridad:** en un recorrido cerrado, cada habitación debe tener un número par de puertas usadas. Por tanto, las habitaciones de grado impar necesitan un número impar de puertas **no usadas**.

   Las habitaciones de grado impar son las del borde que no son esquinas:
   \[
   2(13-2)+2(9-2)=22+14=36.
   \]

3. **Mínimo de puertas no usadas:** en cada lado hay un número impar de estas habitaciones: \(11\) en cada lado largo y \(7\) en cada lado corto. No pueden corregirse todas usando solo puertas entre dos de ellas en el mismo lado, así que cada lado requiere al menos una puerta no usada que salga hacia una habitación de grado par. Eso da al menos \(4\) puertas “de un solo extremo”.

   Esas \(4\) puertas cubren a lo sumo \(4\) de las \(36\) incidencias necesarias; las otras \(32\) requieren al menos \(16\) puertas más. Así que al menos
   \[
   4+16=20
   \]
   puertas deben quedar sin usarse.

4. **La cota se alcanza:** omite \(20\) puertas perimetrales: empareja habitaciones vecinas a lo largo de cada lado, dejando una sin emparejar junto a cada una de dos esquinas opuestas, y omite también las cuatro puertas desde esas habitaciones hacia dichas esquinas. Esto deja todos los grados restantes pares, y la componente con puertas sigue conexa.

   Por el teorema de Euler, existe un recorrido cerrado que usa
   \[
   212-20=192
   \]
   puertas.

\[
\boxed{192}
\]