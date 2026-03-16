You are a focused subagent reviewer for a single holistic investigation batch.

Repository root: /Users/mishari/Library/CloudStorage/OneDrive-Personal/OneDrive Projects/OpenCode/eventyay
Blind packet: /Users/mishari/Library/CloudStorage/OneDrive-Personal/OneDrive Projects/OpenCode/eventyay/.desloppify/review_packet_blind.json
Batch index: 4
Batch name: error_consistency
Batch rationale: seed files for error_consistency review

DIMENSION TO EVALUATE:

## error_consistency
Consistent error strategies, preserved context, predictable failure modes
Look for:
- Mixed error strategies: some functions throw, others return null, others use Result types
- Error context lost at boundaries: catch-and-rethrow without wrapping original
- Inconsistent error types: custom error classes in some modules, bare strings in others
- Silent error swallowing: catches that log but don't propagate or recover
- Missing error handling on I/O boundaries (file, network, parse operations)
Skip:
- Intentional error boundaries at top-level handlers
- Different strategies for different layers (e.g. Result in core, throw in CLI)

YOUR TASK: Read the code for this batch's dimension. Judge how well the codebase serves a developer from that perspective. The dimension rubric above defines what good looks like. Cite specific observations that explain your judgment.

Mechanical scan evidence — navigation aid, not scoring evidence:
The blind packet contains `holistic_context.scan_evidence` with aggregated signals from all mechanical detectors — including complexity hotspots, error hotspots, signal density index, boundary violations, and systemic patterns. Use these as starting points for where to look beyond the seed files.

Seed files (start here):
- app/eventyay/agenda/views/feed.py
- app/eventyay/agenda/views/widget.py
- app/eventyay/agenda/views/utils.py
- app/eventyay/agenda/views/featured.py
- app/eventyay/agenda/views/schedule.py
- app/eventyay/api/auth/devicesecurity.py
- app/eventyay/api/auth/permission.py
- app/eventyay/api/views/oauth.py
- app/eventyay/api/views/stripe.py
- app/eventyay/api/views/access_code.py
- app/eventyay/api/views/device.py
- app/eventyay/api/views/mail.py
- app/eventyay/api/views/organizer.py
- app/eventyay/api/views/question.py
- app/eventyay/api/views/review.py
- app/eventyay/api/views/rooms.py
- app/eventyay/api/views/speaker.py
- app/eventyay/api/views/speaker_information.py
- app/eventyay/api/views/upload.py
- app/eventyay/api/views/user.py
- app/eventyay/api/views/version.py
- app/eventyay/api/views/webhooks.py
- app/eventyay/base/exporters/json.py
- app/eventyay/base/exporters/orderlist.py
- app/eventyay/base/exporters/waitinglist.py
- app/eventyay/base/forms/validators.py
- app/eventyay/base/forms/widgets.py
- app/eventyay/base/models/transaction.py
- app/eventyay/base/models/announcement.py
- app/eventyay/base/models/audit.py
- app/eventyay/base/models/availability.py
- app/eventyay/base/models/base.py
- app/eventyay/base/models/bbb.py
- app/eventyay/base/models/cache.py
- app/eventyay/base/models/chat.py
- app/eventyay/base/models/exhibitor.py
- app/eventyay/base/models/fields.py
- app/eventyay/base/models/invoices.py
- app/eventyay/base/models/janus.py
- app/eventyay/base/models/mixins.py
- app/eventyay/base/models/poll.py
- app/eventyay/base/models/poster.py
- app/eventyay/base/models/roomquestion.py
- app/eventyay/base/models/roulette.py
- app/eventyay/base/models/storage_model.py
- app/eventyay/base/models/streaming.py
- app/eventyay/base/models/systemlog.py
- app/eventyay/base/models/turn.py
- app/eventyay/base/models/world.py
- app/eventyay/consts.py
- app/eventyay/cfp/forms/cfp.py
- app/eventyay/cfp/views/event.py
- app/eventyay/cfp/views/robots.py
- app/eventyay/common/forms/renderers.py
- app/eventyay/common/views/cache.py
- app/eventyay/common/views/redirect.py
- app/eventyay/config/sentry.py
- app/eventyay/control/forms/renderers.py
- app/eventyay/control/forms/checkin.py
- app/eventyay/control/forms/orders.py
- app/eventyay/control/forms/product.py
- app/eventyay/control/forms/widgets.py
- app/eventyay/control/forms/organizer_forms/base_organizer_footer_link_form_set.py
- app/eventyay/control/forms/organizer_forms/event_meta_property_form.py
- app/eventyay/control/forms/organizer_forms/gate_form.py
- app/eventyay/control/forms/organizer_forms/gift_card_update_form.py
- app/eventyay/control/forms/organizer_forms/organizer_settings_form.py
- app/eventyay/control/forms/organizer_forms/web_hook_form.py
- app/eventyay/control/views/geo.py
- app/eventyay/control/views/typeahead.py
- app/eventyay/control/views/main.py
- app/eventyay/control/views/pdf.py
- app/eventyay/control/views/search.py
- app/eventyay/control/views/dashboards.py
- app/eventyay/control/views/shredder.py
- app/eventyay/control/views/global_settings.py
- app/eventyay/control/views/waitinglist.py
- app/eventyay/control/views/admin_views.py
- app/eventyay/control/views/checkin.py
- app/eventyay/control/views/pages.py

RELEVANT FINDINGS — explore with CLI:
These detectors found patterns related to this dimension. Explore the findings,
then read the actual source code.

  desloppify show security --no-budget      # 162 findings
  desloppify show smells --no-budget      # 329 findings

Report actionable issues in issues[]. Use concern_verdict and concern_fingerprint
for findings you want to confirm or dismiss.

Task requirements:
1. Read the blind packet's `system_prompt` — it contains scoring rules and calibration.
2. Start from the seed files, then freely explore the repository to build your understanding.
3. Keep issues and scoring scoped to this batch's dimension.
4. Respect scope controls: do not include files/directories marked by `exclude`, `suppress`, or non-production zone overrides.
5. Return 0-10 issues for this batch (empty array allowed).
6. For error_consistency, use evidence from `holistic_context.errors.exception_hotspots` — files with concentrated exception handling issues. Investigate whether error handling is designed or accidental. Check for broad catches masking specific failure modes.
7. Complete `dimension_judgment` for your dimension — all three fields (strengths, issue_character, score_rationale) are required. Write the judgment BEFORE setting the score.
8. Do not edit repository files.
9. Return ONLY valid JSON, no markdown fences.

Scope enums:
- impact_scope: "local" | "module" | "subsystem" | "codebase"
- fix_scope: "single_edit" | "multi_file_refactor" | "architectural_change"

Output schema:
{
  "batch": "error_consistency",
  "batch_index": 4,
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
