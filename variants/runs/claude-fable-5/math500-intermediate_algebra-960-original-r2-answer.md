## Solución

**Sustitución de Ravi.** Las desigualdades triangulares $a<b+c$, $b<a+c$, $c<a+b$ equivalen a escribir
$$a=y+z,\quad b=z+x,\quad c=x+y$$
con $x,y,z>0$. Para que $a,b,c$ sean enteros positivos, $x,y,z$ deben ser **o todos enteros positivos, o todos semienteros impares** ($\tfrac12,\tfrac32,\dots$), y esta correspondencia es biyectiva con $T$.

El término general se factoriza:
$$\frac{2^a}{3^b 5^c}=\frac{2^{y+z}}{3^{z+x}5^{x+y}}=\left(\frac{1}{15}\right)^{x}\left(\frac{2}{5}\right)^{y}\left(\frac{2}{3}\right)^{z}.$$

**Caso 1: $x,y,z\in\{1,2,3,\dots\}$.**
$$\sum_{x\ge1}\Big(\tfrac1{15}\Big)^x\sum_{y\ge1}\Big(\tfrac25\Big)^y\sum_{z\ge1}\Big(\tfrac23\Big)^z=\frac{1/15}{14/15}\cdot\frac{2/5}{3/5}\cdot\frac{2/3}{1/3}=\frac{1}{14}\cdot\frac{2}{3}\cdot 2=\frac{2}{21}.$$

**Caso 2: $x,y,z\in\{\tfrac12,\tfrac32,\dots\}$.** Escribiendo $x=k+\tfrac12$, etc., con $k,m,n\ge0$, el factor común es
$$\Big(\tfrac1{15}\cdot\tfrac25\cdot\tfrac23\Big)^{1/2}=\sqrt{\tfrac{4}{225}}=\frac{2}{15},$$
y las series geométricas dan
$$\frac{2}{15}\cdot\frac{1}{1-\tfrac1{15}}\cdot\frac{1}{1-\tfrac25}\cdot\frac{1}{1-\tfrac23}=\frac{2}{15}\cdot\frac{15}{14}\cdot\frac{5}{3}\cdot 3=\frac{2}{14}\cdot 5=\frac{5}{7}=\frac{15}{21}.$$

**Total:**
$$\frac{2}{21}+\frac{15}{21}=\frac{17}{21}.$$

$$\boxed{\dfrac{17}{21}}$$