Para calcular la suma dada, recordemos primero que tres enteros positivos $a, b, c$ forman las longitudes de los lados de un triángulo no degenerado si y solo si cumplen las desigualdades triangulares estrictas:
\[a + b > c, \quad a + c > b, \quad b + c > a.\]

### Método 1: Sustitución de Ravi en enteros

Definamos $u = b+c-a$, $v = a+c-b$ y $w = a+b-c$. Las desigualdades triangulares equivalen a que $u, v, w$ sean enteros positivos ($u, v, w \ge 1$). Despejando $a, b, c$, obtenemos:
\[a = \frac{v+w}{2}, \quad b = \frac{u+w}{2}, \quad c = \frac{u+v}{2}.\]

Para que $a, b, c$ sean números enteros, es necesario y suficiente que $u, v, w$ tengan la misma paridad (es decir, que los tres sean pares o los tres sean impares). Esto divide el conjunto $S$ en dos casos disjuntos:

1. **$u, v, w$ son todos pares:** Podemos escribir $u = 2x$, $v = 2y$, $w = 2z$ con $x, y, z \in \mathbb{Z}^+$. Entonces:
   \[a = y+z, \quad b = x+z, \quad c = x+y.\]
   En este caso, el término general de la suma es:
   \[\frac{3^{y+z}}{4^{x+z} 5^{x+y}} = \left(\frac{1}{20}\right)^x \left(\frac{3}{5}\right)^y \left(\frac{3}{4}\right)^z.\]

2. **$u, v, w$ son todos impares:** Podemos escribir $u = 2x-1$, $v = 2y-1$, $w = 2z-1$ con $x, y, z \in \mathbb{Z}^+$. Entonces:
   \[a = y+z-1, \quad b = x+z-1, \quad c = x+y-1.\]
   En este caso, el término general de la suma es:
   \[\frac{3^{y+z-1}}{4^{x+z-1} 5^{x+y-1}} = \frac{4 \cdot 5}{3} \cdot \frac{3^{y+z}}{4^{x+z} 5^{x+y}} = \frac{20}{3} \left(\frac{1}{20}\right)^x \left(\frac{3}{5}\right)^y \left(\frac{3}{4}\right)^z.\]

---

### Cálculo de las series geométricas

Sumando sobre todos los enteros positivos $x, y, z \ge 1$ de forma independiente para el primer caso:
\[\Sigma_1 = \left(\sum_{x=1}^\infty \left(\frac{1}{20}\right)^x\right) \left(\sum_{y=1}^\infty \left(\frac{3}{5}\right)^y\right) \left(\sum_{z=1}^\infty \left(\frac{3}{4}\right)^z\right).\]

Calculamos cada serie geométrica por separado:
- $\displaystyle \sum_{x=1}^\infty \left(\frac{1}{20}\right)^x = \frac{1/20}{1 - 1/20} = \frac{1}{19}$,
- $\displaystyle \sum_{y=1}^\infty \left(\frac{3}{5}\right)^y = \frac{3/5}{1 - 3/5} = \frac{3}{2}$,
- $\displaystyle \sum_{z=1}^\infty \left(\frac{3}{4}\right)^z = \frac{3/4}{1 - 3/4} = 3$.

Multiplicando los tres resultados obtenemos:
\[\Sigma_1 = \frac{1}{19} \cdot \frac{3}{2} \cdot 3 = \frac{9}{38}.\]

Para el segundo caso, tenemos $\Sigma_2 = \frac{20}{3} \Sigma_1$. Por lo tanto, la suma total es:
\[\Sigma = \Sigma_1 + \Sigma_2 = \left(1 + \frac{20}{3}\right)\Sigma_1 = \frac{23}{3} \cdot \frac{9}{38} = \frac{69}{38}.\]

\boxed{\frac{69}{38}}