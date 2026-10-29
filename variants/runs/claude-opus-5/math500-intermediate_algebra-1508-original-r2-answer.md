## Planteamiento

De la recurrencia:

$$a_2=\frac{1}{1-a_1},\qquad a_3=\frac{1}{1-a_2}=\frac{1}{1-\frac{1}{1-a_1}}=\frac{1-a_1}{-a_1}=\frac{a_1-1}{a_1}$$

## Condición $a_3=a_1$

$$\frac{a_1-1}{a_1}=a_1\;\Longrightarrow\; a_1^2-a_1+1=0$$

## Valor de $a_9$

La aplicación $x\mapsto \frac{1}{1-x}$ tiene orden 3, es decir $a_{i+3}=a_i$ para todo $i$. Por tanto

$$a_9=a_6=a_3=a_1$$

## Cálculo de $a_1^9$

De $a_1^2-a_1+1=0$ se obtiene, multiplicando por $(a_1+1)$:

$$a_1^3+1=0\;\Longrightarrow\; a_1^3=-1$$

Entonces

$$a_9^9=a_1^9=(a_1^3)^3=(-1)^3=-1$$

\boxed{-1}