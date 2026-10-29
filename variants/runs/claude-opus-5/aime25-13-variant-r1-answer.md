## Planteamiento

Para cuerdas en posición general dentro de un disco, con $L$ segmentos e $I$ puntos de intersección interiores (todos cruces simples), el número de regiones es

$$R = 1 + L + I.$$

(Comprobación: dos diámetros dan $1+2+1=4$ regiones.)

Aquí $L = 18$, así que basta calcular $\mathbb{E}[I]$, separando tres tipos de cruces.

## 1. Los dos diámetros entre sí

Se cortan en el centro: **1** intersección.

## 2. Cada segmento con los diámetros

Con ejes $x,y$ como diámetros, los cuadrantes son $Q_1=(+,+),\ Q_2=(-,+),\ Q_3=(-,-),\ Q_4=(+,-)$.

Los dos extremos caen en cuadrantes distintos, y cada uno de los $\binom{4}{2}=6$ pares de cuadrantes es equiprobable: 4 pares adyacentes, 2 pares opuestos.

- **Cuadrantes adyacentes** (p. ej. $Q_1,Q_2$): ambos extremos tienen $y>0$, luego el segmento no corta el eje $x$ y corta el eje $y$ exactamente una vez → 1 cruce.
- **Cuadrantes opuestos** (p. ej. $Q_1,Q_3$): cambian de signo tanto $x$ como $y$ → 2 cruces.

$$\mathbb{E}[\text{cruces con diámetros}] = \tfrac{4}{6}\cdot 1 + \tfrac{2}{6}\cdot 2 = \tfrac{4}{3},$$

y para los 16 segmentos: $16\cdot\frac{4}{3} = \frac{64}{3}$.

## 3. Pares de los 16 segmentos

Sea $p$ la probabilidad de que dos segmentos aleatorios se corten. Condicionando en los pares de cuadrantes (36 combinaciones ordenadas equiprobables):

- **Mismo par de cuadrantes** (6 casos): los dos puntos de cada cuadrante se ordenan al azar; se cruzan con probabilidad $\tfrac12$.
- **Pares ajenos, ambos adyacentes** ($\{1,2\}$ vs $\{3,4\}$, etc., 4 casos): nunca se cruzan → $0$.
- **Las dos diagonales** ($\{1,3\}$ vs $\{2,4\}$, 2 casos): los extremos alternan siempre → $1$.
- **Comparten exactamente un cuadrante** (24 casos: 8 adyacente–adyacente, 16 adyacente–diagonal): el cruce depende solo del orden de los dos puntos del cuadrante común, equiprobable → $\tfrac12$.

$$p = \frac{6\cdot\frac12 + 4\cdot 0 + 2\cdot 1 + 8\cdot\frac12 + 16\cdot\frac12}{36} = \frac{3+2+4+8}{36} = \frac{17}{36}.$$

Con $\binom{16}{2}=120$ pares: $120\cdot\frac{17}{36} = \frac{170}{3}$.

## Resultado

$$\mathbb{E}[I] = 1 + \frac{64}{3} + \frac{170}{3} = 1 + 78 = 79,$$

$$\mathbb{E}[R] = 1 + 18 + 79 = 98.$$

\boxed{98}