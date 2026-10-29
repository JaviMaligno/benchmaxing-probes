## Planteamiento

La condición $xy+yz+zx=1$ sugiere la sustitución tangente: si $x=\tan\frac A2$, $y=\tan\frac B2$, $z=\tan\frac C2$ con $A+B+C=\pi$, entonces se cumple automáticamente $xy+yz+zx=1$.

**Primera condición.** Como $x^2+1=\sec^2\frac A2$, llamando $k$ al valor común:
$$\cos^2\tfrac A2=\frac3k,\qquad \cos^2\tfrac B2=\frac4k,\qquad \cos^2\tfrac C2=\frac5k$$
y usando $2\cos^2\frac\theta2=1+\cos\theta$, con $t=1/k$:
$$\cos A=6t-1,\qquad \cos B=8t-1,\qquad \cos C=10t-1.$$

**Identidad de triángulo.** Para $A+B+C=\pi$ vale $\cos^2A+\cos^2B+\cos^2C+2\cos A\cos B\cos C=1$. Sustituyendo:
$$\underbrace{200t^2-48t+3}_{\text{suma de cuadrados}}+\underbrace{960t^3-376t^2+48t-2}_{2\cos A\cos B\cos C}=1$$
$$960t^3-176t^2+1=1\ \Longrightarrow\ 960t^3=176t^2\ \Longrightarrow\ t=\frac{11}{60},\quad k=\frac{60}{11}.$$

**Recuperando las variables.**
$$x^2=\frac{20}{11}-1=\frac9{11},\qquad y^2=\frac{15}{11}-1=\frac4{11},\qquad z^2=\frac{12}{11}-1=\frac1{11}$$
$$x=\frac3{\sqrt{11}},\qquad y=\frac2{\sqrt{11}},\qquad z=\frac1{\sqrt{11}}.$$

**Verificación.** $3\left(\frac9{11}+1\right)=4\left(\frac4{11}+1\right)=5\left(\frac1{11}+1\right)=\frac{60}{11}$ y $xy+yz+zx=\frac{6+2+3}{11}=1$. ✓

Por tanto $x+y+z=\dfrac{6}{\sqrt{11}}=\dfrac{6\sqrt{11}}{11}$.

$$\boxed{\dfrac{6\sqrt{11}}{11}}$$