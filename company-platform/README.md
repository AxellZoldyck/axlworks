# AXLWORKS Company Platform

Autonomous AI company operating system for Axell and the virtual employees Killua, Dipa, Kyou, and Ren.

This platform is intentionally isolated from the existing AXLWORKS public website. The existing Next.js application remains at the repository root; this platform lives in `company-platform/`.

## Phase 1 scope

- FastAPI backend foundation
- PostgreSQL service
- Environment-based configuration
- Database connectivity and readiness endpoint
- Initial employee and audit-log data models
- Docker Compose deployment foundation
- Product, character, security, and implementation documentation

CEO authentication, employee CRUD, Alembic migrations, and audit-log writing are the next Phase 1 implementation tasks. No autonomous external actions are enabled in this foundation commit.

## Local development

1. Copy `.env.example` to `.env` and replace all development secrets.
2. Run `docker compose -f docker-compose.company.yml up --build`.
3. API docs: `http://localhost:8000/docs`
4. Liveness: `http://localhost:8000/health`
5. Readiness: `http://localhost:8000/ready`

The root website's existing `docker-compose.yml` and port 3000 are unchanged.

## Production notes

- Use a private network for PostgreSQL; do not expose port 5432 publicly.
- Put the API behind Caddy or another TLS reverse proxy.
- Use unique, high-entropy secrets in the VPS environment.
- Enable encrypted off-site backups before storing real customer or financial data.
- Keep all external integrations disabled until their permissions and approval policies are implemented.
