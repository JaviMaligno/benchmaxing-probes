Para hallar el valor del producto dado, primero aplicamos las propiedades de los logaritmos a cada término del producto:

$$\log_k \left(7^{k^2 - 1}\right) = (k^2 - 1)\log_k 7 = (k - 1)(k + 1)\frac{\ln 7}{\ln k}$$

$$\log_{k+1} \left(7^{k^2 - 4}\right) = (k^2 - 4)\log_{k+1} 7 = (k - 2)(k + 2)\frac{\ln 7}{\ln(k + 1)}$$

Sustituyendo estas expresiones en el término general del producto, obtenemos:

$$\frac{\log_k \left(7^{k^2 - 1}\right)}{\log_{k+1} \left(7^{k^2 - 4}\right)} = \frac{(k - 1)(k + 1)}{(k - 2)(k + 2)} \cdot \frac{\ln(k + 1)}{\ln k}$$

Ahora podemos separar el producto total en tres productos telescópicos para $k$ desde $3$ hasta $80$:

$$P = \left(\prod_{k=3}^{80} \frac{k - 1}{k - 2}\right) \left(\prod_{k=3}^{80} \frac{k + 1}{k + 2}\right) \left(\prod_{k=3}^{80} \frac{\ln(k + 1)}{\ln k}\right)$$

Evaluamos cada parte por separado:

1. Para el primer producto:
$$\prod_{k=3}^{80} \frac{k - 1}{k - 2} = \frac{2}{1} \cdot \frac{3}{2} \cdot \frac{4}{3} \cdots \frac{79}{78} = 79$$

2. Para el segundo producto:
$$\prod_{k=3}^{80} \frac{k + 1}{k + 2} = \frac{4}{5} \cdot \frac{5}{6} \cdot \frac{6}{7} \cdots \frac{81}{82} = \frac{4}{82} = \frac{2}{41}$$

3. Para el tercer producto:
$$\prod_{k=3}^{80} \frac{\ln(k + 1)}{\ln k} = \frac{\ln 4}{\ln 3} \cdot \frac{\ln 5}{\ln 4} \cdots \frac{\ln 81}{\ln 80} = \frac{\ln 81}{\ln 3} = \frac{\ln(3^4)}{\ln 3} = 4$$

Multiplicando los tres resultados obtenidos:

$$P = 79 \cdot \frac{2}{41} \cdot 4 = \frac{632}{41}$$

Dado que $41$ es un número primo y no divide a $632$ ($632 = 41 \times 15 + 17$), los enteros positivos $m = 632$ y $n = 41$ son coprimos. 

Finalmente, calculamos $m + n$:
$$m + n = 632 + 41 = 673$$

\boxed{673}