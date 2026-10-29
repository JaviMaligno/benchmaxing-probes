Primero factorizo $12!$ en primos:

- Exponente de 2: $\lfloor 12/2 \rfloor + \lfloor 12/4 \rfloor + \lfloor 12/8 \rfloor = 6 + 3 + 1 = 10$
- Exponente de 3: $\lfloor 12/3 \rfloor + \lfloor 12/9 \rfloor = 4 + 1 = 5$
- Exponente de 5: $\lfloor 12/5 \rfloor = 2$
- Exponente de 7: $1$
- Exponente de 11: $1$

Así que $12! = 2^{10} \cdot 3^5 \cdot 5^2 \cdot 7 \cdot 11$.

Si $y = 2^a \cdot 3^b \cdot 5^c \cdot 7^d \cdot 11^e$, entonces $y^3 \mid 12!$ exige que cada exponente triplicado quepa en la factorización:

- $3a \le 10 \Rightarrow a \in \{0,1,2,3\}$ (4 opciones)
- $3b \le 5 \Rightarrow b \in \{0,1\}$ (2 opciones)
- $3c \le 2 \Rightarrow c = 0$ (1 opción)
- $3d \le 1 \Rightarrow d = 0$ (1 opción)
- $3e \le 1 \Rightarrow e = 0$ (1 opción)

El total de valores posibles de $y$ es $4 \cdot 2 \cdot 1 \cdot 1 \cdot 1 = 8$.

$$\boxed{8}$$