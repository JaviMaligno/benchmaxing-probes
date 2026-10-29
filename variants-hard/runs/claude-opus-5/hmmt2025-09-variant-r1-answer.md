## Planteamiento

Sea $p=2029$ (primo). Por interpolación de Lagrange en los nodos $1,2,\dots,2029$:

$$g(x)=\sum_{m\ \text{cuadrado}} \frac{N_m(x)}{D_m},\qquad N_m(x)=\prod_{j\ne m}(x-j),\quad D_m=\prod_{j\ne m}(m-j).$$

Los cuadrados en $\{1,\dots,2029\}$ son $1^2,\dots,45^2$ (pues $45^2=2025$, $46^2=2116$).

**Coeficiente de $x^{2027}$.** Como $N_m$ tiene grado $2028$ y raíces $\{1,\dots,2029\}\setminus\{m\}$, su coeficiente de $x^{2027}$ es $-(S-m)$ con $S=\sum_{j=1}^{2029}j=\tfrac{2029\cdot 2030}{2}$. Por tanto

$$[x^{2027}]g=\sum_{m\ \text{cuadrado}} \frac{-(S-m)}{D_m},\qquad D_m=(-1)^{2029-m}(m-1)!\,(2029-m)!.$$

**Reducción módulo 2029.** Los denominadores son productos de factoriales con factores $<2029$, así que $q$ es coprimo con $2029$ y basta evaluar la fracción módulo $p$.

- $S=2029\cdot 1015\equiv 0$, luego $-(S-m)\equiv m$.
- Por Wilson: $(-1)^{m-1}(m-1)!\,(p-m)!\equiv (p-1)!\equiv -1$, de donde $(m-1)!\,(p-m)!\equiv(-1)^m$.
- Con $(-1)^{2029-m}=(-1)^{m-1}$ queda $D_m\equiv(-1)^{m-1}(-1)^{m}=-1 \pmod{2029}$.

Entonces

$$[x^{2027}]g\equiv \sum_{k=1}^{45}\frac{k^2}{-1}=-\sum_{k=1}^{45}k^2=-\frac{45\cdot 46\cdot 91}{6}=-31395 \pmod{2029}.$$

**Cálculo final.** $31395=15\cdot 2029+960$, así que $-31395\equiv -960\equiv 1069 \pmod{2029}$.

*(Verificación del método con $p=5$: el coeficiente de $x^{3}$ resulta $5/4$, y la predicción $-(1+4)\equiv 0$ coincide con $0\equiv 4s$.)*

$$\boxed{1069}$$