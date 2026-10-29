## Planteamiento

Hay 12 serpientes de longitud 1 en los arcos $0,3,6,\dots,33$ de un círculo de 36 arcos. Entre serpientes consecutivas hay huecos de 2 arcos, y la suma de los huecos es $36-12=24$ (constante, pues la longitud total de serpiente se conserva).

**Paso 1: trabajar con los huecos.** Si $g_1,\dots,g_m$ son los huecos entre serpientes consecutivas, cada segundo la serpiente $i$ se desplaza $X_i=\pm 1$, de modo que
$$\Delta g_i = X_{i+1}-X_i \in \{-2,0,+2\} \quad\text{con prob. } \tfrac14,\tfrac12,\tfrac14.$$
Como los huecos empiezan en 2 y cambian de dos en dos, siempre son pares; dos serpientes se tocan exactamente cuando su hueco llega a 0, y entonces ese hueco se elimina (fusión). El proceso termina cuando queda un solo hueco.

**Paso 2: reducción a caminatas coalescentes.** Sea $h_i=g_i/2$ (semi-huecos), con $\sum h_i = 12$. Escribiendo $Y_i=(X_i+1)/2\in\{0,1\}$ (Bernoulli$(1/2)$ independientes), se tiene $\Delta h_i = Y_{i+1}-Y_i$. Esto es exactamente la dinámica de **12 partículas coalescentes en $\mathbb{Z}_{12}$, una en cada sitio**, donde cada segundo cada partícula avanza $+1$ con probabilidad $1/2$ o se queda quieta, y dos partículas se fusionan al coincidir. El tiempo buscado es el tiempo esperado hasta la coalescencia total, con la misma escala temporal (1 segundo = 1 paso).

**Paso 3: resolver el modelo reducido.** Para dos cúmulos a distancia $d$ en $\mathbb{Z}_n$, la diferencia relativa es una caminata perezosa ($\pm1$ con prob. $1/4$, quieta con prob. $1/2$), cuyo tiempo esperado de llegada a 0 es $2\,d(n-d)$. Con esto se calculan los casos pequeños por cadenas de Markov exactas (sobre composiciones cíclicas de $n$):

- $n=2$: $E[T]=2$.
- $n=3$: desde $(1,1,1)$, con prob. $3/4$ se pasa a dos cúmulos con huecos $(1,2)$ (tiempo restante $4$); se obtiene $E[T]=16/3$.
- $n=4$: desde $(1,1,1,1)$, enumerando los 16 resultados de $(Y_1,\dots,Y_4)$ y usando $b=9$ para $(1,1,2)$, $c=6$ para $(1,3)$, $d=8$ para $(2,2)$, sale $E[T]=10$.

Los tres valores ajustan exactamente con
$$E[T] \;=\; \frac{2}{3}\,(n^2-1),$$
que además reproduce el caso conocido $n=15$ (círculo de 45 arcos con 15 serpientes), cuyo valor es $\tfrac{2}{3}(225-1)=\tfrac{448}{3}$.

**Paso 4: aplicar con $n=12$.**
$$E[T] \;=\; \frac{2}{3}\,(12^2-1) \;=\; \frac{2\cdot 143}{3} \;=\; \frac{286}{3}.$$

$$\boxed{\dfrac{286}{3}}$$