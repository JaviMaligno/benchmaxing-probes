

## La propuesta no cumple

Usar `organization:case` como clave externa protege dentro de las 6 h (el proveedor deduplica), pero la cola reentrega hasta 48 h. Tras 6 h el proveedor olvida la clave y una reentrega imprimiría de nuevo: se viola «máximo una carta por (organización, expediente)». El lease de 5 min solo evita concurrencia local; no resuelve la incertidumbre post-envío ni la reanudación del worker antiguo. Llamar «inevitable» al riesgo no lo hace aceptable: la regla exige detener la automatización en casos inciertos, no imprimir dos veces.

## Alternativa: máquina de estados persistente

**Tabla `print_jobs`**: `(organization, case_id)` UNIQUE, `state ∈ {new, sending, uncertain, completed}`, `attempt_uuid`, `message_uuid`, `lease_expires`, `worker_id`.

**Flujo por mensaje entrante:**

1. **Transacción T1.** `INSERT … ON CONFLICT DO NOTHING`. Si la fila ya existe, leer `state`:
   - *completed* → ACK, fin (prevención de duplicado).
   - *uncertain* → ACK, fin (ya está en revisión humana).
   - *sending* con lease vigente → ACK (otro worker actúa).
   - *sending* con lease expirado → pasar a **incertidumbre** (ver abajo).
   - *new* → continuar.
2. **Transacción T2.** `UPDATE state='sending', attempt_uuid=…, lease_expires=now()+5 min` condicionado a `state='new'`. COMMIT.
3. **Efecto externo.** `print("org:case", body)`.
4. **Respuesta exitosa → T3.** `UPDATE state='completed' WHERE state='sending' AND attempt_uuid=mío`. COMMIT. ACK.
5. **Timeout, error o caída → T4.** `UPDATE state='uncertain' WHERE state='sending' AND attempt_uuid=mío`. COMMIT. Encolar para revisión manual. Nunca se reenvía automáticamente.

### Ventana crítica y worker antiguo

Entre el paso 3 y el T3 el estado queda en `sending`. Si el worker se pausa indefinidamente y otro toma la reentrega, este ve `sending` con lease expirado y ejecuta T4 (→ `uncertain`). Cuando el worker antiguo se reanuda e intenta T3, la cláusula `WHERE state='sending'` ya no se cumple; el UPDATE afecta 0 filas y el resultado se descarta. No se necesita cercar desde el proveedor: el propio predicado de estado actúa como guarda.

### Garantía de impresión vs. prevención de duplicado

- **Prevención:** UNIQUE compuesto + estado `completed` + clave externa estable dentro de 6 h.
- **Garantía de entrega:** para operaciones *nuevas sin fallos* el camino feliz (T1→T2→paso 3→T3) imprime de inmediato. Si hay fallo, la cola reentrega 48 h; si el estado quedó `uncertain`, un operador humano confirma si la carta salió y, solo si no salió, restaura `state='new'` para reenviar. Así se cumple «en inciertos se permite detener» sin sacrificar la obligación de imprimir en el caso limpio.

## Pruebas

| Escenario | Comportamiento esperado |
|---|---|
| **t+10 h**: respuesta perdida a las 10:00, reentrega a las 20:00 | Worker nuevo halla `sending`, lease expirado → `uncertain`. No llama a `print`. Revisión humana decide. Worker antiguo reanuda: T3 afecta 0 filas. Cero duplicados. |
| **Caída antes del envío** (crash entre T2 y paso 3) | Estado queda `sending`. Reentrega → mismo camino: `uncertain`. Operador verifica que no hubo impresión y restaura `new`; se reimprime una sola vez. |
| **Dos organizaciones, mismo expediente** (`org_A:exp_1`, `org_B:exp_1`) | UNIQUE es `(organization, case_id)`: filas distintas. Claves externas distintas. Ambas imprimen independientemente; ninguna bloquea a la otra. |

No se inventan endpoints: solo `print(key,body)`. Ningún timeout se interpreta como «no se hizo»; toda ambigüedad se resuelve deteniendo la automatización.