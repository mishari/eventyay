You are a focused subagent reviewer for a single holistic investigation batch.

Repository root: /Users/mishari/Library/CloudStorage/OneDrive-Personal/OneDrive Projects/OpenCode/eventyay
Blind packet: /Users/mishari/Library/CloudStorage/OneDrive-Personal/OneDrive Projects/OpenCode/eventyay/.desloppify/review_packet_blind.json
Batch index: 17
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
- app/eventyay/base/services/mail.py
- app/eventyay/agenda/views/talk.py
- app/eventyay/eventyay_common/views/auth.py
- app/eventyay/api/serializers/event.py
- app/eventyay/agenda/views/schedule.py
- app/eventyay/control/views/subevents.py
- app/eventyay/presale/views/order.py
- app/eventyay/control/views/product.py
- app/eventyay/api/views/exporters.py
- app/eventyay/base/views/mixins.py
- app/eventyay/control/forms/widgets.py
- app/eventyay/control/views/__init__.py
- app/eventyay/plugins/sendmail/mixins.py
- app/eventyay/presale/views/__init__.py
- app/eventyay/presale/views/cart.py
- app/eventyay/schedule/forms.py
- app/eventyay/storage/views.py
- app/eventyay/agenda/apps.py
- app/eventyay/agenda/permissions.py
- app/eventyay/agenda/tasks.py
- app/eventyay/agenda/urls.py
- app/eventyay/agenda/views/featured.py
- app/eventyay/agenda/views/utils.py
- app/eventyay/api/apps.py
- app/eventyay/api/auth/api_auth.py
- app/eventyay/api/auth/permission.py
- app/eventyay/api/middleware.py
- app/eventyay/api/serializers/access_code.py
- app/eventyay/api/serializers/fields.py
- app/eventyay/api/serializers/legacy.py
- app/eventyay/api/serializers/organizer.py
- app/eventyay/api/serializers/product.py
- app/eventyay/api/serializers/question.py
- app/eventyay/api/serializers/rooms.py
- app/eventyay/api/serializers/stream_schedule.py
- app/eventyay/api/views/__init__.py
- app/eventyay/api/views/product.py
- app/eventyay/api/webhooks.py
- app/eventyay/base/apps.py
- app/eventyay/base/cache.py
- app/eventyay/base/exporter.py
- app/eventyay/base/exporters/__init__.py
- app/eventyay/base/forms/__init__.py
- app/eventyay/base/forms/user.py
- app/eventyay/base/models/access_code.py
- app/eventyay/base/models/auth_token.py
- app/eventyay/base/models/base.py
- app/eventyay/base/models/cache.py
- app/eventyay/base/models/checkin.py
- app/eventyay/base/models/invoices.py
- app/eventyay/base/models/seating.py
- app/eventyay/base/models/slot.py
- app/eventyay/base/models/streaming.py
- app/eventyay/base/models/submission.py
- app/eventyay/base/models/tax.py
- app/eventyay/base/models/transaction.py
- app/eventyay/base/plugins.py
- app/eventyay/base/secrets.py
- app/eventyay/base/services/announcement.py
- app/eventyay/base/services/cancelevent.py
- app/eventyay/base/services/chat.py
- app/eventyay/base/services/invoices.py
- app/eventyay/base/services/janus.py
- app/eventyay/base/services/locking.py
- app/eventyay/base/services/poll.py
- app/eventyay/base/services/poster.py
- app/eventyay/base/services/pricing.py
- app/eventyay/base/services/room.py
- app/eventyay/base/services/tasks.py
- app/eventyay/base/services/teams.py
- app/eventyay/base/services/turn.py
- app/eventyay/base/services/update_check.py
- app/eventyay/base/shredder.py
- app/eventyay/base/tasks.py
- app/eventyay/base/templatetags/eventsignal.py
- app/eventyay/base/templatetags/rich_text.py
- app/eventyay/base/ticketoutput.py
- app/eventyay/base/views/errors.py
- app/eventyay/common/context_processors.py
- app/eventyay/common/exceptions.py
- app/eventyay/common/exporter.py
- app/eventyay/common/forms/widgets.py
- app/eventyay/common/image.py
- app/eventyay/common/mail.py
- app/eventyay/common/signals.py
- app/eventyay/common/templatetags/copyable.py
- app/eventyay/common/templatetags/filesize.py
- app/eventyay/common/templatetags/html_signal.py

Mechanical concern signals — investigate and adjudicate:
Overview (267 signals):
  design_concern: 135 — app/eventyay/agenda/apps.py, app/eventyay/agenda/permissions.py, ...
  mixed_responsibilities: 92 — app/eventyay/agenda/views/schedule.py, app/eventyay/agenda/views/speaker.py, ...
  structural_complexity: 26 — app/eventyay/api/views/event.py, app/eventyay/base/exporters/dekodi.py, ...
  coupling_design: 9 — app/eventyay/api/views/exporters.py, app/eventyay/base/views/mixins.py, ...
  duplication_design: 2 — app/eventyay/base/models/vouchers.py, app/eventyay/control/views/organizer_views/organizer_detail_view_mixin.py
  interface_design: 2 — app/eventyay/api/views/checkin.py, app/eventyay/base/services/cart.py
  systemic_smell: 1 — app/eventyay/agenda/management/commands/export_schedule_html.py

For each concern, read the source code and report your verdict in issues[]:
  - Confirm → full issue object with concern_verdict: "confirmed"
  - Dismiss → minimal object: {concern_verdict: "dismissed", concern_fingerprint: "<hash>"}
    (only these 2 fields required — add optional reasoning/concern_type/concern_file)
  - Unsure → skip it (will be re-evaluated next review)

  - [coupling_design] app/eventyay/api/views/exporters.py
    summary: Coupling pattern — assess if boundaries need adjustment
    question: Is the coupling intentional or does it indicate a missing abstraction boundary?
    evidence: Flagged by: coupling
    evidence: [coupling] Implicit host contract: ExportersMixin depends on 6 undeclared self attrs (do_export, exporters, get_object, get_serializer_kwargs, +2 more)
    fingerprint: 2efe70fd618803a3
  - [coupling_design] app/eventyay/base/views/mixins.py
    summary: Coupling pattern — assess if boundaries need adjustment
    question: Is the coupling intentional or does it indicate a missing abstraction boundary? Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: coupling, orphaned
    evidence: [orphaned] Orphaned file (335 LOC): zero importers, not an entry point
    fingerprint: 6b3f44aafefd9b16
  - [coupling_design] app/eventyay/control/forms/widgets.py
    summary: Coupling pattern — assess if boundaries need adjustment
    question: Is the coupling intentional or does it indicate a missing abstraction boundary? Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: coupling, orphaned
    evidence: [orphaned] Orphaned file (54 LOC): zero importers, not an entry point
    fingerprint: a9a048e143ee5e56
  - [coupling_design] app/eventyay/control/views/__init__.py
    summary: Coupling pattern — assess if boundaries need adjustment
    question: Is the coupling intentional or does it indicate a missing abstraction boundary?
    evidence: Flagged by: coupling
    evidence: [coupling] Implicit host contract: PaginationMixin depends on 4 undeclared self attrs (DEFAULT_PAGINATION, get_paginate_by, paginate_by, request)
    fingerprint: a0476933ab4e8f61
  - [coupling_design] app/eventyay/plugins/sendmail/mixins.py
    summary: Coupling pattern — assess if boundaries need adjustment
    question: Is the coupling intentional or does it indicate a missing abstraction boundary? Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: coupling, orphaned
    evidence: [orphaned] Orphaned file (105 LOC): zero importers, not an entry point
    fingerprint: f7772a8ec688c803
  - [coupling_design] app/eventyay/presale/views/__init__.py
    summary: Coupling pattern — assess if boundaries need adjustment
    question: Can the nesting be reduced with early returns, guard clauses, or extraction into helper functions? Is the coupling intentional or does it indicate a missing abstraction boundary?
    evidence: Flagged by: coupling, structural
    evidence: File size: 449 lines
    fingerprint: 2695e2e0d8f9ef6d
  - [coupling_design] app/eventyay/presale/views/cart.py
    summary: Coupling pattern — assess if boundaries need adjustment
    question: Can the nesting be reduced with early returns, guard clauses, or extraction into helper functions? Is the coupling intentional or does it indicate a missing abstraction boundary?
    evidence: Flagged by: coupling, structural
    evidence: File size: 701 lines
    fingerprint: 971adbb4c68b41f8
  - [coupling_design] app/eventyay/schedule/forms.py
    summary: Coupling pattern — assess if boundaries need adjustment
    question: Is the coupling intentional or does it indicate a missing abstraction boundary? Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: coupling, orphaned
    evidence: [orphaned] Orphaned file (243 LOC): zero importers, not an entry point
    fingerprint: 5fccfb6b86b70442
  - [coupling_design] app/eventyay/storage/views.py
    summary: Coupling pattern — assess if boundaries need adjustment
    question: Is the coupling intentional or does it indicate a missing abstraction boundary?
    evidence: Flagged by: coupling
    evidence: [coupling] Implicit host contract: UploadMixin depends on 4 undeclared self attrs (event, kwargs, permissions, request)
    fingerprint: 6f5794161308a603
  - [design_concern] app/eventyay/agenda/apps.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (14 LOC): zero importers, not an entry point
    fingerprint: 673c3a1ceb5ce8c4
  - [design_concern] app/eventyay/agenda/permissions.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (112 LOC): zero importers, not an entry point
    fingerprint: e7635d3ec5f24474
  - [design_concern] app/eventyay/agenda/tasks.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (29 LOC): zero importers, not an entry point
    fingerprint: 8b89afd5044df14f
  - [design_concern] app/eventyay/agenda/urls.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (224 LOC): zero importers, not an entry point
    fingerprint: 69e9840d8db103be
  - [design_concern] app/eventyay/agenda/views/featured.py
    summary: Design signals from signature, smells
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: signature, smells
    evidence: [signature] 'dispatch' has 6 different signatures across 40 files
    fingerprint: 8d97f738319d56fe
  - [design_concern] app/eventyay/agenda/views/utils.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (261 LOC): zero importers, not an entry point
    fingerprint: 2bc9b1d66c2e4cf4
  - [design_concern] app/eventyay/api/apps.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (12 LOC): zero importers, not an entry point
    fingerprint: 0d82382ce7562c47
  - [design_concern] app/eventyay/api/auth/api_auth.py
    summary: Design signals from orphaned, signature
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, signature
    evidence: [orphaned] Orphaned file (123 LOC): zero importers, not an entry point
    fingerprint: 34fe37c01a515390
  - [design_concern] app/eventyay/api/auth/permission.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (186 LOC): zero importers, not an entry point
    fingerprint: f5d642c564446baf
  - [design_concern] app/eventyay/api/middleware.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (118 LOC): zero importers, not an entry point
    fingerprint: 816ec03d01ee5269
  - [design_concern] app/eventyay/api/serializers/access_code.py
    summary: Design signals from orphaned, signature
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, signature
    evidence: [orphaned] Orphaned file (43 LOC): zero importers, not an entry point
    fingerprint: 37fc3ce7869380f8
  - [design_concern] app/eventyay/api/serializers/fields.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (72 LOC): zero importers, not an entry point
    fingerprint: 84d69b360439cc74
  - [design_concern] app/eventyay/api/serializers/legacy.py
    summary: Design signals from orphaned, signature
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, signature
    evidence: [orphaned] Orphaned file (425 LOC): zero importers, not an entry point
    fingerprint: f14ca9ecc84403c6
  - [design_concern] app/eventyay/api/serializers/organizer.py
    summary: Design signals from orphaned, smells
    question: Is this file truly dead, or is it used via a non-import mechanism (dynamic import, CLI entry point, plugin)?
    evidence: Flagged by: orphaned, smells
    evidence: [orphaned] Orphaned file (316 LOC): zero importers, not an entry point
    fingerprint: ef259174aa6a1b54
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
  - [design_concern] app/eventyay/api/views/__init__.py
    summary: Design signals from dict_keys, signature
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: dict_keys, signature
    evidence: [signature] 'list' has 3 different signatures across 7 files
    fingerprint: db2917bdb30fb307
  - [design_concern] app/eventyay/api/views/product.py
    summary: Design signals from signature, structural
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: signature, structural
    evidence: File size: 620 lines
    fingerprint: ea32d8289f0ebd3c
  - [design_concern] app/eventyay/api/webhooks.py
    summary: Design signals from dict_keys, smells
    question: Review the flagged patterns — are they design problems that need addressing, or acceptable given the file's role?
    evidence: Flagged by: dict_keys, smells
    evidence: [smells] 1x Except handler silently suppresses error (pass/continue, no log)
    fingerprint: 305512126f26ba19
  (+237 more — use `desloppify show <detector> --no-budget` to explore)

RELEVANT FINDINGS — explore with CLI:
These detectors found patterns related to this dimension. Explore the findings,
then read the actual source code.

  desloppify show coupling --no-budget      # 43 findings
  desloppify show dict_keys --no-budget      # 196 findings
  desloppify show dupes --no-budget      # 29 findings
  desloppify show facade --no-budget      # 3 findings
  desloppify show global_mutable_config --no-budget      # 5 findings
  desloppify show orphaned --no-budget      # 170 findings
  desloppify show props --no-budget      # 1 findings
  desloppify show responsibility_cohesion --no-budget      # 7 findings
  desloppify show signature --no-budget      # 56 findings
  desloppify show smells --no-budget      # 326 findings
  desloppify show structural --no-budget      # 113 findings
  desloppify show unused_enums --no-budget      # 8 findings

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
  "batch_index": 17,
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
