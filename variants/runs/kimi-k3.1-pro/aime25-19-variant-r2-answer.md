Usamos \(\log_a(7^b)=b\log_a7=\dfrac{b\ln7}{\ln a}\). Así, cada factor se simplifica como

\[
\frac{\log_k(7^{k^2-1})}{\log_{k+1}(7^{k^2-4})}
=\frac{k^2-1}{k^2-4}\cdot\frac{\ln(k+1)}{\ln k}
=\frac{k-1}{k-2}\cdot\frac{k+1}{k+2}\cdot\frac{\ln(k+1)}{\ln k}.
\]

Al multiplicar desde \(k=3\) hasta \(80\), los tres productos telescópicos dan

\[
\prod_{k=3}^{80}\frac{k-1}{k-2}=79,\qquad
\prod_{k=3}^{80}\frac{k+1}{k+2}=\frac4{82},\qquad
\prod_{k=3}^{80}\frac{\ln(k+1)}{\ln k}
=\frac{\ln81}{\ln3}=4.
\]

Por tanto, el producto original es

\[
79\cdot\frac4{82}\cdot4=\frac{632}{41}.
\]

Como \(632\) y \(41\) son primos relativos, \(m=632\) y \(n=41\). Luego,

\[
\boxed{673}
\]