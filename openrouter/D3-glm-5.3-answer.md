## Reglas finales (implementables)

**R1 Contexto.** Cada usuario opera solo sobre su tenant activo. El rol de admin de plataforma no da acceso a datos de tenants. `cross_tenant_support` solo permite cambiar el tenant activo; tras el cambio se exige pertenencia y rol en el destino, y no convierte a nadie en miembro o gestor.

**R2 Visibilidad por rol.** Miembro: solo sus facturas. Gestor: todas las de su tenant. Invitado: nunca exporta, sin excepciones por permisos.

**R3 Borradas.** Se excluye el borrado lógico por defecto. Solo entra con los tres requisitos simultáneos: rol gestor + `audit_export` + `include_deleted=true`.

**R4 Ventana temporal.** Filtro por fecha UTC de emisión, intervalo `[inicio, fin)`; `YYYY-MM-DD` = medianoche UTC. Límite general 31 días; gestor con `migration_export`: hasta 90 días.

**R5 Restringidas.** Toda factura `restricted` se exporta sin importes, con el resto de campos. Ningún permiso exime.

**R6 Caché.** Solo reutilización segura (ver abajo).

## Casos

- **C1 — PERMITIR.** Gestor de A sin extras: ve toda factura de A. Fecha 2026-01-15 dentro de [2026-01-01, 2026-02-01), rango de 31 días válido. Factura normal: completa con importes.
- **C2 — DENEGAR (esa factura).** `audit_export` solo habilita borradas a gestores; para un miembro no cambia nada. La borrada propia no sale aunque `include_deleted=true`.
- **C3 — DENEGAR (esa factura).** `include_deleted=false` excluye borradas; tener `audit_export` es irrelevante con el flag desactivado.
- **C4 — PERMITIR con importes redactados.** Rango 2026-01-01→2026-04-01 = 90 días exactos, permitido a gestor con `migration_export`. Factura del 2026-01-15, no borrada, de A: visible para gestor, pero al ser `restricted` se exporta sin importes; el resto de campos sí.
- **C5 — DENEGAR.** Invitado nunca exporta; `audit_export` ni `migration_export` lo habilitan (ninguna nota crea excepción para invitados).
- **C6 — DENEGAR.** `cross_tenant_support` cambia el selector, pero exige pertenencia y rol en B; sin pertenencia no hay acceso, y el rol de plataforma no aporta datos de tenants.
- **C7 — DENEGAR (esa factura).** Un miembro solo ve sus propias facturas, nunca las de otro miembro aunque ambas sean de A.
- **C8 — DENEGAR.** El fin es exclusivo: 2026-02-01T00:00:00Z coincide exactamente con el límite superior y queda fuera de [inicio, fin).

## Propuesta del compañero: INCORRECTA, no permitir

Su afirmación falla porque **el tenant no es la unidad de autorización**: dentro del mismo tenant hay resultados distintos por usuario.

Fallos concretos:
1. **Miembro vs gestor:** un miembro reutilizaría el caché del tenant y vería facturas de otros miembros.
2. **`include_deleted` en la clave no basta:** un gestor *sin* `audit_export` que pida `include_deleted=true` heredaría borradas cacheadas por un gestor *con* el permiso.
3. **Límite de rango:** un gestor sin `migration_export` reutilizaría una exportación de 90 días, violando su tope de 31.
4. **Cambios posteriores al cacheado:** facturas borradas o marcadas `restricted` después seguirían saliendo con datos (importes) que ya no deben exponerse; revocaciones de rol, permiso o pertenencia dejarían lecturas obsoletas.

**Reutilización segura debe incorporar o revalidar en cada lectura:**
- Pertenencia vigente al tenant y tenant activo (incluye el caso `cross_tenant_support` sin pertenencia).
- Rol vigente y, si es miembro, filtro por propietario/usuario.
- Permisos efectivos *en el momento de reutilizar*: `audit_export` (para respetar borradas) y `migration_export` (para validar que el rango ≤ tope del usuario).
- Estado actual de datos posteriores al cacheado: re-filtrar o invalidar borrados lógicos y re-aplicar redacción de `restricted` (comparar marcas de tiempo/versiones o invalidar por eventos de borrado y marcado).
- Alternativa robusta: cachear solo el cálculo bruto por (tenant, inicio, fin) y reaplicar autorización, redacción y frescura en cada reutilización, con invalidación inmediata ante cambios de rol, permisos, pertenencia, borrado o marcado `restricted`.