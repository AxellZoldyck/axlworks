# API implementation queue

The first scaffold exposes:
- GET /health — process liveness
- GET /ready — PostgreSQL connectivity

Next Phase 1 endpoints:
- POST /auth/login
- POST /auth/refresh
- POST /auth/logout
- GET /employees
- GET /employees/{slug}
- POST /employees (CEO/admin only)
- PATCH /employees/{slug} (CEO/admin only)

All administrative mutations must create audit records.
