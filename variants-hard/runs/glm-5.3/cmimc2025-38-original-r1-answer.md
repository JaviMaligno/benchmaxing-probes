# Resolución

**Paso 1: Los puntos fijos.**

Las raíces de $x^{2}+2x+5=0$ son $A=-1+2i$ y $B=-1-2i$. Sea $p,q$ las raíces de $x^{2}-2mx+25=0$, de modo que $p+q=2m$ y $pq=25$; es decir, $q=25/p$ y $m=\tfrac12\left(p+\tfrac{25}{p}\right)$.

**Paso 2: La familia de circunferencias por $A$ y $B$.**

Toda circunferencia que pasa por $A$ y $B$ tiene centro en el eje real. Su ecuación se escribe
$$C_D:\ |z|^{2}+D\,\mathrm{Re}(z)+D-5=0,$$
y una verificación directa muestra que $A,B\in C_D$ para todo $D$ real. (Su radio$^2=\tfrac{D^2}{4}-D+5>0$ siempre.)

**Paso 3: Condición de conciclicidad.**

Escribiendo $P=|p|^{2}$, $u=\mathrm{Re}(p)$:
- $p\in C_D$ equivale a $\;P+Du+D-5=0$ \ (Ec. 1)
- Como $q=\tfrac{25\bar p}{P}$, se tiene $|q|^{2}=\tfrac{625}{P}$ y $\mathrm{Re}(q)=\tfrac{25u}{P}$, así que $q\in C_D$ equivale a $\;625+25Du+(D-5)P=0$ \ (Ec. 2)

Un cálculo clave muestra la identidad:
$$\text{(Ec. 2)} = 25\cdot\text{(Ec. 1)} + (D-30)(P-25).$$

Por lo tanto, existen una circunferencia $C_D$ que contiene a los cuatro puntos **si y solo si** se cumple (Ec. 1) junto con $D=30$ o $P=25$.

**Paso 4: Caso $P=25$ (es decir, $|p|=5$).**

Entonces $q=25/p=\bar p$, y la (Ec. 1) exige $D(u+1)=-20$, posible salvo $u=-1$. Como $C_D$ es simétrica respecto al eje real, $\bar p\in C_D$ automáticamente. Esto da
$$m=\tfrac{p+\bar p}{2}=\mathrm{Re}(p)\in[-5,5]\quad (\text{segmento real, longitud } 10).$$
(El punto $m=-1$ da cuatro puntos colineales, un punto aislado que no afecta la longitud.)

**Paso 5: Caso $D=30$.**

Aquí $C_{30}$ es la circunferencia de centro $(-15,0)$ y radio $10\sqrt2$, y la condición es simplemente $p\in C_{30}$. Parametrizando $p=x+iy\in C_{30}$, es decir $y^{2}=-x^{2}-30x-25$ y $P=-30x-25$, con $m=s+it$:
$$s=\frac{3x^{2}}{6x+5},\qquad t=\frac{y(3x+5)}{6x+5}.$$
Sustituyendo $w=6x+5$ y eliminando $w$ (usando $w^{2}+25=(10+12s)w$) se obtiene limpiamente
$$3s^{2}+3t^{2}+50s+75=0 \iff \left(s+\tfrac{25}{3}\right)^{2}+t^{2}=\left(\tfrac{20}{3}\right)^{2},$$
una circunferencia de centro $-\tfrac{25}{3}$ y radio $\tfrac{20}{3}$. (Verificación: $p=-15+10\sqrt2\,i$ produce $m=-\tfrac{135}{17}+\tfrac{80\sqrt2}{17}i$, que satisface la ecuación; y $s$ recorre exactamente $[-15,-\tfrac53]$, cubriendo la circunferencia completa dos veces, pero como conjunto es una sola vuelta.)

**Paso 6: Longitud total.**

El conjunto $U$ es la unión de:
- la circunferencia de radio $\tfrac{20}{3}$: longitud $2\pi\cdot\tfrac{20}{3}=\tfrac{40\pi}{3}$;
- el segmento real $[-5,5]$: longitud $10$.

$$\frac{40\pi}{3}+10=\frac{10(4\pi+3)}{3}$$

$$\boxed{\dfrac{10(4\pi+3)}{3}}$$