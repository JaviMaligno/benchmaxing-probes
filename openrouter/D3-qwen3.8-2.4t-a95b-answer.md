

## Reglas finales implementables

1. **Aislamiento por tenant**: solo el tenant activo es visible. `cross_tenant_support` permite al admin cambiar tenant, pero exige pertenencia y rol en el destino; no otorga membresía.
2. **Visibilidad**: miembro → solo facturas propias; gestor → todas del tenant; invitado → nunca exporta. Admin de plataforma no accede a datos de tenant salvo regla 1.
3. **Borrado lógico**: excluido por defecto. Solo gestor + `audit_export` + `include_deleted=true` las incluye. Miembros e invitados quedan excluidos siempre.
4. **Intervalo temporal**: `[inicio, fin)` sobre fecha UTC de emisión; YYYY-MM-DD ≡ medianoche UTC. Límite general 31 días; `migration_export` amplía a 90 (solo gestores).
5. **Restricted**: se eliminan importes de toda factura `restricted`; el resto de campos se mantiene. Ningún permiso exime.
6. **Caché**: exportaciones reutilizables se almacenan (ver evaluación abajo).

## Decisiones C1-C8

| Caso | Decisión | Motivo |
|------|----------|--------|
| C1 | **PERMITIR** | Gestor ve todas las facturas de A; factura normal, fecha 01-15 ∈ [01-01, 02-01); rango 31 d. |
| C2 | **DENEGAR** | `audit_export` solo aplica a gestores. Miembro no puede incluir borradas aunque posea el permiso. |
| C3 | **DENEGAR** | Factura borrada + `include_deleted=false` → queda excluida; el permiso no se activa sin la bandera. |
| C4 | **PERMITIR** (sin importes) | `migration_export` habilita 90 d (01-01→01-04 = 90 d exactos). Factura `restricted`: se suprimen importes, resto visible. |
| C5 | **DENEGAR** | Invitado nunca exporta; permisos extra no modifican esa prohibición. |
| C6 | **DENEGAR** | `cross_tenant_support` permite el cambio, pero sin pertenencia ni rol en B no se supera la verificación posterior. |
| C7 | **DENEGAR** | Miembro solo ve facturas propias; la factura pertenece a otro miembro. |
| C8 | **DENEGAR** | Emisión = 2026-02-01T00:00:00Z coincide con el extremo abierto `fin`; intervalo `[inicio, fin)` la excluye. |

## Evaluación de la propuesta de caché del compañero

El compañero propone clave `(tenant, inicio, fin, include_deleted)` y afirma que, al filtrar por tenant, no puede haber fuga entre usuarios. **Es incorrecto.**

**Problema estructural**: la clave omite el eje de visibilidad. Un miembro y un gestor del mismo tenant consultarían la misma entrada, pero el miembro solo debe ver sus facturas y el gestor todas. Compartir el resultado completo expondría facturas ajenas al miembro.

**Qué debe incorporar o revalidar una reutilización segura:**

1. **Identidad y rol en la clave (o en la verificación de lectura)**: como mínimo `(tenant, user_id, rol, inicio, fin, include_deleted)`. Si se prefiere una clave más corta por rendimiento, la lectura debe revalidar que el solicitante sigue teniendo el mismo rol y que las facturas devueltas respetan su visibilidad.
2. **Invalidación ante cambios de permisos**: revocación de `audit_export` o `migration_export`, o cambio de rol (miembro→gestor o viceversa), debe invalidar o marcar como *stale* la entrada. Un gestor que pierde `audit_export` no puede seguir leyendo una caché que incluye borradas.
3. **Borrado lógico posterior**: si una factura se borra lógicamente tras cachearse, la entrada debe invalidarse o filtrarse en la lectura; de lo contrario se servirían datos que ya no deben aparecer.
4. **Restricción posterior**: si una factura pasa a `restricted` después de generarse la caché, los importes quedarían expuestos. Se requiere invalidación o enmascaramiento en la entrega.
5. **TTL corto + verificación de integridad**: incluso sin eventos explícitos, un TTL limitado (p. ej. 5-15 min) reduce la ventana de inconsistencia.

En resumen: la caché no puede ser un blob compartido por tenant; necesita granularidad por usuario/rol y un mecanismo de invalidación reactiva a cambios de estado (permisos, borrado, restricción).