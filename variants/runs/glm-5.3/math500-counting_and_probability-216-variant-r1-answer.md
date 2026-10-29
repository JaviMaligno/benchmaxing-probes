## Planteamiento

Hay 9 ingenieros y 6 diseñadores, es decir, 15 personas en total. Queremos formar un equipo de 5 miembros que tenga **al menos un ingenieros y al menos un diseñador**.

## Método 1: Complemento

Contamos todos los equipos posibles y restamos los que **no** cumplen la condición (es decir, los que son solo ingenieros o solo diseñadores).

- Total de equipos de 5 entre 15 personas:
$$\binom{15}{5} = 3003$$

- Equipos de solo ingenieros (imposible tener diseñador):
$$\binom{9}{5} = 126$$

- Equipos de solo diseñadores (imposible tener ingenieros):
$$\binom{6}{5} = 6$$

Por el principio de inclusión-exclusión, los equipos válidos son:
$$3003 - 126 - 6 = 2871$$

## Método 2: Verificación por casos

Repartimos los 5 puestos entre ingenieros ($e$) y diseñadores ($d$), con $e \geq 1$, $d \geq 1$, $e + d = 5$:

| Ingenieros | Diseñadores | Cálculo | Resultado |
|:---:|:---:|:---:|:---:|
| 1 | 4 | $\binom{9}{1}\binom{6}{4} = 9 \cdot 15$ | $135$ |
| 2 | 3 | $\binom{9}{2}\binom{6}{3} = 36 \cdot 20$ | $720$ |
| 3 | 2 | $\binom{9}{3}\binom{6}{2} = 84 \cdot 15$ | $1260$ |
| 4 | 1 | $\binom{9}{4}\binom{6}{1} = 126 \cdot 6$ | $756$ |

Sumando: $135 + 720 + 1260 + 756 = 2871$ ✓ (coincide con el Método 1).

## Respuesta

$$\boxed{2871}$$