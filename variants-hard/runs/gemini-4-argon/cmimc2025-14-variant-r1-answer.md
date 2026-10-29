Para hallar el número de componentes conexas $d_{n,k}$ del grafo $H_{n,k}$, podemos modelar el conjunto de vértices como el espacio vectorial $\mathbb{F}_2^n$ (las cadenas binarias de longitud $n$ con la operación suma módulo $2$, o XOR componente a componente).

Dos vértices $u, v \in \mathbb{F}_2^n$ son adyacentes si y solo si su suma $u + v$ tiene peso de Hamming exactamente $k$ (es decir, tiene exactamente $k$ unos). Por lo tanto, $H_{n,k}$ es el grafo de Cayley del grupo abeliano $(\mathbb{F}_2^n, +)$ generado por el conjunto $S_{n,k}$ de todos los vectores de peso $k$.

En este grafo de Cayley, la componente conexa que contiene al vector cero $\mathbf{0}$ es el subespacio vectorial $\langle S_{n,k} \rangle$ generado por $S_{n,k}$, y las demás componentes conexas son las clases laterales (cosets) de $\langle S_{n,k} \rangle$. En consecuencia, el número de componentes conexas es el índice del subgrupo:
$$d_{n,k} = \frac{2^n}{|\langle S_{n,k} \rangle|}.$$

Analizamos los casos según los valores de $k$ y $n$:

1. **Caso $k = n$:**
   El único vector de peso $n$ es el vector con todos sus elementos iguales a $1$, es decir, $\mathbf{1} = (1, 1, \dots, 1)$. El subespacio generado es $\langle S_{n,n} \rangle = \{\mathbf{0}, \mathbf{1}\}$, que tiene tamaño $2$. Por lo tanto:
   $$d_{n,n} = \frac{2^n}{2} = 2^{n-1}.$$

2. **Caso $1 \le k < n$:**
   Dado que $0 \le k-1 \le n-2$, para cualquier par de coordenadas distintas $i \neq j$, podemos elegir $k-1$ posiciones entre las $n-2$ restantes y formar dos vectores de peso $k$: uno con unos en esas $k-1$ posiciones y en $i$, y otro con unos en esas $k-1$ posiciones y en $j$. La suma de estos dos vectores tiene unos únicamente en las posiciones $i$ y $j$.
   
   Esto implica que $\langle S_{n,k} \rangle$ contiene todos los vectores de peso $2$. Como los vectores de peso $2$ generan el subespacio $E_n$ de todos los vectores de peso par (el cual tiene dimensión $n-1$ y tamaño $2^{n-1}$), tenemos que $E_n \subseteq \langle S_{n,k} \rangle$. Esto da lugar a dos subcasos:
   - **Si $k$ es par ($1 \le k < n$):** Todos los vectores de $S_{n,k}$ tienen peso par, por lo que $S_{n,k} \subseteq E_n$. Así, $\langle S_{n,k} \rangle = E_n$, que tiene tamaño $2^{n-1}$, y por tanto:
     $$d_{n,k} = \frac{2^n}{2^{n-1}} = 2.$$
   - **Si $k$ es impar ($1 \le k < n$):** Los vectores de $S_{n,k}$ tienen peso impar y no pertenecen a $E_n$. Como $E_n$ tiene dimensión $n-1$, al añadir cualquier vector fuera de $E_n$ se genera todo el espacio $\mathbb{F}_2^n$. Así, $|\langle S_{n,k} \rangle| = 2^n$, y por tanto:
     $$d_{n,k} = \frac{2^n}{2^n} = 1.$$

---

### Cálculo de la suma

Separamos la suma doble en los términos con $k = n$ y los términos con $1 \le k < n$:
$$\sum_{n=1}^{12} \sum_{k=1}^{n} d_{n,k} = \sum_{n=1}^{12} d_{n,n} + \sum_{n=1}^{12} \sum_{k=1}^{n-1} d_{n,k}.$$

1. **Suma para $k = n$:**
   $$\sum_{n=1}^{12} d_{n,n} = \sum_{n=1}^{12} 2^{n-1} = 2^{12} - 1 = 4096 - 1 = 4095.$$

2. **Suma para $1 \le k < n$:**
   Intercambiando el orden de sumación, cada $k \in \{1, 2, \dots, 11\}$ aparece para $n = k+1, \dots, 12$, es decir, $12 - k$ veces:
   $$\sum_{k=1}^{11} (12 - k) d_{n,k} = \sum_{\substack{1 \le k \le 11 \\ k \text{ impar}}} (12 - k) \cdot 1 + \sum_{\substack{1 \le k \le 11 \\ k \text{ par}}} (12 - k) \cdot 2.$$
   - Para $k$ impar ($k = 1, 3, 5, 7, 9, 11$):
     $$11 + 9 + 7 + 5 + 3 + 1 = 36.$$
   - Para $k$ par ($k = 2, 4, 6, 8, 10$):
     $$2 \cdot (10 + 8 + 6 + 4 + 2) = 2 \cdot 30 = 60.$$
   
   Sumando ambas partes para $1 \le k < n$, obtenemos $36 + 60 = 96$.

Finalmente, sumamos todos los términos:
$$4095 + 96 = 4191.$$

\boxed{4191}