# Solución

## Planteamiento

Sea $k$ el valor común:
$$3(x^2+1)=4(y^2+1)=5(z^2+1)=k.$$
Como $z^2=\tfrac{k}{5}-1>0$, se cumple $k>5$.

## Paso 1: Sustitución trigonométrica

Al ser $x,y,z>0$, existen ángulos únicos $A,B,C\in\left(0,\tfrac{\pi}{2}\right)$ tales que
$$x=\tan A,\qquad y=\tan B,\qquad z=\tan C.$$

## Paso 2: La condición $xy+yz+zx=1$ fuerza $A+B+C=\tfrac{\pi}{2}$

Expandiendo el coseno de una suma triple:
$$\cos(A+B+C)=\cos A\cos B\cos C\,\bigl(1-\tan A\tan B-\tan B\tan C-\tan C\tan A\bigr)=\cos A\cos B\cos C\,(1-xy-yz-zx)=0.$$
Como $0<A,B,C<\tfrac{\pi}{2}$, la suma está en $\left(0,\tfrac{3\pi}{2}\right)$ y no puede alcanzar $\tfrac{3\pi}{2}$; por tanto
$$A+B+C=\frac{\pi}{2}.$$

## Paso 3: Identidad clave

Si $A+B+C=\tfrac{\pi}{2}$, entonces
$$\sin^2 A+\sin^2 B+\sin^2 C=1-2\sin A\,\sin B\,\sin C. \qquad (\star)$$
*Prueba:* de $\cos C=\sin(A+B)=\sin A\cos B+\cos A\sin B$ se obtiene, elevando al cuadrado y usando $\cos(A+B)=\sin C$:
$$\cos^2 C=\sin^2 A+\sin^2 B+2\sin A\sin B\sin C;$$
sumando $\sin^2 C$ a ambos lados queda $(\star)$. $\blacksquare$

## Paso 4: Cosenos desde la primera condición

De $k=3\sec^2 A=4\sec^2 B=5\sec^2 C$:
$$\cos^2 A=\frac{3}{k},\quad \cos^2 B=\frac{4}{k},\quad \cos^2 C=\frac{5}{k}
\;\Longrightarrow\;
\sin^2 A=\frac{k-3}{k},\;\; \sin^2 B=\frac{k-4}{k},\;\; \sin^2 C=\frac{k-5}{k}.$$

## Paso 5: Ecuación para $k$

Sustituyendo en $(\star)$:
$$\frac{(k-3)+(k-4)+(k-5)}{k}=\frac{3k-12}{k}=1-\frac{2\sqrt{(k-3)(k-4)(k-5)}}{k^{3/2}}
\;\Longleftrightarrow\;
\frac{6-k}{k}=\frac{\sqrt{(k-3)(k-4)(k-5)}}{k^{3/2}}.$$
El lado derecho es positivo (pues $k>5$), luego $k<6$. Elevando al cuadrado y multiplicando por $k^3$:
$$(6-k)^2\,k=(k-3)(k-4)(k-5).$$
Expandiendo ambos lados:
$$k^3-12k^2+36k=k^3-12k^2+47k-60\;\Longrightarrow\;11k=60\;\Longrightarrow\;k=\frac{60}{11}\in(5,6).\;\checkmark$$

## Paso 6: Cálculo de $x,y,z$ y verificación

$$x^2=\frac{k}{3}-1=\frac{20}{11}-1=\frac{9}{11}\;\Rightarrow\;x=\frac{3}{\sqrt{11}},\qquad
y^2=\frac{k}{4}-1=\frac{4}{11}\;\Rightarrow\;y=\frac{2}{\sqrt{11}},\qquad
z^2=\frac{k}{5}-1=\frac{1}{11}\;\Rightarrow\;z=\frac{1}{\sqrt{11}}.$$

**Verificación:**
- $3(x^2+1)=3\cdot\tfrac{20}{11}=\tfrac{60}{11}$, $\quad 4(y^2+1)=4\cdot\tfrac{15}{11}=\tfrac{60}{11}$, $\quad 5(z^2+1)=5\cdot\tfrac{12}{11}=\tfrac{60}{11}$. ✓
- $xy+yz+zx=\dfrac{6+2+3}{11}=1$. ✓

(La unicidad es clara: cualquier solución fuerza $k=\tfrac{60}{11}$, pues la ecuación es lineal en $k$ tras cancelar $k^3-12k^2$, y luego $x,y,z$ son las raíces cuadradas positivas únicas.)

## Conclusión

$$x+y+z=\frac{3+2+1}{\sqrt{11}}=\frac{6}{\sqrt{11}}=\frac{6\sqrt{11}}{11}\approx 1{,}809$$

$$\boxed{\dfrac{6\sqrt{11}}{11}}$$