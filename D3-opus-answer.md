## Reglas finales implementables

**R1 — Tenant.** La exportación se limita al tenant activo. Sin excepciones.

**R2 — Rol.** Invitado: nunca exporta. Miembro: solo facturas de las que es propietario. Gestor: todas las del tenant.

**R3 — Borrado lógico.** Excluidas por defecto. Única excepción: rol gestor **y** permiso `audit_export` **y** `include_deleted=true` (las tres condiciones).

**R4 — Admin de plataforma.** El rol no otorga acceso a datos de ningún tenant. `cross_tenant_support` solo habilita cambiar el tenant activo en el selector; tras el cambio se exige pertenencia y rol propios en el destino, que el permiso no confiere.

**R5 — Rango.** Filtro por fecha UTC de emisión, intervalo semiabierto `[inicio, fin)`. `YYYY-MM-DD` = medianoche UTC. Máximo 31 días; máximo 90 días solo para gestor con `migration_export`.

**R6 — Restricted.** En toda factura marcada `restricted` se eliminan los importes; el resto de campos se incluye. Ningún permiso exime.

**Orden de evaluación:** tenant → rol → rango → visibilidad de fila → borrado → redacción.

## Decisiones C1–C8

Rango base 2026-01-01 → 2026-02-01 = 31 días exactos, válido.

| Caso | Decisión | Motivo |
|---|---|---|
| C1 | **PERMITIR** (completa) | Gestor, factura viva de su tenant, dentro de rango. |
| C2 | **DENEGAR** (la factura) | `audit_export` solo habilita borradas a **gestores**; el miembro puede exportar, pero la factura borrada no sale. |
| C3 | **DENEGAR** (la factura) | Requiere las tres condiciones; `include_deleted=false` bloquea. |
| C4 | **PERMITIR sin importes** | 90 días exactos, cubiertos por `migration_export` de gestor; `restricted` obliga a suprimir importes. |
| C5 | **DENEGAR** (la exportación) | Invitado nunca exporta; los permisos no alteran esa regla. |
| C6 | **DENEGAR** | Sin pertenencia ni rol en B; `cross_tenant_support` solo cambia el selector. |
| C7 | **DENEGAR** | Miembro solo ve facturas propias. |
| C8 | **DENEGAR** | `2026-02-01T00:00:00Z` es el extremo excluido de `[inicio, fin)`. |

## Sobre la propuesta del compañero

**Es incorrecta.** Filtrar por tenant no impide fugas *dentro* del tenant: la visibilidad de fila depende del rol. Con la clave `(tenant, inicio, fin, include_deleted)`, un miembro que pida el mismo rango obtiene el artefacto generado por un gestor y ve las facturas de todos (rompe C7). Peor: con `include_deleted=true` en la clave, un gestor sin `audit_export` reutiliza el resultado de otro que sí lo tiene (rompe C3).

**Qué debe incorporar una reutilización segura:**

1. **Clave por alcance efectivo, no por usuario.** `scope = "all"` (gestor) o `"owner:<user_id>"` (miembro), derivado *en el momento de la petición*. Así se comparte entre gestores sin fugar hacia miembros, y una degradación de rol cambia la clave: el ex-gestor deja de poder acertar la entrada `all`. Añadir a la clave el `include_deleted` **efectivo** (ya resuelto contra `audit_export`), no el solicitado.

2. **Revalidación en cada acierto, no solo al escribir.** Recalcular rol y permisos actuales y comprobar que el scope y los flags de la entrada coinciden con los recalculados. Incluir un `identity_version` (epoch de roles/permisos del usuario y del tenant) que se incrementa en cada revocación, de modo que quitar `audit_export` o `migration_export` invalide inmediatamente lo cacheado.

3. **Invalidación por cambios en los datos posteriores al cacheado.** Un borrado lógico o un marcado `restricted` aplicado después deja el artefacto obsoleto y filtra datos que ya no deben salir. Mantener un `tenant_data_version` que se incremente en cada soft-delete, restauración o cambio de `restricted`, e incluirlo en la clave; complementar con invalidación dirigida al rango de fechas afectado y TTL corto como red de seguridad.

4. **Redacción fuera de la caché o versionada.** Almacenar únicamente el artefacto ya redactado, nunca importes en claro reutilizables; incluir `redaction_policy_version` en la clave. Alternativa preferible: cachear el conjunto de IDs y aplicar redacción en lectura.

5. **Nunca degradar entradas:** un artefacto con borradas no puede servir a una petición sin borradas por simple filtrado posterior si el consumidor no reaplica la política completa.