# Solución paso a paso

**Paso 1: Tratar a cada partido como un bloque.**
Como todos los miembros de cada partido deben sentarse juntos, formamos tres unidades:
- Bloque Verde (6 personas)
- Bloque Liberal (4 personas)
- El miembro independiente (1 persona)

**Paso 2: Ordenar los bloques alrededor de la mesa circular.**
Con 3 unidades alrededor de una mesa circular, donde las rotaciones son equivalentes, el número de ordenaciones es:
$$(3-1)! = 2! = 2$$

**Paso 3: Permutar dentro de cada bloque.**
- Los 6 Verdes pueden ordenarse entre sí: $6! = 720$ formas
- Los 4 Liberales pueden ordenarse entre sí: $4! = 24$ formas
- El independiente: $1$ forma

**Paso 4: Multiplicar.**
$$2 \times 6! \times 4! \times 1 = 2 \times 720 \times 24 = 34560$$

\boxed{34560}