# Phase 1 — Company Foundation

## Goal

Create a secure, deployable backend foundation without changing the existing AXLWORKS public website.

## Work breakdown

### P1.1 — Repository isolation
- [x] Create a dedicated `company-platform/` module.
- [x] Preserve root Next.js app and its existing Docker Compose file.
- [x] Add product and implementation documentation.

### P1.2 — Backend and infrastructure scaffold
- [x] Add FastAPI application entry point.
- [x] Add environment-based settings.
- [x] Add PostgreSQL Docker service.
- [x] Add API container definition.
- [x] Add liveness and database readiness endpoints.
- [x] Add initial Employee and AuditLog SQLAlchemy models.
- [ ] Add Alembic migration environment and initial migration.
- [ ] Add automated tests and CI.

### P1.3 — Identity and employee registry
- [ ] Add CEO user model and secure password hashing.
- [ ] Add JWT access/refresh session strategy and logout/revocation.
- [ ] Add bootstrap CEO process that requires explicit secrets.
- [ ] Add employee list/detail endpoints.
- [ ] Seed Killua, Dipa, Kyou, and Ren as inactive/unconnected agents.
- [ ] Add role-based authorization and ownership checks.

### P1.4 — Audit and operational safety
- [ ] Write immutable audit events for authentication and administrative changes.
- [ ] Add request IDs and structured logs.
- [ ] Add rate limiting and secure CORS configuration.
- [ ] Add backup/restore runbook.
- [ ] Verify secrets are not committed.

## Acceptance criteria

1. Existing root Next.js website still builds and deploys independently.
2. Company API starts from Docker Compose.
3. PostgreSQL health check passes.
4. `GET /health` returns liveness status.
5. `GET /ready` returns success only when the database is reachable.
6. Employee model supports stable IDs, role, status, and timestamps.
7. Audit events can be traced to an actor and request.
8. CEO authentication and employee endpoints pass automated tests before any real integration is enabled.

## Safety gates

No WhatsApp sending, Google Ads changes, customer registration submission, or financial execution is enabled in Phase 1. External actions remain disabled until explicit permission scopes, approvals, idempotency, and audit coverage are tested.
