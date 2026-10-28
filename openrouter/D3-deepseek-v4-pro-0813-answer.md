Revisión sintética de especificación

**Reglas finales implementables**
- Solo exportan usuarios autenticados con tenant activo. Invitados nunca exportan. Administrador de plataforma sin pertenencia/rol en el tenant no accede a datos.
- Miembro ve solo sus facturas; gestor ve todas las de su tenant.
- Facturas borradas lógicamente no se exportan, salvo gestor con `audit_export` y con `include_deleted=true`.
- Rango temporal UTC de emisión: `[inicio, fin)`, máximo 31 días; gestores con `migration_export` pueden hasta 90 días. Fechas `YYYY-MM-DD` son medianoche UTC.
- Toda factura `restricted` se exporta sin importes; ningún permiso exime.
- `cross_tenant_support` solo permite cambiar tenant activo; después se exige pertenencia y rol en el tenant destino.
- Caché reutilizable solo si se revalida el contexto de seguridad actual.

**Decisiones**

- **C1: PERMITIR.** Gestor de A ve factura normal no borrada de su tenant dentro del rango válido.
- **C2: DENEGAR.** El miembro no puede incluir borradas; `audit_export` solo habilita a gestores.
- **C3: DENEGAR.** `include_deleted=false` excluye la factura borrada, aunque el gestor tenga `audit_export`.
- **C4: PERMITIR, sin importes.** El gestor con `migration_export` puede pedir 90 días; la factura `restricted` se incluye sin importes.
- **C5: DENEGAR.** Los invitados nunca exportan, aunque tengan `audit_export` o `migration_export`.
- **C6: DENEGAR.** `cross_tenant_support` permite cambiar al tenant B, pero no otorga pertenencia ni rol en B.
- **C7: DENEGAR.** Miembro solo ve facturas propias; no puede exportar facturas de otro miembro.
- **C8: DENEGAR.** La emisión es exactamente en el extremo final `2026-02-01T00:00:00Z`; el intervalo `[inicio, fin)` la excluye.

**Evaluación de la propuesta del compañero**

No es correcta. Cachear por `(tenant, inicio, fin, include_deleted)` y compartir entre todos los usuarios del tenant evita fugas entre tenants, pero no entre usuarios del mismo tenant: un miembro recibiría facturas ajenas si se reutiliza el resultado de un gestor. Tampoco respeta permisos como `audit_export`, `migration_export`, ni la eliminación de importes en facturas `restricted`.

Una reutilización segura debe revalidar al servir:
- que el usuario sigue perteneciendo al tenant y mantiene su rol y permisos;
- aplicar filtro de visibilidad miembro/gestor;
- que las facturas no hayan sido borradas o marcadas `restricted` después de cachear;
- que `restricted` se sirva sin importes;
- invalidar o versionar la caché ante cambios de rol, permisos, borrado lógico o restricción.

No basta añadir usuario a la clave: hay que revalidar cambios posteriores y aplicar filtros de seguridad al momento de servir.