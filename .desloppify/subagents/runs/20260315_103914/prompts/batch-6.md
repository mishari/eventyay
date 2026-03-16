You are a focused subagent reviewer for a single holistic investigation batch.

Repository root: /Users/mishari/Library/CloudStorage/OneDrive-Personal/OneDrive Projects/OpenCode/eventyay
Blind packet: /Users/mishari/Library/CloudStorage/OneDrive-Personal/OneDrive Projects/OpenCode/eventyay/.desloppify/review_packet_blind.json
Batch index: 6
Batch name: abstraction_fitness
Batch rationale: seed files for abstraction_fitness review

DIMENSION TO EVALUATE:

## abstraction_fitness
Python abstraction fitness: favor direct modules, explicit domain APIs, and bounded packages over indirection and generic helper surfaces.
Look for:
- Functions that only forward args/kwargs to another function without policy or translation
- Protocol/base-class abstractions with one concrete implementation and no extension pressure
- Cross-module wrapper chains where calls hop through helper layers before reaching real logic
- Project-wide reliance on generic helper modules instead of bounded domain packages
- Over-broad dict/config/context parameters used as implicit parameter bags
Skip:
- Django/FastAPI/SQLAlchemy framework boundaries that require adapters or dependency hooks
- Wrappers that add retries, metrics, auth checks, caching, or tracing
- Intentional package facades used to stabilize public import paths
- Migration shims with active callers and clear sunset plan

YOUR TASK: Read the code for this batch's dimension. Judge how well the codebase serves a developer from that perspective. The dimension rubric above defines what good looks like. Cite specific observations that explain your judgment.

Mechanical scan evidence — navigation aid, not scoring evidence:
The blind packet contains `holistic_context.scan_evidence` with aggregated signals from all mechanical detectors — including complexity hotspots, error hotspots, signal density index, boundary violations, and systemic patterns. Use these as starting points for where to look beyond the seed files.

Seed files (start here):
- app/eventyay/agenda/views/utils.py
- app/eventyay/presale/utils.py
- app/eventyay/features/analytics/graphs/utils.py
- app/eventyay/eventyay_common/utils.py
- app/eventyay/features/social/utils.py
- app/eventyay/common/views/helpers.py
- app/eventyay/event/utils.py
- app/eventyay/schedule/utils.py
- app/eventyay/eventyay_common/views/account/common.py
- app/eventyay/control/views/orders.py
- app/eventyay/control/views/event.py
- app/eventyay/control/views/product.py
- app/eventyay/cfp/flow.py
- app/eventyay/base/models/event.py
- app/eventyay/presale/views/order.py
- app/eventyay/control/views/admin.py
- app/eventyay/control/views/subevents.py
- app/eventyay/base/payment.py
- app/eventyay/control/views/organizer.py
- app/eventyay/control/views/organizer_views/organizer_view.py
- app/eventyay/control/views/vouchers.py
- app/eventyay/control/views/organizer_views/device_view.py
- app/eventyay/control/views/users.py
- app/eventyay/eventyay_common/views/event.py
- app/eventyay/orga/views/review.py
- app/eventyay/orga/views/submission.py
- app/eventyay/plugins/banktransfer/views.py
- app/eventyay/base/orderimport.py
- app/eventyay/control/views/organizer_views/gate_view.py
- app/eventyay/control/logdisplay.py
- app/eventyay/eventyay_common/views/auth.py
- app/eventyay/plugins/sendmail/signals.py
- app/eventyay/base/services/orders.py
- app/eventyay/base/models/orders.py
- app/eventyay/api/views/order.py
- app/eventyay/orga/views/cfp.py
- app/eventyay/cfp/views/user.py
- app/eventyay/orga/views/event.py
- app/eventyay/presale/views/cart.py
- app/eventyay/orga/views/schedule.py
- app/eventyay/api/serializers/order.py
- app/eventyay/eventyay_common/views/account/two_factor_auth.py
- app/eventyay/presale/urls.py
- app/eventyay/control/forms/orders.py
- app/eventyay/orga/views/dashboard.py
- app/eventyay/base/views/mixins.py
- app/eventyay/api/views/checkin.py
- app/eventyay/base/services/user.py
- app/eventyay/base/services/mail.py
- app/eventyay/base/models/product.py
- app/eventyay/base/models/vouchers.py
- app/eventyay/base/services/cancelevent.py
- app/eventyay/base/services/cart.py
- app/eventyay/common/views/cache.py
- app/eventyay/schedule/ascii.py
- app/eventyay/presale/views/event.py
- app/eventyay/presale/views/organizer.py
- app/eventyay/common/forms/widgets.py
- app/eventyay/control/forms/__init__.py
- app/eventyay/common/forms/mixins.py
- app/eventyay/base/models/mail.py
- app/eventyay/base/services/checkin.py
- app/eventyay/base/services/chat.py
- app/eventyay/base/auth.py
- app/eventyay/agenda/views/speaker.py
- app/eventyay/core/utils/statsd.py
- app/eventyay/api/filters/review.py
- app/eventyay/api/filters/schedule.py
- app/eventyay/base/configurations/__init__.py
- app/eventyay/base/models/__init__.py
- app/eventyay/base/tasks.py
- app/eventyay/common/forms/__init__.py
- app/eventyay/common/middleware/__init__.py
- app/eventyay/common/views/__init__.py
- app/eventyay/control/forms/organizer_forms/__init__.py
- app/eventyay/control/views/organizer_views/__init__.py
- app/eventyay/eventyay_common/views/account/__init__.py
- app/eventyay/orga/forms/__init__.py
- app/eventyay/person/forms/__init__.py
- app/eventyay/presale/checkoutflowstep/__init__.py

RELEVANT FINDINGS — explore with CLI:
These detectors found patterns related to this dimension. Explore the findings,
then read the actual source code.

  desloppify show facade --no-budget      # 15 findings
  desloppify show props --no-budget      # 3 findings
  desloppify show responsibility_cohesion --no-budget      # 53 findings
  desloppify show structural --no-budget      # 166 findings

Report actionable issues in issues[]. Use concern_verdict and concern_fingerprint
for findings you want to confirm or dismiss.

Task requirements:
1. Read the blind packet's `system_prompt` — it contains scoring rules and calibration.
2. Start from the seed files, then freely explore the repository to build your understanding.
3. Keep issues and scoring scoped to this batch's dimension.
4. Respect scope controls: do not include files/directories marked by `exclude`, `suppress`, or non-production zone overrides.
5. Return 0-10 issues for this batch (empty array allowed).
6. For abstraction_fitness, use evidence from `holistic_context.abstractions`:
7. - `delegation_heavy_classes`: classes where most methods forward to an inner object — entries include class_name, delegate_target, sample_methods, and line number.
8. - `facade_modules`: re-export-only modules with high re_export_ratio — entries include samples (re-exported names) and loc.
9. - `typed_dict_violations`: TypedDict fields accessed via .get()/.setdefault()/.pop() — entries include typed_dict_name, violation_type, field, and line number.
10. - `complexity_hotspots`: files where mechanical analysis found extreme parameter counts, deep nesting, or disconnected responsibility clusters.
11. Include `delegation_density`, `definition_directness`, and `type_discipline` alongside existing sub-axes in dimension_notes when evidence supports it.
12. Complete `dimension_judgment` for your dimension — all three fields (strengths, issue_character, score_rationale) are required. Write the judgment BEFORE setting the score.
13. Do not edit repository files.
14. Return ONLY valid JSON, no markdown fences.

Scope enums:
- impact_scope: "local" | "module" | "subsystem" | "codebase"
- fix_scope: "single_edit" | "multi_file_refactor" | "architectural_change"

Output schema:
{
  "batch": "abstraction_fitness",
  "batch_index": 6,
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
