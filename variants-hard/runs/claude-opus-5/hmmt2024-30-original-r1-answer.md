## Planteamiento

Sean $\angle PAB=\angle PDA=a$, $\angle PAD=\angle PDC=b$, $\angle PBA=\angle PCB=c$, $\angle PBC=\angle PCD=d$.

**1. Relación entre las distancias.** Aplicando el teorema del seno en los cuatro triángulos $APB$, $BPC$, $CPD$, $DPA$:

- $\triangle APD$: $\dfrac{PA}{\sin a}=\dfrac{PD}{\sin b}\Rightarrow PD=4\dfrac{\sin b}{\sin a}$
- $\triangle BPC$: $\dfrac{PB}{\sin c}=\dfrac{PC}{\sin d}\Rightarrow \sin d=2\sin c$
- $\triangle APB$: $\dfrac{PA}{\sin c}=\dfrac{PB}{\sin a}\Rightarrow \sin c=\tfrac45\sin a$
- $\triangle DPC$: $PD=10\dfrac{\sin d}{\sin b}$

De ahí $\sin d=\tfrac85\sin a$ y $4\sin^2b=16\sin^2a\Rightarrow \sin b=2\sin a$, luego $\boxed{PD=8}$ (nótese $PA\cdot PC=PB\cdot PD=40$).

Así, con $\sin a=5k$: $\;\sin a:\sin b:\sin c:\sin d=5:10:4:8$.

**2. Suma de ángulos.** Los cuatro ángulos en $P$ suman $360°$, y cada uno vale $180°-(\cdot)-(\cdot)$, de donde
$$a+b+c+d=180°.$$

**3. Determinación de $k$.** De $\cos(a+b)=-\cos(c+d)$:
$$\sqrt{(1-25k^2)(1-100k^2)}+\sqrt{(1-16k^2)(1-64k^2)}=82k^2.$$
Elevando al cuadrado dos veces, con $u=k^2$, los términos de grado 4 y los lineales se cancelan y queda
$$24871\,u^2=2624000\,u^3\Rightarrow u=\frac{24871}{2624000}.$$
Esto da, racionalizando:
$$\cos a=\frac{283}{16\sqrt{410}},\quad \cos b=\frac{37}{8\sqrt{410}},\quad \cos c=\frac{373}{20\sqrt{410}},\quad \cos d=\frac{127}{10\sqrt{410}}.$$

**4. Los lados.** Como $a+c=180°-(b+d)$ y $a+b=180°-(c+d)$:
$$AB=CD=\tfrac1k\sin(a+c),\qquad DA=\tfrac{4}{5k}\sin(a+b),\qquad BC=\tfrac{5}{4k}\sin(a+b).$$
Usando $\sin(a+c)/k=5\cos c+4\cos a$ y $\sin(a+b)/k=5\cos b+10\cos a$:
$$\text{Perímetro}=2(5\cos c+4\cos a)+\tfrac{41}{20}(5\cos b+10\cos a)=\frac{373/2+16131/32+1517/32}{\sqrt{410}}=\frac{738}{\sqrt{410}}.$$

Es decir, $\dfrac{738}{410}\sqrt{410}=\dfrac95\sqrt{410}\approx 36.45$ (verificado numéricamente con $AB=CD\approx8.102$, $DA\approx7.901$, $BC\approx12.345$).

$$\boxed{\dfrac{9\sqrt{410}}{5}}$$