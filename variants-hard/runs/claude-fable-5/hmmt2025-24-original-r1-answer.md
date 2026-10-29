## Planteamiento

Coloco el centro de $S_3$ en el origen $O$, con $A=(-10,0)$, $B=(10,0)$.

**Relación para $S_2$ dentro de $S_3$.** Sea $M_2$ el punto medio del diámetro de $S_2$ (su centro), con radio $r_2$. Como el arco de $S_2$ es tangente a $AB$ en $C=(m,0)$, el centro está a altura $r_2$: $M_2=(m,r_2)$.

El diámetro de $S_2$ es una cuerda de $S_3$: si $u$ es el vector unitario a lo largo de esa cuerda, sus extremos $M_2\pm r_2u$ están a distancia $10$ de $O$. Igualando $|M_2+r_2u|^2=|M_2-r_2u|^2=100$ se obtiene:
$$M_2\cdot u=0 \qquad\text{y}\qquad |M_2|^2+r_2^2=100.$$

De la segunda ecuación: $m^2+r_2^2+r_2^2=100$, es decir $m^2=100-2r_2^2$. Entonces:
$$AC\cdot CB=(10+m)(10-m)=100-m^2=2r_2^2.$$

**Relación para $S_1$ dentro de $S_2$.** Sea $M_1$ el centro de $S_1$ con radio $r_1=1$. Su diámetro es horizontal (paralelo a $AB$), con dirección $u_1$. Aplicando la misma condición de cuerda dentro del círculo de $S_2$:
$$(M_1-M_2)\cdot u_1=0 \qquad\text{y}\qquad |M_1-M_2|^2+1=r_2^2.$$

Como $u_1$ es horizontal, $M_1-M_2$ es vertical: $M_1-M_2=(0,d)$ con $d^2=r_2^2-1$.

**Tangencia del arco de $S_1$ con el diámetro de $S_2$.** La recta del diámetro de $S_2$ pasa por $M_2$ con dirección $u$, y como $M_2\cdot u=0$, su normal unitaria es $n=\dfrac{M_2}{|M_2|}=\dfrac{(m,r_2)}{\sqrt{m^2+r_2^2}}$. La distancia de $M_1$ a esa recta debe ser $1$:
$$\frac{|(0,d)\cdot(m,r_2)|}{\sqrt{m^2+r_2^2}}=\frac{d\,r_2}{\sqrt{m^2+r_2^2}}=1.$$

Usando $m^2+r_2^2=100-r_2^2$:
$$d^2r_2^2=100-r_2^2 \quad\Longrightarrow\quad (r_2^2-1)r_2^2=100-r_2^2.$$

Con $x=r_2^2$: $x^2-x=100-x$, de donde $x^2=100$ y $r_2^2=10$.

**Conclusión.**
$$AC\cdot CB=2r_2^2=20.$$

$$\boxed{20}$$