

Sea \(h=\frac12\) la probabilidad de que una puerta horizontal esté abierta y \(v=\frac34\) la probabilidad de que una puerta vertical esté abierta.

Entre dos columnas consecutivas, ambas puertas horizontales están cerradas con probabilidad \(\frac14\). Como esto ocurre independientemente en cada corte, casi seguramente eventualmente aparece un corte totalmente bloqueado, así que el número de celdas alcanzables es finito con probabilidad \(1\).

Exploramos el proceso por columnas. Después de procesar una columna, solo importan los estados posibles en la columna actual:

- **Estado \(D\)**: las dos celdas de la columna actual son alcanzables y están conectadas al componente de Mira.
- **Estado \(S\)**: exactamente una celda de la columna actual es alcanzable; la otra pertenece a un componente separado de tamaño \(d\), que aún podría conectarse más adelante.

Definimos:

- \(A\): número esperado de celdas alcanzables adicionales desde un estado \(D\), sin contar las ya alcanzadas.
- \(B\): si en estado \(S\) hay un componente separado de tamaño \(d\), su contribución esperada al tamaño final es \(Bd\).
- \(C\): número esperado de celdas alcanzables adicionales desde un estado \(S\), excluyendo el componente alcanzable actual y la contribución \(Bd\) del componente separado.

Así, si el componente alcanzable actual tiene tamaño \(s\), la esperanza final es:

\[
s+A \quad \text{en estado } D,
\]
\[
s+Bd+C \quad \text{en estado } S.
\]

### Transiciones desde \(D\)

Desde una columna donde ambas celdas son alcanzables:

- Con probabilidad \(\frac14\), ambas puertas horizontales hacia la siguiente columna están abiertas: las dos nuevas celdas son alcanzables y seguimos en \(D\).
- Con probabilidad \(\frac12\), exactamente una puerta horizontal está abierta:
  - si la puerta vertical de la nueva columna está abierta, probabilidad \(\frac34\), las dos nuevas celdas son alcanzables: estado \(D\);
  - si está cerrada, probabilidad \(\frac14\), solo una nueva celda es alcanzable y la otra queda como componente separado de tamaño \(1\): estado \(S\).
- Con probabilidad \(\frac14\), ambas puertas horizontales están cerradas: el proceso termina.

Por tanto,

\[
A=\frac58(2+A)+\frac18(1+B+C).
\]

Es decir,

\[
3A=11+B+C. \tag{1}
\]

### Transiciones desde \(S\)

Supongamos que la celda alcanzable está en la fila \(R\) y la otra en la fila \(O\). Las puertas horizontales hacia la siguiente columna tienen cuatro casos equiprobables:

1. Ambas cerradas: el proceso termina.
2. \(R\) abierta, \(O\) cerrada:
   - si la vertical nueva está abierta, las dos celdas nuevas son alcanzables: estado \(D\);
   - si está cerrada, seguimos en \(S\), con un nuevo componente separado de tamaño \(1\).
3. \(R\) cerrada, \(O\) abierta: el componente de Mira no llega a la siguiente columna, así que el proceso termina.
4. Ambas abiertas:
   - si la vertical nueva está abierta, el componente separado se une al de Mira: estado \(D\);
   - si está cerrada, seguimos en \(S\), y el componente separado crece en \(1\).

El componente separado actual se cuenta si ocurre el caso 4 con vertical abierta, probabilidad \(\frac{3}{16}\), o si ocurre el caso 4 con vertical cerrada, probabilidad \(\frac{1}{16}\), y luego eventualmente se conecta. Así,

\[
B=\frac{3}{16}+\frac{1}{16}B,
\]

de donde

\[
B=\frac15.
\]

Para \(C\), los casos relevantes son cuando la puerta de la fila alcanzable está abierta. En cada uno de esos dos casos, con probabilidad total \(\frac12\):

- si la vertical nueva está abierta, se añaden \(2\) celdas y luego esperamos \(A\) más;
- si está cerrada, se añade \(1\) celda y queda un componente separado nuevo de tamaño \(1\), aportando \(B+C\).

Por tanto,

\[
C=\frac38(2+A)+\frac18(1+B+C).
\]

Es decir,

\[
7C=7+3A+B. \tag{2}
\]

Con \(B=\frac15\), las ecuaciones (1) y (2) son

\[
3A=\frac{56}{5}+C,
\]
\[
7C=\frac{36}{5}+3A.
\]

Resolviendo,

\[
A=\frac{214}{45}, \qquad C=\frac{46}{15}.
\]

### Columna inicial

En la primera columna, Mira empieza en la

celda superior izquierda. La puerta vertical de esa primera columna está abierta con probabilidad \(\frac34\) y cerrada con probabilidad \(\frac14\).

- Si está abierta, ambas celdas de la primera columna son alcanzables: tamaño inicial \(2\), estado \(D\). Esperanza total: \(2+A\).
- Si está cerrada, solo la celda superior es alcanzable, y la inferior es un componente separado de tamaño \(1\): estado \(S\) con \(s=1\), \(d=1\). Esperanza total: \(1+B+C\).

Por tanto, la esperanza pedida es

\[
E=\frac34(2+A)+\frac14(1+B+C).
\]

Sustituyendo \(A=\frac{214}{45}\), \(B=\frac15\), \(C=\frac{46}{15}\):

\[
2+A=2+\frac{214}{45}=\frac{304}{45},
\]

\[
1+B+C=1+\frac15+\frac{46}{15}
=\frac{64}{15}.
\]

Entonces

\[
E=\frac34\cdot\frac{304}{45}+\frac14\cdot\frac{64}{15}
=\frac{76}{15}+\frac{16}{15}
=\frac{92}{15}.
\]

\[
\boxed{\frac{92}{15}}
\]