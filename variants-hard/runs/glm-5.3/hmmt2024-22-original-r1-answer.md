## Planteamiento

Sea $BC = a$ y denotemos $\angle B = \beta$, $\angle C = \gamma$, con $\beta + \gamma = 90^\circ$. Sean $b = AC$, $c = AB$ (por tanto $b = a\sin\beta$, $c = a\sin\gamma$). Sin pérdida de generalidad, supongo $\beta > \gamma$; si no, se intercambian $B$ y $C$ y las distancias $DE$, $EF$ no cambian.

Defino $\varphi = \frac{\beta - \gamma}{2}$, de modo que $\beta = 45^\circ + \varphi$ y $\gamma = 45^\circ - \varphi$, con $0 \le \varphi < 45^\circ$.

**Posiciones sobre $BC$, medidas desde $B$:**

- **Mediana:** $F$ es el punto medio, así que $BF = \frac{a}{2}$.
- **Altura:** $BD = \dfrac{c^2}{a} = a\sin^2\gamma = a\cdot\dfrac{1-\sin 2\varphi}{2}$.
- **Bisectriz:** por el teorema de la bisectriz, $BE = \dfrac{a\,c}{b+c} = a\cdot\dfrac{\sin\gamma}{\sin\beta+\sin\gamma}$. Usando $\sin\beta + \sin\gamma = \sqrt2\cos\varphi$ y $\sin\gamma = \frac{\sqrt2}{2}(\cos\varphi - \sin\varphi)$:
$$BE = \frac{a}{2}\left(1 - \tan\varphi\right).$$

## Cálculo de $DE$ y $EF$

Como $\cos 2\varphi > 0$, se cumple $BD < BE < BF$, es decir, el orden es $B, D, E, F, C$. Entonces:

$$EF = BF - BE = \frac{a}{2}\tan\varphi,$$

$$DE = BE - BD = \frac{a}{2}\left(\sin 2\varphi - \tan\varphi\right) = \frac{a}{2}\cdot\frac{\sin\varphi\cos 2\varphi}{\cos\varphi} = EF\cdot\cos 2\varphi.$$

## Resolviendo

Del dato $DE = 3$, $EF = 5$:

$$\cos 2\varphi = \frac{DE}{EF} = \frac{3}{5} \quad\Rightarrow\quad \sin 2\varphi = \frac{4}{5} \quad\Rightarrow\quad \tan\varphi = \frac{\sin 2\varphi}{1+\cos 2\varphi} = \frac{4/5}{8/5} = \frac{1}{2}.$$

Entonces:

$$EF = \frac{a\tan\varphi}{2} = 5 \quad\Rightarrow\quad a = \frac{10}{\tan\varphi} = \frac{10}{1/2} = 20.$$

## Verificación

Con $\tan\varphi = \frac12$: $\gamma \approx 18.435^\circ$, $AB = 2\sqrt{10}$, $AC = 6\sqrt{10}$, $BC = 20$.

- $BD = \frac{AB^2}{BC} = \frac{40}{20} = 2$
- $BE = \frac{BC\cdot AB}{AB+AC} = \frac{20\cdot 2\sqrt{10}}{8\sqrt{10}} = 5$
- $BF = 10$

Luego $DE = 5 - 2 = 3$ ✓ y $EF = 10 - 5 = 5$ ✓.

$$\boxed{20}$$