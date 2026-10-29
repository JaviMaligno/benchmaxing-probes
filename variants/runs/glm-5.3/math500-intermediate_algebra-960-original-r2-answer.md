## Planteamiento

Los triples de $T$ son ordenados y cumplen la desigualdad triangular **estricta**: $a<b+c$, $b<a+c$, $c<a+b$.

**Cambio de variables.** Para $(a,b,c)\in T$ defino
$$u=b+c-a,\qquad v=a+c-b,\qquad w=a+b-c,$$
que son enteros $\ge 1$. Inversamente,
$$a=\frac{v+w}{2},\qquad b=\frac{u+w}{2},\qquad c=\frac{u+v}{2},$$
que son enteros $\ge 1$ precisamente cuando $u\equiv v\equiv w \pmod 2$ (y entonces forman triángulo, pues $a<b+c \iff 0<2u$, etc.). Esto da una biyección entre $T$ y los triples $(u,v,w)\ge 1$ con paridad común.

## Caso 1: $u,v,w$ impares

Escribo $u=2u'+1$, $v=2v'+1$, $w=2w'+1$ con $u',v',w'\ge 0$. Entonces $a=v'+w'+1$, $b=u'+w'+1$, $c=u'+v'+1$, y
$$\frac{2^a}{3^b5^c}=\frac{2}{15}\left(\frac1{15}\right)^{u'}\left(\frac25\right)^{v'}\left(\frac23\right)^{w'}.$$
Sumando las series geométricas:
$$S_{\text{impar}}=\frac{2}{15}\cdot\frac{15}{14}\cdot\frac{5}{3}\cdot 3=\frac{5}{7}.$$

## Caso 2: $u,v,w$ pares

Escribo $u=2u''$, $v=2v''$, $w=2w''$ con $u'',v'',w''\ge 1$. Ahora $a=v''+w''$, $b=u''+w''$, $c=u''+v''$, y
$$\frac{2^a}{3^b5^c}=\left(\frac{1}{15}\right)^{u''}\left(\frac25\right)^{v''}\left(\frac23\right)^{w''},$$
de modo que
$$S_{\text{par}}=\frac1{14}\cdot\frac23\cdot 2=\frac{2}{21}.$$

## Resultado

$$S=\frac57+\frac2{21}=\frac{15+2}{21}=\frac{17}{21}.$$

**Verificación independiente.** Para $(b,c)$ fijos, el rango válido de $a$ es $|b-c|<a<b+c$, así que
$$S=\sum_{b,c\ge1}\frac{2^{\,b+c}-2^{\,|b-c|+1}}{3^b5^c}=\frac43-\left(\frac17+\frac27+\frac2{21}\right)=\frac43-\frac{11}{21}=\frac{17}{21}.\ \checkmark$$

$$\boxed{\dfrac{17}{21}}$$