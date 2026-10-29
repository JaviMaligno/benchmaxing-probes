Queremos los puntos de intersección de $p(x)$ y $q(x)$. Observo que ambos contienen **exactamente los mismos términos dependientes de $\lfloor x\rfloor$**:

$$e^{2x^2-|\lfloor x\rfloor|!},\qquad \binom{19+735235|\lfloor x\rfloor|}{2356},\qquad \phi(|\lfloor x\rfloor|+1)$$

y también el mismo término $51x^4$. Por lo tanto, al igualar $p(x)=q(x)$, todo esto se cancela para **todo** $x$, y queda solo:

$$\big(3x^3-4x^2+5x+2\big)=\big(4x^3-7x^2-8x+17\big)$$

$$-x^3+3x^2+13x-15=0 \quad\Longleftrightarrow\quad x^3-3x^2-13x+15=0$$

**Resuelvo la cúbica:** pruebo $x=1$:
$$1-3-13+15=0\ \checkmark$$

Divido entre $(x-1)$:
$$x^3-3x^2-13x+15=(x-1)(x^2-2x-15)=(x-1)(x-5)(x+3)$$

Raíces: $x=-3,\ 1,\ 5$.

**Verificación rápida en $x=5$:**
$$p:\ 51(625)+3(125)-4(25)+25+2=32177$$
$$q:\ 51(625)+4(125)-7(25)-40+17=32177\ \checkmark$$

Como el resto de términos es idéntico en ambas funciones, la intersección es genuina. El mayor valor de $x$ es $5$.

$$\boxed{5}$$