## Planteamiento

**Paso 1: Factorizar las desigualdades.**

$$x - yz < y - zx \iff x(1+z) - y(1+z) < 0 \iff (1+z)(x-y) < 0$$
$$y - zx < z - xy \iff y(1+x) - z(1+x) < 0 \iff (1+x)(y-z) < 0$$

**Paso 2: Coordenadas en el plano.**

Con $z = 75 - x - y$ tenemos $1+z = 76 - x - y$ y $y - z = x + 2y - 75$, así que en coordenadas $(x,y)$:

$$(76-x-y)(x-y) < 0 \qquad (1+x)(x+2y-75) < 0$$

Cada desigualdad exige que dos factores lineales tengan signos opuestos: son "cuñas" entre pares de rectas
$$L_1:\ y=x,\quad L_2:\ x+y=76,\quad L_3:\ x=-1,\quad L_4:\ x+2y=75.$$

- Desigualdad I: **I-a** $\{y>x,\ x+y<76\}$ o **I-b** $\{y<x,\ x+y>76\}$.
- Desigualdad II: **II-a** $\{x>-1,\ x+2y<75\}$ o **II-b** $\{x<-1,\ x+2y>75\}$.

**Paso 3: Las tres regiones.**

- **I-b ∩ II-b es vacía:** $y<x<-1$ obliga a $x+y<-2$, contradiciendo $x+y>76$. (Por eso hay solo tres regiones.)
- **I-a ∩ II-b** y **I-b ∩ II-a**: cuñas no acotadas entre $L_2$ y $L_4$ (vértice común $(77,-1)$), una a cada lado de $L_3$.
- **I-a ∩ II-a**: aquí $x+y<76$ es redundante (pues $y>x>-1$ da $x+y < (x+2y)-y < 75-y < 76$), quedando el triángulo $\{x>-1,\ y>x,\ x+2y<75\}$ — **la región finita**, con vértices
$$L_3\cap L_1 = (-1,-1),\qquad L_3\cap L_4 = (-1,38),\qquad L_1\cap L_4 = (25,25).$$

(Verificación con un punto interior, p. ej. $(7,20)$: $(76-27)(7-20)<0$ y $(8)(7+40-75)<0$ ✓.)

**Paso 4: Área.**

En coordenadas $(x,y)$, con la fórmula del shoelace:
$$\tfrac12\big|(-1)(38-25)+(-1)(25+1)+25(-1-38)\big| = \tfrac12|-13-26-975| = 507.$$

La parametrización $(x,y)\mapsto(x,\,y,\,75-x-y)$ del plano tiene elemento de área $\sqrt{1+1+1}=\sqrt{3}$, así que el área real es $507\sqrt{3}$.

**Verificación directa en 3D:** los vértices son $P_1=(25,25,25)$, $P_2=(-1,38,38)$, $P_3=(-1,-1,77)$, y
$$\tfrac12\left|(-26,13,13)\times(-26,-26,52)\right| = \tfrac12\left|(1014,1014,1014)\right| = 507\sqrt{3}.\ \checkmark$$

Por lo tanto, $a=507$, $b=3$ (libre de cuadrados), y

$$a+b = 507+3 = \boxed{510}$$