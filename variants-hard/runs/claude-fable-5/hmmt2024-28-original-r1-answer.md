## Planteamiento

El pentágono convexo $ABTCD$ se descompone con las diagonales $TA$ y $TD$ en tres triángulos: $TAB$, $TAD$ y $TCD$. Como las circunferencias de $TAB$ y $TCD$ son tangentes internamente, lo son en $T$ (ambas pasan por $T$), y comparten la recta tangente $\ell$ en $T$, quedando ambas del mismo lado de $\ell$.

Coloco $T$ en el origen con $\ell$ como eje $x$. Si un rayo desde $T$ forma ángulo $\alpha$ con $\ell$, la cuerda correspondiente en una circunferencia de radio $R$ tangente a $\ell$ en $T$ mide $2R\sin\alpha$ (ángulo semiinscrito). Con $\angle BTA=\beta$, $\angle CTD=\gamma$, la convexidad da $\beta+\gamma=30^\circ$ (pues $\angle BTC=120^\circ$ y $\angle ATD=90^\circ$). Si $\theta$ es el ángulo de $TB$ con $\ell$ y $\varphi=\theta+\beta$:

$$TB=2R_1\sin\theta=4,\quad TA=2R_1\sin\varphi,\quad TD=2R_2\cos\varphi,\quad TC=2R_2\sin(\theta+120^\circ)=5.$$

**Condición $AB=CD$:** las cuerdas dan $2R_1\sin\beta=2R_2\sin\gamma$, es decir
$$\frac{4\sin\beta}{\sin\theta}=\frac{5\sin(30^\circ-\beta)}{\sin(\theta+120^\circ)}\;\Longrightarrow\;\tan\beta=\frac{5\sin\theta}{4\sqrt3\cos\theta+(5\sqrt3-4)\sin\theta}.$$

**Condición de área:** con $s=\sin\theta$, $u=\sin(\theta+120^\circ)$,
$$[ABT]+[TCD]+[TAD]=\frac{8u\sin\varphi\sin\beta+10u\sin\beta\cos\varphi+10\sin\varphi\cos\varphi}{su}=22,$$
donde usé $12.5\,s\sin\gamma=10\,u\sin\beta$ (de la condición $AB=CD$).

## Resolución

Resolviendo el sistema en $\theta$ (la función es monótona en la región válida $\theta<60^\circ$), la raíz está en $\theta\approx 58.17^\circ$, con $\beta\approx 29.17^\circ$, $\gamma\approx 0.83^\circ$, $\varphi\approx 87.37^\circ$. Verificación: $TA\approx 4.70$, $TD\approx 7.29$, y las áreas son $[ABT]\approx 4.58$, $[TCD]\approx 0.26$, $[TAD]\approx 17.149$, que suman $22$. ✓

El área buscada es
$$[TAD]=\tfrac12\,TA\cdot TD=\frac{5\sin 2\varphi}{\sin\theta\,\sin(\theta+120^\circ)}\approx 17.1489 = 64(2-\sqrt3).$$

$$\boxed{64\left(2-\sqrt{3}\right)}$$