---
title: "Part 3: High-Assurance Perception"
date: "2026-04-04"
description: "Eliminating hallucinations in repository scans using Strict Grounding constraints in the GCX Vector Protocol."
tags: ["prompt-engineering", "gemini-cli", "grounding", "reliability"]
---

# Part 3: High-Assurance Perception

*This is Part 3 of the "Architecting Deterministic Agents" series, detailing the cognitive architecture upgrades inside the GCX Vector Protocol.*

## The Problem: The "Common Sense" Hallucination

One of the most persistent challenges in autonomous engineering agents is the model's tendency to rely on its "parametric knowledge" (what it learned during training) rather than the "contextual reality" (what is actually in your repository).

In the context of the Vector Protocol, this manifested most often during the `/vector:scan` (perception) and `/vector:context` (maintenance) phases. For example, if a project used a popular framework like React, a model might "hallucinate" the existence of a `src/components/` directory or a specific utility file because most React projects follow that pattern—even if the specific repository being scanned did not.

These false-positives create "drift" in the protocol state, leading to plans that reference non-existent files and execution steps that inevitably fail.

## The Research: Strict Grounding

To combat this, we looked to [Google's official developer instructions for Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/prompting-strategies). Google provides a specific, high-intensity grounding clause designed to minimize hallucination by restricting the model's knowledge base to the provided context.

The principle is simple: **explicitly forbid the use of common sense for factual repository queries.**

By treating the provided context as the *absolute limit of truth*, we force the model to acknowledge when information is missing rather than guessing based on industry standard patterns.

## The Implementation: Injecting Grounding Clauses

In v1.15.0 of the Vector Protocol, we integrated a standardized grounding mandate into the `<constraints>` section of our perception-focused commands.

Here is the implementation used in `commands/vector/scan.toml` and `commands/vector/context.toml`:

```xml
<constraints>
- **Strict Grounding:** You are a strictly grounded assistant limited to the information provided in the User Context and repository files. In your answers, rely **only** on the facts that are directly observed. You must **not** access or utilize your own knowledge or common sense to answer factual repository queries. Do not assume or infer from the provided facts; simply report them exactly as they appear. Your answer must be factual and fully truthful to the provided text and file system, leaving absolutely no room for speculation or interpretation.
</constraints>
```

### Why this specific language?

The use of phrases like "absolute limit of truth" and "completely untruthful if not mentioned" (from the full Google SI) acts as a high-magnitude weight in the model's attention mechanism. It signals that for this specific phase, accuracy is valued infinitely higher than creativity or helpfulness.

## The Impact

Since implementing Strict Grounding constraints, the Vector Protocol has achieved **high-assurance perception**:
- **Reliable Drift Detection:** The `/vector:scan` command now only reports drift when there is a verifiable difference between `PLAN.md` and the file system.
- **Fact-Based Maintenance:** `/vector:context` no longer suggests "standard" dependencies that aren't actually in the `package.json` or `go.mod`.
- **Honest Uncertainty:** When the model cannot find a file, it now correctly reports "File not found" instead of assuming a default path. This allows the user to provide the correct path manually, keeping the protocol loop honest.

---

*Next in the series:* **[Part 4: The "Context-First" Architecture](04-context-first-architecture.md)** - *Defeating the "Lost in the Middle" phenomenon by optimizing the sequence of data and instructions.*
