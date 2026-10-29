Vamos a razonar paso a paso.

Sea \(z\) una raíz 2027-ésima de la unidad, \(z\neq 1\). Queremos calcular

\[
S=\sum_{k=1}^{2027}\frac{1}{1+z^k}.
\]

**Paso 1: Propiedades de las raíces de la unidad**

Como \(z^{2027}=1\), los números \(z,z^2,\dots,z^{2027}\) son exactamente todas las raíces 2027-ésimas de la unidad, cada una apareciendo una vez (pues \(z\) es raíz primitiva o, en general, la lista recorre todas las raíces porque 2027 es primo). De hecho, \(2027\) es primo, así que cualquier \(z\neq 1\) con \(z^{2027}=1\) es raíz primitiva.

**Paso 2: Relación con la raíz conjugada**

Para cualquier \(k\), se cumple

\[
\frac{1}{1+z^k}+\frac{1}{1+z^{-k}}
=\frac{1}{1+z^k}+\frac{1}{1+\frac1{z^k}}
=\frac{1}{1+z^k}+\frac{z^k}{z^k+1}
=\frac{1+z^k}{1+z^k}=1.
\]

**Paso 3: Agrupación por pares**

Como \(z^{2027}=1\), tenemos \(z^{-k}=z^{2027-k}\). Por lo tanto, los términos se pueden emparejar:

\[
\frac{1}{1+z^k}+\frac{1}{1+z^{2027-k}}=1.
\]

Los valores \(k=1,2,\dots,2026\) forman \(1013\) pares, y queda el término con \(k=2027\) sin pareja, que es

\[
\frac{1}{1+z^{2027}}=\frac{1}{1+1}=\frac12.
\]

Entonces,

\[
S=1013\cdot 1+\frac12=1013+\frac12=\frac{2027}{2}.
\]

**Conclusión:**

\[
\boxed{\frac{2027}{2}}
\]