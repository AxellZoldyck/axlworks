# AXLWORKS Company Platform — Product Specification

## Product decisions

- Brand: AXLWORKS
- Product: Autonomous Company Operating System
- Owner and final decision-maker: Axell (human CEO)
- AI employees: Killua, Dipa, Kyou, Ren
- Agent mode: autonomous for bounded, approved workflows
- Office: stylized isometric 3D, interactive and continuously simulated
- CEO control: web dashboard and WhatsApp
- Hosting: self-managed VPS with Docker
- Primary language: Indonesian; technical records and identifiers use English

## Core principles

1. The company database is the source of truth.
2. Agents operate in the backend; the 3D office visualizes real backend state.
3. Agents continue scheduled work when the browser is closed.
4. Autonomy is bounded by explicit tools, scopes, budgets, rate limits, and policies.
5. Axell retains final authority over strategy, material spending, and sensitive actions.
6. Every consequential action must be attributable and auditable.
7. A failed or unavailable agent must not block unrelated agents.

## UI information architecture

- Overview: company KPIs, alerts, agent status, approvals requiring attention.
- Virtual Office: isometric building, floor selector, room navigation, agent inspection.
- AI Employees: profile, role, tools, permissions, health, performance, cost.
- Communication: internal agent messages and CEO conversations.
- Task Center: queue, owner, priority, status, due date, execution history.
- Business Intelligence: leads, registrations, installations, ad performance, CPL, conversion.
- Finance: transactions, commission, expenses, cash flow, budgets, reconciliation.
- Approvals: proposals, evidence, risk, amount, decision, expiry, audit history.
- Company Knowledge: verified products, pricing, SOPs, territory and policy documents.
- Settings: integrations, schedules, access control, API usage, backups.

## Office layout

Ground floor: reception, Dipa's customer relations room, Kyou's analytics room, Ren's finance room, meeting room, lounge.

Upper floor: Axell's CEO office, Killua's executive office, executive meeting room, strategy room.

## Character design direction

All employee characters are original custom stylized 3D designs. Do not copy copyrighted anime character models, costumes, logos, or exact facial designs. Each character needs a consistent model sheet, palette, silhouette, rig, facial expressions, and state animations.

- Axell: executive silhouette, tailored navy outfit, calm and decisive posture.
- Killua: silver hair, cool blue-white palette, alert posture, precise gestures.
- Dipa: approachable silhouette, blue-teal palette, open gestures and expressive face.
- Kyou: analytical silhouette, dark navy palette, compact purposeful movements.
- Ren: formal charcoal palette with muted amber accents, composed posture.

## Responsive behavior

Desktop: full interactive 3D office and multi-panel workspace.

Mobile: compact office overview, employee cards, task/approval actions, chat with Killua, and reduced-detail 3D mode. Critical workflows must remain usable without WebGL.

## Non-goals for Phase 1

- No live WhatsApp messaging.
- No Google Ads mutation or budget changes.
- No money transfers.
- No autonomous customer promises or registration submissions.
- No 3D assets or animation production yet.
