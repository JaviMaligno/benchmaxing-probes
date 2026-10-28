La propuesta no cumple la regla. Usar `organization:case` como clave y un lease de 5 minutos con reenvío automático al expirar solo evita duplicados mientras el proveedor recuerde la clave (6 h). En el caso descrito, la impresión se acepta a las 10:00 y la reentrega llega a t+10 h: el proveedor ya olvidó la clave y el reenvío con la misma key imprime una segunda carta. Decir que ese riesgo es «inevitable» es falso: se evita no reenviando ante incertidumbre. Tampoco es correcto asumir que un timeout implica que el trabajo remoto no se hizo.

**Alternativa con estados persistentes.** Tabla con UNIQUE compuesto `(organización, expediente)`, columnas `estado`, `claim_token`, `lease_hasta`. La clave para `print` no debe ser `attempt_uuid`; debe ser determinista, p. ej. `organización:expediente`, para aprovechar la deduplicación de 6 h solo como mitigación, nunca como garantía.

- **Pendiente:** nadie ha intentado imprimir. En transacción, reclamar: pasar a `imprimiendo` con `claim_token` único y `lease_hasta` (p. ej. 5 min). Solo el poseedor del token puede llamar a `print`.
- **Imprimiendo (lease vigente):** se persiste la intención **antes** de emitir el efecto externo. Si `print` responde OK, el poseedor hace `UPDATE … WHERE claim_token = <token>` y pasa a `completado`. Si falla al confirmar o el lease expira sin confirmación, transición a `incierto`; quedará detenido para revisión manual. No hay reenvío automático.
- **Incierto:** el efecto pudo o no haberse producido. Nunca se reimprime automáticamente; la reentrega con el mismo `message_uuid` no dispara `print`. Requiere intervención humana. Esto cumple la cláusula «en casos inciertos se permite detener la automatización».
- **Completado:** las reentregas se ignoran.

**Ventana entre guardar estado y emitir el efecto.** El cambio `pendiente → imprimiendo` con token es una transacción local antes de `print`. Si el worker cae en ese hueco, el registro queda `imprimiendo` con lease activo; al vencer pasa a `incierto`, no a reimprimir. Nadie reimprime mientras no haya evidencia de que no se envió; ante la duda, se detiene.

**Reanudación del worker antiguo.** Al despertar, el worker viejo solo puede completar mediante `UPDATE … WHERE claim_token = <su token>`. Si su lease expiró y otro worker reclamó (cambió el token), su `UPDATE` afecta 0 filas: no puede marcar `completado` ni volver a imprimir. Sin «cerca» desde el proveedor: el token invalida al poseedor antiguo en la DB durable.

**Separación.**
- *Prevención de duplicados:* UNIQUE compuesto + reclamación con token + transición a `incierto` (no reimpresión) cuando no hay confirmación + ignorar reentregas en `incierto`/`completado`.
- *Garantía de impresión:* solo se garantiza para operaciones nuevas sin fallos: `pendiente` con claim vigente imprime y completa. Ante pérdida de respuesta o lease vencido la garantía se suspende deliberadamente a favor de no duplicar; la carta pendiente queda en `incierto` para revisión. No se puede garantizar ambas cosas a la vez sin consulta ni cancelación.

**Pruebas.**
1. *t+10 h:* a las 10:00 se acepta el `print` y se pierde la respuesta; el lease expira y el worker queda pausado. A t+10 h llega la reentrega. El worker que reclama ve el intento sin confirmar y lo marca `incierto`, sin llamar a `print`. Aserción: una sola carta emitida, cero duplicados.
2. *Caída antes del envío:* el worker persiste `imprimiendo` con token y cae antes de invocar `print`. Al expirar el lease, otro worker lo marca `incierto`; no reimprime. Aserción: cero impresiones y estado `incierto`, no reenvío automático. El worker viejo, al reanudarse con token inválido, no puede completar ni reenviar.
3. *Dos organizaciones, mismo expediente:* `organización A` y `organización B` reclaman filas distintas por el UNIQUE compuesto y emiten claves distintas. Aserción: dos cartas, una por organización, sin conflicto.