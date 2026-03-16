You are a focused subagent reviewer for a single holistic investigation batch.

Repository root: /Users/mishari/Library/CloudStorage/OneDrive-Personal/OneDrive Projects/OpenCode/eventyay
Blind packet: /Users/mishari/Library/CloudStorage/OneDrive-Personal/OneDrive Projects/OpenCode/eventyay/.desloppify/review_packet_blind.json
Batch index: 7
Batch name: dependency_health
Batch rationale: seed files for dependency_health review

DIMENSION TO EVALUATE:

## dependency_health
Unused deps, version conflicts, multiple libs for same purpose, heavy deps
Look for:
- Multiple libraries for the same purpose (e.g. moment + dayjs, axios + fetch wrapper)
- Heavy dependencies pulled in for light use (e.g. lodash for one function)
- Circular dependency cycles visible in the import graph
- Unused dependencies in package.json/requirements.txt
- Version conflicts or pinning issues visible in lock files
Skip:
- Dev dependencies (test, build, lint tools)
- Peer dependencies required by frameworks

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

Task requirements:
1. Read the blind packet's `system_prompt` — it contains scoring rules and calibration.
2. Start from the seed files, then freely explore the repository to build your understanding.
3. Keep issues and scoring scoped to this batch's dimension.
4. Respect scope controls: do not include files/directories marked by `exclude`, `suppress`, or non-production zone overrides.
5. Return 0-10 issues for this batch (empty array allowed).
6. Complete `dimension_judgment` for your dimension — all three fields (strengths, issue_character, score_rationale) are required. Write the judgment BEFORE setting the score.
7. Do not edit repository files.
8. Return ONLY valid JSON, no markdown fences.

Scope enums:
- impact_scope: "local" | "module" | "subsystem" | "codebase"
- fix_scope: "single_edit" | "multi_file_refactor" | "architectural_change"

Output schema:
{
  "batch": "dependency_health",
  "batch_index": 7,
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
