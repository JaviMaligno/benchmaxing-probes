## Solución

**Convención.** Cuadrantes I–IV en sentido antihorario; cada cuerda se obtiene eligiendo dos puntos uniformes en la circunferencia, condicionados a quedar en cuadrantes distintos. Como los cuatro arcos son iguales, cada cuerda elige su **par de cuadrantes uniformemente entre los 6 pares** (4 adyacentes, 2 opuestos), con puntos uniformes e independientes en los arcos.

**Paso 1: Fórmula de conteo.** Con probabilidad $1$ los $18$ segmentos están en posición general (ningún punto triple interior, ningún extremo repetido, ninguna cuerda por el centro). Añadiendo los segmentos uno a uno, un segmento nuevo que cruza a $k$ anteriores queda cortado en $k+1$ trozos y cada trozo parte una región en dos, así que

$$R \;=\; 1 + 18 + I \;=\; 19 + I,$$

donde $I$ es el número total de puntos de intersección **interiores** entre pares de segmentos. Por linealidad, basta calcular $E[I]=\sum_{\text{pares}}P(\text{cruce})$.

**Paso 2: par diámetro–diámetro.** Se cruzan en el centro: aporta $\;1$.

**Paso 3: pares diámetro–cuerda ($32$ pares).** Una cuerda cruza un diámetro dado sii sus extremos quedan en lados opuestos de la recta del diámetro (la cuerda está dentro del disco, así que el cruce con la recta cae dentro del diámetro). Para el eje $x$: los pares de cuadrantes que separan arriba/abajo son $\{I,III\},\{I,IV\},\{II,III\},\{II,IV\}$, es decir $4$ de $6$:

$$P=\frac{4}{6}=\frac23,\qquad\text{aporte } 32\cdot\frac23=\frac{64}{3}.$$

**Paso 4: pares cuerda–cuerda ($\binom{16}{2}=120$ pares).** Dos cuerdas se cruzan en el interior **ssi sus extremos se alternan** en la circunferencia. Fijemos la cuerda 1 y promediemos sobre la cuerda 2.

*Cuerda 1 en cuadrantes adyacentes* (p. ej. $a\in$ QI, $b\in$ QII; prob. $\tfrac46$). Cuerda 2 según su par de cuadrantes:

| par de cuerda 2 | I–II | II–III | III–IV | IV–I | I–III | II–IV |
|---|---|---|---|---|---|---|
| $P(\text{cruce})$ | $\tfrac12$ | $\tfrac12$ | $0$ | $\tfrac12$ | $\tfrac12$ | $\tfrac12$ |

(En los casos con $\tfrac12$, el cruce depende del orden relativo de los extremos que comparten un mismo arco de cuadrante —una moneda al aire—; con cuerda 2 en III–IV ambos extremos caen en el mismo lado de la cuerda 1 y nunca cruzan.)

$$\text{media}=\frac{\tfrac12\cdot 5+0}{6}=\frac5{12}.$$

*Cuerda 1 en cuadrantes opuestos* (p. ej. $a\in$ QI, $b\in$ QIII; prob. $\tfrac26$). La cuerda 1 separa el arco que contiene a QII del que contiene a QIV, así que si la cuerda 2 va de QII a QIV **cruza siempre**; los otros cinco casos dan $\tfrac12$:

$$\text{media}=\frac{\tfrac12\cdot 5+1}{6}=\frac7{12}.$$

Por lo tanto

$$P(\text{dos cuerdas se cruzan})=\frac46\cdot\frac5{12}+\frac26\cdot\frac7{12}=\frac{17}{36},\qquad\text{aporte }120\cdot\frac{17}{36}=\frac{170}{3}.$$

**Paso 5: total.**

$$E[I]=1+\frac{64}{3}+\frac{170}{3}=1+78=79,\qquad E[R]=19+79=98.$$

$$\boxed{98}$$