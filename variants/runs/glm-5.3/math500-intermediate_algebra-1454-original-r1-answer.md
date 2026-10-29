## Solución

**Paso 1: Interpretar cada radical.**

Completando el cuadrado en el tercer término:
$$x^2 + y^2 - 80x - 100y + 4100 = (x-40)^2 + (y-50)^2.$$

Sea $P = (x,y)$ y $A = (40,50)$. Entonces:
$$F(x,y) = \underbrace{\sqrt{x^2 + 20^2}}_{\text{catetos } x,\,20} + \underbrace{\sqrt{y^2 + 30^2}}_{\text{catetos } y,\,30} + \underbrace{PA}_{\text{distancia } P \to A}.$$

**Paso 2: Convexidad.**

Cada término es convexo; los dos primeros son *estrictamente* convexos, pues
$$\frac{d^2}{dx^2}\sqrt{x^2+400} = \frac{400}{(x^2+400)^{3/2}} > 0, \qquad \frac{d^2}{dy^2}\sqrt{y^2+900} = \frac{900}{(y^2+900)^{3/2}} > 0.$$
Como $F$ es estrictamente convexa, cualquier punto crítico interior es el **único mínimo global**. Basta encontrarlo.

**Paso 3: Ecuaciones de primer orden.**

Con $d = PA$, introducimos ángulos agudos: $\tan\alpha = \frac{x}{20}$, $\tan\beta = \frac{y}{30}$, y $\theta$ el ángulo de $\vec{PA} = (40-x,\,50-y)$ con el eje $x$. Entonces:
$$\frac{\partial F}{\partial x} = \frac{x}{\sqrt{x^2+400}} + \frac{x-40}{d} = 0 \iff \sin\alpha = \cos\theta \iff \alpha = 90^\circ - \theta,$$
$$\frac{\partial F}{\partial y} = \frac{y}{\sqrt{y^2+900}} + \frac{y-50}{d} = 0 \iff \sin\beta = \sin\theta \iff \beta = \theta.$$

**Paso 4: Resolver el sistema.**

De $\tan\alpha = \cot\theta$ y $\tan\beta = \tan\theta$:
$$x(50-y) = 20(40-x), \qquad y(40-x) = 30(50-y).$$

Sustituyendo $u = 40-x$, $v = 50-y$ (o sea $x = 40-u$, $y = 50-v$):
$$(40-u)v = 20u, \qquad (50-v)u = 30v.$$
De la primera: $u = \frac{40v}{v+20}$. Sustituyendo en la segunda (con $v>0$):
$$\frac{40(50-v)}{v+20} = 30 \;\Rightarrow\; 2000 - 40v = 30v + 600 \;\Rightarrow\; v = 20, \quad u = 20.$$

Luego $(x,y) = (20,30)$, que está dentro del rectángulo ($0\le 20\le 40$, $0\le 30\le 50$).

**Paso 5: Valor y verificación.**

$$F(20,30) = \sqrt{800} + \sqrt{1800} + \sqrt{400+900-1600-3000+4100} = 20\sqrt2 + 30\sqrt2 + 20\sqrt2 = 70\sqrt2 \approx 98.99.$$

Comprobación de las derivadas: $\frac{20}{\sqrt{800}} - \frac{20}{\sqrt{800}} = 0$ y $\frac{30}{\sqrt{1800}} - \frac{20}{\sqrt{800}} = \frac{\sqrt2}{2} - \frac{\sqrt2}{2} = 0$. Por la convexidad estricta, es el mínimo global (las esquinas dan más; p. ej. $F(40,50) = \sqrt{2000}+\sqrt{3400}\approx 103$).

\boxed{70\sqrt{2}}