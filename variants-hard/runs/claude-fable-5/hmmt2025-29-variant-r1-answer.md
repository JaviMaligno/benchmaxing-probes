## Planteamiento

Coloco coordenadas: $P=(0,0)$, $Q=(w,0)$, $R=(w,30)$, $S=(0,30)$, con $w = PQ$, y sea $Y=(x,y)$.

**Condición del ángulo recto.** $\angle PYQ = 90^\circ$ significa que $Y$ está en la circunferencia de diámetro $PQ$:
$$x^2 + y^2 = wx.$$

**Circuncentros.** En $\triangle PYS$, el lado $PS = 30$ y el circunradio es $17$, así que el circuncentro está en la mediatriz $y=15$, a distancia $\sqrt{17^2 - 15^2} = 8$ de $PS$. Como el triángulo es acutángulo, el centro está dentro, en $(8, 15)$. Análogamente, el circuncentro de $\triangle QYR$ (radio $25$) está a $\sqrt{25^2-15^2}=20$ de $QR$, en $(w-20, 15)$.

**Ecuaciones de las circunferencias.** $Y$ pertenece a ambas:

- $(x-8)^2+(y-15)^2=289 \;\Rightarrow\; x^2+y^2 = 16x + 30y$
- $(x-(w-20))^2+(y-15)^2=625 \;\Rightarrow\; x^2+y^2 = 2(w-20)x + 30y + 400 - (w-20)^2$

De la primera, usando $x^2+y^2 = wx$:
$$30y = (w-16)x.$$

Sustituyendo en la segunda, con $u = w-20$:
$$x(16-2u) = 400 - u^2 \quad\Rightarrow\quad x = \frac{(20-u)(20+u)}{2(8-u)}.$$

De $x^2+y^2 = wx$ con $y = \frac{(u+4)x}{30}$:
$$x\big(900+(u+4)^2\big) = 900(u+20) \quad\Rightarrow\quad x = \frac{900(u+20)}{900+(u+4)^2}.$$

## Resolución

Igualando ambas expresiones y cancelando $(u+20)>0$:
$$1800(8-u) = (20-u)\big(u^2+8u+916\big),$$
que se reduce a
$$u^3 - 12u^2 - 1044u - 3920 = 0.$$

Una raíz es $u=-4$ (daría $w=16$, pero entonces $y=0$ y $Y$ quedaría sobre $PQ$: degenerado, se descarta). Factorizando:
$$(u+4)(u^2 - 16u - 980) = 0 \;\Rightarrow\; u = 8 \pm \sqrt{1044} = 8 \pm 6\sqrt{29}.$$

La raíz $u = 8 - 6\sqrt{29}$ da $w<0$, así que $u = 8 + 6\sqrt{29}$ y
$$w = u + 20 = 28 + 6\sqrt{29} \approx 60.31.$$

**Verificación:** con $w \approx 60.31$ se obtiene $Y \approx (18.95,\ 27.99)$, que está dentro del rectángulo; se comprueba numéricamente que $x^2+y^2 = wx$, y todos los ángulos de $\triangle PYS$ ($\approx 34^\circ, 84^\circ, 62^\circ$) y de $\triangle QYR$ ($\approx 56^\circ, 87^\circ, 37^\circ$) son agudos. ✓

$$\boxed{28 + 6\sqrt{29}}$$