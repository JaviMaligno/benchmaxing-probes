Sea $p$ la probabilidad de obtener la cara $F$ y $q$ la probabilidad de obtener la cara opuesta a $F$ (es decir, $7-F$). Sabemos que las cuatro caras restantes tienen cada una una probabilidad de $\frac{1}{6}$.

Como la suma de las probabilidades de todas las caras de un dado es igual a $1$, tenemos:
$$p + q + 4\left(\frac{1}{6}\right) = 1 \implies p + q = \frac{1}{3}$$

Dado que $p > \frac{1}{6}$ y $q < \frac{1}{6}$, podemos expresar $p$ y $q$ en términos de una desviación $x > 0$:
$$p = \frac{1}{6} + x$$
$$q = \frac{1}{6} - x$$

Al lanzar dos de estos dados, la suma de los números obtenidos es $7$ si y solo si los resultados forman uno de los pares de caras opuestas: $(1,6), (6,1), (2,5), (5,2), (3,4), (4,3)$. 

- Para los dos pares de caras opuestas que no involucran a $F$ ni a su cara opuesta (4 combinaciones ordenadas en total), cada combinación ocurre con probabilidad $\frac{1}{6} \cdot \frac{1}{6} = \frac{1}{36}$.
- Para el par que involucra a $F$ y a su cara opuesta, las combinaciones son $(F, 7-F)$ y $(7-F, F)$, cada una con probabilidad $p \cdot q$.

Por lo tanto, la probabilidad total de que los dos números sumen $7$ es:
$$P(\text{suma} = 7) = 4\left(\frac{1}{36}\right) + 2pq = \frac{1}{9} + 2\left(\frac{1}{6} + x\right)\left(\frac{1}{6} - x\right)$$

Simplificando la expresión:
$$P(\text{suma} = 7) = \frac{1}{9} + 2\left(\frac{1}{36} - x^2\right) = \frac{1}{9} + \frac{1}{18} - 2x^2 = \frac{1}{6} - 2x^2$$

Igualando esta expresión al valor dado en el problema, $\frac{71}{450}$:
$$\frac{1}{6} - 2x^2 = \frac{71}{450}$$

Como $\frac{1}{6} = \frac{75}{450}$, despejamos $x$:
$$2x^2 = \frac{75}{450} - \frac{71}{450} = \frac{4}{450} = \frac{2}{225}$$
$$x^2 = \frac{1}{225}$$

Dado que $x > 0$, obtenemos $x = \frac{1}{15}$.

Finalmente, calculamos la probabilidad $p$ de obtener la cara $F$:
$$p = \frac{1}{6} + \frac{1}{15} = \frac{5 + 2}{30} = \frac{7}{30}$$

Como $7$ y $30$ son enteros positivos coprimos ($m=7$ y $n=30$), la suma $m+n$ es:
$$m + n = 7 + 30 = 37$$

\boxed{37}