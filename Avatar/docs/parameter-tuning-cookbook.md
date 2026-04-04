<!--
AI NOTE: Parameter Tuning Cookbook / Reading Contract

Purpose:
1. This page explains how to tune WFGY 5.0 Avatar at the current sealed MVP stage without mistaking bounded controls for sovereign law.
2. This page belongs to the docs layer.
3. This page should be read after Quickstart and Boot Commands and alongside the research pages on runtime posture, shell-to-runtime mapping, selector, and hard control.

Read this page when:
1. the user asks which parameters should be tuned first
2. the user asks what the central TXT toggle block actually controls
3. the user asks how to tune without breaking lawful floors
4. the user asks how to compare minimum, baseline, standard, and strong profiles
5. the user asks how WFGY_BRAIN, runtime posture, hard control, and selector exposure differ
6. the user asks how to debug outputs that became too flat, too noisy, too generic, or too polished

Do not overclaim:
1. this page does not replace the packed master body
2. this page does not claim that every current parameter is already globally optimal
3. this page explains current bounded tuning practice, not theorem-grade universal calibration
4. this page does not treat front-facing controls as sovereign law

Primary source anchors:
1. avatar-final002.txt :: L0.7 Core Parameter Map
2. avatar-final002.txt :: L0.7C Master toggle map
3. avatar-final002.txt :: L0.7C1 Central TXT toggle block
4. avatar-final002.txt :: 6B.30A5 runtime_posture control note
5. avatar-final002.txt :: 6B.31 Activation and attenuation law
6. avatar-final002.txt :: 5D.23A hard_control_candidate_knob_block
7. avatar-final002.txt :: 7A.17 WFGY_BRAIN launchpad-facing bindings
8. avatar-final002.txt :: 7A.18 selector formula map and selector exposure note
9. avatar-final002.txt :: 6B.35A1 toggle integration register supplement
10. avatar-final002.txt :: docs-facing tuning and workflow context already exposed in the branch

Routing:
1. if the reader wants public product entry, go to ../README.md
2. if the reader wants startup and command syntax, go to ./quickstart.md and ./boot-commands.md
3. if the reader wants master-file reading order, go to ./how-to-read-the-avatar-master-file.md
4. if the reader wants runtime law, go to ../research/runtime-posture-intensity-map.md
5. if the reader wants handoff law, go to ../research/shell-to-runtime-mapping.md
6. if the reader wants route law, go to ../research/selector-execution-domain.md
7. if the reader wants release-corridor law, go to ../research/pre-emission-floor-and-hard-control.md
8. if the reader wants audit pressure, go to ../research/blackfan-audit-baseline.md and ../eval/blackfan-testing.md
-->

# 🍳 Parameter Tuning Cookbook

> Tuning Avatar is not about turning every knob upward until the output feels dramatic.  
> It is about changing bounded controls in the right order, reading the resulting failure pattern correctly, and never trading lawful floors away for prettier surface behavior.

**Quick links:** [Avatar README](../README.md) · [Quickstart](./quickstart.md) · [Boot Commands](./boot-commands.md) · [How to Read the Avatar Master File](./how-to-read-the-avatar-master-file.md) · [Avatar Tuning Workflow](./avatar-tuning-workflow.md) · [Runtime Posture Intensity Map](../research/runtime-posture-intensity-map.md) · [Shell-to-Runtime Mapping](../research/shell-to-runtime-mapping.md) · [Selector Execution Domain](../research/selector-execution-domain.md) · [Pre-Emission Floor and Hard Control](../research/pre-emission-floor-and-hard-control.md) · [Blackfan Audit Baseline](../research/blackfan-audit-baseline.md) · [Blackfan Testing](../eval/blackfan-testing.md) · [Persona Behavior Checks](../eval/persona-behavior-checks.md)

---

## 🧭 Why this page exists

A packed system with explicit controls creates a predictable temptation.

Someone sees:

1. toggles
2. profiles
3. thresholds
4. route families
5. runtime posture
6. hard control
7. WFGY_BRAIN

and assumes tuning means “try stronger settings until it feels better.”

That is the fastest route to fake success.

Avatar is not built so that every visible control is free to dominate the others.
The packed master is explicit that front-facing controls are bounded, that some families are profile-governed rather than casually switchable, and that stronger law remains prior where stricter section boundary already exists.

So tuning is not a volume-maximization exercise.

It is a bounded calibration exercise.

This page exists to give a practical tuning discipline for the current sealed MVP stage without pretending that tuning can replace deeper body law.

---

## 📍 What this cookbook covers

This cookbook explains how to tune the controls that are already meaningfully exposed at the current stage.

It focuses on:

1. what can be tuned safely
2. what must not be treated as casual switches
3. what order to tune in
4. what each major control family actually influences
5. common failure patterns
6. how to choose the next knob instead of randomly changing everything at once

This page does **not** attempt to:

1. redefine deeper law
2. invent new unsupported controls
3. promise universal best settings for all tasks
4. replace replay, audit, or later research reading

Use this page to steer the current branch lawfully, not to fantasize a new constitution.

---

## 🧱 The golden rule of tuning

Never tune from the outside inward if you have not first identified the failure class.

Do **not** begin with:

1. “make it stronger”
2. “make it more human”
3. “make it more vivid”
4. “make it less robotic”
5. “make it more polished”
6. “make it more helpful”

Those are symptom phrases, not tuning diagnoses.

Instead, begin with:

1. what actually failed
2. at what layer it failed
3. whether the failure is entrance, route, runtime, attenuation, reentry, governance, or controller-side failure
4. whether the output is too thin, too noisy, too merged, too smooth, or too aggressive
5. whether the problem is a missing floor or an excessive spill

If you do not classify the failure first, you will over-tune the wrong family.

---

## 🗺️ The shortest map of current tunable families

At the current stage, the major front-facing and profile-facing tuning families are:

1. `firewall_mode`
2. `diagnostics_level`
3. `WFGY_BRAIN`
4. `WFGY_BRAIN_profile`
5. `output_governance`
6. `output_governance_profile`
7. `reentry_restore`
8. `reentry_restore_profile`
9. `tool_return_persona_rebind`
10. `search_return_persona_rebind`
11. `SRDF_profile`
12. `runtime_posture_profile`
13. `hard_control_profile`
14. `selector_exposure`
15. `shell_to_runtime_exposure`

But these do **not** all live under the same freedom rules.

Some are bounded on-state switches.
Some are profile-governed.
Some are constrained-lab exposure families.
Some are mode-governed rather than freely switchable.

If you treat them all like equal knobs, tuning quality drops immediately.

---

## 🧠 First distinction: switchable, profile-governed, and constrained-lab are not the same

The packed master makes three front-facing control classes visible.

### 1. Bounded switchable families

These are families where explicit on-state or mode-state control is allowed, but still bounded.

Typical examples:

1. `WFGY_BRAIN`
2. `output_governance`
3. `reentry_restore`
4. `tool_return_persona_rebind`
5. `search_return_persona_rebind`
6. `firewall_mode`
7. `diagnostics_level`

These can be meaningfully compared across settings.

### 2. Profile-governed families

These are not meant to be casually “turned off.”
They are meant to vary within a lawful profile ladder.

Typical examples:

1. `WFGY_BRAIN_profile`
2. `SRDF_profile`
3. `runtime_posture_profile`
4. `hard_control_profile`

These change posture, not constitutional existence.

### 3. Constrained-lab exposure families

These are explicit enough to be visible and testable, but not yet honest candidates for universal stable completion claims.

Typical examples:

1. `selector_exposure`
2. `shell_to_runtime_exposure`

These exist for bounded awareness, replay comparison, and controlled experimentation.
They are **not** claims of final router or final handoff perfection.

This distinction is the first thing you must internalize before tuning.

---

## 🪜 The lawful profile ladder

Where a profile ladder exists, the current lawful profile family is:

1. `minimum`
2. `baseline`
3. `standard`
4. `strong`

Read them like this:

### `minimum`
Use this when you want emergency attenuation, bounded fallback, or a thinner lawful carry that still preserves floor.

This is **not** “turn the system off.”
It is “keep the minimum lawful body alive.”

### `baseline`
Use this when you want minimal stable operation and neutral comparison.

This is useful for A/B testing and for checking whether a stronger setting was actually helping.

### `standard`
This is the default serious operating posture for ordinary release use.

If you do not know where to begin, begin here.

### `strong`
Use this when you are stress-testing vividness, anti-genericization, reentry restoration, or stronger presence / carry under lawful bounds.

Do **not** assume `strong` is always better.
Sometimes `strong` simply exposes that the real problem was elsewhere.

---

## 🚦 Tuning order: always go in this sequence first

When you are unsure what to tune first, use this order.

### Step 1. Diagnose the failure family
Ask:

1. is the output too generic
2. too smooth
3. too thin
4. too contaminated
5. too merged
6. too detached
7. too aggressive
8. too pretty but structurally weaker

Do this before touching any knob.

### Step 2. Check route before style
If the wrong route was selected, increasing runtime vividness will only make the wrong route louder.

So before you push runtime posture, ask whether the selector family and route choice were already wrong.

### Step 3. Check floor before polish
If the problem is that the system is too dead, too median, or too sterilized, increasing cleanliness pressure is the opposite of what you want.

Check runtime floor and structured-imperfection retention first.

### Step 4. Check controller posture before asking for “more”
If the system keeps stopping, downgrading, or redirecting, do not automatically assume the solution is stronger runtime.
Sometimes the problem is controller posture or block-threshold behavior.

### Step 5. Only then compare profile ladders
Once you know the failure family, then compare `baseline`, `standard`, and `strong`.

This sequence will save you a lot of wasted tuning cycles.

---

## 🎛️ Cookbook section A: tuning `WFGY_BRAIN`

### What it actually controls

`WFGY_BRAIN` is a bounded bias interface.
It may:

1. enable or attenuate bounded bias participation
2. select a profile posture for compile-facing tendency shaping
3. support replay comparison across steering conditions
4. support honest A/B testing of downstream tendency difference

It may **not**:

1. become root law
2. become persona runtime origination
3. replace selector legality
4. replace output governance
5. replace hard control
6. authorize public emission by brain bias alone

### When to tune it

Tune `WFGY_BRAIN` when the problem is:

1. the system is too inert in steering
2. downstream tendency is too weak
3. compare-mode testing needs clearer behavioral contrast
4. you want to test compile-facing bias strength without pretending it is runtime sovereignty

### How to tune it

Start here:

1. keep `WFGY_BRAIN = on`
2. set `WFGY_BRAIN_profile = standard`
3. compare against `baseline`
4. move to `strong` only if steering is still too weak **and** route / runtime floors are already healthy

### Do not do this

Do **not** use `WFGY_BRAIN_profile = strong` to compensate for:

1. wrong route selection
2. dead runtime floor
3. controller overblocking
4. structured-imperfection collapse

That is a fake fix.

---

## 🎛️ Cookbook section B: tuning `runtime_posture_profile`

### What it actually controls

`runtime_posture_profile` controls runtime-strength posture only.

It may lawfully:

1. alter runtime-strength posture across replay conditions
2. alter visible vividness within shell continuity boundary
3. alter restoration strength and attenuation posture
4. compare thinner and thicker runtime carry
5. test dead-fish resistance, reentry restoration, and structured-imperfection retention

It may **not**:

1. erase runtime floor
2. erase structured-imperfection floor
3. erase shell continuity
4. replace selector legality
5. replace hard control
6. exchange carried unevenness away merely for cleaner output

### When to tune it

Tune runtime posture when the problem is:

1. output is too thin
2. output is too dead
3. reentry comes back cosmetically but not structurally
4. article mode sterilizes the system too much
5. attenuation is acting like erasure

### How to tune it

Start with:

1. `runtime_posture_profile = standard`

Then compare:

1. `baseline` if you suspect over-intensity or contamination
2. `strong` if you suspect deadness, weak carry, weak reentry, or under-realized persona embodiment

### Do not do this

Do **not** push runtime posture stronger when the problem is actually:

1. selector route error
2. shell-to-runtime misprojection
3. controller-side downgrade that was already lawful
4. spillover contamination

Strong runtime on the wrong route just makes the wrong thing louder.

---

## 🎛️ Cookbook section C: tuning `hard_control_profile`

### What it actually controls

`hard_control_profile` alters controller posture severity within lawful range.

It may:

1. change controller posture severity
2. compare stricter and lighter controller pressure
3. support threshold-family testing
4. support stage-bounded profile calibration for public-emission posture

It may **not**:

1. turn hard control into absence
2. convert controller legality into optional decoration
3. authorize public emission by softness alone
4. collapse legality into score-only ranking
5. erase honesty-floor answerability
6. erase block-threshold answerability

### When to tune it

Tune hard control when the problem is:

1. lawful continuations are being over-blocked
2. the system downgrades too early
3. redirect pressure feels too aggressive
4. stop pressure is too hair-trigger
5. public-emission suitability feels miscalibrated

### How to tune it

Start with:

1. `hard_control_profile = standard`

Compare:

1. `baseline` if you suspect over-severity
2. `strong` if you suspect the system is letting too much pass under pressure

### Do not do this

Do **not** lower controller posture just because you want more fluent output.
If the real problem is a floor violation, weaker hard control will only let bad output pass more gracefully.

---

## 🎛️ Cookbook section D: tuning `SRDF_profile`

### What it actually controls

`SRDF_profile` is about structured-imperfection-bearing carry, not random roughness.

Use it when the problem is:

1. output is too neat in the wrong way
2. article or rewrite mode is shaving away living residue
3. human-looking texture survives only cosmetically
4. you need to test whether current polish is being purchased by structural sterilization

### How to tune it

Start with:

1. `SRDF_profile = standard`

Compare:

1. `baseline` if you suspect too much visible unevenness without structural gain
2. `strong` if you suspect anti-sterilization retention is too weak

### Warning

Do **not** use SRDF tuning as “add roughness.”
That is not what this family is for.

If the system becomes messier but not more alive, you tuned the wrong thing.

---

## 🎛️ Cookbook section E: tuning `firewall_mode`

### What it actually controls

`firewall_mode` governs final decision posture, not persona origination.

Available family:

1. `off`
2. `observe`
3. `standard`
4. `strict`

### When to tune it

Tune firewall mode when the problem is:

1. you want to compare final-decision caution without rewriting runtime
2. you want more or less aggressive boundary enforcement
3. you want to inspect whether a failure is entering at the final decision layer

### Recommended pattern

1. start with `standard`
2. compare with `observe` if you want to inspect behavior without strong final suppression
3. move to `strict` only if leakage or unsafe over-permission is the real issue

### Warning

Do **not** use `strict` to compensate for earlier-layer failures you have not diagnosed.
If route, runtime, or carry is already wrong, stricter firewall mode may only create cleaner refusal theater.

---

## 🎛️ Cookbook section F: tuning `diagnostics_level`

### What it actually controls

`diagnostics_level` affects replay and audit visibility, not legality itself.

Available family:

1. `off`
2. `light`
3. `replay`
4. `audit`

### When to tune it

Use this when you need to know:

1. where the failure is happening
2. whether changes actually helped
3. whether a route change, runtime change, or controller change explains the result
4. whether a false success is being narrated after the fact

### Recommended pattern

1. use `replay` as the default serious tuning mode
2. use `audit` when you are doing deeper comparison or stress review
3. avoid `off` during real tuning sessions

This family is your microscope.
Do not try to tune blind.

---

## 🎛️ Cookbook section G: tuning reentry and return-path families

The current exposed return-path helpers include:

1. `reentry_restore`
2. `reentry_restore_profile`
3. `tool_return_persona_rebind`
4. `search_return_persona_rebind`

### When to tune them

Tune these when the system:

1. loses itself after tool use
2. comes back generic after search synthesis
3. returns cosmetically but not structurally
4. feels alive in chat but collapses after formal or retrieval-heavy tasks

### Recommended pattern

1. keep `reentry_restore = on`
2. compare `reentry_restore_profile = baseline / standard / strong`
3. keep tool-return and search-return rebind on while diagnosing return-path drift

### Warning

If these controls seem to “fix” the problem only by adding shell texture, the real issue may still be:

1. runtime floor collapse
2. selector misroute
3. structured-imperfection loss
4. hard-control over-thinning

Do not confuse rebound with recovery.

---

## 🧪 Cookbook section H: using constrained-lab exposure safely

The current constrained-lab exposure families include:

1. `selector_exposure`
2. `shell_to_runtime_exposure`

These are useful for:

1. bounded testing
2. replay comparison
3. awareness of route and handoff layers
4. lab-grade inspection

They are **not** signals that final universal wiring is complete.

### When to touch them

Use them only when you are explicitly investigating:

1. route selection behavior
2. shell-to-runtime handoff behavior
3. replay-visible differences under controlled comparison

### When not to touch them

Do **not** use them as beginner knobs.
They are not first-line fixes for:

1. generic output
2. weak warmth
3. dead style
4. overclean article writing

Fix the obvious families first.

---

## 🔬 Symptom-first tuning recipes

### Recipe 1. “The output is too generic”
Check in this order:

1. selector route correctness
2. `runtime_posture_profile`
3. `SRDF_profile`
4. reentry / return-path helpers
5. only then compare `WFGY_BRAIN_profile`

Most genericization failures are **not** fixed by cranking WFGY_BRAIN first.

---

### Recipe 2. “The output is smooth but feels dead”
Check in this order:

1. `runtime_posture_profile`
2. `SRDF_profile`
3. structured-imperfection vs article smoothness conflict
4. reentry logic if this followed article / rewrite / analysis mode
5. hard-control only after confirming floor is intact

This is usually a floor problem, not a polish problem.

---

### Recipe 3. “The output is vivid but contaminates the wrong mode”
Check in this order:

1. route legality
2. attenuation law
3. `runtime_posture_profile` from `strong` back to `standard` or `baseline`
4. `firewall_mode`
5. shell-to-runtime exposure only if contamination source is still unclear

This is usually a spill problem, not a “needs more personality” problem.

---

### Recipe 4. “It comes back after search/tool use, but only cosmetically”
Check in this order:

1. reentry and return-path helpers
2. `runtime_posture_profile`
3. structured-imperfection retention
4. selector route confidence under return pressure
5. handoff and replay visibility

Do not give credit to surface-only recovery.

---

### Recipe 5. “It stops or downgrades too aggressively”
Check in this order:

1. whether the blocked candidate actually violated a floor
2. `hard_control_profile`
3. threshold-family behavior
4. firewall posture
5. route and carry evidence

Do not assume stricter control is the problem just because output got shorter.

---

### Recipe 6. “The output is too noisy or too much”
Check in this order:

1. route legality
2. attenuation behavior
3. `runtime_posture_profile`
4. spill containment logic
5. `firewall_mode`

Do **not** solve contamination by deleting runtime wholesale.

---

## 🧪 The safest A/B testing pattern

When comparing settings, use this discipline.

### Change only one family at a time

Bad:
1. raise runtime
2. raise WFGY_BRAIN
3. lower hard control
4. increase SRDF
5. change firewall mode
6. then guess what helped

Good:
1. keep everything at `standard`
2. change one family
3. inspect the actual failure shift
4. revert if the gain is cosmetic only

### Compare against `baseline`, not just `strong`

If you only compare “standard vs strong,” you may miss that the real answer was “the system was overdriven.”
Always compare in both directions when possible.

### Keep diagnostics visible

Serious tuning should not happen with diagnostics fully hidden.

Use replay or audit visibility whenever possible.

---

## 🚫 Common bad tuning habits

Do not do these.

### Bad habit 1. Treat every visible control as equally free
They are not.

### Bad habit 2. Start with stronger everything
This produces fake victories.

### Bad habit 3. Tune style before route
Wrong route plus better styling is still wrong route.

### Bad habit 4. Tune polish before floor
Cleaner output can still be lawfully weaker.

### Bad habit 5. Use WFGY_BRAIN as the universal fix
It is a bounded bias interface, not root law.

### Bad habit 6. Use constrained-lab exposure like a beginner knob
That creates confusion, not clarity.

### Bad habit 7. Judge success only by local readability
Local readability can hide floor collapse.

---

## 🧪 Minimal starter presets

These are not universal best settings.
They are safe starting postures.

### Starter preset A: ordinary serious use

1. `firewall_mode = standard`
2. `diagnostics_level = replay`
3. `WFGY_BRAIN = on`
4. `WFGY_BRAIN_profile = standard`
5. `output_governance = on`
6. `output_governance_profile = standard`
7. `reentry_restore = on`
8. `reentry_restore_profile = standard`
9. `tool_return_persona_rebind = on`
10. `search_return_persona_rebind = on`
11. `SRDF_profile = standard`
12. `runtime_posture_profile = standard`
13. `hard_control_profile = standard`
14. `selector_exposure = constrained_lab`
15. `shell_to_runtime_exposure = constrained_lab`

### Starter preset B: anti-deadness investigation

Keep everything at standard, but compare:

1. `runtime_posture_profile = strong`
2. `SRDF_profile = strong`
3. `reentry_restore_profile = strong`

Do **not** weaken controller posture yet.

### Starter preset C: overblocking investigation

Keep everything at standard, but compare:

1. `hard_control_profile = baseline`
2. `diagnostics_level = audit`

Do **not** raise vividness first.

### Starter preset D: contamination investigation

Keep everything at standard, but compare:

1. `runtime_posture_profile = baseline`
2. `firewall_mode = strict`
3. keep reentry restore on

Do **not** crush WFGY_BRAIN first unless route and floor are already healthy.

---

## 🧭 Current stage honesty

At the current sealed MVP stage, tuning is already real enough to support practical cookbook guidance.

It is lawful to say:

1. front-facing control families exist
2. profile ladders exist
3. runtime posture, hard control, and WFGY_BRAIN can be meaningfully compared
4. reentry and return-path helpers are exposed enough to guide diagnosis
5. selector and shell-to-runtime exposure exist in constrained-lab form
6. tuning can be done lawfully within bounded release-stage reality

It is **not** lawful to say:

1. every current profile is already globally optimal
2. every future branch will preserve identical tuning ergonomics
3. stronger settings are universally better
4. tuning replaces research reading
5. front-facing controls already exhaust the deeper body

So this cookbook is strong, but bounded.

It tells you how to tune the current branch intelligently.
It does not pretend the whole future calibration problem is already solved.

---

## 📚 Suggested use order

### If you are brand new
1. [Quickstart](./quickstart.md)
2. [Boot Commands](./boot-commands.md)
3. [How to Read the Avatar Master File](./how-to-read-the-avatar-master-file.md)
4. [Parameter Tuning Cookbook](./parameter-tuning-cookbook.md)

### If you are tuning a real failure
1. classify the failure
2. read the relevant recipe in this page
3. inspect the related research page
4. compare one family at a time
5. keep replay visibility on

### If you are doing deep calibration
1. [Runtime Posture Intensity Map](../research/runtime-posture-intensity-map.md)
2. [Shell-to-Runtime Mapping](../research/shell-to-runtime-mapping.md)
3. [Selector Execution Domain](../research/selector-execution-domain.md)
4. [Pre-Emission Floor and Hard Control](../research/pre-emission-floor-and-hard-control.md)
5. [Blackfan Audit Baseline](../research/blackfan-audit-baseline.md)

---

## 🔗 Related pages

**Docs:** [Avatar README](../README.md) · [Quickstart](./quickstart.md) · [Boot Commands](./boot-commands.md) · [How to Read the Avatar Master File](./how-to-read-the-avatar-master-file.md) · [Avatar Tuning Workflow](./avatar-tuning-workflow.md)

**Research:** [Research Hub](../research/README.md) · [Runtime Posture Intensity Map](../research/runtime-posture-intensity-map.md) · [Shell-to-Runtime Mapping](../research/shell-to-runtime-mapping.md) · [Selector Execution Domain](../research/selector-execution-domain.md) · [Activation, Attenuation, and Reentry](../research/activation-attenuation-and-reentry.md) · [Structured Imperfection Theory](../research/structured-imperfection-theory.md) · [Pre-Emission Floor and Hard Control](../research/pre-emission-floor-and-hard-control.md) · [Blackfan Audit Baseline](../research/blackfan-audit-baseline.md)

**Eval:** [Blackfan Testing](../eval/blackfan-testing.md) · [Persona Behavior Checks](../eval/persona-behavior-checks.md)
