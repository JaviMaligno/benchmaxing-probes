Para calcular la suma dada, recordemos primero que una terna de enteros positivos $(a,b,c)$ pertenece a $T$ (es decir, forma los lados de un triángulo no degenerado) si y solo si cumple las desigualdades triangulares estrictas:
\[a < b + c, \quad b < a + c, \quad c < a + b.\]

Para cualesquiera $b, c \ge 1$ fijos, la condición sobre $a$ equivale a:
\[|b - c| + 1 \le a \le b + c - 1.\]

Sumando primero respecto a $a$, obtenemos una serie geométrica finita:
\[\sum_{a = |b-c|+1}^{b+c-1} 2^a = 2^{b+c} - 2^{|b-c|+1}.\]

Sustituyendo esto en la suma original $S$, podemos separarla en dos términos:
\[S = \sum_{b=1}^{\infty} \sum_{c=1}^{\infty} \frac{2^{b+c} - 2^{|b-c|+1}}{3^b 5^c} = S_1 - S_2,\]
donde
\[S_1 = \sum_{b=1}^{\infty} \sum_{c=1}^{\infty} \frac{2^{b+c}}{3^b 5^c} \quad \text{y} \quad S_2 = \sum_{b=1}^{\infty} \sum_{c=1}^{\infty} \frac{2^{|b-c|+1}}{3^b 5^c}.\]

**Cálculo de $S_1$:**
Podemos factorizar $S_1$ como el producto de dos series geométricas convergentes:
\[S_1 = \left(\sum_{b=1}^{\infty} \left(\frac{2}{3}\right)^b\right) \left(\sum_{c=1}^{\infty} \left(\frac{2}{5}\right)^c\right) = \frac{2/3}{1 - 2/3} \cdot \frac{2/5}{1 - 2/5} = 2 \cdot \frac{2}{3} = \frac{4}{3}.\]

**Cálculo de $S_2$:**
Dividimos la suma en tres casos según la relación entre $b$ y $c$:

1. **Caso $b = c$:**
   \[\sum_{b=1}^{\infty} \frac{2^1}{3^b 5^b} = 2 \sum_{b=1}^{\infty} \left(\frac{1}{15}\right)^b = 2 \cdot \frac{1/15}{1 - 1/15} = \frac{2}{14} = \frac{1}{7}.\]

2. **Caso $b > c$:** Haciendo el cambio de variable $b = c + k$ con $k \ge 1$:
   \[\sum_{c=1}^{\infty} \sum_{k=1}^{\infty} \frac{2^{k+1}}{3^{c+k} 5^c} = 2 \left(\sum_{c=1}^{\infty} \left(\frac{1}{15}\right)^c\right) \left(\sum_{k=1}^{\infty} \left(\frac{2}{3}\right)^k\right) = 2 \cdot \frac{1}{14} \cdot 2 = \frac{2}{7}.\]

3. **Caso $b < c$:** Haciendo el cambio de variable $c = b + k$ con $k \ge 1$:
   \[\sum_{b=1}^{\infty} \sum_{k=1}^{\infty} \frac{2^{k+1}}{3^b 5^{b+k}} = 2 \left(\sum_{b=1}^{\infty} \left(\frac{1}{15}\right)^b\right) \left(\sum_{k=1}^{\infty} \left(\frac{2}{5}\right)^k\right) = 2 \cdot \frac{1}{14} \cdot \frac{2}{3} = \frac{2}{21}.\]

Sumando los tres casos obtenemos $S_2$:
\[S_2 = \frac{1}{7} + \frac{2}{7} + \frac{2}{21} = \frac{3 + 6 + 2}{21} = \frac{11}{21}.\]

Finalmente, restamos $S_2$ de $S_1$:
\[S = \frac{4}{3} - \frac{11}{21} = \frac{28 - 11}{21} = \frac{17}{21}.\]

\boxed{\frac{17}{21}}