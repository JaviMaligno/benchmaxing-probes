## Planteamiento

Queremos maximizar
$$f(a,b)=\frac{a-b}{a^4+b^4+96}.$$

El denominador siempre es positivo, así que el máximo es positivo y requiere $a>b$.

**Paso 1: Reducir a una variable.**

Fijemos $s = a - b > 0$. Para este valor de $s$, conviene que el denominador sea lo más pequeño posible. Escribiendo $a = \frac{s}{2}+t$, $b = -\frac{s}{2}+t$, tenemos
$$a^4+b^4=\left(\tfrac{s}{2}+t\right)^4+\left(\tfrac{s}{2}-t\right)^4,$$
que es creciente en $|t|$ (los términos en $t$ de grado impar se cancelan y los pares suman). Por tanto el mínimo se alcanza en $t=0$, es decir $a=\frac{s}{2}$, $b=-\frac{s}{2}$, dando
$$a^4+b^4 \ge 2\left(\frac{s}{2}\right)^4 = \frac{s^4}{8}.$$

**Paso 2: Optimizar en $s$.**

Así que
$$f(a,b) \le \frac{s}{\frac{s^4}{8}+96} = \frac{8s}{s^4+768}.$$
Maximicemos $g(s)=\dfrac{8s}{s^4+768}$ para $s>0$. Derivando:
$$g'(s)=\frac{8(s^4+768)-8s\cdot 4s^3}{(s^4+768)^2}=\frac{8(768-3s^4)}{(s^4+768)^2}.$$
Se anula cuando $s^4=256$, es decir $s=4$, y $g'$ cambia de positiva a negativa ahí, así que es máximo:
$$g(4)=\frac{32}{256+768}=\frac{32}{1024}=\frac{1}{32}.$$

**Paso 3: Verificar que se alcanza.**

Con $s=4$ tomamos $a=2$, $b=-2$:
$$\frac{2-(-2)}{2^4+(-2)^4+96}=\frac{4}{16+16+96}=\frac{4}{128}=\frac{1}{32}. \checkmark$$

Por lo tanto, el mayor valor posible es
$$\boxed{\dfrac{1}{32}}$$