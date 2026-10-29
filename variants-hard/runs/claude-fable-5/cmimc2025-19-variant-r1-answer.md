## Planteamiento con filtro de raíces de la unidad

El número de subconjuntos de $\{1,\dots,20\}$ con $|T|\equiv k \pmod 5$ es

$$N_k=\frac{1}{5}\sum_{j=0}^{4}\omega^{-jk}(1+\omega^j)^{20},\qquad \omega=e^{2\pi i/5}.$$

**Evaluar $(1+\omega^j)^{20}$.** Como $1+\omega^j = 2\cos(\pi j/5)\,e^{i\pi j/5}$, al elevar a la 20 la fase es $e^{4\pi i j}=1$, así que $(1+\omega^j)^{20}=\big(2\cos(\pi j/5)\big)^{20}$, un número real. Con $\varphi=\tfrac{1+\sqrt5}{2}$:

- $j=1,4$: $2\cos(\pi/5)=\varphi$ y $2\cos(4\pi/5)=-\varphi$, ambos dan $\varphi^{20}=:A$.
- $j=2,3$: $2\cos(2\pi/5)=\varphi^{-1}$ y $2\cos(3\pi/5)=-\varphi^{-1}$, ambos dan $\varphi^{-20}=:B$.

Agrupando pares conjugados, con $c_1=2\cos(2\pi k/5)$ y $c_2=2\cos(4\pi k/5)$:

$$N_k=\frac{1}{5}\Big[2^{20}+2\cos\!\big(\tfrac{2\pi k}{5}\big)A+2\cos\!\big(\tfrac{4\pi k}{5}\big)B\Big].$$

**Usar números de Lucas.** Como $\varphi^n+(-\varphi)^{-n}=L_n$:

- $A+B=\varphi^{20}+\varphi^{-20}=L_{20}=15127$
- $\varphi^{19}-\varphi^{-19}=L_{19}=9349$
- $\varphi^{21}-\varphi^{-21}=L_{21}=24476$

Con $2\cos(2\pi/5)=\varphi^{-1}$ y $2\cos(4\pi/5)=-\varphi$, las desviaciones $5\cdot 2^{20}\big(q(k)-\tfrac15\big)$ son:

- $k=0$: $2(A+B)=2L_{20}=30254$
- $k=1,4$: $\varphi^{-1}A-\varphi B=\varphi^{19}-\varphi^{-19}=L_{19}=9349$
- $k=2,3$: $-\varphi A+\varphi^{-1}B=-(\varphi^{21}-\varphi^{-21})=-L_{21}=-24476$

**Verificación:** $N_0=\tfrac{2^{20}+30254}{5}=215766$, $N_1=N_4=211585$, $N_2=N_3=204820$; la suma da $1048576=2^{20}$. ✓ Además la suma de desviaciones es $30254+2(9349)-2(24476)=0$. ✓

**Suma de valores absolutos:**

$$\sum_{k=0}^4\Big|q(k)-\tfrac15\Big|=\frac{30254+2\cdot 9349+2\cdot 24476}{5\cdot 2^{20}}=\frac{97904}{5242880}=\frac{6119}{327680}.$$

$$\boxed{\dfrac{6119}{327680}}$$