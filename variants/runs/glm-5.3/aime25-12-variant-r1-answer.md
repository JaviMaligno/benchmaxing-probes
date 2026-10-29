## Planteamiento

**Paso 1: Factorizar las desigualdades.** Con $x+y+z=87$, calculamos las diferencias:

$$x-yz-(y-zx)=x-y+z(x-y)=(x-y)(1+z)$$
$$y-zx-(z-xy)=y-z+x(y-z)=(y-z)(1+x)$$

La cadena $x-yz<y-zx<z-xy$ equivale a:
$$(x-y)(1+z)<0 \qquad (y-z)(1+x)<0$$

**Paso 2: Parametrizar el plano.** Sea $u=x-y$, $v=y-z$. Entonces:
$$x=29+\tfrac{2u+v}{3},\qquad y=29+\tfrac{v-u}{3},\qquad z=29-\tfrac{u+2v}{3}$$

Según los signos de $1+x$ y $1+z$ hay cuatro casos; dos resultan vacíos o iguales a los demás ($u>0,v>0$ obliga a $x>z$... y con $x<-1$ sería vacío), quedando **tres regiones convexas disjuntas**:

- **Caso $x>-1,\ z>-1$:** exige $u<0,\ v<0$, con $2u+v>-90$ y $u+2v<90$ (automático).
- **Caso $x<-1,\ z>-1$:** $u<0,\ v>0$, $2u+v<-90$: región no acotada.
- **Caso $x>-1,\ z<-1$:** $u>0,\ v<0$, $u+2v>60$: región no acotada.

**Paso 3: La región finita** es la del primer caso: el triángulo en el plano $(u,v)$ con
$$u<0,\qquad v<0,\qquad 2u+v>-90,$$
cuyos vértices son $(0,0)$, $(-45,0)$, $(0,-90)$. Su área en el plano de parámetros es $\tfrac12\cdot 45\cdot 90=2025$.

**Paso 4: Corrección de escala.** El área física en $\mathbb{R}^3$ usa los vectores tangentes $t_u=\tfrac13(2,-1,-1)$, $t_v=\tfrac13(1,1,-2)$:
$$|t_u\times t_v|^2=|t_u|^2|t_v|^2-(t_u\cdot t_v)^2=\tfrac49-\tfrac19=\tfrac13$$

Así que el área verdadera es $\dfrac{2025}{\sqrt{3}}=675\sqrt{3}$.

**Verificación directa:** los vértices físicos son $(29,29,29)$, $(-1,44,44)$, $(-1,-1,89)$; con lados $15\sqrt6$, $30\sqrt6$ y ángulo de $60°$ entre ellos:
$$\text{Área}=\tfrac12\cdot 15\sqrt6\cdot 30\sqrt6\cdot\tfrac{\sqrt3}{2}=675\sqrt3\ \checkmark$$

(Un punto interior de prueba: $(19,29,39)$ da $-1112<-712<-512$, que cumple la cadena.)

Entonces $a=675$, $b=3$, y $a+b=678$.

$$\boxed{678}$$