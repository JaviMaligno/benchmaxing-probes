Numeremos las letras como posiciones: $A=1,\dots,L=12$, así que $G=7$.

Condicionamos en el compañero $y$ de $G$. Hay $11$ opciones para $y$, y para cada una quedan $945$ formas de emparejar las otras $10$ letras.

**Caso 1: $y>7$** (es decir, $y\in\{8,9,10,11,12\}$).  
La palabra con $G$ es $(7,y)$. Para que sea la última, todas las demás palabras deben tener primera letra $\le 6$. Las letras restantes son las $6$ bajas $\{1,\dots,6\}$ y las $4$ altas $\{8,\dots,12\}\setminus\{y\}$. Ningún par puede estar formado por dos altas, así que cada alta debe emparejarse con una baja distinta:

$$
6\cdot 5\cdot 4\cdot 3 = 360.
$$

Esto ocurre para $5$ valores de $y$, aportando $5\cdot 360=1800$.

**Caso 2: $y<7$** (es decir, $y\in\{1,\dots,6\}$).  
La palabra con $G$ es $(y,7)$. Para que sea la última, todas las demás palabras deben tener primera letra $<y$, lo que exige que cada par contenga una letra de $\{1,\dots,y-1\}$. Como hay $5$ pares restantes, necesitamos al menos $5$ letras menores que $y$, así que $y-1\ge5$, es decir $y=6$.

Si $y=6$, las letras restantes son $\{1,2,3,4,5\}$ y $\{8,9,10,11,12\}$. Cada par debe mezclar una de cada grupo, lo que da:

$$
5! = 120.
$$

Por tanto, los casos favorables son:

$$
1800 + 120 = 1920.
$$

El total de emparejamientos es:

$$
\frac{12!}{2^6\cdot 6!} = 10395.
$$

Así:

$$
P=\frac{1920}{10395}=\frac{128}{693}.
$$

Entonces $m+n=128+693=821$.

\boxed{821}