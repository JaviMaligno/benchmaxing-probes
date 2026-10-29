Pinky no se enferma el día que se pone rosa exactamente cuando el total de camarones cae en **10 exactamente** (si salta de 9 a 11, ese mismo día se pone rosa y se enferma).

**Paso 1: Plantear la recurrencia.** Sea $p(n)$ la probabilidad de que el total acumulado pase por el valor $n$ en algún momento. Para alcanzar $n$, el último paso viene de $n-1$ (comiendo 1) o de $n-2$ (comiendo 2), cada uno con probabilidad $\tfrac12$:

$$p(n) = \tfrac12\,p(n-1) + \tfrac12\,p(n-2), \qquad p(0)=1,\ p(1)=\tfrac12.$$

**Paso 2: Resolver.** La ecuación característica $x^2 = \tfrac12 x + \tfrac12$ tiene raíces $x=1$ y $x=-\tfrac12$, así que

$$p(n) = \frac{2}{3} + \frac{1}{3}\left(-\frac12\right)^{n}.$$

(Verificación: $p(0)=1$, $p(1)=\tfrac23-\tfrac16=\tfrac12$. ✓)

**Paso 3: Evaluar en $n=10$.**

$$p(10) = \frac{2}{3} + \frac{1}{3}\cdot\frac{1}{1024} = \frac{2048 + 1}{3072} = \frac{2049}{3072} = \frac{683}{1024}.$$

$$\boxed{\dfrac{683}{1024}}$$