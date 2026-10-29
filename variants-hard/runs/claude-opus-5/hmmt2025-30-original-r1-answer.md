## Planteamiento

Coloco el prisma como $[0,a]\times[0,b]\times[0,c]$ y el plano como $ux+vy+wz=h$ con $u,v,w>0$. Definiendo $X=\sqrt{u^{-2}+v^{-2}}$, $Y=\sqrt{v^{-2}+w^{-2}}$, $Z=\sqrt{u^{-2}+w^{-2}}$, las seis aristas del hexágono (en orden, sobre las caras $z=0,\;x=a,\;y=0,\;z=c,\;x=0,\;y=b$) resultan:

$$(ua+vb-h)X,\quad (h-ua)Y,\quad (ua+wc-h)Z,\quad (h-wc)X,\quad (vb+wc-h)Y,\quad (h-vb)Z$$

## Uso de las diferencias de lados opuestos

Con $T=ua+vb+wc-2h$, las diferencias de lados opuestos dan:

$$TX=45-55=-10,\qquad -TY=66-54=12,\qquad TZ=63-77=-14$$

Luego, con $t=|T|$: $\;X=\tfrac{10}{t},\;Y=\tfrac{12}{t},\;Z=\tfrac{14}{t}$.

## Recuperar $u,v,w$

Con $U=u^{-2},V=v^{-2},W=w^{-2}$:

$$U+V=\frac{100}{t^2},\qquad V+W=\frac{144}{t^2},\qquad U+W=\frac{196}{t^2}$$

de donde $U+V+W=\frac{220}{t^2}$ y por tanto

$$U=\frac{76}{t^2},\qquad V=\frac{24}{t^2},\qquad W=\frac{120}{t^2}$$

es decir $u^2=\tfrac{t^2}{76},\;v^2=\tfrac{t^2}{24},\;w^2=\tfrac{t^2}{120}$.

(Las sumas de lados opuestos son consistentes: dan $ua=vb=wc=10t$ y $h=\tfrac{31}{2}t$, que reproducen exactamente $45,66,63,55,54,77$.)

## Distancia del centro

El centro es $(a/2,b/2,c/2)$, así que

$$d=\frac{|ua+vb+wc-2h|}{2\sqrt{u^2+v^2+w^2}}=\frac{t}{2\,t\sqrt{\frac1{76}+\frac1{24}+\frac1{120}}}$$

Y $\frac1{76}+\frac1{24}+\frac1{120}=\frac{30+95+19}{2280}=\frac{144}{2280}=\frac{6}{95}$, luego

$$d=\frac12\sqrt{\frac{95}{6}}=\frac{\sqrt{570}}{12}\approx 1.989$$

$$\boxed{\dfrac{\sqrt{570}}{12}}$$