# Bitey Trainer

**Internal Bitey IA capability for training, evaluation, validation, and intelligence evolution.**

Bitey Trainer is not an application, web/Android channel, or second brain. It is an internal capability of Bitey IA that can train and validate specialized capabilities used by its modules, including JobIA.

## Language and naming standard

All repository documentation, API contracts, backend/frontend references, variable names, model fields, JSON keys, configuration keys, dataset fields, evaluation identifiers, and internal technical references must use **English**.

Human-facing evaluation text may be localized when required, but technical identifiers must remain English and stable.

Examples: `job_id`, `skill`, `location`, `modality`, `match_score`, `application`, `evaluation`, `dataset_version`.

Do not introduce Spanish variable names, JSON keys, API parameters, database fields, or internal identifiers in new code.

## Architectural position

```text
                         BITEY IA
                    general intelligence
                           │
                    BITEY TRAINER
             training · evaluation
              validation · evolution
                           │
              validated capabilities
                           ▼
                         JOBIA
                employment/work module
                           │
                    contract jobia-v1
                      ┌────┴────┐
                      ▼         ▼
                  JobIA-Web JobIA-app
                     Web      Android
                   channel     channel
```

`Bitey IA Web` is the web channel of Bitey IA. `JobIA-Web` and `JobIA-app` are JobIA channels. Trainer does not directly control any interface.

## Responsibilities

Trainer develops and validates specialized capabilities such as:

- opportunity discovery and normalization;
- duplicate and stale-opportunity detection;
- transferable-skill matching;
- language, location, and modality analysis;
- compensation analysis;
- HUMAN/BITEY/HYBRID classification;
- scoring, ranking, and explanations;
- CV/proposal/application preparation;
- AI response evaluation;
- feedback and regression learning.

## JobIA lifecycle

```text
Define → Implement → Test → Measure → Improve
       → Validate → Publish capability → JobIA consumes
```

JobIA is the specialized employment/work module and exposes its capabilities to its web and Android channels. Trainer does not create a second public backend or duplicate channel APIs.

## Bidirectional relationship

- **Bitey IA → JobIA:** when a request requires specialized employment/work knowledge or actions.
- **JobIA → Bitey IA:** when general reasoning, orchestration, memory, tools, model selection, or general policies are required.
- **Bitey Trainer → JobIA:** provides trained and validated specialized capabilities and evaluation.

Integrations use versioned contracts and APIs, never direct coupling between web interfaces.

## Security

- No provider secrets in source code.
- Data isolated by account/tenant.
- Authorization enforced by backend services.
- No automatic exposure of private JobIA data.
- Automation must not impersonate users or bypass identity, evaluation, or platform terms.

## Principle

> **Bitey IA is the general system. Bitey Trainer is an internal capability for training and validation. JobIA is the specialized employment/work module. JobIA-Web and JobIA-app are its web and Android channels. Bitey IA Web is the web channel of Bitey IA.**
