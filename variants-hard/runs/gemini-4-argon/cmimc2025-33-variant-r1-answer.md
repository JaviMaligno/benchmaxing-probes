Para encontrar el menor número natural $n$ que cumple la condición dada, primero simplificamos la expresión para la composición $k$-ésima de $g(x) = x^3 - 3x$.

Observamos que si hacemos el cambio de variable $x = t + \frac{1}{t}$, obtenemos:
$$g\left(t + \frac{1}{t}\right) = \left(t + \frac{1}{t}\right)^3 - 3\left(t + \frac{1}{t}\right) = t^3 + 3t + \frac{3}{t} + \frac{1}{t^3} - 3t - \frac{3}{t} = t^3 + \frac{1}{t^3}$$

Aplicando esta propiedad de manera inductiva $k$ veces, se tiene que:
$$g^k\left(t + \frac{1}{t}\right) = t^{3^k} + \frac{1}{t^{3^k}}$$

Dado que el argumento evaluado es $\frac{n^2+1}{n} = n + \frac{1}{n}$, al sustituir $t = n$ resulta:
$$g^k\left(\frac{n^2+1}{n}\right) = n^{3^k} + \frac{1}{n^{3^k}}$$

La desigualdad del problema se transforma entonces en:
$$\left|n^{3^k} + \frac{1}{n^{3^k}} - c^{72}\right| < \frac{1}{100}$$

Analicemos los posibles valores del número natural $n$:

1. **Caso $n = 1$:**
   Para cualquier $k$, tenemos $1^{3^k} + \frac{1}{1^{3^k}} = 2$. La desigualdad sería $|2 - c^{72}| < \frac{1}{100}$, la cual no tiene solución para ningún número natural $c$ (pues $c=1$ da $1$ y $c \ge 2$ da $c^{72} \ge 2^{72}$).

2. **Caso $n \ge 2$:**
   Tanto $n^{3^k}$ como $c^{72}$ son números enteros. Como $n \ge 2$ y $k \ge 1$, tenemos que $n^{3^k} \ge 2^3 = 8$, por lo que $0 < \frac{1}{n^{3^k}} \le \frac{1}{8}$.
   Si $n^{3^k} \neq c^{72}$, al ser ambos enteros, su distancia es al menos $1$, es decir, $|n^{3^k} - c^{72}| \ge 1$. Por la desigualdad triangular:
   $$\left|n^{3^k} - c^{72} + \frac{1}{n^{3^k}}\right| \ge |n^{3^k} - c^{72}| - \frac{1}{n^{3^k}} \ge 1 - \frac{1}{8} = \frac{7}{8} > \frac{1}{100}$$
   Por lo tanto, para que se cumpla la desigualdad es estrictamente necesario que la parte entera se anule:
   $$n^{3^k} = c^{72} \quad \text{y} \quad \frac{1}{n^{3^k}} < \frac{1}{100}$$

Descomponiendo el exponente $72$ en factores primos tenemos $72 = 2^3 \cdot 3^2 = 8 \cdot 9$. La ecuación $n^{3^k} = c^{72}$ equivale a:
$$n^{3^k} = \left(c^8\right)^9$$

Dado que $\text{mcd}(3^k, 8) = 1$ para todo $k$, para que $n^{3^k}$ sea una potencia de exponente $72$, el número $n$ debe ser necesariamente una octava potencia perfecta, es decir, $n = m^8$ para algún número natural $m \ge 2$.

Para minimizar $n$, tomamos el menor valor posible $m = 2$, lo que nos da:
$$n = 2^8 = 256$$

Verificamos que con $n = 256$, basta elegir $k = 2$ y $c = 2$ para obtener:
$$n^{3^2} = (2^8)^9 = 2^{72} = c^{72}$$
y además $\frac{1}{2^{72}} < \frac{1}{100}$, cumpliendo todas las condiciones.

\boxed{256}