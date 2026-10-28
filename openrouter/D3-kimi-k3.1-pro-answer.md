## Reglas finales implementables

1. **Ámbito y visibilidad:** toda exportación se limita al tenant activo. Un miembro solo exporta sus facturas; un gestor, todas las de ese tenant. Los invitados nunca exportan. El administrador de plataforma no tiene acceso por ese solo rol.
2. **Cambio de tenant:** `cross_tenant_support` solo permite al administrador usar el selector. Tras cambiar, debe acreditar pertenencia y rol en el tenant destino; el permiso no le otorga visibilidad de miembro o gestor.
3. **Intervalo:** filtrar por `issued_at` en UTC, con `[inicio, fin)`: inicio incluido, fin excluido. Una fecha `YYYY-MM-DD` representa las 00:00:00 UTC. Máximo general: 31 días; un gestor con `migration_export` puede solicitar hasta 90 días.
4. **Borradas:** se excluyen siempre, salvo que el solicitante sea gestor, tenga `audit_export` y envíe `include_deleted=true`. El permiso no habilita esta excepción para miembros o invitados.
5. **Restringidas:** toda factura `restricted` se exporta sin importes, conservando los demás campos permitidos. Ningún permiso elimina esta obligación.
6. La caché es solo una optimización: nunca sustituye la autorización ni las reglas de visibilidad y transformación vigentes.

## Decisiones

- **C1 — PERMITIR:** gestor de A; factura normal de A, dentro del intervalo.
- **C2 — DENEGAR:** es miembro; `audit_export` no le permite incluir borradas.
- **C3 — DENEGAR** para esa factura: con `include_deleted=false`, debe excluirse aunque el gestor tenga `audit_export`.
- **C4 — PERMITIR:** el gestor con `migration_export` puede usar el intervalo de 90 días. Se incluye la factura, pero **sin importes** por ser `restricted`.
- **C5 — DENEGAR:** los invitados nunca exportan, independientemente de sus permisos.
- **C6 — DENEGAR:** falta pertenencia y rol en B; `cross_tenant_support` solo permite seleccionar el tenant.
- **C7 — DENEGAR:** un miembro no puede exportar facturas de otro miembro.
- **C8 — DENEGAR** para esa factura: emitida exactamente en `fin`, queda fuera por ser el intervalo semiabierto.

## Evaluación de la propuesta de caché

**Es incorrecta.** Filtrar por tenant evita fugas entre tenants, pero no entre usuarios del mismo tenant. La clave propuesta podría entregar a un miembro facturas ajenas visibles para un gestor, borradas a quien ya no tenga `audit_export`, o importes ocultados incorrectamente. Tampoco basta con añadir el identificador de usuario.

Una reutilización segura debe:

- **Reautorizar cada solicitud con el estado actual:** tenant activo, pertenencia, rol, propiedad/visibilidad, permisos, intervalo e `include_deleted`. Si cambian rol o permisos, invalidar o descartar resultados incompatibles; por ejemplo, revocar `audit_export` impide reutilizar una exportación con borradas, y revocar `migration_export` impide reutilizar una de más de 31 días.
- **Separar la caché por contexto efectivo de visibilidad y seguridad**, no solo por tenant e intervalo, o almacenar datos intermedios y volver a filtrarlos antes de servirlos.
- **Garantizar frescura mediante invalidación/versionado o revalidación:** si una factura se borra después de cachear, debe omitirse salvo la excepción de auditoría vigente; si pasa a `restricted`, deben eliminarse sus importes antes de responder. Ante cualquier duda de vigencia, regenerar.