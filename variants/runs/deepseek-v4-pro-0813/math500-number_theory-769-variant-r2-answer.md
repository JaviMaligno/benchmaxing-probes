Calculamos cada base módulo $11$:

$$
117 \equiv 7 \pmod{11}, \qquad 194 \equiv 7 \pmod{11}.
$$

Por tanto,

$$
117^{36}+194^{38} \equiv 7^{36}+7^{38} \pmod{11}.
$$

Como $7$ no es divisible por $11$, por el pequeño teorema de Fermat:

$$
7^{10} \equiv 1 \pmod{11}.
$$

Entonces reducimos los exponentes módulo $10$:

$$
7^{36} \equiv 7^6 \pmod{11}, \qquad 7^{38} \equiv 7^8 \pmod{11}.
$$

Calculamos potencias de $7$:

$$
7^2 \equiv 49 \equiv 5,
$$

$$
7^4 \equiv 5^2 \equiv 25 \equiv 3,
$$

$$
7^6 \equiv 7^4 \cdot 7^2 \equiv 3\cdot 5 \equiv 15 \equiv 4,
$$

$$
7^8 \equiv (7^4)^2 \equiv 3^2 \equiv 9.
$$

Sumamos:

$$
7^6+7^8 \equiv 4+9 \equiv 13 \equiv 2 \pmod{11}.
$$

Por lo tanto, el residuo es:

$$
\boxed{2}
$$