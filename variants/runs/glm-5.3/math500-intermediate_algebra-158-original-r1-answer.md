## Razonamiento

Queremos maximizar $P = ab^2c^3d^4$ con $a+b+c+d=10$, donde todas las variables son positivas.

**Método: AM-GM ponderado.**

Escribimos la suma de 10 términos (1 copia de $a$, 2 de $b/2$... más precisely, usamos las potencias como pesos):

$$\underbrace{\frac{a}{1}+\cdots+\frac{a}{1}}_{1}+\underbrace{\frac{b}{2}+\cdots+\frac{b}{2}}_{2}+\underbrace{\frac{c}{3}+\cdots+\frac{c}{3}}_{3}+\underbrace{\frac{d}{4}+\cdots+\frac{d}{4}}_{4} = a+b+c+d = 10.$$

Aplicando AM-GM a estos 10 términos:

$$\frac{10}{10} \geq \left(\left(\tfrac{a}{1}\right)^1\left(\tfrac{b}{2}\right)^2\left(\tfrac{c}{3}\right)^3\left(\tfrac{d}{4}\right)^4\right)^{1/10},$$

es decir,

$$1 \geq \frac{ab^2c^3d^4}{1^1\cdot 2^2\cdot 3^3\cdot 4^4} \quad\Longrightarrow\quad ab^2c^3d^4 \leq 2^2\cdot 3^3\cdot 4^4.$$

La igualdad se alcanza cuando todos los términos coinciden:

$$\frac{a}{1}=\frac{b}{2}=\frac{c}{3}=\frac{d}{4}=1 \quad\Longrightarrow\quad a=1,\ b=2,\ c=3,\ d=4,$$

que efectivamente suma $10$. El valor máximo es:

$$1^1\cdot 2^2\cdot 3^3\cdot 4^4 = 1\cdot 4\cdot 27\cdot 256 = 27648.$$

**Verificación por cálculo (Lagrange):** $\nabla$: $b^2c^3d^4 = \lambda$, $2ab\,c^3d^4=\lambda$, $3ab^2c^2d^4=\lambda$, $4ab^2c^3d^3=\lambda$ da $b=2a$, $c=3a$, $d=4a$, y $10a=10$ da $a=1$. Coincide.

$$\boxed{27648}$$