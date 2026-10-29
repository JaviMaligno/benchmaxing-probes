## Planteamiento

Coloco coordenadas: $P=(0,0)$, $Q=(w,0)$, $R=(w,30)$, $S=(0,30)$, con $w=PQ$ lo buscado, y $Y=(x,y)$ interior.

**Condición $\angle PYQ=90^\circ$:** $Y$ está en la circunferencia de diámetro $PQ$, es decir
$$y^2=x(w-x).$$
Escribo $u=x$, $v=w-x$, $s=u+v=w$, de modo que $y^2=uv$.

**Triángulo $\triangle PYS$ ($R=17$):** el lado $PS=30$ se opone al ángulo en $Y$, así que $\sin\angle PYS=\frac{30}{34}=\frac{15}{17}$; al ser el triángulo acutángulo, $\cos\angle PYS=\frac{8}{17}$.

Con los vectores $\vec{YP}=(-u,-y)$, $\vec{YS}=(-u,30-y)$: el producto vectorial da $30u$, luego $|YP||YS|=34u$, y el producto escalar da
$$u^2+y^2-30y=\tfrac{8}{17}\cdot 34u=16u\ \Longrightarrow\ us-30y=16u.$$

**Triángulo $\triangle QYR$ ($R=25$):** $\sin\angle QYR=\frac{30}{50}=\frac35$, $\cos\angle QYR=\frac45$, y análogamente $|YQ||YR|=50v$, con
$$v^2+y^2-30y=\tfrac45\cdot 50v=40v\ \Longrightarrow\ vs-30y=40v.$$

## Resolución

De ambas: $30y=u(s-16)=v(s-40)$, luego $u=k(s-40)$, $v=k(s-16)$. Sustituyendo en $y^2=uv$:
$$\frac{k^2(s-40)^2(s-16)^2}{900}=k^2(s-40)(s-16)\ \Longrightarrow\ (s-16)(s-40)=900.$$

Es decir $s^2-56s-260=0$, de donde
$$s=28+6\sqrt{29}\approx 60{,}31$$
(la otra raíz es negativa).

**Verificación:** $k=\frac{s}{2s-56}\approx0{,}9333$, $u\approx18{,}96$, $v\approx41{,}36$, $y\approx28<30$, luego $Y$ es interior, y ambos triángulos resultan acutángulos.

$$\boxed{28+6\sqrt{29}}$$