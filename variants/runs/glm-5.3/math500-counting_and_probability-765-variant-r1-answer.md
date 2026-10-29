# Resolución paso a paso

## Definir variables

Sea:
- $C$ = conjunto de estudiantes que toman cálculo
- $P$ = conjunto de estudiantes que toman física
- $Q$ = conjunto de estudiantes que toman química

## Datos

- Total de estudiantes: 390, y 20 no toman ninguna → $|C \cup P \cup Q| = 370$
- $|C \cap P \cap Q| = 20$
- $|C| = 200$
- $|Q| = 2|P|$
- $|C \cap Q| = 80$
- $|P \cap Q| = 80$
- $|C \cap P| = 35$

## Aplicar inclusión-exclusión

$$|C \cup P \cup Q| = |C| + |P| + |Q| - |C \cap P| - |C \cap Q| - |P \cap Q| + |C \cap P \cap Q|$$

Sustituyendo:

$$370 = 200 + |P| + 2|P| - 35 - 80 - 80 + 20$$

$$370 = 3|P| + 25$$

$$3|P| = 345 \implies |P| = 115$$

## Verificación (regiones del diagrama de Venn)

- Solo $C$: $200 - 15 - 60 - 20 = 105$
- Solo $P$: $115 - 15 - 60 - 20 = 20$
- Solo $Q$: $230 - 60 - 60 - 20 = 90$
- Solo $C \cap P$: $35 - 20 = 15$; solo $C \cap Q$: $60$; solo $P \cap Q$: $60$; triple: $20$

Suma: $105 + 20 + 90 + 15 + 60 + 60 + 20 = 370$ ✓ (todas las regiones son no negativas)

## Respuesta

\boxed{115}