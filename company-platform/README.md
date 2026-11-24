# AXLWORKS Company Platform
Autonomous AI company operating system for Axell and AI employees Killua, Dipa, Kyou, and Ren.

This module is isolated from the existing Next.js website at the repository root.

## Phase 1
- FastAPI and PostgreSQL
- Alembic migrations
- Explicit CEO bootstrap
- Argon2 password hashing and short-lived JWT access tokens
- Authenticated employee directory
- Initial successful-login audit event

## Run locally
1. Enter `company-platform/`.
2. Copy `.env.example` to `.env`.
3. Replace all example secrets. Set a real CEO email and unique password of at least 12 characters.
4. Run `docker compose up --build`.
5. API docs: http://localhost:8001/docs
6. Health: http://localhost:8001/health
7. Readiness: http://localhost:8001/ready

API binds to 127.0.0.1:8001 on host. Put it behind TLS reverse proxy for remote use. PostgreSQL is not published to host.

## Endpoints
POST /auth/login · GET /auth/me · POST /auth/logout · GET /employees · GET /employees/{slug} · GET /health · GET /ready

Logout currently tells client to discard the stateless access token. Server-side revocation and refresh sessions are not yet implemented. Do not expose publicly without TLS, rate limiting, session revocation, and production CORS settings.

No WhatsApp sending, Google Ads changes, financial execution, or customer registration submission is enabled.
