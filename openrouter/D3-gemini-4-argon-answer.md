### 1. Reglas Finales Implementables

*   **Autorización y Alcance:** Solo exportan usuarios con pertenencia y rol válido en el tenant activo.
    *   `Gestor`: exporta todas las facturas del tenant.
    *   `Miembro`: exporta únicamente sus propias facturas.
    *   `Invitado`: nunca exporta (ningún permiso altera esto).
    *   `Administrador de plataforma`: sin acceso a datos. Con `cross_tenant_support` puede cambiar su tenant activo, pero sigue requiriendo pertenencia y rol (`Gestor` o `Miembro`) en el tenant destino para exportar.
*   **Filtro Temporal:** Basado en fecha de emisión UTC bajo intervalo semiabierto `[inicio, fin)`. El formato `YYYY-MM-DD` equivale a `00:00:00Z`. El rango máximo es de **31 días**, ampliable hasta **90 días** exclusivamente para `Gestores` con el permiso `migration_export`.
*   **Borrados Lógicos:** Las facturas borradas se excluyen por defecto. Solo se incluyen si el usuario es `Gestor`, tiene el permiso `audit_export` y solicita explícitamente `include_deleted=true`.
*   **Enmascaramiento (`restricted`):** A toda factura marcada como `restricted` se le deben suprimir los importes, manteniendo el resto de campos. Ningún rol ni permiso exime de esta regla.

---

### 2. Decisiones por Caso (C1–C8)
*(Nota: el rango por defecto `[2026-01-01T00:00:00Z, 2026-02-01T00:00:00Z)` abarca exactamente 31 días).*

*   **C1: PERMITIR.** Es Gestor en su tenant activo A, el rango es válido (31 días) y la factura es normal y está dentro del intervalo.
*   **C2: DENEGAR.** El permiso `audit_export` solo habilita exportar facturas borradas a los Gestores; no modifica los permisos de los Miembros.
*   **C3: DENEGAR** *(la inclusión de la factura).* Aunque es Gestor con `audit_export`, pasa el parámetro `include_deleted=false`, por lo que la factura borrada no sale.
*   **C4: PERMITIR (sin importes).** Es Gestor con `migration_export` y pide exactamente 90 días (31 ene + 28 feb + 31 mar = 90). La factura sale por no estar borrada, pero **se deben omitir sus importes** por ser `restricted`.
*   **C5: DENEGAR.** Los Invitados nunca pueden exportar, independientemente de los permisos adicionales que tengan asignados.
*   **C6: DENEGAR.** `cross_tenant_support` permite cambiar el selector al tenant B, pero no otorga pertenencia ni rol en B.
*   **C7: DENEGAR.** Un Miembro solo tiene acceso a sus propias facturas, nunca a las de otros miembros de su tenant.
*   **C8: DENEGAR** *(la inclusión de la factura).* El intervalo `[inicio, fin)` es abierto a la derecha. La fecha `2026-02-01T00:00:00Z` coincide exactamente con el límite superior `fin`, quedando fuera del rango.

---

### 3. Evaluación de la Propuesta de Caché

**¿Es correcta?**
**No, es incorrecta e insegura.** Aislar solo por tenant ignora las reglas de control de acceso internas (provocando fugas de datos *intra-tenant*) y la mutabilidad del estado de las facturas. Un Miembro o Invitado podría recibir la caché generada por un Gestor (viendo facturas ajenas), o un usuario sin `audit_export` podría forzar `include_deleted=true` y leer una caché previa con facturas borradas.

**Requisitos para una reutilización segura:**

1.  **Revalidación de autorización en tiempo real (Cambios de rol/permisos):** Antes de leer la caché, el sistema debe validar los permisos y el rol *actuales* del solicitante frente a la petición. Si a un Gestor se le revoca `audit_export`, `migration_export` o pasa a ser Miembro/Invitado tras haberse creado la caché, esta validación previa rechazará la solicitud antes de tocar la caché.
2.  **Segregación de alcance en la clave:** La clave debe incorporar el alcance de visibilidad: `(tenant, inicio, fin, include_deleted, alcance)`, donde `alcance` sea `ALL` (para Gestores) o `USER:<id>` (para Miembros).
3.  **Gestión de borrados y restricciones posteriores:** Si una factura se borra lógicamente o pasa a ser `restricted` *después* de cachear, servir el resultado estático filtraría datos prohibidos o importes restringidos. Para solucionarlo se debe:
    *   Invalidar las cachés del tenant (o incluir una versión de estado `tenant_mutation_version` en la clave) ante cualquier evento de borrado o cambio en la marca `restricted` de una factura.
    *   Alternativamente, no cachear el archivo final, sino evaluar el estado `deleted` y enmascarar los importes de registros `restricted` dinámicamente al momento de servir.