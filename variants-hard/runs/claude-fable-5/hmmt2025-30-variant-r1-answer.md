## Planteamiento

Coloco la caja como $[0,a]\times[0,b]\times[0,c]$ y el plano como $px+qy+rz=d$ con $p,q,r>0$ y $p^2+q^2+r^2=1$. El hexágono tiene sus vértices en seis aristas de la caja, y cada lado yace en una cara; los lados opuestos del hexágono están en caras opuestas.

Calculando los vértices y las longitudes de los lados en orden, se obtiene (con $u=\sqrt{\tfrac1{p^2}+\tfrac1{r^2}}$, $v=\sqrt{\tfrac1{p^2}+\tfrac1{q^2}}$, $w=\sqrt{\tfrac1{q^2}+\tfrac1{r^2}}$):

$$S_1=\alpha u,\quad S_2=\beta v,\quad S_3=\gamma w,\quad S_4=\delta u,\quad S_5=\varepsilon v,\quad S_6=\zeta w,$$

donde $\alpha=pa+rc-d$, $\beta=d-rc$, $\gamma=qb+rc-d$, $\delta=d-qb$, $\varepsilon=pa+qb-d$, $\zeta=d-pa$.

## Clave: diferencias de lados opuestos

Nótese que
$$\alpha-\delta=\varepsilon-\beta=\gamma-\zeta=pa+qb+rc-2d =: s,$$
y la distancia del centro $(a/2,b/2,c/2)$ al plano es exactamente $|s|/2$.

Con los lados $44,60,54,52,50,66$ (pares opuestos: $44\&52$, $60\&50$, $54\&66$):

$$s=\frac{44-52}{u}=\frac{50-60}{v}=\frac{54-66}{w}\ \Rightarrow\ u=\frac{8}{t},\ v=\frac{10}{t},\ w=\frac{12}{t},\quad t:=|s|.$$

## Resolviendo

De $u^2,v^2,w^2$ despejo:
$$\frac1{p^2}=\frac{u^2+v^2-w^2}{2}=\frac{10}{t^2},\qquad \frac1{q^2}=\frac{90}{t^2},\qquad \frac1{r^2}=\frac{54}{t^2}.$$

La normalización $p^2+q^2+r^2=1$ da
$$t^2\left(\frac1{10}+\frac1{90}+\frac1{54}\right)=t^2\cdot\frac{27+3+5}{270}=t^2\cdot\frac{7}{54}=1\ \Rightarrow\ t^2=\frac{54}{7}.$$

Por tanto la distancia es
$$\frac{t}{2}=\frac12\sqrt{\frac{54}{7}}=\sqrt{\frac{27}{14}}=\frac{3\sqrt{42}}{14}.$$

(Verificación del método: con los datos del problema clásico $45,66,63,55,54,77$ este mismo procedimiento da $\sqrt{95/24}$, el resultado conocido.)

$$\boxed{\dfrac{3\sqrt{42}}{14}}$$