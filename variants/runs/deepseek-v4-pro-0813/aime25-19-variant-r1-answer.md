El producto es

$$P=\prod_{k=3}^{80} \frac{\log_k\left(7^{k^2-1}\right)}{\log_{k+1}\left(7^{k^2-4}\right)}.$$

Recordemos que $\log_a(b^c)=c\log_a b$ y $\log_a b=\dfrac{\ln b}{\ln a}$.

Entonces,

$$\log_k\left(7^{k^2-1}\right)=(k^2-1)\log_k 7 = (k^2-1)\frac{\ln 7}{\ln k},$$

y

$$\log_{k+1}\left(7^{k^2-4}\right)=(k^2-4)\log_{k+1}7=(k^2-4)\frac{\ln 7}{\ln(k+1)}.$$

Luego cada factor vale

$$\frac{k^2-1}{k^2-4}\cdot \frac{\ln(k+1)}{\ln k}.$$

Calculamos:

$$k^2-1=(k-1)(k+1),\qquad k^2-4=(k-2)(k+2).$$

Entonces

$$P=\prod_{k=3}^{80}\frac{(k-1)(k+1)}{(k-2)(k+2)}\cdot \frac{\ln(k+1)}{\ln k}
= \prod_{k=3}^{80}\frac{k-1}{k-2}\cdot \frac{k+1}{k+2}\cdot \frac{\ln(k+1)}{\ln k}.$$

Separando los productos:

$$\prod_{k=3}^{80}\frac{k-1}{k-2}=\frac{2}{1}\cdot\frac{3}{2}\cdots\frac{79}{78}=79.$$

$$\prod_{k=3}^{80}\frac{k+1}{k+2}=\frac{4}{5}\cdot\frac{5}{6}\cdots\frac{81}{82}=\frac{4}{82}=\frac{2}{41}.$$

$$\prod_{k=3}^{80}\frac{\ln(k+1)}{\ln k}=\frac{\ln 81}{\ln 3}=\log_3 81=4.$$

Por lo tanto,

$$P=79\cdot \frac{2}{41}\cdot 4=\frac{632}{41}.$$

Entonces $m=632$ y $n=41$, así que

$$m+n=632+41=673.$$

\boxed{673}