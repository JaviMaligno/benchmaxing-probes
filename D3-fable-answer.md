## Reglas finales consolidadas

1. Toda exportación opera solo sobre el tenant activo del usuario.
2. Invitados nunca exportan, sin excepción alguna (ningún permiso lo altera).
3. Miembros exportan solo sus propias facturas; gestores, todas las del tenant.
4. Facturas borradas lógicamente excluidas por defecto; se incluyen únicamente si el solicitante es gestor con `audit_export` **y** envía `include_deleted=true`.
5. Filtro por fecha de emisión UTC, intervalo semiabierto `[inicio, fin)`; fechas `YYYY-MM-DD` = medianoche UTC. Límite 31 días; gestores con `migration_export` pueden llegar a 90.
6. Toda factura `restricted` se exporta sin importes; el resto de campos sí sale. Ningún permiso exime.
7. El rol de administrador de plataforma no da acceso a datos. Con `cross_tenant_support` puede cambiar de tenant activo, pero tras el cambio se exige pertenencia y rol en el destino.

## Decisiones C1–C8

(Rango por defecto `[2026-01-01, 2026-02-01)` = 31 días exactos, válido; emisión 2026-01-15 salvo C8.)

- **C1 — PERMITIR.** Gestor ve todas las facturas de su tenant; rango válido.
- **C2 — DENEGAR.** `audit_export` solo habilita a gestores; la nota de 09:20 no cambia permisos de miembros. La factura borrada queda excluida aunque sea propia.
- **C3 — DENEGAR** (la factura no sale). Tiene el permiso, pero `include_deleted=false`: la condición es conjunta, así que la borrada se excluye de la exportación.
- **C4 — PERMITIR** (sin importes). El rango 2026-01-01 a 2026-04-01 son exactamente 90 días (31+28+31; 2026 no es bisiesto), dentro del límite de `migration_export`. La factura `restricted` sale con los importes eliminados.
- **C5 — DENEGAR.** Invitados nunca exportan; ninguna nota posterior lo modificó, y ambos permisos declaran explícitamente no cambiar reglas de invitados.
- **C6 — DENEGAR.** `cross_tenant_support` solo permite el cambio de selector; sin pertenencia ni rol en B no hay acceso, y el permiso no lo convierte en miembro ni gestor.
- **C7 — DENEGAR.** Un miembro solo ve sus propias facturas.
- **C8 — DENEGAR** (factura fuera de rango). El intervalo es `[inicio, fin)`: `2026-02-01T00:00:00Z` coincide con `fin` y queda excluida.

## Evaluación de la propuesta de caché

**Es incorrecta.** Filtrar por tenant no basta, por tres motivos:

1. **Alcance por rol dentro del tenant.** Un miembro solo debe ver sus facturas; una caché compartida generada por un gestor le filtraría las de otros miembros (justo lo que C7 deniega). Los invitados ni siquiera deben poder leerla.
2. **`include_deleted` en la clave no autoriza.** Que la clave incluya el flag no verifica que quien reutiliza la entrada sea gestor con `audit_export`; un miembro podría leer una caché con borradas.
3. **Datos obsoletos.** Una factura borrada o marcada `restricted` *después* de cachear seguiría apareciendo (o con importes) en entradas antiguas.

**Reutilización segura:**

- **Clave por alcance de visibilidad**, no solo por tenant: `(tenant, alcance, inicio, fin, include_deleted)`, donde alcance es `todas` (gestores) o `miembro:<id>`. Los invitados nunca leen ni escriben caché.
- **Autorización en el momento de servir, no de cachear:** al reutilizar una entrada, revalidar rol y permisos *actuales* del solicitante (gestor vigente para alcance `todas`; `audit_export` vigente si `include_deleted=true`; `migration_export` vigente si el rango excede 31 días). Así un cambio de rol o revocación posterior invalida el acceso aunque la entrada exista.
- **Invalidación por mutación:** versionar los datos del tenant (o por factura) e invalidar/revalidar entradas cuando una factura se borra, restaura o cambia su marca `restricted`. Alternativa: TTL corto más comprobación de versión al servir.
- **Enmascarado `restricted` idealmente al servir**, no horneado en la entrada, para que un cambio de marca posterior surta efecto sin depender solo de la invalidación.

En resumen: la caché puede compartirse solo entre usuarios con **idéntico alcance efectivo**, y cada lectura debe repetir la autorización y comprobar frescura.