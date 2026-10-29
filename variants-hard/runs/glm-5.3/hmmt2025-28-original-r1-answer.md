## Planteamiento

Coloco el círculo de radio 5 centrado en el origen. Como $AB \parallel CD$ y $A,B,C,D$ son concíclicos, el trapecio es isósceles con eje de simetría el eje $y$.

**Coordenadas:**
- $A=(-2, h_1)$, $B=(2, h_1)$ con $h_1^2 = 25 - 4 = 21$
- $D=(-t, h_2)$, $C=(t, h_2)$ con $t^2 + h_2^2 = 25$ y $t>2$
- Como $D$ está entre $E$ y $C$: $E = (-(t+2), h_2)$

**Punto $M$ (punto medio de $AE$):**
$$M=\left(-\frac{t+4}{2},\ \frac{h_1+h_2}{2}\right)$$

## Usar que $M$ está en el círculo

$$\left(\frac{t+4}{2}\right)^2 + \left(\frac{h_1+h_2}{2}\right)^2 = 25 \implies (t+4)^2 + (h_1+h_2)^2 = 100$$

Expandiendo con $t^2+h_2^2 = 25$ e $h_1^2 = 21$:

$$25 + 8t + 16 + 21 + 2h_1h_2 = 100 \implies 4t + h_1h_2 = 19$$

(Resolviendo: se necesita $h_1, h_2$ de signos opuestos, y $4t-19=\sqrt{21(25-t^2)}$ da $37t^2-152t-164=0$, con raíz válida $t=\frac{76+6\sqrt{329}}{37}\approx 4.995$, que cumple $2t>4$.)

## Calcular $MD$

$$MD^2 = \left(\frac{t-4}{2}\right)^2 + \left(\frac{h_1-h_2}{2}\right)^2 = \frac{(t-4)^2 + (h_1-h_2)^2}{4}$$

Con $(t-4)^2 = t^2-8t+16$ y $(h_1-h_2)^2 = 21 + (25-t^2) - 2h_1h_2$, usando $h_1h_2 = 19-4t$:

$$(h_1-h_2)^2 = 46 - t^2 - 38 + 8t = 8 - t^2 + 8t$$

Sumando:

$$MD^2 = \frac{(t^2 - 8t + 16) + (8 - t^2 + 8t)}{4} = \frac{24}{4} = 6$$

(Verificación numérica: con $t\approx 4.9955$, $h_1=\sqrt{21}$, $h_2\approx -0.2141$, se obtiene $MD^2 \approx 6.000$ ✓)

$$MD = \boxed{\sqrt{6}}$$