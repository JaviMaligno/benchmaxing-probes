

Trabajamos en el grupo \(S_5\). Escribiremos \(pq\) para \(p\circ q\), es decir, \(pq(x)=p(q(x))\). Las condiciones del enunciado son

\[
fgh=g,\quad hgf=g,\quad ghf=h,\quad fhg=h,\quad hfg=f,\quad gfh=f.
\]

Equivalentemente, cualquier producto de los tres en cualquier orden da como resultado el factor central.

Sea

\[
u=f^{-1}g,
\]

de modo que \(g=fu\). Usamos dos de las igualdades:

\[
fgh=g \quad\text{y}\quad gfh=f.
\]

De ellas,

\[
h=g^{-1}f^{-1}g
\]

y también

\[
h=f^{-1}g^{-1}f.
\]

Por tanto,

\[
g^{-1}f^{-1}g=f^{-1}g^{-1}f.
\]

Invirtiendo esta igualdad,

\[
g^{-1}fg=f^{-1}gf.
\]

Sustituyendo \(g=fu\),

\[
u^{-1}fu=uf.
\]

Multiplicando por la izquierda por \(u\),

\[
fu=u^2f. \tag{1}
\]

Además,

\[
h=g^{-1}f^{-1}g=u^{-1}f^{-1}u=f^{-1}u^{-1}. \tag{2}
\]

Ahora imponemos otra de las igualdades, por ejemplo \(ghf=h\). Usando (1) y (2),

\[
ghf=(fu)(f^{-1}u^{-1})f=fuf^{-1}u^{-1}f=u^2u^{-1}f=uf.
\]

Como debe cumplirse \(ghf=h=f^{-1}u^{-1}\), obtenemos

\[
uf=f^{-1}u^{-1}.
\]

Multiplicando por la izquierda por \(f\),

\[
fuf=u^{-1}. \tag{3}
\]

Por otro lado, de (1), multiplicando por la derecha por \(f\),

\[
fuf=u^2f^2.
\]

Comparando con (3),

\[
u^2f^2=u^{-1},
\]

y por tanto

\[
f^2=u^{-3}. \tag{4}
\]

Así, \(f^2\) es una potencia de \(u\), luego conmuta con \(u\). Pero aplicando (1) dos veces,

\[
f^2uf^{-2}=u^4.
\]

Como \(f^2\) conmuta con \(u\), el lado izquierdo es simplemente \(u\). Entonces

\[
u^4=u,
\]

de donde

\[
u^3=e.
\]

Luego, por (4),

\[
f^2=e.
\]

Así, toda solución está determinada por un par \((f,u)\) tal que

\[
f^2=e,\qquad u^3=e,\qquad fuf=u^{-1},
\]

y entonces

\[
g=fu,\qquad h=fu^{-1}.
\]

Recíprocamente, cualquier par \((f,u)\) con esas tres condiciones produce una solución. En efecto, si \(u=e\), entonces \(f=g=h\) con \(f^2=e\), y las igualdades son inmediatas. Si \(u\neq e\), usando \(fu=u^{-1}f\) y \(fu^{-1}=uf\), se comprueba directamente:

\[
\begin{aligned}
fgh&=f(fu)(fu^{-1})=fu=g,\\
hgf&=(fu^{-1})(fu)f=fu=g,\\
ghf&=(fu)(fu^{-1})f=fu^{-1}=h,\\
fhg&=f(fu^{-1})(fu)=fu^{-1}=h,\\
hfg&=(fu^{-1})f(fu)=f,\\
gfh&=(fu)f(fu^{-1})=f.
\end{aligned}
\]

La correspondencia \((f,u)\leftrightarrow(f,g,h)\) es biyectiva, pues \(u=f^{-1}g\). Así que basta contar tales pares en \(S_5\).

### Caso 1: \(u=e\)

Entonces solo pedimos \(f^2=e\), es decir, \(f\) es una involución de \(S_5\). Las involuciones en \(S_5\) son:

- la identidad: \(1\),
- transposiciones: \(\binom{5}{2}=10\),
- productos de dos transposiciones disjuntas: \(\binom{5}{4}\cdot 3=15\).

Total:

\[
1+10+15=26.
\]

### Caso 2: \(u\neq e\)

Como \(u^3=e\) y estamos en \(S_5\), \(u\) debe ser un 3-ciclo. Hay

\[
\binom{5}{3}\cdot 2=20
\]

3-ciclos.

Fijemos un 3-ciclo \(u\), con soporte \(S\) de tamaño \(3\). La condición

\[
fuf=u^{-1}
\]

implica que \(f\) conserva el soporte \(S\). Sobre \(S\), \(f\) debe invertir el 3-ciclo; las únicas involuciones que hacen esto son las tres transposiciones de \(S\).

Fuera de \(S\) quedan dos puntos. Sobre ellos, \(f\) puede ser la identidad o la transposición que los intercambia: \(2\) opciones.

Por tanto, para cada 3-ciclo \(u\) hay

\[
3\cdot 2=6
\]

elecciones de \(f\). Esto aporta

\[
20\cdot 6=120
\]

soluciones.

Sumando ambos casos,

\[
26+120=146.
\]

\[
\boxed{146}
\]