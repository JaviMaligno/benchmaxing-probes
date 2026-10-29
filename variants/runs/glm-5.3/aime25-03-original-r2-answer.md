Voy a resolver el problema paso a paso.

## Planteamiento

Cada uno de los 9 jugadores elige chocolate (C), vainilla (V) o fresa (S), con al menos un jugador por sabor y C > V > S ≥ 1. Necesito las ternas de enteros positivos con C + V + S = 9 y C > V > S.

**Enumeración de ternas válidas:**
- S = 1, V = 2, C = 6 ✓
- S = 1, V = 3, C = 5 ✓
- S = 1, V = 4, C = 4 ✗ (C = V)
- S = 2, V = 3, C = 4 ✓
- S ≥ 3: exigiría V ≥ 4 y C ≥ 5, suma ≥ 12 ✗

## Cálculo de N

Para cada terna, el número de asignaciones es multinomial:

- **(C, V, S) = (6, 2, 1):** $\dfrac{9!}{6!\,2!\,1!} = \dfrac{9 \cdot 8 \cdot 7}{2} = 252$

- **(C, V, S) = (5, 3, 1):** $\dfrac{9!}{5!\,3!\,1!} = \dfrac{9 \cdot 8 \cdot 7 \cdot 6}{6} = 504$

- **(C, V, S) = (4, 3, 2):** $\dfrac{9!}{4!\,3!\,2!} = \dfrac{362880}{288} = 1260$

**Total:**
$$N = 252 + 504 + 1260 = 2016$$

## Resto módulo 1000

$$2016 \bmod 1000 = 16$$

\boxed{16}