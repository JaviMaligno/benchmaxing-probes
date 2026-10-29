## Solución

**Paso 1: Triángulos en B y E.**
En el triángulo $ABC$, con $AB=14$, $BC=7$ y $\angle B=60^\circ$, por ley de cosenos:
$$AC^2 = 14^2+7^2-2\cdot14\cdot7\cdot\tfrac12 = 147 \implies AC = 7\sqrt3.$$
Como $AC^2+BC^2 = 147+49 = 196 = AB^2$, el ángulo $\angle ACB = 90^\circ$ y $\angle BAC = 30^\circ$.

En el triángulo $AED$, con $EA=26$, $DE=13$ y $\angle E=60^\circ$:
$$AD^2 = 26^2+13^2-26\cdot13 = 507 \implies AD = 13\sqrt3,$$
y $AD^2+DE^2 = 507+169 = 676 = EA^2$, así que $\angle ADE = 90^\circ$ y $\angle DAE = 30^\circ$.

**Paso 2: Separar la suma.**
$$f(X) = \underbrace{(AX+CX+DX)}_{\text{punto de Fermat de } \triangle ACD} + \underbrace{(BX+EX)}_{\ge BE}.$$

**Mínimo de $AX+CX+DX$:** en $\triangle ACD$, con $AC=7\sqrt3$, $CD=24$, $AD=13\sqrt3$, se tiene $\cos\angle CAD = \frac{147+507-576}{2\cdot 7\sqrt3\cdot 13\sqrt3} = \frac17$, luego $\sin\angle CAD = \frac{4\sqrt3}{7}$ y el área es $\frac12\cdot 7\sqrt3\cdot 13\sqrt3\cdot\frac{4\sqrt3}{7} = 78\sqrt3$. Todos los ángulos son menores de $120^\circ$, así que el mínimo (en el punto de Fermat $P$) vale
$$\sqrt{\frac{AC^2+CD^2+AD^2+4\sqrt3\,[ACD]}{2}} = \sqrt{\frac{1230+936}{2}} = \sqrt{1083} = 19\sqrt3.$$

**Longitud de $BE$:** con coordenadas $A=(0,0)$, $C=(7\sqrt3,0)$, $D=\left(\tfrac{13\sqrt3}{7},\tfrac{156}{7}\right)$, se obtiene $B=(7\sqrt3,-7)$ y $E=\left(-\tfrac{39\sqrt3}{7},\tfrac{169}{7}\right)$ (verificando $DE=13$). Entonces
$$BE^2 = \left(\tfrac{88\sqrt3}{7}\right)^2+\left(\tfrac{218}{7}\right)^2 = \frac{23232+47524}{49} = 1444 \implies BE = 38.$$

**Paso 3: Las dos igualdades se alcanzan a la vez.**
En el punto de Fermat $P$, $\angle APC = 120^\circ$; como $\angle ABC = 60^\circ$, el cuadrilátero $ABCP$ es cíclico, y por ángulos inscritos $\angle APB = \angle ACB = 90^\circ$. Análogamente, $ADPE$ es cíclico y $\angle APE = \angle ADE = 90^\circ$. Como $B$ y $E$ quedan en lados opuestos de la recta $AP$, resulta $\angle BPE = 180^\circ$: el punto $P$ está sobre el segmento $BE$. Por tanto ambas cotas se alcanzan simultáneamente:
$$f_{\min} = 38 + 19\sqrt3.$$

Así $m=38$, $n=19$, $p=3$, y $m+n+p = 60$.

$$\boxed{60}$$