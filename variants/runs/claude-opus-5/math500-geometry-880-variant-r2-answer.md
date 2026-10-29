## Planteamiento

Coloco coordenadas: largo $x\in[0,15]$, ancho $y\in[0,12]$, alto $z\in[0,9]$.

- Paredes laterales ($12\times 9$): $x=0$ y $x=15$.
- Pared trasera ($15\times 9$): $y=0$; pared frontal: $y=12$.
- Araña: $A=(0,\;1,\;8)$ (a 1 ft del techo, a 1 ft de la pared trasera).
- Polilla: $M=(15,\;11,\;1)$ (a 1 ft del suelo, a 1 ft de la pared frontal).

El suelo está prohibido, así que hay que desplegar (unfold) las caras permitidas y medir rectas.

## Ruta 1: pared lateral → techo → pared lateral

Desplegando con el techo como base: $A\mapsto(-1,1)$ y $M\mapsto(23,11)$.

$$d=\sqrt{24^2+10^2}=\sqrt{676}=26$$

## Ruta 2: pared lateral → pared frontal (o trasera) → pared lateral

Recorrido horizontal $1+15+11=27$, diferencia vertical $8-1=7$:

$$d=\sqrt{27^2+7^2}=\sqrt{778}\approx 27.9$$

## Ruta 3: pared lateral → techo → pared frontal → pared lateral

Techo como base: la araña queda en $(-1,1)$. La pared frontal se despliega a $(x,\;21-z)$, y sobre ella se despliega la pared $x=15$: un punto $(15,y,z)$ va a $\big(15+(12-y),\;21-z\big)$, luego $M\mapsto(16,20)$.

$$d=\sqrt{17^2+19^2}=\sqrt{289+361}=\sqrt{650}=5\sqrt{26}\approx 25.495$$

Verificación de que la recta cruza las aristas en orden y dentro de cada cara: sale de la pared $x=0$ en $(0,\;2.12)$, cruza la arista techo–pared frontal en $x\approx 8.84\in[0,15]$, y pasa a la pared $x=15$ en la arista vertical a altura $z\approx 2.12\in[0,9]$. Es un camino admisible.

## Otras combinaciones

- Lateral → trasera → techo → lateral: $\sqrt{24^2+12^2}=\sqrt{720}\approx 26.8$
- Lateral → techo → trasera → lateral: $\sqrt{27^2+9^2}=\sqrt{810}\approx 28.5$
- Lateral → frontal → techo → lateral y rutas de cuatro caras: $\ge\sqrt{730}\approx 27$

La menor de todas es $5\sqrt{26}\approx 25.5$.

\boxed{5\sqrt{26}}