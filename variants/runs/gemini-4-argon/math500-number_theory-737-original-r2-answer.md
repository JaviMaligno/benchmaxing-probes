Para resolver este problema paso a paso, primero debemos encontrar la suma de los divisores propios de $284$, y luego calcular la suma de los divisores propios del número resultante.

**Paso 1: Encontrar la suma de los divisores propios de 284.**
Descomponemos $284$ en sus factores primos:
$$284 = 2^2 \times 71$$

Los divisores positivos de $284$ son: $1, 2, 4, 71, 142$ y $284$.
Los divisores propios (aquellos menores que $284$) son: $1, 2, 4, 71$ y $142$.

Sumamos estos divisores propios:
$$1 + 2 + 4 + 71 + 142 = 220$$

**Paso 2: Encontrar la suma de los divisores propios de 220.**
Ahora descomponemos $220$ en sus factores primos:
$$220 = 2^2 \times 5 \times 11$$

Los divisores propios de $220$ son: $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$ y $110$.

Sumamos estos divisores propios (o usamos la fórmula de la suma de divisores restando el propio número):
$$\sigma(220) - 220 = (1 + 2 + 4)(1 + 5)(1 + 11) - 220 = 7 \times 6 \times 12 - 220 = 504 - 220 = 284$$

*(Nota: $220$ y $284$ forman el par más pequeño de números amigos).*

\boxed{284}