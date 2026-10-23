# Starter principles vs operator observations (Starter set version 4)

Strength: MATCH = same substance; PARTIAL = overlapping but not the same rule; none = no match.
Observation ids are from observation-log/ and archive/ (0018 has no Principle line).

| # | Starter principle | Matching observations |
|---|---|---|
| 1 | Open-source skills include a licence | no match |
| 2 | Open-source skills: attribution and feedback path | no match |
| 3 | Skills with rules need a pre-flight verification step | PARTIAL: 0001, 0006, 0028 (unenforced rules decay; they argue for mechanical enforcement, not a re-read step) |
| 4 | Open-source skills carry no client-identifying info | no match |
| 5 | Tool-agnostic language, concrete examples first | no match |
| 6 | Structured output grounded in multiple real examples | no match |
| 7 | Subagents: complete inputs, verified outputs | PARTIAL: 0024 (subagent reports show only their batch), 0023 (delegate capability vs rule) |
| 8 | Graceful tool-failure recovery | no match |
| 9 | Match interaction modality to conversation energy | no match |
| 10 | Small actionable sets inline AND in a file | no match |
| 11 | Skills need pruning, not just growth | no match |
| 12 | Canonical identifiers, never reconstructed | PARTIAL: 0021 (identity vs bytes) |
| 13 | Workspace-file skills keep a reference index | no match |
| 14 | Scheduled tasks invoke skills, not reimplement | no match |
| 15 | Scheduled prompts are lightweight orchestrators | no match |
| 16 | Interrupted operations are partial; verify state before retry | MATCH: 0015; PARTIAL: 0014 |
| 17 | Never suggest manual typing as a workaround | no match |
| 18 | Browser automation is a costly last resort | no match |
| 19 | API-access skills note network-sandbox implications | no match |
| 20 | Skills contain only behaviour-changing content | no match |
| 21 | Agent-agnostic language in open-source skills | no match |
| 22 | Vendor guidance needs dated changelog check | PARTIAL: 0016, 0011 (use source's own access path; vendor docs outrank untested claim) |
| 23 | No aggregation across different segments / unmeasured baseline | PARTIAL: 0035 (check where it happens) |
| 24 | Fetch the instance before describing it | PARTIAL: 0016, 0007 |
| 25 | One verified reason beats two | no match |
| 26 | Companion skill declares coverage boundary | no match |
| 27 | Every skill ships as bundle, progressive disclosure | no match |
| 28 | Absence never established by a summarising instrument | MATCH: 0007, 0016, 0024, 0008 |
| 29 | Skill holds method; dated values in workspace file | no match |

Counts: MATCH 2 (16, 28); PARTIAL only 6 (3, 7, 12, 22, 23, 24); no match 21.
