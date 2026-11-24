# Phase 1 — Company Foundation

## Completed in this increment
- [x] CEO user model and Argon2 password hashing.
- [x] Short-lived signed JWT access tokens.
- [x] Login and current-user endpoints.
- [x] Authenticated employee list/detail endpoints.
- [x] Idempotent seed for Killua, Dipa, Kyou, Ren (all inactive).
- [x] Explicit CEO bootstrap with 12+ character password requirement.
- [x] Alembic initial migration.
- [x] Initial API tests for health and unauthenticated access.
- [x] API startup runs migration, CEO bootstrap, employee seed.

## Still required before production
- [ ] Run Docker build, migration, and tests in real environment.
- [ ] Server-side token/session revocation and login rate limiting.
- [ ] Administrative employee management endpoints.
- [ ] Request IDs and structured logs.
- [ ] Audit records for all administrative mutations.
- [ ] Production CORS and TLS reverse proxy.
- [ ] Backup/restore runbook and secret review.

## Safety
No WhatsApp sends, Google Ads changes, customer registration submission, or financial execution.
