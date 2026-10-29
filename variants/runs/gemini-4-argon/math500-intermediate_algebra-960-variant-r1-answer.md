Para calcular la suma pedida, recordemos primero que tres enteros positivos $a, b, c$ forman las longitudes de los lados de un triángulo no degenerado si y solo si satisfacen las tres desigualdades triangulares estrictas:
\[a < b + c, \quad b < a + c, \quad \text{y} \quad c < a + b.\]

Sea $T$ el conjunto de todas las ternas ordenadas de enteros positivos $(a,b,c)$ tales que $a < b + c$:
\[T = \{(a,b,c) \in \mathbb{Z}_+^3 : a < b + c\}.\]

Para que una terna $(a,b,c) \in T$ **no** pertenezca a $S$, debe fallar alguna de las otras dos desigualdades triangulares; es decir, debe cumplirse que $b \ge a + c$ o bien $c \ge a + b$. 
Definamos los conjuntos:
\[B = \{(a,b,c) \in \mathbb{Z}_+^3 : b \ge a + c\},\]
\[C = \{(a,b,c) \in \mathbb{Z}_+^3 : c \ge a + b\}.\]

Observemos lo siguiente:
1. Si $(a,b,c) \in B$, como $c \ge 1$, se tiene $b + c \ge a + 2c > a$, por lo que $B \subset T$. Análogamente, $C \subset T$.
2. Los conjuntos $B$ y $C$ son disjuntos, ya que si $b \ge a + c$ y $c \ge a + b$, sumando ambas desigualdades obtendríamos $b + c \ge 2a + b + c \implies 2a \le 0$, lo cual es imposible para enteros positivos.

Por lo tanto, $T$ se puede particionar en la unión disjunta $T = S \sqcup B \sqcup C$, de donde se sigue que:
\[\sum_{(a,b,c) \in S} \frac{3^a}{4^b 5^c} = \sum_{(a,b,c) \in T} \frac{3^a}{4^b 5^c} - \sum_{(a,b,c) \in B} \frac{3^a}{4^b 5^c} - \sum_{(a,b,c) \in C} \frac{3^a}{4^b 5^c},\]
siempre que las tres series del lado derecho converjan. Calcularemos cada una por separado.

### 1. Suma sobre $T$
Dado que $a, b, c$ son enteros positivos, la condición $a < b + c$ equivale a $1 \le a \le b + c - 1$. Fijando $b, c \ge 1$ y sumando primero sobre $a$:
\[\sum_{a=1}^{b+c-1} 3^a = \frac{3^{b+c} - 3}{3 - 1} = \frac{3^{b+c} - 3}{2}.\]

Sustituyendo esto en la suma sobre $T$:
\[\Sigma_T = \sum_{b=1}^\infty \sum_{c=1}^\infty \frac{3^{b+c} - 3}{2 \cdot 4^b 5^c} = \frac{1}{2} \left(\sum_{b=1}^\infty \left(\frac{3}{4}\right)^b\right) \left(\sum_{c=1}^\infty \left(\frac{3}{5}\right)^c\right) - \frac{3}{2} \left(\sum_{b=1}^\infty \left(\frac{1}{4}\right)^b\right) \left(\sum_{c=1}^\infty \left(\frac{1}{5}\right)^c\right).\]

Evaluando cada serie geométrica:
- $\sum_{b=1}^\infty \left(\frac{3}{4}\right)^b = \frac{3/4}{1 - 3/4} = 3$
- $\sum_{c=1}^\infty \left(\frac{3}{5}\right)^c = \frac{3/5}{1 - 3/5} = \frac{3}{2}$
- $\sum_{b=1}^\infty \left(\frac{1}{4}\right)^b = \frac{1/4}{1 - 1/4} = \frac{1}{3}$
- $\sum_{c=1}^\infty \left(\frac{1}{5}\right)^c = \frac{1/5}{1 - 1/5} = \frac{1}{4}$

Por consiguiente:
\[\Sigma_T = \frac{1}{2}(3)\left(\frac{3}{2}\right) - \frac{3}{2}\left(\frac{1}{3}\right)\left(\frac{1}{4}\right) = \frac{9}{4} - \frac{1}{8} = \frac{17}{8}.\]

### 2. Suma sobre $B$
En $B$ tenemos $a \ge 1$, $c \ge 1$ y $b \ge a + c$. Escribiendo $b = a + c + k$ con $k \ge 0$:
\[\Sigma_B = \sum_{a=1}^\infty \sum_{c=1}^\infty \sum_{k=0}^\infty \frac{3^a}{4^{a+c+k} 5^c} = \left(\sum_{a=1}^\infty \left(\frac{3}{4}\right)^a\right) \left(\sum_{c=1}^\infty \left(\frac{1}{20}\right)^c\right) \left(\sum_{k=0}^\infty \left(\frac{1}{4}\right)^k\right).\]

Calculando cada factor:
\[\Sigma_B = (3) \cdot \left(\frac{1/20}{1 - 1/20}\right) \cdot \left(\frac{1}{1 - 1/4}\right) = 3 \cdot \frac{1}{19} \cdot \frac{4}{3} = \frac{4}{19}.\]

### 3. Suma sobre $C$
En $C$ tenemos $a \ge 1$, $b \ge 1$ y $c \ge a + b$. Escribiendo $c = a + b + k$ con $k \ge 0$:
\[\Sigma_C = \sum_{a=1}^\infty \sum_{b=1}^\infty \sum_{k=0}^\infty \frac{3^a}{4^b 5^{a+b+k}} = \left(\sum_{a=1}^\infty \left(\frac{3}{5}\right)^a\right) \left(\sum_{b=1}^\infty \left(\frac{1}{20}\right)^b\right) \left(\sum_{k=0}^\infty \left(\frac{1}{5}\right)^k\right).\]

Calculando cada factor:
\[\Sigma_C = \left(\frac{3}{2}\right) \cdot \left(\frac{1}{19}\right) \cdot \left(\frac{1}{1 - 1/5}\right) = \frac{3}{2} \cdot \frac{1}{19} \cdot \frac{5}{4} = \frac{15}{152}.\]

### Resultado final
Restando las contribuciones de $B$ y $C$ a la suma sobre $T$:
\[\sum_{(a,b,c) \in S} \frac{3^a}{4^b 5^c} = \Sigma_T - \Sigma_B - \Sigma_C = \frac{17}{8} - \frac{4}{19} - \frac{15}{152}.\]

Usando el denominador común $152 = 8 \times 19$:
\[\sum_{(a,b,c) \in S} \frac{3^a}{4^b 5^c} = \frac{323 - 32 - 15}{152} = \frac{276}{152} = \frac{69}{38}.\]

\boxed{\frac{69}{38}}