## Planteamiento

El número $a$ queda registrado si y solo si la ficha $a$ ocupa la raíz en algún instante de registro **antes** de que la ficha 6 llegue a la raíz (dos fichas no pueden estar en la raíz a la vez, así que no hay empates). Como el proceso termina con probabilidad 1, para cada $a \neq 6$:

$$q(a) = P(\tau_a < \tau_6),$$

donde $\tau$ es el primer instante en que cada ficha visita la raíz. Basta seguir el par (posición de $a$, posición de 6), que es una cadena de Markov: en cada paso se elige una de las 6 aristas; si toca a una ficha, esta se mueve; si conecta ambas, se intercambian.

## Estados (módulo simetría del árbol)

Con raíz $R$, nodos medios $L, Rt$ y hojas, y $f_i = P(a \text{ gana})$:

- $S_1$: $a$ en un medio, 6 en el otro medio — estado inicial del **2**.
- $S_2$: $a$ en medio, 6 en hoja hija de $a$; $S_3$: $a$ en medio, 6 en hoja del otro lado.
- $S_4$: $a$ en hoja hija del medio donde está 6 — estado inicial del **5** y del **7**.
- $S_5$: $a$ en hoja del lado opuesto a 6 (6 en medio) — estado inicial del **1** y del **3**.
- $S_6$: hojas hermanas; $S_7$: hojas en lados opuestos.

## Simetrías y ecuaciones

Como siempre gana exactamente una ficha, $f(x,y) + f(y,x) = 1$. Los automorfismos del árbol dan:

$$f_1 = f_6 = f_7 = \tfrac12, \qquad f_2 + f_4 = 1, \qquad f_3 + f_5 = 1.$$

Enumerando las 6 aristas en cada estado se obtienen, por ejemplo:

$$3f_2 = 1 + f_4 + f_6, \qquad 4f_5 = f_1 + 2f_7.$$

Sustituyendo: $3f_2 = 1 + (1-f_2) + \tfrac12 \Rightarrow f_2 = \tfrac58,\ f_4 = \tfrac38$; y $4f_5 = \tfrac12 + 1 \Rightarrow f_5 = \tfrac38,\ f_3 = \tfrac58$. Todas las ecuaciones restantes ($3f_4 = f_2+f_6$, $2f_6 = f_2+f_4$, $4f_3 = 1+2f_7+f_1$, $2f_7 = f_3+f_5$) se verifican.

## Resultado

$$q(2) = f_1 = \tfrac12, \qquad q(1)=q(3)=f_5=\tfrac38, \qquad q(5)=q(7)=f_4=\tfrac38.$$

$$q(1)+q(2)+q(3)+q(5)+q(7) = \tfrac12 + 4\cdot\tfrac38 = 2.$$

$$\boxed{2}$$