**Razonamiento paso a paso:**

El subcomité debe tener 5 miembros y al menos un miembro de cada partido. Esto significa que hay que excluir los casos en los que todos los miembros son del mismo partido.

1. **Casos posibles sin restricción:**

   Elegimos 5 personas de un total de 14:

   \[
   \binom{14}{5} = 2002
   \]

2. **Casos no permitidos (todos de un solo partido):**

   - Todos republicanos: elegir 5 de 8 republicanos.

     \[
     \binom{8}{5} = 56
     \]

   - Todos demócratas: elegir 5 de 6 demócratas.

     \[
     \binom{6}{5} = 6
     \]

   (No es posible elegir 5 demócratas y además republicanos al mismo tiempo, así que estos casos son disjuntos.)

3. **Casos válidos:**

   \[
   \binom{14}{5} - \binom{8}{5} - \binom{6}{5}
   = 2002 - 56 - 6
   = 1940
   \]

Por lo tanto, el número de formas es:

\[
\boxed{1940}
\]