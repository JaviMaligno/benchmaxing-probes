# Planteamiento

Sea la caja $[0,a]\times[0,b]\times[0,c]$ y el plano $\mathcal Q:\ \alpha x+\beta y+\gamma z = D$ con $\alpha,\beta,\gamma>0$, cortando las 6 caras (sección hexagonal). Escribo $X=\alpha a$, $Y=\beta b$, $Z=\gamma c$, y $u=\tfrac1\alpha,\ v=\tfrac1\beta,\ w=\tfrac1\gamma$.

En una sección hexagonal de un ortoedro, **los lados opuestos del hexágono yacen sobre caras opuestas de la caja** (y por tanto son paralelos). Así, las parejas de lados opuestos son las posiciones $(1,4),(2,5),(3,6)$:
$$(44,52),\qquad (60,50),\qquad (54,66).$$

# Longitudes de los lados

Calculando los puntos de corte del plano con las aristas, los dos lados sobre las caras $x=a$ y $x=0$ miden:
$$(D-X)\sqrt{v^2+w^2} \qquad\text{y}\qquad (Y+Z-D)\sqrt{v^2+w^2},$$
y análogamente, con $m_2=\sqrt{u^2+v^2}$ y $m_3=\sqrt{u^2+w^2}$, los de las caras $z$ son $(X+Y-D)m_2,\ (D-Z)m_2$ y los de las caras $y$ son $(D-Y)m_3,\ (X+Z-D)m_3$.

# Ecuaciones clave

Sea $N = X+Y+Z-2D$. En cada pareja de lados opuestos, la **diferencia** de longitudes es $Nm_i$ (con el $m_i$ correspondiente). Por lo tanto:
$$|N|\,m_1 = 66-54 = 12,\qquad |N|\,m_3 = 60-50 = 10,\qquad |N|\,m_2 = 52-44 = 8.$$
(es decir, las diferencias $12,10,8$ forman un triángulo rectángulo). Entonces:
$$u^2=\frac{m_2^2+m_3^2-m_1^2}{2}=\frac{10}{N^2},\quad v^2=\frac{54}{N^2},\quad w^2=\frac{90}{N^2},$$
de donde
$$\alpha^2+\beta^2+\gamma^2=N^2\left(\frac1{10}+\frac1{54}+\frac1{90}\right)=N^2\cdot\frac{7}{54}.$$

# Distancia del centro al plano

El centro de la caja es $\left(\tfrac a2,\tfrac b2,\tfrac c2\right)$, así que la distancia al plano es
$$d=\frac{\left|\tfrac{X+Y+Z}{2}-D\right|}{\sqrt{\alpha^2+\beta^2+\gamma^2}}=\frac{|N|}{2\sqrt{\alpha^2+\beta^2+\gamma^2}}=\frac{|N|}{2|N|\sqrt{7/54}}=\frac12\sqrt{\frac{54}{7}}=\sqrt{\frac{27}{14}}=\frac{3\sqrt{42}}{14}.$$

(Verificación explícita: con $N=-1$ se obtiene $D=17$, $X=11{.}5$, $Y=11$, $Z=10{.}5$, $a=11{.}5\sqrt{10}$, $b=11\sqrt{54}$, $c=10{.}5\sqrt{90}$, y el hexágono mide exactamente $44,60,54,52,50,66$ en ese orden.)

$$\boxed{\dfrac{3\sqrt{42}}{14}}$$