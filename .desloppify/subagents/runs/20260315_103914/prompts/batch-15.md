You are a focused subagent reviewer for a single holistic investigation batch.

Repository root: /Users/mishari/Library/CloudStorage/OneDrive-Personal/OneDrive Projects/OpenCode/eventyay
Blind packet: /Users/mishari/Library/CloudStorage/OneDrive-Personal/OneDrive Projects/OpenCode/eventyay/.desloppify/review_packet_blind.json
Batch index: 15
Batch name: design_coherence
Batch rationale: seed files for design_coherence review

DIMENSION TO EVALUATE:

## design_coherence
Are structural design decisions sound — functions focused, abstractions earned, patterns consistent?
Look for:
- Functions doing too many things — multiple distinct responsibilities in one body
- Parameter lists that should be config/context objects — many related params passed together
- Files accumulating issues across many dimensions — likely mixing unrelated concerns
- Deep nesting that could be flattened with early returns or extraction
- Repeated structural patterns that should be data-driven
Skip:
- Functions that are long but have a single coherent responsibility
- Parameter lists where grouping would obscure meaning — do NOT recommend config/context objects or dependency injection wrappers just to reduce parameter count; only group when the grouping has independent semantic meaning
- Files that are large because their domain is genuinely complex, not because they mix concerns
- Nesting that is inherent to the problem (e.g., recursive tree processing)
- Do NOT recommend extracting callable parameters or injecting dependencies for 'testability' — direct function calls are simpler and preferred unless there is a concrete decoupling need

YOUR TASK: Read the code for this batch's dimension. Judge how well the codebase serves a developer from that perspective. The dimension rubric above defines what good looks like. Cite specific observations that explain your judgment.

Mechanical scan evidence — navigation aid, not scoring evidence:
The blind packet contains `holistic_context.scan_evidence` with aggregated signals from all mechanical detectors — including complexity hotspots, error hotspots, signal density index, boundary violations, and systemic patterns. Use these as starting points for where to look beyond the seed files.

Seed files (start here):
- app/eventyay/api/versions.py
- app/eventyay/base/middleware.py
- app/eventyay/base/signals.py
- app/eventyay/common/text/phrases.py
- app/eventyay/control/forms/filter.py
- app/eventyay/api/serializers/order.py
- app/eventyay/control/views/orders.py
- app/eventyay/base/forms/questions.py
- app/eventyay/control/forms/global_settings.py
- app/eventyay/base/models/event.py
- app/eventyay/base/email.py
- app/eventyay/control/navigation.py
- app/eventyay/base/services/orders.py
- app/eventyay/control/logdisplay.py
- app/eventyay/base/payment.py
- app/eventyay/api/views/checkin.py
- app/eventyay/base/exporter.py
- app/eventyay/base/services/mail.py
- app/eventyay/control/views/subevents.py
- app/eventyay/agenda/views/talk.py
- app/eventyay/api/serializers/event.py
- app/eventyay/presale/views/order.py
- app/eventyay/control/views/product.py
- app/eventyay/base/services/user.py
- app/eventyay/control/views/__init__.py
- app/eventyay/api/serializers/fields.py
- app/eventyay/api/serializers/product.py
- app/eventyay/api/serializers/question.py
- app/eventyay/api/serializers/rooms.py
- app/eventyay/api/serializers/stream_schedule.py
- app/eventyay/api/webhooks.py
- app/eventyay/base/cache.py
- app/eventyay/base/forms/__init__.py
- app/eventyay/base/forms/user.py
- app/eventyay/base/models/access_code.py
- app/eventyay/base/models/auth_token.py
- app/eventyay/base/models/base.py
- app/eventyay/base/models/cache.py
- app/eventyay/base/models/checkin.py
- app/eventyay/base/models/seating.py
- app/eventyay/base/models/submission.py
- app/eventyay/base/models/tax.py
- app/eventyay/base/models/transaction.py
- app/eventyay/base/plugins.py
- app/eventyay/base/secrets.py
- app/eventyay/base/services/announcement.py
- app/eventyay/base/services/cancelevent.py
- app/eventyay/base/services/chat.py
- app/eventyay/base/services/invoices.py
- app/eventyay/base/services/locking.py
- app/eventyay/base/services/poll.py
- app/eventyay/base/services/poster.py
- app/eventyay/base/services/pricing.py
- app/eventyay/base/services/room.py
- app/eventyay/base/services/teams.py
- app/eventyay/base/services/update_check.py
- app/eventyay/base/shredder.py
- app/eventyay/base/tasks.py
- app/eventyay/base/templatetags/rich_text.py
- app/eventyay/base/ticketoutput.py
- app/eventyay/base/views/errors.py
- app/eventyay/common/context_processors.py
- app/eventyay/common/exceptions.py
- app/eventyay/common/image.py
- app/eventyay/common/mail.py
- app/eventyay/common/templatetags/filesize.py
- app/eventyay/common/text/console.py
- app/eventyay/common/urls.py
- app/eventyay/control/context.py
- app/eventyay/control/forms/page.py
- app/eventyay/control/forms/vouchers.py
- app/eventyay/control/urls.py
- app/eventyay/control/views/geo.py
- app/eventyay/control/views/orderimport.py
- app/eventyay/control/views/organizer.py
- app/eventyay/control/views/pages.py
- app/eventyay/control/views/shredder.py
- app/eventyay/control/views/user.py
- app/eventyay/core/utils/redis.py
- app/eventyay/core/utils/statsd.py
- app/eventyay/eventyay_common/views/account/basic.py
- app/eventyay/eventyay_common/views/organizer.py
- app/eventyay/features/live/consumers.py
- app/eventyay/features/live/decorators.py
- app/eventyay/features/live/modules/auth.py
- app/eventyay/features/live/modules/chat.py
- app/eventyay/features/live/modules/room.py
- app/eventyay/features/social/utils.py
- app/eventyay/helpers/__init__.py
- app/eventyay/helpers/formats/en_AU/formats.py
- app/eventyay/helpers/formats/en_CA/formats.py
- app/eventyay/helpers/formats/en_GB/formats.py
- app/eventyay/helpers/formats/en_US/formats.py
- app/eventyay/helpers/periodic.py
- app/eventyay/helpers/reportlab.py
- app/eventyay/helpers/stripe_utils.py
- app/eventyay/orga/context_processors.py
- app/eventyay/orga/forms/export.py
- app/eventyay/orga/forms/schedule.py
- app/eventyay/orga/urls.py
- app/eventyay/plugins/banktransfer/csvimport.py
- app/eventyay/plugins/banktransfer/mt940import.py

Mechanical concern signals — investigate and adjudicate:
Overview (213 signals):
  mixed_responsibilities: 92 — app/eventyay/agenda/views/schedule.py, app/eventyay/agenda/views/speaker.py, ...
  design_concern: 83 — app/eventyay/api/serializers/fields.py, app/eventyay/api/serializers/product.py, ...
  structural_complexity: 26 — app/eventyay/api/views/event.py, app/eventyay/base/exporters/dekodi.py, ...
  systemic_pattern: 4 — app/eventyay/agenda/apps.py, app/eventyay/agenda/views/featured.py, ...
  systemic_smell: 3 — app/eventyay/agenda/management/commands/export_schedule_html.py, app/eventyay/agenda/tasks.py, app/eventyay/agenda/views/utils.py
  duplication_design: 2 — app/eventyay/base/models/vouchers.py, app/eventyay/control/views/organizer_views/organizer_detail_view_mixin.py
  interface_design: 2 — app/eventyay/api/views/checkin.py, app/eventyay/base/services/cart.py
  coupling_design: 1 — app/eventyay/control/views/__init__.py

For each concern, read the source code and report your verdict in issues[]:
  - Confirm → full issue object with concern_verdict: "confirmed"
  - Dismiss → minimal object: {concern_verdict: "dismissed", concern_fingerprint: "<hash>"}
    (only these 2 fields required — add optional reasoning/concern_type/concern_file)
  - Unsure → skip it (will be re-evaluated next review)

  - [coupling_design] app/eventyay/control/views/__init__.py
    summary: Coupling pattern — assess if boundaries need adjustment
    question: Is the coupling intentional or does it indicate a missing abstraction boundary?
    evidence: Flagged by: coupling
    evidence: [coupling] Implicit host contract: PaginationMixin depends on 4 undeclared self attrs (DEFAULT_PAGINATION, get_paginate_by, paginate_by, request)
    fingerprint: a0476933ab4e8f61
  - [design_concern] app/eventyay/api/serializers/fields.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (72 LOC): zero importers, not an entry point
    fingerprint: 84d69b360439cc74
  - [design_concern] app/eventyay/api/serializers/product.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (483 LOC): zero importers, not an entry point
    fingerprint: 29122427428d3f49
  - [design_concern] app/eventyay/api/serializers/question.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (309 LOC): zero importers, not an entry point
    fingerprint: 3cbdf289cd3d2f2f
  - [design_concern] app/eventyay/api/serializers/rooms.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (44 LOC): zero importers, not an entry point
    fingerprint: f8f20192a957adef
  - [design_concern] app/eventyay/api/serializers/stream_schedule.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (148 LOC): zero importers, not an entry point
    fingerprint: 3646fb4a85e6823b
  - [design_concern] app/eventyay/api/webhooks.py
    summary: Design signals from dict_keys, smells
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: dict_keys, smells
    evidence: [smells] 1x Except handler silently suppresses error (pass/continue, no log)
    fingerprint: 305512126f26ba19
  - [design_concern] app/eventyay/base/cache.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (123 LOC): zero importers, not an entry point
    fingerprint: 69da9cabd42b9a33
  - [design_concern] app/eventyay/base/exporter.py
    summary: Design signals from smells
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: smells
    evidence: [smells] 1x Except handler silently suppresses error (pass/continue, no log)
    fingerprint: b1eb957c4f4edfde
  - [design_concern] app/eventyay/base/forms/__init__.py
    summary: Design signals from signature, smells
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: signature, smells
    evidence: [signature] 'save' has 9 different signatures across 59 files
    fingerprint: 3b6d1a2dc1dbf111
  - [design_concern] app/eventyay/base/forms/user.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (141 LOC): zero importers, not an entry point
    fingerprint: fa4ff4913590c369
  - [design_concern] app/eventyay/base/models/access_code.py
    summary: Design signals from signature, smells
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: signature, smells
    evidence: [signature] 'is_valid' has 2 different signatures across 3 files
    fingerprint: 8921ad552a7d8e0a
  - [design_concern] app/eventyay/base/models/auth_token.py
    summary: Design signals from orphaned, signature
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, signature
    evidence: [orphaned] Orphaned file (112 LOC): zero importers, not an entry point
    fingerprint: e96a36b98dd9919b
  - [design_concern] app/eventyay/base/models/base.py
    summary: Design signals from dict_keys, smells
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: dict_keys, smells
    evidence: [smells] 1x High cyclomatic complexity (>12 decision points)
    fingerprint: 7fb869f45a462cb0
  - [design_concern] app/eventyay/base/models/cache.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (166 LOC): zero importers, not an entry point
    fingerprint: f10ba5a61087de7a
  - [design_concern] app/eventyay/base/models/checkin.py
    summary: Design signals from smells
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: smells
    evidence: [smells] 1x High cyclomatic complexity (>12 decision points)
    fingerprint: adc806f4b829d3b7
  - [design_concern] app/eventyay/base/models/seating.py
    summary: Design signals from smells
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: smells
    evidence: [smells] 2x Too many optional params — consider a config object
    fingerprint: d4e9bd9ef486d9f9
  - [design_concern] app/eventyay/base/models/submission.py
    summary: Design signals from structural
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: structural
    evidence: File size: 1128 lines
    fingerprint: bd8b62b79f5b9008
  - [design_concern] app/eventyay/base/models/tax.py
    summary: Design signals from smells
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: smells
    evidence: [smells] 1x Except handler silently suppresses error (pass/continue, no log)
    fingerprint: 340250405635e736
  - [design_concern] app/eventyay/base/models/transaction.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (29 LOC): zero importers, not an entry point
    fingerprint: 7db6af80707884dc
  - [design_concern] app/eventyay/base/plugins.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (138 LOC): zero importers, not an entry point
    fingerprint: 0da40080d1d92399
  - [design_concern] app/eventyay/base/secrets.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (243 LOC): zero importers, not an entry point
    fingerprint: 9094db2b4cea34f7
  - [design_concern] app/eventyay/base/services/announcement.py
    summary: Design signals from orphaned, signature
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, signature
    evidence: [orphaned] Orphaned file (50 LOC): zero importers, not an entry point
    fingerprint: 03a03e7f04610be2
  - [design_concern] app/eventyay/base/services/cancelevent.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (365 LOC): zero importers, not an entry point
    fingerprint: 275060188a7c2846
  - [design_concern] app/eventyay/base/services/chat.py
    summary: Design signals from smells, structural
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: smells, structural
    evidence: File size: 589 lines
    fingerprint: 50bcbbab4ca3ee51
  - [design_concern] app/eventyay/base/services/invoices.py
    summary: Design signals from smells
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: smells
    evidence: [smells] 1x Catch block that only logs (swallowed error)
    fingerprint: 5cd87902641d5b7f
  - [design_concern] app/eventyay/base/services/locking.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (150 LOC): zero importers, not an entry point
    fingerprint: e7b2ae50379ebcf2
  - [design_concern] app/eventyay/base/services/poll.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (111 LOC): zero importers, not an entry point
    fingerprint: 5c924315c7e7ffca
  - [design_concern] app/eventyay/base/services/poster.py
    summary: Design signals from orphaned, signature
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, signature
    evidence: [orphaned] Orphaned file (237 LOC): zero importers, not an entry point
    fingerprint: 5f2c22418486a810
  - [design_concern] app/eventyay/base/services/pricing.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (109 LOC): zero importers, not an entry point
    fingerprint: b81d40fee9bd51d8
  (+183 more — use `desloppify show <detector> --no-budget` to explore)

RELEVANT FINDINGS — explore with CLI:
These detectors found patterns related to this dimension. Explore the findings,
then read the actual source code.

  desloppify show coupling --no-budget      # 39 findings
  desloppify show dict_keys --no-budget      # 193 findings
  desloppify show dupes --no-budget      # 29 findings
  desloppify show facade --no-budget      # 2 findings
  desloppify show global_mutable_config --no-budget      # 5 findings
  desloppify show orphaned --no-budget      # 147 findings
  desloppify show props --no-budget      # 1 findings
  desloppify show responsibility_cohesion --no-budget      # 7 findings
  desloppify show signature --no-budget      # 53 findings
  desloppify show smells --no-budget      # 334 findings
  desloppify show structural --no-budget      # 110 findings

Report actionable issues in issues[]. Use concern_verdict and concern_fingerprint
for findings you want to confirm or dismiss.

Task requirements:
1. Read the blind packet's `system_prompt` — it contains scoring rules and calibration.
2. Start from the seed files, then freely explore the repository to build your understanding.
3. Keep issues and scoring scoped to this batch's dimension.
4. Respect scope controls: do not include files/directories marked by `exclude`, `suppress`, or non-production zone overrides.
5. Return 0-10 issues for this batch (empty array allowed).
6. For design_coherence, use evidence from `holistic_context.scan_evidence.signal_density` — files where multiple mechanical detectors fired. Investigate what design change would address multiple signals simultaneously. Check `scan_evidence.complexity_hotspots` for files with high responsibility cluster counts.
7. Workflow integrity checks: when reviewing orchestration/queue/review flows,
8. xplicitly look for loop-prone patterns and blind spots:
9. - repeated stale/reopen churn without clear exit criteria or gating,
10. - packet/batch data being generated but dropped before prompt execution,
11. - ranking/triage logic that can starve target-improving work,
12. - reruns happening before existing open review work is drained.
13. If found, propose concrete guardrails and where to implement them.
14. Complete `dimension_judgment` for your dimension — all three fields (strengths, issue_character, score_rationale) are required. Write the judgment BEFORE setting the score.
15. Do not edit repository files.
16. Return ONLY valid JSON, no markdown fences.

Scope enums:
- impact_scope: "local" | "module" | "subsystem" | "codebase"
- fix_scope: "single_edit" | "multi_file_refactor" | "architectural_change"

Output schema:
{
  "batch": "design_coherence",
  "batch_index": 15,
  "assessments": {"<dimension>": <0-100 with one decimal place>},
  "dimension_notes": {
    "<dimension>": {
      "evidence": ["specific code observations"],
      "impact_scope": "local|module|subsystem|codebase",
      "fix_scope": "single_edit|multi_file_refactor|architectural_change",
      "confidence": "high|medium|low",
      "issues_preventing_higher_score": "required when score >85.0",
      "sub_axes": {"abstraction_leverage": 0-100, "indirection_cost": 0-100, "interface_honesty": 0-100, "delegation_density": 0-100, "definition_directness": 0-100, "type_discipline": 0-100}  // required for abstraction_fitness when evidence supports it; all one decimal place
    }
  },
  "dimension_judgment": {
    "<dimension>": {
      "strengths": ["0-5 specific things the codebase does well from this dimension's perspective"],
      "issue_character": "one sentence characterizing the nature/pattern of issues from this dimension's perspective",
      "score_rationale": "2-3 sentences explaining the score from this dimension's perspective, referencing global anchors"
    }  // required for every assessed dimension; do not omit
  },
  "issues": [{
    "dimension": "<dimension>",
    "identifier": "short_id",
    "summary": "one-line defect summary",
    "related_files": ["relative/path.py"],
    "evidence": ["specific code observation"],
    "suggestion": "concrete fix recommendation",
    "confidence": "high|medium|low",
    "impact_scope": "local|module|subsystem|codebase",
    "fix_scope": "single_edit|multi_file_refactor|architectural_change",
    "root_cause_cluster": "optional_cluster_name_when_supported_by_history",
    "concern_verdict": "confirmed|dismissed  // for concern signals only",
    "concern_fingerprint": "abc123  // required when dismissed; copy from signal fingerprint",
    "reasoning": "why dismissed  // optional, for dismissed only"
  }],
  "retrospective": {
    "root_causes": ["optional: concise root-cause hypotheses"],
    "likely_symptoms": ["optional: identifiers that look symptom-level"],
    "possible_false_positives": ["optional: prior concept keys likely mis-scoped"]
  }
}
