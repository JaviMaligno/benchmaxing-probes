**Paso 1: Simetría en $a$ y $b$.** La expresión depende de $a+b$ en el numerador y de $ab$ en el denominador. Fijando $a+b$, por AM-GM el producto $ab$ es máximo cuando $a=b$, lo que minimiza la expresión. Así que ponemos $a=b$.

**Paso 2: Reducir a una variable.** Con $a=b$, la expresión es
$$\frac{(2a+c)\big[4a^2+(2a+4c)^2\big]}{a^2c}=\frac{4(2a+c)(2a^2+4ac+4c^2)}{a^2c}.$$
Como es homogénea de grado 0, sea $x=c/a$:
$$f(x)=\frac{4(2+x)(4x^2+4x+2)}{x}=4\left(4x^2+12x+10+\frac{4}{x}\right).$$

**Paso 3: Minimizar.** Derivando:
$$f'(x)=4\left(8x+12-\frac{4}{x^2}\right)=0\;\Longrightarrow\;2x^3+3x^2-1=0.$$
Se verifica que $x=\tfrac12$ es raíz: $2\cdot\tfrac18+3\cdot\tfrac14-1=0$. Como $f\to\infty$ en $0^+$ y en $\infty$, este punto crítico es el mínimo.

**Paso 4: Evaluar.**
$$f\!\left(\tfrac12\right)=4\left(4\cdot\tfrac14+12\cdot\tfrac12+10+\tfrac{4}{1/2}\right)=4(1+6+10+8)=4\cdot 25=100.$$

El mínimo se alcanza, por ejemplo, con $a=b=2,\ c=1$: $(5)(16+64)/4=100$. ✓

$$\boxed{100}$$