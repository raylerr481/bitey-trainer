# Bitey Trainer

**Bitey Trainer is the employment and AI-training intelligence module of Bitey IA / Supracerebro.**

It is not the future mobile employment application itself. That product is **JobIA**.

## Mission

Bitey Trainer develops, tests, and operates the intelligence needed to discover, evaluate, rank, and prepare work opportunities. It can support two related goals:

1. Find legitimate opportunities where Bitey itself can provide AI/automation/training/evaluation services when the client and platform explicitly permit that model.
2. Find and prepare opportunities for a human worker, using that person's real skills, languages, location, availability, and professional profile.

The system also supports **HYBRID** workflows in which Bitey performs permitted automation while a human performs required judgment, validation, identity, physical action, language, or approval.

## Relationship with JobIA

**JobIA is the user-facing application. Bitey Trainer is the intelligence module behind it.**

```text
                 BITEY IA / SUPRACEREBRO
                          |
                          v
                   BITEY TRAINER
              employment intelligence
                          |
                          v
                    JobIA API
                          |
                          v
                        JOBIA
                   mobile application
```

JobIA should not reimplement matching, ranking, evaluation, or opportunity intelligence that has already been validated in Bitey Trainer. Instead, stable Bitey Trainer capabilities become reusable services/contracts consumed by JobIA.

## Development algorithm: build in Bitey Trainer, consume in JobIA

This repository is developed continuously while JobIA remains a future product.

For every new capability:

1. **Define** the employment-intelligence requirement.
2. **Implement** it in Bitey Trainer.
3. **Test** it against realistic opportunities and worker profiles.
4. **Measure** match quality, false positives, false negatives, language/skill gaps, duplicates, stale jobs, and unsuitable recommendations.
5. **Improve** the rules, scoring, prompts, adapters, and data contracts.
6. **Validate** the capability with repeatable tests.
7. **Publish a stable interface** that JobIA can consume later.
8. **Integrate** the validated capability into the JobIA API/mobile product.
9. **Collect explicit feedback** from JobIA users to improve future Bitey Trainer versions.

This prevents JobIA from becoming a second, disconnected intelligence engine.

## Universal worker intelligence

Bitey Trainer must work for many types of workers, not only programmers or AI professionals.

It should be able to build and evaluate profiles for, among others:

- Accountants.
- Economics graduates.
- Teachers.
- Administrative workers.
- Data-entry workers.
- Writers.
- Programmers.
- IT technicians.
- Designers.
- Customer-support workers.
- Construction workers.
- Skilled trades.
- Freelancers.
- Remote workers.
- Other professions and practical occupations.

A worker may describe their abilities in ordinary language. Bitey Trainer should extract structured skills, transferable skills, experience, language capability, preferences, and constraints without requiring the worker to know the exact terminology used by a job board.

## Current human-profile test

The first real-world validation profile is based on Rayler's professional capabilities and preferences. It includes IT, programming, networks, databases, cloud, AI tools, Excel, Word, data entry, technical writing, QA, fast typing, education/computer-science background, and Spanish/Portuguese/English proficiency levels.

This profile is a **test profile and implementation reference**, not a template that should be hard-coded into JobIA. Future JobIA users must create their own profiles.

## Opportunity modes

### HUMAN

The platform/client requires a human worker. Bitey Trainer assists with discovery, matching, analysis, preparation, and reporting. It must not impersonate the human.

### BITEY

The opportunity explicitly allows an agent, service provider, or automated workflow and its terms permit Bitey to perform the work. Bitey can execute authorized work through appropriate backend integrations.

### HYBRID

Bitey performs permitted research, drafting, automation, testing, or pre-evaluation while the human completes required human-only actions.

**Never misrepresent an AI agent as a human and never bypass platform, identity, assessment, employment, or client requirements.**

## Core capabilities

- Opportunity discovery.
- Source normalization.
- Duplicate detection.
- Stale/closed opportunity detection when possible.
- Skill matching.
- Transferable-skill matching.
- Language matching.
- Location and work-mode matching.
- Compensation analysis.
- Experience-level analysis.
- HUMAN/BITEY/HYBRID classification.
- Match scoring from 0–100.
- Explainable strengths and gaps.
- Opportunity prioritization.
- Application preparation.
- CV/proposal assistance.
- Human evaluation workflows.
- AI-response evaluation.
- Training/evaluation dataset support.
- Reporting and notification events.
- Feedback-based ranking improvement.

## Repetitive digital work focus

A major target category is legitimate work involving repetitive or structured digital tasks, including:

- Writing and rewriting.
- Data entry.
- Spreadsheet work.
- Document processing.
- Content review.
- AI response evaluation.
- Human-in-the-loop evaluation.
- Prompt testing.
- Data annotation.
- QA.
- Simple human interaction.
- Repetitive programming/coding tasks.
- Technical documentation.

Bitey Trainer should determine whether each task is suitable for full automation, human execution, or a hybrid workflow.

## AI Trainer / AI work

Bitey Trainer also searches for opportunities where **Bitey itself could be contracted as an AI/automation/training service**, subject to explicit client and platform authorization.

This is distinct from searching for employment for a human user.

The engine therefore needs two principal target identities:

```text
BITEY AS SERVICE PROVIDER
          |
          +--> AI training
          +--> AI evaluation
          +--> automation
          +--> data processing
          +--> QA / testing

HUMAN WORKER
          |
          +--> employment
          +--> freelance
          +--> remote work
          +--> hybrid work
          +--> local work
```

A third target is **HYBRID: Bitey + Human**.

## JobIA integration contract

As capabilities stabilize, Bitey Trainer should expose reusable services to the JobIA backend, such as:

```text
POST /trainer/profile/analyze
POST /trainer/opportunities/search
POST /trainer/opportunities/match
POST /trainer/opportunities/evaluate
POST /trainer/applications/prepare
POST /trainer/reports/generate
POST /trainer/alerts/evaluate
```

Exact endpoints are subject to implementation and security review. The important architectural rule is that JobIA consumes **validated trainer capabilities** rather than duplicating the engine.

## Data flow

```text
Worker profile / Bitey service profile
                 |
                 v
          Bitey Trainer
                 |
       +---------+---------+
       |                   |
       v                   v
 Opportunity search    Profile analysis
       |                   |
       +---------+---------+
                 v
              Matching
                 |
                 v
             Ranking
                 |
          +------+------+
          |             |
          v             v
       Report        Alert
          |
          v
        JobIA
```

## Quality loop

Every validated opportunity and explicit user decision can produce a quality signal:

```text
Find → Match → Explain → User reviews → Accept/Reject
                                  |
                                  v
                           Feedback signal
                                  |
                                  v
                           Better ranking
```

Quality improvements must be measured, reproducible, and privacy-aware.

## Technology direction

Bitey Trainer is designed to integrate with the broader Bitey IA stack, including Supabase and controlled AI-provider routing. Provider-specific credentials must remain server-side.

The trainer must support deterministic tests and mocks so core behavior can be validated without requiring paid external AI APIs.

## Status

Current stage: **active intelligence-engine development and real-world validation**.

Immediate priorities:

1. Test opportunity discovery.
2. Test worker-profile matching.
3. Test HUMAN/BITEY/HYBRID classification.
4. Improve reports and alerts.
5. Validate reusable API contracts for JobIA.
6. Expand testing beyond one technical profile to multiple professions.

## Roadmap

### Trainer foundation
- Stable profile schema.
- Opportunity schema.
- Matching engine.
- Scoring and explanations.
- Repeatable test suite.

### Employment intelligence
- Multi-source discovery.
- Better semantic matching.
- Language and location reasoning.
- Compensation normalization.
- Personalized ranking.

### AI work intelligence
- AI-training opportunity detection.
- AI-evaluation workflows.
- Agent-permitted work classification.
- Human-in-the-loop orchestration.

### JobIA integration
- Secure API contracts.
- JobIA profile synchronization.
- Opportunity feed.
- Alerts.
- Application preparation.
- User feedback loop.

### Future mobile product
JobIA will eventually package these validated capabilities into an Android/iOS application distributed through official app stores.

## Guiding principle

> **Bitey Trainer builds and validates the intelligence. JobIA puts that intelligence in the hands of workers.**
