# Bitey Trainer

Bitey Trainer is the training/evaluation layer subordinate to Bitey IA Web.

## Purpose
- Evaluate AI responses using reproducible test cases.
- Build and validate training datasets.
- Route future provider integrations through a controlled adapter layer.
- Record evaluation results for later integration with Bitey Web and Supabase.

## Smoke test
The initial test suite runs without external API keys. It validates the core trainer contract using a deterministic mock provider.

## Status
Initial scaffold and local smoke-test harness.
