Para hallar el valor del producto dado, primero simplificamos el término general utilizando las propiedades de los logaritmos:

$$\frac{\log_k \left(7^{k^2 - 1}\right)}{\log_{k+1} \left(7^{k^2 - 4}\right)} = \frac{(k^2 - 1)\log_k 7}{(k^2 - 4)\log_{k+1} 7}$$

Aplicando la fórmula de cambio de base $\log_b a = \frac{\ln a}{\ln b}$, obtenemos:

$$\frac{\log_k 7}{\log_{k+1} 7} = \frac{\ln 7 / \ln k}{\ln 7 / \ln(k+1)} = \frac{\ln(k+1)}{\ln k}$$

De este modo, podemos separar el producto original $P$ en dos productos telescópicos:

$$P = \left( \prod_{k=3}^{80} \frac{\ln(k+1)}{\ln k} \right) \cdot \left( \prod_{k=3}^{80} \frac{k^2 - 1}{k^2 - 4} \right)$$

**Paso 1: Evaluar el primer producto**

$$\prod_{k=3}^{80} \frac{\ln(k+1)}{\ln k} = \frac{\ln 4}{\ln 3} \cdot \frac{\ln 5}{\ln 4} \cdot \frac{\ln 6}{\ln 5} \cdots \frac{\ln 81}{\ln 80} = \frac{\ln 81}{\ln 3} = \log_3(81) = 4$$

**Paso 2: Evaluar el segundo producto**

Factorizamos el numerador y el denominador de cada fracción:

$$\prod_{k=3}^{80} \frac{k^2 - 1}{k^2 - 4} = \prod_{k=3}^{80} \frac{(k - 1)(k + 1)}{(k - 2)(k + 2)} = \left( \prod_{k=3}^{80} \frac{k - 1}{k - 2} \right) \cdot \left( \prod_{k=3}^{80} \frac{k + 1}{k + 2} \right)$$

Calculamos cada parte por separado:

1. $\prod_{k=3}^{80} \frac{k - 1}{k - 2} = \frac{2}{1} \cdot \frac{3}{2} \cdot \frac{4}{3} \cdots \frac{79}{78} = 79$
2. $\prod_{k=3}^{80} \frac{k + 1}{k + 2} = \frac{4}{5} \cdot \frac{5}{6} \cdot \frac{6}{7} \cdots \frac{81}{82} = \frac{4}{82} = \frac{2}{41}$

Multiplicando ambos resultados parciales:

$$\prod_{k=3}^{80} \frac{k^2 - 1}{k^2 - 4} = 79 \cdot \frac{2}{41} = \frac{158}{41}$$

**Paso 3: Combinar ambos productos y hallar $m + n$**

Multiplicamos los resultados del Paso 1 y del Paso 2:

$$P = 4 \cdot \frac{158}{41} = \frac{632}{41}$$

Dado que $41$ es un número primo y no divide a $632$ ($632 = 41 \times 15 + 17$), los enteros positivos $m = 632$ y $n = 41$ son coprimos. Finalmente, calculamos $m + n$:

$$m + n = 632 + 41 = 673$$

\boxed{673}