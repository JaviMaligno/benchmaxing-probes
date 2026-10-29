Vamos a resolverlo paso a paso.

**Paso 1: Total de subcomités de 5 miembros sin restricción**

Hay 8 republicanos y 6 demócratas, es decir, 14 personas en total. El número de subcomités de 5 miembros es:

\[
\binom{14}{5} = 2002
\]

**Paso 2: Subcomités con solo republicanos (sin demócratas)**

\[
\binom{8}{5} = 56
\]

**Paso 3: Subcomités con solo demócratas (sin republicanos)**

El subcomité debe tener 5 miembros, pero solo hay 6 demócratas:

\[
\binom{6}{5} = 6
\]

**Paso 4: Aplicar el complemento**

Queremos subcomités con al menos un miembro de cada partido. Restamos al total los subcomités que tienen solo republicanos o solo demócratas:

\[
2002 - 56 - 6 = 1940
\]

\[
\boxed{1940}
\]