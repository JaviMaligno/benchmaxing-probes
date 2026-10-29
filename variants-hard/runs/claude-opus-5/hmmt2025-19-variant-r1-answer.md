## Planteamiento

Una cuerda de un polígono convexo que corta dos lados **adyacentes** es exactamente la que "corta una esquina" (separa un único vértice). Uso geometría integral.

**Medida de rectas.** Si una recta se parametriza por $(\theta,p)$ (dirección y distancia al origen) y corta la frontera en los puntos de parámetros de arco $s_1,s_2$ con ángulos $\varphi_1,\varphi_2$ respecto a la frontera, derivando las condiciones $E_i\cdot n=p$ se obtiene

$$dp\,d\theta=\frac{\sin\varphi_1\sin\varphi_2}{\ell}\,ds_1\,ds_2 ,$$

(se comprueba en el círculo: da $2\pi R$ = perímetro).

**Dos puntos al azar.** Con $dP\,dQ=|t_1-t_2|\,dt_1dt_2\,dp\,d\theta$ y $\int\!\!\int_0^\ell |t_1-t_2|=\ell^3/3$:

$$\mathbb P(S)=\frac{1}{3A^2}\int_S \ell^3\,dp\,d\theta .$$

## Caso adyacente

Hexágono de lado 1, $A=\tfrac{3\sqrt3}{2}$, $3A^2=\tfrac{81}{4}$. Fijo un vértice $V$ (ángulo interior $120^\circ$) y tomo la cuerda con extremos a distancias $a,b\in[0,1]$ de $V$ sobre los dos lados. Entonces $\ell^2=a^2+ab+b^2$ y, por el teorema del seno, $\sin\varphi_1=\tfrac{b\sin120^\circ}{\ell}$, $\sin\varphi_2=\tfrac{a\sin120^\circ}{\ell}$, luego

$$\ell^3\cdot\frac{\sin\varphi_1\sin\varphi_2}{\ell}=\tfrac34\,ab .$$

Por vértice: $\tfrac34\int_0^1\!\!\int_0^1 ab\,da\,db=\tfrac{3}{16}$, y con los 6 vértices $I_{\text{ady}}=\tfrac98$.

$$\mathbb P=\frac{9/8}{81/4}=\frac{1}{18}$$

## Verificación

Con el mismo método, lados opuestos dan integrando constante $3$, es decir $I_{\text{op}}=3\cdot3=9$ y $\mathbb P=\tfrac{4}{9}$ (resultado conocido); los pares separados por un lado dan $\tfrac34(1+b)(2-a)$, o sea $6\cdot\tfrac{27}{16}=\tfrac{81}{8}$ y $\mathbb P=\tfrac12$. Suma: $\tfrac1{18}+\tfrac49+\tfrac12=1$ ✓

$$\boxed{\dfrac{1}{18}}$$