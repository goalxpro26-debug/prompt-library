#!/usr/bin/env python3
"""Generate 5000 bulk prompts for Prompt Press, reproducibly.

Method (honest, not hand-written 5000 essays):
  5 categories x 20 templates x 10 slot-A values x 5 slot-B values = 1000 per category.
Each (template, A, B) triple is unique, so every title, slug and prompt is distinct.
The 85 curated prompts stay untouched; bulk prompts get ids bulk-*.
Re-run: python3 scripts/generate-bulk.py  (idempotent — skips existing bulk ids)
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "src/data/prompts.json"

def slug(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:80]

def T(title, slug_base, prompt, tags):
    return {"title": title, "slug_base": slug_base, "prompt": prompt, "tags": tags}

# Each template uses {A} and {B}. A/B are filled, so the result is a
# personalised, immediately usable prompt — not a blank template.
CATEGORIES = {
 "b2b-frame-control": (
  ["DTC brand founders","SaaS founders","Shopify store owners","TikTok Shop sellers","skincare brands","fitness brands","fashion brands","food brands","tech startups","marketing agencies"],
  ["AI UGC creatives","3D motion graphics","Meta video ads","Character Lock campaigns","performance ad retainers"],
  [
   T("Silent Authority Pitch","silent-authority-pitch","Draft a LinkedIn outreach sequence targeting {A} that uses strategic silence and frame control. Position {B} not as a pitch, but as a critical diagnosis of their current ad spend bleed.",["linkedin","outreach"]),
   T("Soft-Pressure Follow-Up","soft-pressure-follow-up","Create a follow-up email for a high-ticket {B} lead in the {A} space who ghosted. Use calculated vulnerability and soft pressure to trigger fear of missing out on the Q4 rush without sounding desperate.",["follow-up","email"]),
   T("Logic-Reversal Negotiation","logic-reversal-negotiation","A {A} prospect claims {B} is too expensive. Script a live call response that turns their logic around, shifting the frame from cost to the opportunity cost of unoptimized creatives.",["negotiation","pricing"]),
   T("Egotistical Hook DM","egotistical-hook-dm","Write a cold DM to a marketing director at {A} that acknowledges their work, then subtly points out one character-consistency flaw in their ads, positioning {B} as the elite fix.",["dm","cold-outreach"]),
   T("Takeaway Proposal","takeaway-proposal","Draft a project proposal for {A} for {B}. Include a takeaway section that sets strict boundaries on availability to increase perceived value, with clear scope, timeline and next step.",["proposal"]),
   T("Frame-Reset Discovery Agenda","frame-reset-discovery-agenda","Outline a 15-minute discovery call agenda for {A} about {B}. Structure the questions so the prospect qualifies themselves, covering current spend, creative bottlenecks and decision process.",["discovery-call","agenda"]),
   T("Competitor Disruption Script","competitor-disruption-script","Write a script for {A} comparing us to a cheaper competitor for {B}. Address the comparison calmly, contrast outcomes and process, and avoid direct insults.",["competitor","objection"]),
   T("Trust-Building Vulnerability Post","trust-building-vulnerability-post","Draft a LinkedIn post for {A} sharing a real challenge in delivering {B}, what went wrong, what was fixed, and the lesson — to build trust with B2B leads without oversharing client details.",["linkedin","trust"]),
   T("Diagnostic Authority Audit","diagnostic-authority-audit","Create a free audit framework for {A} focused on {B}. List 7 checks, what good looks like for each, and how the audit report leads naturally to a paid next step.",["audit"]),
   T("Uncomfortable Silence Closer","uncomfortable-silence-closer","Script the final 3 minutes of a closing call with {A} for {B}. Detail exactly when to pause for 3 seconds after presenting pricing, what to say next, and how to handle silence without backfilling.",["closing"]),
   T("Referral Request Script","referral-request-script","Write a short referral request for a happy {A} client of {B}. Make it easy to say yes: one sentence, one ideal introduction, and a reason it helps the referred brand.",["referral"]),
   T("Case Study Pitch","case-study-pitch","Draft a pitch to {A} built around a {B} case study. Structure: before, what changed, result in plain numbers, and the one lesson a similar brand can apply this week.",["case-study","pitch"]),
   T("Retainer Upsell Conversation","retainer-upsell-conversation","Script an upsell conversation moving {A} from a one-off {B} project to a monthly retainer. Anchor on continuity, creative testing cadence and the cost of starting over each month.",["retainer","upsell"]),
   T("Price Objection Reframe","price-objection-reframe","A {A} prospect says {B} is out of budget. Write three calm reframes: scope-down option, phased option, and walk-away option — each with what it includes and excludes.",["pricing","objection"]),
   T("Testimonial Request","testimonial-request","Write a testimonial request to {A} after delivering {B}. Ask for one specific outcome, one specific moment, and permission to use it, with a 2-sentence example they can edit.",["testimonial"]),
   T("Partnership Pitch","partnership-pitch","Draft a partnership pitch to {A} for co-marketing {B}. Define who brings what, who benefits, the first joint test, and how success will be measured in 30 days.",["partnership"]),
   T("Q4 Rush Campaign Plan","q4-rush-campaign-plan","Plan a Q4 rush campaign for {A} using {B}. Include hook angles, creative volume per week, testing priorities, and the cutoff date after which new concepts stop.",["q4","campaign"]),
   T("Objection Handling Cheat Sheet","objection-cheat-sheet","Build an objection cheat sheet for selling {B} to {A}. Cover price, timing, trust and 'we do it in-house' — each with a one-line acknowledge, a question, and a next step.",["objection"]),
   T("Cold Email Sequence","cold-email-sequence","Write a 3-email cold sequence to {A} for {B}. Email 1: diagnosis. Email 2: proof. Email 3: clean close or takeaway. Keep each under 120 words.",["email","sequence"]),
   T("Discovery Call Debrief Template","discovery-call-debrief-template","Create a debrief template after a discovery call with {A} about {B}. Capture budget, timeline, decision makers, creative gaps, risks, and the exact follow-up promised.",["debrief","template"]),
  ],
 ),
 "genius-os-tech": (
  ["3D racing game","Flutter arcade game","Astro web tool","Android launcher","UE5 shooter","Three.js web game","financial calculator","Ludo mobile game","web utility app","2D puzzle game"],
  ["performance","stability","build pipeline","state management","asset delivery"],
  [
   T("Sprint Bottleneck Fix","sprint-bottleneck-fix","Apply the Leverage Matrix to {A}. Identify the critical failure point for {B}, then outline a 60-minute time-contained sprint with a single measurable done-state.",["sprint","leverage"]),
   T("Inversion Analysis","inversion-analysis","Run an Inversion analysis on {A} focused on {B}. List the three most likely ways it fails, then redesign each failure point today with a concrete prevention step.",["inversion"]),
   T("Time Container Plan","time-container-plan","Define done for a 90-minute deep work session on {A} for {B}. Break it into three 30-minute blocks, each with an outcome, and a hard stop rule to prevent over-engineering.",["time-container","deep-work"]),
   T("Feedback Loop Metric","feedback-loop-metric","Apply the Feedback Loop principle to {A}. What exact signal should be measured in the first 7 days to prove {B} is holding, and what threshold triggers a fix?",["feedback-loop","metric"]),
   T("Operations Batching Schedule","operations-batching-schedule","Categorize all operations for {A} around {B} into a low-impact/low-effort batching schedule, so routine work never drains high-focus windows.",["batching","operations"]),
   T("Halfway Question Protocol","halfway-question-protocol","Halfway through a 2-hour sprint on {A}, create a Halfway Question protocol that forces a return to core {B} and drops visual polish until the core works.",["focus","protocol"]),
   T("Pre-Mortem","pre-mortem","Conduct a pre-mortem on {A} for {B}. Name the single mistake that would break it on mobile, how it would show up, and how to prevent it before shipping.",["pre-mortem"]),
   T("Upgrade Time Container","upgrade-time-container","Set a strict time container to upgrade {A} for {B}. Break it into 45-minute blocks with clearly defined outcomes to prevent scope creep, and list what is explicitly out of scope.",["upgrade"]),
   T("Diagnostic Test","diagnostic-test","Create a short diagnostic test to verify {B} is functioning correctly in {A} before committing the final build. Include pass/fail criteria for each check.",["diagnostic"]),
   T("End-of-Day Reset Routine","end-of-day-reset-routine","Design a 10-minute end-of-day routine for {A} that prepares {B} for tomorrow morning, removing all starting friction for the highest-leverage task.",["routine"]),
   T("Bug Triage Sprint","bug-triage-sprint","Design a 60-minute bug triage sprint for {A} focused on {B}. Sort bugs by user impact and fix cost, fix the top one, and park the rest with a reason.",["bug","triage"]),
   T("Build Pipeline Checklist","build-pipeline-checklist","Write a build pipeline checklist for {A} covering {B}. Include signing, version bump, asset check, and a final verification step before any release.",["build","checklist"]),
   T("Performance Audit","performance-audit","Run a performance audit on {A} for {B}. Measure the three slowest paths, name the likely cause for each, and propose the cheapest fix first.",["performance","audit"]),
   T("Code Review Sprint","code-review-sprint","Plan a code review sprint for {A} focused on {B}. Review for correctness first, then readability, then performance — with a done-state for each file reviewed.",["code-review"]),
   T("Asset Optimization Plan","asset-optimization-plan","Create an asset optimization plan for {A} around {B}. List assets by size, cut or compress the top offenders, and verify quality after each change.",["assets","optimization"]),
   T("State Management Refactor","state-management-refactor","Plan a focused refactor of {A} for {B}. Isolate one state flow, write its done-state, refactor it, and test it before touching the next flow.",["refactor","state"]),
   T("Release Verification Run","release-verification-run","Define a release verification run for {A} covering {B}. Include install, first-run, core loop, and edge-case checks, with a stop rule if any critical check fails.",["release","verification"]),
   T("Scope-Creep Guard","scope-creep-guard","Write a scope-creep guard for {A} on {B}. List what is in, what is out, and the exact question to ask before adding any new feature mid-sprint.",["scope"]),
   T("Morning Startup Friction Remover","morning-startup-friction-remover","Remove morning startup friction for {A} and {B}. List every manual step to start work, automate or document the top three, and time the new startup.",["friction","morning"]),
   T("Weekly Tech Review","weekly-tech-review","Design a 30-minute weekly tech review for {A} on {B}. Review what shipped, what broke, what was learned, and the single priority for next week.",["review","weekly"]),
  ],
 ),
 "creative-character-lock": (
  ["wellness drink","skincare brand","fashion brand","food brand","fitness brand","tech gadget","home product","coffee brand","pet product","travel brand"],
  ["TikTok","Instagram Reels","YouTube Shorts","Meta ads","TikTok Shop"],
  [
   T("3-Second Hook Script","three-second-hook-script","Script a 15-second {B} ad for {A}. Embed a pattern-interrupt in the first 3 seconds, one clear idea, and a single call to action — no clutter, no misleading claim.",["hook","ad"]),
   T("Character Lock Memory Palace","character-lock-memory-palace","Design a Memory Palace framework for {A} on {B} to keep character consistency across a 10-video campaign: prompt seeds, seed values and negative prompts, organised by scene.",["character-lock","memory-palace"]),
   T("Micro-Expression Ad Audit","micro-expression-ad-audit","Create an audit checklist for {A} on {B} to spot AI-face failures: eye movement, lip sync, hand detail and lighting consistency, with a fix for each failure.",["audit","faces"]),
   T("Visual Storyboard","visual-storyboard","Draft a visual storyboard for {A} on {B}. Six frames: hook, problem, product moment, proof, transformation, CTA — each with shot, on-screen text and sound note.",["storyboard"]),
   T("Soft Reject Creative Pitch","soft-reject-creative-pitch","Write an email rejecting a weak concept for {A} on {B} and pivoting to a stronger angle. Use a soft reject, give one reason, and propose the better concept with its hook.",["pitch","client"]),
   T("Workflow Leverage Review","workflow-leverage-review","Evaluate the workflow for {A} on {B}. Name the high-effort, low-impact tasks, and say for each: eliminate, simplify, or delay — with the time saved.",["workflow","leverage"]),
   T("Viral Format Reverse-Engineering","viral-format-reverse-engineering","Break down a competitor viral {B} ad for {A}. Deconstruct pacing, sound design and frame shifts, then build a superior template that keeps the structure but changes the angle.",["viral","analysis"]),
   T("Landing Page Copy","landing-page-copy","Write landing page copy for {A} on {B}. Headline, problem, proof, what is included, and CTA — with privacy or quality as the honest differentiator, no invented claims.",["copywriting","landing-page"]),
   T("Asset Pack Launch Plan","asset-pack-launch-plan","Create a launch plan for {A} on {B} as an asset or content pack. Define the theme, the first 5 pieces, pricing logic, and the feedback metric that decides the next pack.",["launch","assets"]),
   T("Engagement Loop Design","engagement-loop-design","Design an engagement loop for {A} on {B}. Use varied timing and genuine value — not spam — to bring users back, with a frequency cap and an opt-out.",["engagement","retention"]),
   T("Thumbnail Concept Set","thumbnail-concept-set","Generate 5 thumbnail concepts for {A} on {B}. Each: one idea, 2–5 words of text, dominant subject, and why it works at small size.",["thumbnail"]),
   T("Caption System","caption-system","Build a caption system for {A} on {B}. Rules for line length, keyword emphasis, timing and readability on mobile, with three example captions.",["captions"]),
   T("Sound Design Brief","sound-design-brief","Write a sound design brief for {A} on {B}. Music mood, sound effects per beat, silence moments, and what to avoid so the edit stays professional.",["sound","brief"]),
   T("Ad Angle Matrix","ad-angle-matrix","Build an ad angle matrix for {A} on {B}. Five angles — problem, proof, comparison, story, offer — each with a hook line and the audience it fits best.",["angles","matrix"]),
   T("Creative Testing Plan","creative-testing-plan","Plan a creative test for {A} on {B}. Test one variable at a time, define the sample and duration, and state in advance what result means keep, kill or iterate.",["testing"]),
   T("Brand Voice Guide","brand-voice-guide","Write a one-page brand voice guide for {A} on {B}. Tone, words to use, words to avoid, and three before/after examples of the same message.",["brand","voice"]),
   T("Content Series Outline","content-series-outline","Outline a 5-part content series for {A} on {B}. Each episode has a different hook and angle, the same core facts, and no repetition between episodes.",["series"]),
   T("Repurposing Package","repurposing-package","Turn one long video for {A} into a {B} package. Give duration, hook, caption style, title, on-screen text and CTA, adapted — not just cropped — for the platform.",["repurposing"]),
   T("Hook Testing Sprint","hook-testing-sprint","Design a hook testing sprint for {A} on {B}. Write 10 hooks, rank them by relevance and curiosity without clickbait, and test the top 3 first.",["hooks","testing"]),
   T("Visual Consistency Checklist","visual-consistency-checklist","Create a visual consistency checklist for {A} on {B}. Colour, type, character, lighting and framing — checked before publish, with a fix for each miss.",["consistency","checklist"]),
  ],
 ),
 "deep-work": (
  ["architecture planning","coding sprint","content planning","client pitching","game design","writing session","video editing","app development","marketing planning","research session"],
  ["60-minute block","90-minute block","2-hour block","4-hour morning block","10-minute reset"],
  [
   T("Focus Protocol","focus-protocol","Design a {B} for {A}. Integrate strategic silence for the environment, a single task, a phone-off rule, and a clear done-state at the end.",["focus","protocol"]),
   T("Define Done Sprint","define-done-sprint","For {A}, explicitly define done for a {B}. List the outcome, the file or artefact produced, and the check that proves it is finished.",["done-state"]),
   T("Energy Trap Interrupt","energy-trap-interrupt","Create a psychological interrupt for {A} during a {B}. When a low-impact, high-effort distraction appears, name it as an energy trap and return to the task with one sentence.",["energy","distraction"]),
   T("Pre-Meeting Grounding Routine","pre-meeting-grounding-routine","Translate slow movement, relaxed posture and steady eye contact into a pre-meeting routine before {A}, sized to fit a {B} window.",["meeting","routine"]),
   T("Frictionless Workspace Setup","frictionless-workspace-setup","Redesign the workspace for {A} so the first action in a {B} is the easiest possible action. List friction points, remove the top three, and time the new startup.",["workspace","friction"]),
   T("Cognitive Load Offloading Map","cognitive-load-offloading-map","Use a Memory Palace map for {A} across a {B}. Place each project in a room, with its next action, so context-switching does not require re-remembering everything.",["memory-palace","context-switch"]),
   T("No Perfection Manifesto","no-perfection-manifesto","Draft a personal manifesto for {A} based on Parkinson's Law for a {B}. State the rule: ship, measure feedback, iterate — and what perfectionism is not allowed to delay.",["manifesto"]),
   T("Daily Signal Challenge","daily-signal-challenge","Map a daily challenge for {A} in a {B} format. Name the one daily signal to measure, the target, and what to change if the signal misses two days in a row.",["challenge","signal"]),
   T("Reactivity Shield","reactivity-shield","Create a reactivity shield for {A} when a setback hits during a {B}. Pause, name the fact, diagnose the technical issue, and pick the next action — without frustration driving the response.",["resilience"]),
   T("Asymmetrical Effort Audit","asymmetrical-effort-audit","Audit {A} for a {B}. Where is effort spread evenly instead of concentrated on the leverage point that drives most of the result? Reallocate the next block accordingly.",["leverage","audit"]),
   T("Morning Startup Routine","morning-startup-routine","Build a morning startup routine for {A} that fits a {B}. First action, environment setup, and the single priority — no inbox first.",["morning","routine"]),
   T("Shutdown Ritual","shutdown-ritual","Design a shutdown ritual for {A} at the end of a {B}. Review what was done, capture tomorrow's first action, and close all loops so the day ends clean.",["shutdown","ritual"]),
   T("Distraction Audit","distraction-audit","Run a distraction audit on {A} over a {B}. Log every interruption, sort by source, and eliminate or batch the top two sources tomorrow.",["distraction","audit"]),
   T("Single-Task Sprint","single-task-sprint","Run a single-task sprint for {A} in a {B}. One task, no tabs, no multitasking, and a visible timer — with a break rule that does not break focus.",["single-task"]),
   T("Weekly Review Template","weekly-review-template","Create a weekly review template for {A} sized to a {B}. What shipped, what broke, what was learned, and the single priority for next week.",["review","weekly"]),
   T("Energy Management Plan","energy-management-plan","Build an energy management plan for {A} around a {B}. Match the hardest task to peak energy, admin to low energy, and protect a recovery slot.",["energy"]),
   T("Context-Switch Protocol","context-switch-protocol","Write a context-switch protocol for {A} between tasks in a {B}. Capture state, close the old task, start the new one with its first action — in under 2 minutes.",["context-switch"]),
   T("Procrastination Interrupter","procrastination-interrupter","Create a procrastination interrupter for {A} during a {B}. Shrink the task to a 2-minute first step, start it, and only then decide whether to continue.",["procrastination"]),
   T("Deep Work Environment Checklist","deep-work-environment-checklist","Write an environment checklist for {A} before a {B}. Notifications, desk, water, timer, and task — checked in 60 seconds before starting.",["environment","checklist"]),
   T("End-of-Week Reset","end-of-week-reset","Design an end-of-week reset for {A} in a {B}. Archive finished work, list open loops, and set Monday's first action so the weekend is actually off.",["reset","weekly"]),
  ],
 ),
 "ecosystem-scaling": (
  ["freefinancialcal.com","texttotable.site","NOIR // VORTEX 4K launcher","Orqa Ludo Grove","Call of Honour","Fab asset packs","Flutter arcade games","Astro web tools","ORQA Games publisher","B2B ad agency"],
  ["retention","monetization","growth","cross-promotion","trust"],
  [
   T("Retention Hook Flow","retention-hook-flow","Design a user flow for {A} focused on {B}. Use progress, anchoring and clear value — not dark patterns — to make users return and trust the product.",["retention","flow"]),
   T("Thought-Leadership Article","thought-leadership-article","Write a thought-leadership article for {A} on {B}. Make a clear argument, give evidence, and position the honest differentiator without calling competitors unsafe without proof.",["thought-leadership"]),
   T("Release Schedule Strategy","release-schedule-strategy","Plan a release schedule for {A} around {B}. Sequence launches so none get buried, with a feedback metric that decides the next release theme.",["release","strategy"]),
   T("Monetization Economy","monetization-economy","Design a monetization economy for {A} focused on {B}. Offer real free value, create optional paid removal of friction, and state prices and what is included plainly.",["monetization"]),
   T("Lore and Content Bible","lore-and-content-bible","Structure a lore/content bible for {A} around {B}. Use the method of Loci to organise factions, tiers and environments so new content stays consistent.",["lore","bible"]),
   T("Cross-Promotion Funnel","cross-promotion-funnel","Map a cross-promotion funnel for {A} focused on {B}. Move users between products without ad fatigue, with frequency caps and a clear benefit at each step.",["cross-promotion","funnel"]),
   T("Agentic Workflow","agentic-workflow","Design an automated workflow for {A} focused on {B}. List the agents, their inputs and outputs, human checkpoints, and what stops the workflow if quality drops.",["agents","automation"]),
   T("Publisher Identity Statement","publisher-identity-statement","Draft a brand positioning statement for {A} on {B}. Connect with the audience honestly while projecting competence, with no invented credentials.",["branding","positioning"]),
   T("Growth Loop Design","growth-loop-design","Design a growth loop for {A} focused on {B}. Name the shareable feature, who shares it, why they share it, and how the loop is measured.",["growth","loop"]),
   T("Ecosystem Synergy Map","ecosystem-synergy-map","Create a synergy map for {A} around {B}. Show how cash flow, audience and content feed each other, and where a break in one loop hurts the others.",["ecosystem","synergy"]),
   T("Onboarding Flow","onboarding-flow","Design an onboarding flow for {A} focused on {B}. First value in under 2 minutes, no forced signup unless needed, and a clear next step after onboarding.",["onboarding"]),
   T("Pricing Experiment","pricing-experiment","Plan a pricing experiment for {A} on {B}. Test one price change, define the metric, duration and sample, and state in advance what result means keep or revert.",["pricing","experiment"]),
   T("Referral Loop","referral-loop","Build a referral loop for {A} focused on {B}. Reward both sides, make sharing one tap, and track referral source so the loop can be improved.",["referral","loop"]),
   T("Content Flywheel","content-flywheel","Design a content flywheel for {A} around {B}. One core piece becomes five formats, each feeding the next, with a weekly cadence that is actually sustainable.",["content","flywheel"]),
   T("Trust Building Page","trust-building-page","Write a trust-building page for {A} on {B}. Real proof, real limits, privacy handling in plain language, and contact details — no vague claims.",["trust","page"]),
   T("Churn Reduction Plan","churn-reduction-plan","Create a churn reduction plan for {A} focused on {B}. Identify the top exit moments, fix the top one, and measure retention at 7 and 30 days.",["churn","retention"]),
   T("Partnership Funnel","partnership-funnel","Map a partnership funnel for {A} on {B}. Outreach, first joint test, success metric, and the decision point to scale or stop the partnership.",["partnership","funnel"]),
   T("Analytics Dashboard Brief","analytics-dashboard-brief","Write an analytics brief for {A} on {B}. Five metrics only, what each means, what action each triggers, and what is deliberately not tracked.",["analytics"]),
   T("Community Building Plan","community-building-plan","Plan community building for {A} around {B}. One gathering place, one weekly ritual, and one way members help each other — without forced engagement.",["community"]),
   T("Scale Without Burnout Plan","scale-without-burnout-plan","Plan scaling {A} for {B} without burnout. Cap weekly output, batch routine work, and protect one deep-work block per day for the core product.",["scaling","sustainability"]),
  ],
 ),
}

def main():
    d = json.loads(DATA.read_text())
    existing_ids = {x["id"] for x in d["prompts"]}
    added = 0
    for cat, (alist, blist, templates) in CATEGORIES.items():
        assert len(templates) == 20, (cat, len(templates))
        assert len(alist) == 10 and len(blist) == 5
        n = 0
        for ti, tpl in enumerate(templates):
            for ai, A in enumerate(alist):
                for bi, B in enumerate(blist):
                    n += 1
                    pid = f"bulk-{cat[:4]}-{ti+1:02d}-{ai+1:02d}-{bi+1:02d}"
                    # shorter, stable id: bulk-b2b-01-01-01 etc — keep cat prefix readable
                    prefix = {"b2b-frame-control":"b2b","genius-os-tech":"tech","creative-character-lock":"cre","deep-work":"dw","ecosystem-scaling":"eco"}[cat]
                    pid = f"bulk-{prefix}-{ti+1:02d}-{ai+1:02d}-{bi+1:02d}"
                    if pid in existing_ids:
                        continue
                    title = f"{tpl['title']} — {A} / {B}"
                    slug_ = f"{tpl['slug_base']}-{slug(A)}-{slug(B)}"
                    prompt = tpl["prompt"].replace("{A}", A).replace("{B}", B)
                    summ = prompt.split(". ")[0].strip()
                    if not summ.endswith("."): summ += "."
                    if len(summ) > 160: summ = summ[:157] + "..."
                    d["prompts"].append({
                        "id": pid, "slug": slug_, "title": title, "category": cat,
                        "summary": summ, "prompt": prompt, "variables": [], "tags": tpl["tags"] + ["bulk"],
                    })
                    existing_ids.add(pid)
                    added += 1
        print(cat, "generated", n)
    d["version"] = "1.3.0"
    DATA.write_text(json.dumps(d, indent=2) + "\n")
    print(f"added={added} total={len(d['prompts'])}")
    # uniqueness checks
    slugs = [x["slug"] for x in d["prompts"]]
    prompts = [x["prompt"] for x in d["prompts"]]
    assert len(slugs) == len(set(slugs)), "duplicate slugs"
    assert len(prompts) == len(set(prompts)), "duplicate prompts"
    print("uniqueness OK: slugs and prompts all distinct")

if __name__ == "__main__":
    main()
