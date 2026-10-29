Primero, calculamos el número total de formas de elegir un equipo de 5 personas entre 15 (9 ingenieros + 6 diseñadores):

\[
\binom{15}{5} = 3003
\]

Después, restamos los casos que **no** cumplen la condición de tener al menos un ingeniero y al menos un diseñador, es decir:

1. Equipos con **cero diseñadores** (solo ingenieros): eligiendo 5 de los 9 ingenieros:

\[
\binom{9}{5} = 126
\]

2. Equipos con **cero ingenieros** (solo diseñadores): pero solo hay 6 diseñadores, así que elegir 5 de 6:

\[
\binom{6}{5} = 6
\]

Como estos dos casos son mutuamente excluyentes, la cantidad de equipos válidos es:

\[
\binom{15}{5} - \binom{9}{5} - \binom{6}{5}
= 3003 - 126 - 6
= 2871
\]

\[
\boxed{2871}
\]