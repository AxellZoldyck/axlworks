# AXLWORKS — Character Design Bible

## Art direction

Stylized miniature 3D office simulation. Original anime-inspired characters with professional proportions and readable silhouettes. Avoid direct recreation of existing franchise characters. Use soft studio lighting, clean materials, subtle fabric detail, and expressive but restrained facial animation.

## Shared technical requirements

Each character asset should include:
- Neutral front, side, and three-quarter views
- Consistent height scale and head/body proportions
- PBR materials and optimized textures
- Humanoid rig with facial blendshapes where practical
- Idle, walk, sit, type, think, talk, meeting, celebrate, and error/concern states
- LOD variants for mobile performance
- Stable asset ID and version

## Axell — Human CEO avatar

Role: owner and final approver.

Visual: tailored deep-navy jacket, light neutral shirt, clean silhouette, confident but approachable posture. The CEO avatar is an optional representation of the owner, not an AI agent.

## Killua — Executive Secretary / Chief of Staff

Visual: silver-white hair, cool blue and white palette, refined office-casual outfit, alert eyes, precise gestures.

Behavior: moves between executive office, meeting room, and employee workspaces; idle state should communicate attentiveness rather than constant motion.

## Dipa — Customer Relations

Visual: friendly face, blue-teal palette, modern smart-casual outfit, welcoming posture.

Behavior: seated at customer support desk while handling conversations; talking state when sending a response; thinking state while preparing a reply.

## Kyou — Business Intelligence

Visual: dark hair, midnight-blue palette, neat analytical outfit, focused posture.

Behavior: works at data displays; thinking while evaluating metrics; presents charts during meetings.

## Ren — Finance Manager

Visual: dark charcoal outfit with restrained amber accent, composed posture, organized desk.

Behavior: reviews ledgers, checks receipts, reconciles records, and presents finance reports.

## Animation state mapping

- idle: no active task
- working: task execution
- thinking: model/tool reasoning in progress
- communicating: sending or receiving internal message
- meeting: assigned to an active meeting
- awaiting_approval: blocked on CEO decision
- error: task failed or agent needs intervention
- offline: worker unavailable

Animation state must be driven by backend events and persisted state, never by random client-side behavior.
