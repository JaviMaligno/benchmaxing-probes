Para calcular la suma pedida, primero caracterizamos el conjunto $T$ de ternas de enteros positivos $(a,b,c)$ que pueden ser las longitudes de los lados de un triángulo no degenerado.

### Paso 1: Condición de existencia del triángulo
Por la desigualdad triangular, tres enteros positivos $a, b, c$ forman los lados de un triángulo si y solo si:
\[a + b > c, \quad a + c > b \quad \text{y} \quad b + c > a.\]
Fijados dos enteros positivos cualesquiera $b, c \ge 1$, estas tres condiciones equivalen a:
\[|b - c| < a < b + c.\]
Dado que $a, b, c$ son números enteros, los valores posibles de $a$ son aquellos que satisfacen:
\[|b - c| + 1 \le a \le b + c - 1.\]

### Paso 2: Suma respecto de $a$
Reescribimos la suma total agrupando primero respecto a $a$ para $b$ y $c$ fijos:
\[S = \sum_{(a,b,c) \in T} \frac{2^a}{3^b 5^c} = \sum_{b=1}^{\infty} \sum_{c=1}^{\infty} \frac{1}{3^b 5^c} \sum_{a = |b-c|+1}^{b+c-1} 2^a.\]
Calculamos la suma geométrica finita interna:
\[\sum_{a = |b-c|+1}^{b+c-1} 2^a = 2^{b+c} - 2^{|b-c|+1}.\]
Por lo tanto, podemos separar la suma doble en dos series convergentes $S = S_1 - S_2$, donde:
\[S_1 = \sum_{b=1}^{\infty} \sum_{c=1}^{\infty} \frac{2^{b+c}}{3^b 5^c}, \qquad S_2 = \sum_{b=1}^{\infty} \sum_{c=1}^{\infty} \frac{2^{|b-c|+1}}{3^b 5^c}.\]

### Paso 3: Cálculo de $S_1$
La primera suma se factoriza directamente como el producto de dos series geométricas:
\[S_1 = \left(\sum_{b=1}^{\infty} \left(\frac{2}{3}\right)^b\right) \left(\sum_{c=1}^{\infty} \left(\frac{2}{5}\right)^c\right) = \frac{2/3}{1 - 2/3} \cdot \frac{2/5}{1 - 2/5} = 2 \cdot \frac{2}{3} = \frac{4}{3}.\]

### Paso 4: Cálculo de $S_2$
Para calcular $S_2$, dividimos los pares $(b,c)$ en tres casos según la relación de orden entre $b$ y $c$:

1. **Caso $b = c$:**
   \[\sum_{b=1}^{\infty} \frac{2^1}{3^b 5^b} = 2 \sum_{b=1}^{\infty} \left(\frac{1}{15}\right)^b = 2 \cdot \frac{1/15}{1 - 1/15} = 2 \cdot \frac{1}{14} = \frac{1}{7}.\]

2. **Caso $b > c$:** Haciendo el cambio $b = c + k$ con $k \ge 1$, tenemos $|b - c| = k$:
   \[\sum_{c=1}^{\infty} \sum_{k=1}^{\infty} \frac{2^{k+1}}{3^{c+k} 5^c} = 2 \left(\sum_{c=1}^{\infty} \left(\frac{1}{15}\right)^c\right) \left(\sum_{k=1}^{\infty} \left(\frac{2}{3}\right)^k\right) = 2 \cdot \frac{1}{14} \cdot 2 = \frac{2}{7}.\]

3. **Caso $b < c$:** Haciendo el cambio $c = b + k$ con $k \ge 1$, tenemos $|b - c| = k$:
   \[\sum_{b=1}^{\infty} \sum_{k=1}^{\infty} \frac{2^{k+1}}{3^b 5^{b+k}} = 2 \left(\sum_{b=1}^{\infty} \left(\frac{1}{15}\right)^b\right) \left(\sum_{k=1}^{\infty} \left(\frac{2}{5}\right)^k\right) = 2 \cdot \frac{1}{14} \cdot \frac{2}{3} = \frac{2}{21}.\]

Sumando las tres contribuciones para $S_2$:
\[S_2 = \frac{1}{7} + \frac{2}{7} + \frac{2}{21} = \frac{3 + 6 + 2}{21} = \frac{11}{21}.\]

### Paso 5: Resultado final
Restando $S_2$ de $S_1$, obtenemos:
\[S = S_1 - S_2 = \frac{4}{3} - \frac{11}{21} = \frac{28 - 11}{21} = \frac{17}{21}.\]

\boxed{\frac{17}{21}}