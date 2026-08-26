# Bitey Trainer

**Bitey Trainer is the internal intelligence and training engine of JobIA within the Bitey IA ecosystem.**

It is **not an app** and it is not a separate user-facing product. JobIA is the user-facing product; Bitey Trainer develops and validates the intelligence that JobIA consumes.

## Ecosystem role

```text
                    BITEY IA
                 SUPRACEREBRO
                      │
                    JobIA
                      │
               Bitey Trainer
              internal engine
                      │
                  JobIA App
```

Bitey IA remains the complete general-purpose AI. Trainer is a specialized capability and does not replace or restrict the Supracerebro.

## Mission

Develop, test and validate intelligence for legitimate employment and AI-work opportunities, including discovery, normalization, matching, ranking, evaluation, preparation and feedback.

Trainer can support:

- AI training/evaluation opportunities.
- IT and other professional opportunities.
- Human-in-the-loop work.
- Automated work only where explicitly permitted.
- Hybrid workflows requiring both Bitey and human action.

## Core capabilities

- Opportunity discovery and normalization.
- Duplicate/stale detection.
- Skill and transferable-skill matching.
- Language, location and modality matching.
- Compensation analysis.
- HUMAN/BITEY/HYBRID classification.
- Match scoring and explanations.
- Opportunity prioritization.
- CV/proposal/application assistance.
- AI-response evaluation and training workflows.
- Feedback-based ranking improvement.
- Reports and notification events.

## JobIA contract

Validated Trainer capabilities become secure backend services consumed by JobIA. JobIA should not duplicate the matching/training engine.

```text
Define → Implement → Test → Measure → Improve → Validate → Publish contract → JobIA consumes
```

Exact API endpoints may evolve; security, authorization and stable contracts are mandatory.

## Execution modes

**HUMAN:** the user performs the work.

**BITEY:** the opportunity explicitly permits an agent/service and applicable terms allow execution.

**HYBRID:** Bitey performs permitted preparation/automation while the human completes required actions.

Trainer must never impersonate a human or bypass platform, identity, assessment, employment or client requirements.

## Quality loop

```text
Find → Match → Explain → User decision → Feedback → Better ranking
```

Results must be measurable, reproducible and privacy-aware.

## Integration with Bitey IA

Trainer may use the authorized Bitey IA infrastructure, Supabase and controlled AI-provider routing. Provider credentials remain server-side. Trainer capabilities enrich JobIA and may contribute authorized, privacy-safe knowledge to the broader Bitey IA ecosystem.

## Privacy and security

- No provider secrets in source code.
- Account and tenant isolation.
- Secure backend authentication/authorization.
- No automatic exposure of private JobIA data to other users or modules.
- External providers must be used according to their terms.

## Status

Active intelligence-engine development and validation for JobIA.

## Guiding principle

> **Bitey Trainer builds and validates JobIA intelligence; JobIA puts that intelligence in the hands of workers; Bitey IA remains the general Supracerebro.**
