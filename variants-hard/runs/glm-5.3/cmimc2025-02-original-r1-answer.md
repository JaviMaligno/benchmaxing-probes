## Razonamiento

**1. Configuración.** Las parábolas son $y=(x-a)^2$ con $a\in\{0,5,10,\ldots,45\}$: son $10$ parábolas.

**2. Puntos de corte.** Si $k>0$, la recta $y=k$ corta cada parábola en dos puntos: $x=a\pm\sqrt{k}$. En total habría a lo sumo $10\cdot 2=20$ puntos. Para obtener $19$ puntos distintos, debe coincidir **exactamente un** par de puntos.

**3. Condición de coincidencia.** Dos parábolas con parámetros $a\ne b$ comparten un punto de la recta solo si los cortes son "cruzados":
$$a+\sqrt{k}=b-\sqrt{k}\quad\Longrightarrow\quad |a-b|=2\sqrt{k}.$$
(Signos iguales obligarían $a=b$.)

**4. Conteo de pares.** Las diferencias entre parámetros son múltiplos de $5$. Una diferencia de $5d$ la tienen $10-d$ pares:
- $d=1$ (dif. $5$): $9$ pares → $11$ puntos.
- $d=2$ (dif. $10$): $8$ pares → $12$ puntos. …
- $d=9$ (dif. $45$): solo el par $(0,45)$ → exactamente una coincidencia → $19$ puntos. ✓

**5. Cálculo de $k$.** Con $|a-b|=45$:
$$2\sqrt{k}=45\quad\Longrightarrow\quad \sqrt{k}=22.5\quad\Longrightarrow\quad k=\left(\frac{45}{2}\right)^2=\frac{2025}{4}.$$

**6. Verificación.** Con $\sqrt{k}=22.5$, los puntos $a-22.5$ son $\{-22.5,-17.5,\ldots,22.5\}$ ($10$ valores) y los $a+22.5$ son $\{22.5,27.5,\ldots,67.5\}$ ($10$ valores). El único repetido es $22.5$ (viene de $a=45$ y de $a=0$). Total: $20-1=19$ puntos distintos. ✓

$$\boxed{\dfrac{2025}{4}}$$