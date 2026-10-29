## Planteamiento

Denotemos los nodos: $r$ = raíz, $a$ = hijo izquierdo, $b$ = hijo derecho, $c,d$ = hojas de $a$, $e,f$ = hojas de $b$, con el $7$ inicialmente en $f$. Configuración inicial: $r{:}4$, $a{:}2$, $b{:}6$, $c{:}1$, $d{:}3$, $e{:}5$, $f{:}7$. Cada paso elige una de las $6$ aristas con probabilidad $1/6$ y permuta los números de sus extremos.

**Reducción a dos etiquetas.** Aunque el estado completo es una permutación de $7$ números, para calcular $p(a)$ basta seguir la posición $X_t$ del número $a$ y la posición $Y_t$ del número $7$: el par $(X_t,Y_t)$ es por sí mismo una cadena de Markov sobre pares de nodos distintos (si la arista toca el nodo de $X$, se mueve $X$; si toca el de $Y$, se mueve $Y$; si los une, se intercambian; si no, nada cambia). Los demás números no influyen en este par.

Escribimos el valor de la raíz en los tiempos $0,1,\dots,T$ con $T=\min\{t: Y_t=r\}$. Escribir el número $a$ equivale a $X_t=r$ para algún $t\le T$; como $X_T\neq r$ (ahí está el $7$),

$$p(a)=\mathbb{P}(X \text{ visita } r \text{ estrictamente antes que } Y).$$

Sea $h(x,y)$ esa probabilidad partiendo de $X=x,\,Y=y$; luego $p(a)=h(x_0,f)$, con $x_0$ la posición inicial de $a$.

## Dos simetrías

1. **Intercambio de roles:** la dinámica trata a $X$ e $Y$ por igual y nunca empatan (siempre ocupan nodos distintos), así que $h(x,y)+h(y,x)=1$.
2. **Automorfismos:** todo automorfismo del árbol fija $r$ (único nodo de grado $2$) y preserva la dinámica: $h(\sigma x,\sigma y)=h(x,y)$. El grupo lo generan $\alpha\colon c\leftrightarrow d$, $\beta\colon e\leftrightarrow f$, $\rho\colon a\leftrightarrow b,\ c\leftrightarrow e,\ d\leftrightarrow f$.

## Valores que caen por pura simetría

- $p(1)=h(c,f)$: el automorfismo $\rho\alpha\beta$ intercambia $c\leftrightarrow f$, luego $h(c,f)=h(f,c)=1-h(c,f)$, así que $p(1)=\tfrac12$.
- $p(3)=h(d,f)$: $\rho$ intercambia $d\leftrightarrow f$, así que $p(3)=\tfrac12$.
- $p(5)=h(e,f)$: $\beta$ intercambia $e\leftrightarrow f$, así que $p(5)=\tfrac12$.

## Cálculo de $p(6)=h(b,f)$

Desde $(b,f)$: las aristas $(r,a),(a,c),(a,d)$ no tocan $b$ ni $f$ (se queda); $(r,b)$ lleva $X\to r$ (éxito, valor $1$); $(b,e)$ lleva a $(e,f)=\tfrac12$; $(b,f)$ los intercambia, llevando a $(f,b)$:
$$6h(b,f)=3h(b,f)+1+\tfrac12+h(f,b).$$
Desde $(f,b)$: tres aristas lo dejan igual; $(r,b)$ lleva $Y\to r$ (fallo, $0$); $(b,e)$ lleva a $(f,e)=\tfrac12$; $(b,f)$ los intercambia, llevando a $(b,f)$:
$$6h(f,b)=3h(f,b)+\tfrac12+h(b,f).$$
Con la relación de roles $h(f,b)=1-h(b,f)$, la segunda ecuación da $3\big(1-h(b,f)\big)=\tfrac12+h(b,f)$, es decir $h(b,f)=\tfrac58$. Luego $p(6)=\tfrac58$.

## Cálculo de $p(2)=h(a,f)$

Primero, $h(a,b)=\tfrac12$: $\rho$ intercambia $a,b$, así que $h(a,b)=h(b,a)=1-h(a,b)$.

Desde $(a,f)$: $(r,a)$ lleva $X\to r$ (éxito, $1$); $(r,b),(b,e)$ lo dejan igual ($2$ casos); $(a,c)$ y $(a,d)$ llevan a $(c,f)$ y $(d,f)$, que valen $\tfrac12$ cada una; $(b,f)$ lleva $Y\to b$, es decir $(a,b)$:
$$6h(a,f)=2h(a,f)+1+\tfrac12+\tfrac12+\tfrac12 \implies 4h(a,f)=\tfrac52\implies h(a,f)=\tfrac58.$$
Luego $p(2)=\tfrac58$.

## Suma final

$$p(1)+p(2)+p(3)+p(5)+p(6)=\tfrac12+\tfrac58+\tfrac12+\tfrac12+\tfrac58=\frac{11}{4}.$$

(Comprobación de coherencia: $p(4)=1$ y $p(7)=1$, así que el número esperado de valores distintos anotados es $2+\tfrac{11}{4}=\tfrac{19}{4}<7$, razonable.)

$$\boxed{\dfrac{11}{4}}$$