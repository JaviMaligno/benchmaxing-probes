Para encontrar el valor de $a+b+c$, podemos utilizar una sustitución trigonométrica basada en las identidades de un triángulo.

Dado que $a, b, c$ son números reales positivos tales que $ab + bc + ca = 1$, podemos definir $a, b, c$ como las cotangentes de los ángulos de un triángulo acutángulo con ángulos $A, B, C \in \left(0, \frac{\pi}{2}\right)$ y $A + B + C = \pi$:
$$a = \cot A, \quad b = \cot B, \quad c = \cot C$$

Usando la identidad trigonométrica $\cot^2 \theta + 1 = \csc^2 \theta = \frac{1}{\sin^2 \theta}$, reescribimos la primera condición del problema:
$$\frac{2}{\sin^2 A} = \frac{3}{\sin^2 B} = \frac{4}{\sin^2 C}$$

Tomando el recíproco y la raíz cuadrada en cada término (dado que $\sin A, \sin B, \sin C > 0$), obtenemos:
$$\frac{\sin A}{\sqrt{2}} = \frac{\sin B}{\sqrt{3}} = \frac{\sin C}{2}$$

Por la Ley de los Senos, esto significa que $A, B, C$ son los ángulos de un triángulo cuyos lados opuestos son proporcionales a $x = \sqrt{2}$, $y = \sqrt{3}$ y $z = 2$. 
Notemos que $x^2 + y^2 = 2 + 3 = 5 > 4 = z^2$, lo que confirma que el triángulo es acutángulo y, por tanto, sus cotangentes son positivas.

Por la Ley de los Cosenos y la fórmula del área $S$ de un triángulo ($S = \frac{1}{2}yz \sin A$), sabemos que:
$$\cot A = \frac{\cos A}{\sin A} = \frac{\frac{y^2+z^2-x^2}{2yz}}{\frac{2S}{yz}} = \frac{y^2 + z^2 - x^2}{4S}$$

Análogamente, para $\cot B$ y $\cot C$:
$$\cot B = \frac{x^2 + z^2 - y^2}{4S}, \quad \cot C = \frac{x^2 + y^2 - z^2}{4S}$$

Sumando las tres expresiones, obtenemos:
$$a + b + c = \cot A + \cot B + \cot C = \frac{x^2 + y^2 + z^2}{4S}$$

Calculamos el numerador:
$$x^2 + y^2 + z^2 = 2 + 3 + 4 = 9$$

Para hallar el denominador $4S$, utilizamos la fórmula de Herón en su forma algebraica:
$$16S^2 = 2(x^2y^2 + y^2z^2 + z^2x^2) - (x^4 + y^4 + z^4)$$

Sustituyendo $x^2 = 2$, $y^2 = 3$ y $z^2 = 4$:
$$16S^2 = 2(2\cdot 3 + 3\cdot 4 + 4\cdot 2) - (2^2 + 3^2 + 4^2)$$
$$16S^2 = 2(6 + 12 + 8) - (4 + 9 + 16) = 2(26) - 29 = 52 - 29 = 23$$

Tomando la raíz cuadrada, obtenemos $4S = \sqrt{23}$.

Finalmente, sustituimos ambos resultados para obtener la suma buscada:
$$a + b + c = \frac{9}{\sqrt{23}} = \frac{9\sqrt{23}}{23}$$

\boxed{\frac{9\sqrt{23}}{23}}