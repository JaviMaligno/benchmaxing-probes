# Solución

## Paso 1: ¿Qué vale cada casilla después de $t$ minutos?

Como la actualización es simultánea y $\max$ se compone consigo misma, por inducción tras $t$ minutos cada casilla contiene

$$x_i^{(t)} = \max_{|k|\le t} x_{i+k},$$

es decir, el máximo de una **ventana cíclica de longitud $2t+1$**. Tras $60$ minutos: ventanas de longitud $121$.

## Paso 2: ¿Qué valores originales sobreviven?

Como los valores son continuos, son distintos casi seguramente. Un valor $x_j$ aparece en el círculo tras $60$ minutos si y solo si existe alguna ventana de $121$ posiciones consecutivas **que contenga a $j$** y en la que $x_j$ sea el máximo estricto; es decir, existe un bloque de $121$ posiciones consecutivas conteniendo a $j$ donde las otras $120$ posiciones tienen valores $< x_j$.

Por simetría cíclica (los valores son i.i.d.), la esperanza del número de valores distintos es

$$E = 1011 \cdot P(\text{el valor } x_1 \text{ sobrevive}).$$

## Paso 3: Condicionar en $x_1 = v$

Dado $x_1 = v$, los otros $1010$ valores son i.i.d. uniformes; cada uno es $< v$ con probabilidad $v$, independientemente.

Sea $\lambda$ la distancia (hacia la izquierda, cíclicamente) hasta el primer valor $> v$, y $\rho$ la análoga hacia la derecha.

- Si **ningún** valor supera $v$ (probabilidad $v^{1010}$), $x_1$ es el máximo global y sobrevive (su "hueco" mide $1011 \ge 121$).
- Si hay algún valor mayor, el bloque máximo de posiciones con valores $<v$ que contiene a $1$ tiene tamaño $\lambda + \rho - 1$, así que $x_1$ sobrevive $\iff \lambda + \rho \ge 122$.

Distribuciones: $P(\lambda = \ell) = v^{\ell-1}(1-v)$ para $1 \le \ell \le 1010$. Dado $\lambda = \ell$, las posiciones a la derecha a distancias $1,\dots, 1010-\ell$ no están restringidas por ese evento (son distintas de las de la izquierda, pues $121 \ll 1011$), así que $P(\rho \ge r \mid \lambda=\ell) = v^{r-1}$ siempre que $r \le 1011-\ell$; en particular para $r = 122-\ell$. Entonces:

$$
P(\text{sobrevive} \mid v) = v^{1010} + \underbrace{\sum_{\ell=1}^{121} v^{\ell-1}(1-v)\,v^{121-\ell}}_{\ell < 122:\ \rho \ge 122-\ell} + \underbrace{\sum_{\ell=122}^{1010} v^{\ell-1}(1-v)}_{\lambda \ge 122:\ \text{automático}}
$$

$$= v^{1010} + 121(1-v)v^{120} + \bigl(v^{121} - v^{1010}\bigr) = v^{120}\bigl(121 - 120v\bigr).$$

## Paso 4: Integrar sobre $v$

$$P(x_1 \text{ sobrevive}) = \int_0^1 v^{120}(121 - 120v)\,dv = 121\cdot\frac{1}{121} - 120\cdot\frac{1}{122} = 1 - \frac{60}{61} = \frac{1}{61}.$$

(De hecho, en general el resultado es $P = \frac{1}{t+1}$ siempre que $n \ge 2t+2$; verificado por enumeración completa en casos chicos: $n=4, t=1$ da exactamente $2$, y $n=5, t=1$ da esperanza $2.5 = \frac{n}{t+1}$.)

## Paso 5: Concluir

$$E = 1011 \cdot \frac{1}{61} = \frac{1011}{61}.$$

$$\boxed{\dfrac{1011}{61}}$$