## Planteamiento

Queremos maximizar
$$f(x,y)=\frac{x-y}{x^4+y^4+6}.$$

**Paso 1: El denominador siempre es positivo.**
Como $x^4+y^4\ge 0$, se tiene $x^4+y^4+6\ge 6>0$. Por lo tanto, dividir entre él no invierte desigualdades.

**Paso 2: Reducir a una desigualdad.**
Si logramos probar que
$$4(x-y)\le x^4+y^4+6 \quad\text{para todo } (x,y),$$
entonces $f(x,y)\le \tfrac14$ para todo $(x,y)$.

**Paso 3: Minimizar $g(x,y)=x^4+y^4-4x+4y+6$.**
La función $g$ es separable:
$$g(x,y)=\underbrace{(x^4-4x)}_{\text{solo }x}+\underbrace{(y^4+4y)}_{\text{solo }y}+6.$$

- Para $h_1(x)=x^4-4x$: $h_1'(x)=4x^3-4=0\iff x=1$, con $h_1''(1)=12>0$; mínimo global (la función es coerciva) con valor $h_1(1)=-3$.
- Para $h_2(y)=y^4+4y$: $h_2'(y)=4y^3+4=0\iff y=-1$, con $h_2''(-1)=12>0$; mínimo global con valor $h_2(-1)=-3$.

Por lo tanto:
$$g(x,y)\ge -3-3+6=0,$$
con igualdad exactamente en $(x,y)=(1,-1)$. Es decir,
$$x^4+y^4+6\ge 4(x-y),$$
con igualdad únicamente en $(1,-1)$.

**Paso 4: Conclusión.**
Como el denominador es positivo:
$$f(x,y)=\frac{x-y}{x^4+y^4+6}\le \frac14,$$
y la igualdad se alcanza en $(x,y)=(1,-1)$:
$$f(1,-1)=\frac{1-(-1)}{1+1+6}=\frac{2}{8}=\frac14.$$

El valor máximo es $\boxed{\dfrac{1}{4}}$.