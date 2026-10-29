## Planteamiento

**Modelo:** Lena enhebra las seis cuentas en las seis posiciones del círculo en un orden aleatorio uniforme. Las $6!=720$ secuencias de cuentas son equiprobables, y como las dos E son indistinguibles entre sí (igual que las dos T), cada *palabra* de letras aparece $2!\cdot 2!=4$ veces. Luego las posiciones etiquetadas reciben una palabra uniforme entre

$$\frac{6!}{2!\,2!}=180$$

disposiciones distintas.

**Casos favorables:** el brazalete sirve si la disposición obtenida es una rotación o reflexión de L‑E‑T‑T‑E‑R. El grupo diedral $D_6$ tiene orden 12, así que la órbita de LETTER tiene tamaño $12/|\text{estabilizador}|$.

Veamos si alguna simetría fija la palabra cíclica $(L,E,T,T,E,R)$ en posiciones $0..5$:

- Rotaciones: las seis rotaciones LETTER, ETTERL, TTERLE, TERLET, ERLETT, RLETTE son todas distintas (ninguna rotación propia la fija, pues L aparece una sola vez).
- Reflexiones por ejes que pasan por cuentas: eje $0\text{–}3$ exige $E=R$ ✗; eje $1\text{–}4$ exige $L=T$ ✗; eje $2\text{–}5$ exige $E=T$ ✗.
- Reflexiones por puntos medios: eje entre $2\text{–}3$ exige $L=R$ ✗; entre $0\text{–}1$ exige $L=E$ ✗; entre $4\text{–}5$ exige $E=R$ ✗.

El estabilizador es trivial, así que la órbita tiene exactamente **12** disposiciones distintas (las 6 rotaciones de LETTER y las 6 de su reverso RETTEL).

## Probabilidad

$$P=\frac{12}{180}=\frac{1}{15}$$

(Comprobación con el modelo de cuentas: $12\cdot 4/720 = 48/720 = 1/15$.)

$$\boxed{\dfrac{1}{15}}$$