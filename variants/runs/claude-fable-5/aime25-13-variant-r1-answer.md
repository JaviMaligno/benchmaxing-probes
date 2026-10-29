## Planteamiento

Para cuerdas en un disco en posición general, la fórmula de Euler da:

$$R = 1 + L + I$$

donde $L$ es el número de cuerdas e $I$ el número de puntos de intersección interiores. Con $L = 18$ fijo, solo hay que calcular $E[I]$.

## Intersecciones esperadas

**1. Entre los dos diámetros:** se cortan en el centro, aportando exactamente $1$.

**2. Cada segmento aleatorio con los diámetros:** los dos extremos caen en cuadrantes distintos, y los 6 pares de cuadrantes (4 adyacentes, 2 opuestos) son equiprobables. Si los cuadrantes son adyacentes (prob. $2/3$) el segmento cruza $1$ diámetro; si son opuestos (prob. $1/3$) cruza los $2$:

$$E = \tfrac{2}{3}\cdot 1 + \tfrac{1}{3}\cdot 2 = \tfrac{4}{3} \quad\Rightarrow\quad 16\cdot\tfrac{4}{3} = \tfrac{64}{3}.$$

**3. Entre pares de segmentos aleatorios:** condicionando en los pares de cuadrantes de cada segmento (36 combinaciones equiprobables) y usando que dos cuerdas se cortan si y solo si sus extremos se alternan en la circunferencia:

- Opuesto–opuesto, mismo par (2 casos): prob. $1/2$. Pares opuestos distintos (2 casos): prob. $1$ (siempre se alternan).
- Opuesto–adyacente (16 casos): siempre comparten un cuadrante; prob. $1/2$.
- Adyacente–adyacente: mismo par (4 casos) o compartiendo un cuadrante (8 casos): prob. $1/2$; pares adyacentes disjuntos como $\{1,2\}$ y $\{3,4\}$ (4 casos): prob. $0$.

$$P(\text{corte}) = \frac{2\cdot\frac12 + 2\cdot 1 + 16\cdot\frac12 + 12\cdot\frac12 + 4\cdot 0}{36} = \frac{17}{36}.$$

Con $\binom{16}{2} = 120$ pares:

$$E = 120\cdot\frac{17}{36} = \frac{170}{3}.$$

## Resultado

$$E[R] = 1 + 18 + \underbrace{1}_{\text{diámetros}} + \underbrace{\tfrac{64}{3}}_{\text{con diámetros}} + \underbrace{\tfrac{170}{3}}_{\text{entre segmentos}} = 20 + \frac{234}{3} = 20 + 78 = 98.$$

$$\boxed{98}$$