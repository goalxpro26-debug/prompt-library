#!/usr/bin/env python3
"""Generate 5000 Marketing + 5000 Graphic Designing prompts, reproducibly.

Method: 2 categories x 25 templates x 20 slot-A x 10 slot-B = 5000 per category.
Each (template, A, B) triple is unique. Curated prompts untouched; bulk ids bulk2-*.
Idempotent: python3 scripts/generate-bulk-2.py
"""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "src/data/prompts.json"
def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:80]
def T(title, slug_base, prompt, tags):
    return {"title": title, "slug_base": slug_base, "prompt": prompt, "tags": tags}

CATEGORIES = {
 "marketing": (
  ["DTC brands","SaaS companies","Shopify stores","skincare brands","fitness brands","fashion brands","food brands","tech startups","marketing agencies","local businesses","coaches","content creators","e-commerce brands","B2B software companies","health brands","beauty brands","home goods brands","pet brands","travel brands","education brands"],
  ["Instagram","TikTok","LinkedIn","Email","Meta ads","Google ads","SEO","Content marketing","Influencer marketing","Retention marketing"],
  [
   T("Campaign Plan","campaign-plan","Create a 30-day campaign plan for {A} on {B}. Define the goal, audience, core message, content pillars, posting cadence, and the metric that decides what to scale or kill.",["campaign","plan"]),
   T("Funnel Map","funnel-map","Map a full funnel for {A} on {B}. Awareness, consideration, conversion and retention — with one offer, one CTA and one metric per stage.",["funnel"]),
   T("Ad Copy Set","ad-copy-set","Write 5 ad copy variations for {A} on {B}. Each with a different hook — problem, proof, story, comparison, offer — under 40 words, with a clear CTA and no invented claims.",["ad-copy"]),
   T("Email Sequence","email-sequence","Write a 4-email sequence for {A} on {B}. Welcome, value, proof, offer — each under 150 words, one idea per email, and a clean unsubscribe-friendly close.",["email","sequence"]),
   T("Social Content Calendar","social-content-calendar","Build a 2-week content calendar for {A} on {B}. Daily idea, format, hook and CTA, balanced across education, proof and promotion — no more than 20% direct selling.",["calendar","content"]),
   T("Launch Plan","launch-plan","Plan a product launch for {A} on {B}. Pre-launch tease, launch week, post-launch follow-up, with deadlines, assets needed and success metrics.",["launch"]),
   T("SEO Content Plan","seo-content-plan","Create an SEO content plan for {A} on {B}. 10 topics by search intent, one primary keyword angle per topic, and the internal link that each piece should point to.",["seo","content"]),
   T("Lead Magnet Idea","lead-magnet-idea","Design a lead magnet for {A} on {B}. One specific problem, one quick win, format, title, and the follow-up email that delivers it and invites the next step.",["lead-magnet"]),
   T("Retargeting Plan","retargeting-plan","Build a retargeting plan for {A} on {B}. Segment by behaviour — viewed, cart, past buyer — with a different message and frequency cap for each segment.",["retargeting"]),
   T("Brand Messaging Guide","brand-messaging-guide","Write a one-page brand messaging guide for {A} on {B}. Audience, problem, promise, proof, tone, and three messages to use and three to avoid.",["branding","messaging"]),
   T("Influencer Outreach Script","influencer-outreach-script","Write an influencer outreach script for {A} on {B}. Personalised opener, clear deliverable, fair compensation note, and a no-pressure close.",["influencer","outreach"]),
   T("Customer Journey Map","customer-journey-map","Map the customer journey for {A} on {B}. Touchpoints, emotions, friction points and fixes — from first discovery to repeat purchase.",["journey"]),
   T("Pricing Promotion Plan","pricing-promotion-plan","Plan a promotion for {A} on {B} without training customers to wait for discounts. Offer structure, duration, urgency mechanism and margin guardrails.",["promotion","pricing"]),
   T("Testimonial Collection Plan","testimonial-collection-plan","Create a testimonial collection plan for {A} on {B}. When to ask, what to ask, how to get permission, and how to turn one testimonial into three formats.",["testimonial"]),
   T("Community Building Plan","community-building-plan","Plan community building for {A} on {B}. One gathering place, one weekly ritual, and one way members help each other — without forced engagement.",["community"]),
   T("Analytics Review Template","analytics-review-template","Create a weekly analytics review template for {A} on {B}. Five metrics only, what each means, what action each triggers, and what is deliberately not tracked.",["analytics","review"]),
   T("Competitor Analysis Brief","competitor-analysis-brief","Write a competitor analysis brief for {A} on {B}. Top 3 competitors, their positioning, content gaps, and one angle we can own that they are not using.",["competitor","analysis"]),
   T("Content Repurposing Plan","content-repurposing-plan","Turn one core piece for {A} into a {B} repurposing plan. Five formats from one idea, each adapted — not just cropped — for the channel.",["repurposing"]),
   T("Seasonal Campaign Idea","seasonal-campaign-idea","Generate a seasonal campaign idea for {A} on {B}. Theme, hook, offer, timeline and the one metric that proves it worked.",["seasonal","campaign"]),
   T("Referral Program Design","referral-program-design","Design a referral program for {A} on {B}. Reward both sides, make sharing one tap, and track source so the program can be improved.",["referral"]),
   T("Onboarding Email Flow","onboarding-email-flow","Design an onboarding email flow for {A} on {B}. First value in the first email, no forced upsell, and a clear next step after each email.",["onboarding","email"]),
   T("Viral Hook Testing Plan","viral-hook-testing-plan","Plan a hook testing sprint for {A} on {B}. Ten hooks, ranked by relevance and curiosity without clickbait, test the top three first with a clear keep/kill rule.",["hooks","testing"]),
   T("Brand Story Framework","brand-story-framework","Write a brand story framework for {A} on {B}. Hero, problem, guide, plan, success and failure stakes — in under 200 words, in the brand's own voice.",["story","branding"]),
   T("Paid Ads Testing Plan","paid-ads-testing-plan","Plan a paid ads test for {A} on {B}. One variable at a time, budget, duration, audience size, and the result that means scale, iterate or stop.",["paid-ads","testing"]),
   T("Retention Email Series","retention-email-series","Write a retention email series for {A} on {B}. Win-back, value reminder and feedback request — timed to behaviour, not just calendar, with an easy opt-out.",["retention","email"]),
  ],
 ),
 "graphic-designing": (
  ["social media graphic","poster","flyer","logo concept","packaging design","banner ad","infographic","brochure","business card","menu design","invitation card","book cover","magazine layout","billboard","email header","presentation slide","product label","t-shirt design","website hero graphic","event ticket"],
  ["minimalist","luxury","bold editorial","playful","vintage","futuristic","organic","modern premium","retro","clean corporate"],
  [
   T("Layout Design","layout-design","Design a {A} in {B} style. Use a strong hierarchy, one dominant element, balanced spacing and a clear focal point. State the grid, margins and where the eye should go first, second and third.",["layout"]),
   T("Colour Palette","colour-palette","Create a colour palette for a {A} in {B} style. Five colours with roles — primary, secondary, accent, background, text — plus contrast notes for readability on mobile.",["colour","palette"]),
   T("Typography System","typography-system","Design a typography system for a {A} in {B} style. Two complementary type styles maximum, sizes for headline, subhead and body, and rules for spacing and alignment.",["typography"]),
   T("Composition Brief","composition-brief","Write a composition brief for a {A} in {B} style. Subject placement, negative space, depth and balance — and what to remove if the design feels crowded.",["composition"]),
   T("Brand Identity Concept","brand-identity-concept","Create a brand identity concept for a {A} in {B} style. Logo direction, colour, type and one usage rule — consistent enough to recognise across formats.",["brand","identity"]),
   T("Social Graphic Template","social-graphic-template","Build a reusable template for a {A} in {B} style. Fixed grid, text safe areas, and swap points for headline, image and CTA — so future versions stay consistent.",["template","social"]),
   T("Print-Ready Checklist","print-ready-checklist","Write a print-ready checklist for a {A} in {B} style. Size, bleed, resolution, colour mode, fonts outlined, and a final proof check before sending to print.",["print","checklist"]),
   T("Visual Hierarchy Audit","visual-hierarchy-audit","Audit a {A} in {B} style for visual hierarchy. Rank every element by attention, name what competes with the headline, and propose one fix per competing element.",["audit","hierarchy"]),
   T("Mood Board Brief","mood-board-brief","Create a mood board brief for a {A} in {B} style. Five reference directions — colour, texture, type, imagery, mood — each with why it fits and what to avoid copying.",["mood-board"]),
   T("Icon Set Direction","icon-set-direction","Design an icon set direction for a {A} in {B} style. Stroke, corner, size and spacing rules, plus three example icons that prove the system works.",["icons"]),
   T("Poster Concept Set","poster-concept-set","Generate three poster concepts for a {A} in {B} style. Each: one idea, headline placement, dominant visual, and why it works at a glance from 3 metres.",["poster","concept"]),
   T("Packaging Layout","packaging-layout","Design a packaging layout for a {A} in {B} style. Front hierarchy, mandatory information placement, and how the design reads on a shelf at small size.",["packaging"]),
   T("Banner Ad Variations","banner-ad-variations","Create three banner ad variations for a {A} in {B} style. Same message, different hook, layout and CTA placement — with the size and safe-area rules for each.",["banner","ad"]),
   T("Infographic Structure","infographic-structure","Structure an infographic for a {A} in {B} style. One title, numbered sections, simple visuals, and a 30-second scan test — no invented statistics.",["infographic"]),
   T("Presentation Design System","presentation-design-system","Build a presentation design system for a {A} in {B} style. Cover, content and closing slides, with text limits per slide and image rules.",["presentation"]),
   T("Logo Refinement Brief","logo-refinement-brief","Write a logo refinement brief for a {A} in {B} style. What works, what fails at small size, and three precise changes — not a full redesign unless needed.",["logo"]),
   T("Colour Accessibility Check","colour-accessibility-check","Run a colour accessibility check for a {A} in {B} style. Contrast ratios for text, colour-blind safe combinations, and fixes that keep the style intact.",["accessibility","colour"]),
   T("Grid System Design","grid-system-design","Design a grid system for a {A} in {B} style. Columns, gutters, breakpoints and alignment rules, with one example layout built on the grid.",["grid"]),
   T("Photography Direction","photography-direction","Write a photography direction brief for a {A} in {B} style. Lighting, framing, colour grade and subject direction — so photos match the design, not fight it.",["photography"]),
   T("Illustration Style Guide","illustration-style-guide","Create an illustration style guide for a {A} in {B} style. Line, shape, colour and texture rules, plus three do and three don't examples.",["illustration","style"]),
   T("Social Carousel System","social-carousel-system","Design a social carousel system for a {A} in {B} style. Cover slide, content slides and closing slide, with a consistent header, footer and swipe cue.",["carousel","social"]),
   T("Brand Guidelines Page","brand-guidelines-page","Write a one-page brand guidelines summary for a {A} in {B} style. Logo, colour, type, imagery and voice — enough for a new designer to stay on-brand.",["brand","guidelines"]),
   T("Design Critique Framework","design-critique-framework","Create a design critique framework for a {A} in {B} style. Five questions — clarity, hierarchy, consistency, readability, emotion — with a score and fix for each.",["critique"]),
   T("Rebrand Concept","rebrand-concept","Develop a rebrand concept for a {A} in {B} style. What to keep, what to change, why, and how the transition rolls out without confusing existing customers.",["rebrand"]),
   T("Ad Creative Brief","ad-creative-brief","Write an ad creative brief for a {A} in {B} style. Audience, single message, mandatory elements, format, and the one action the viewer should take.",["ad","brief"]),
  ],
 ),
}
def main():
    d = json.loads(DATA.read_text())
    # add categories if missing
    labels = {"marketing": ("Marketing", "Campaigns, funnels, copy, email, social and growth — by audience and channel."),
              "graphic-designing": ("Graphic Designing", "Layout, colour, type and composition — by project type and visual style.")}
    existing = {c["id"] for c in d["categories"]}
    for cid, (label, desc) in labels.items():
        if cid not in existing:
            d["categories"].append({"id": cid, "label": label, "description": desc})
    existing_ids = {x["id"] for x in d["prompts"]}
    added = 0
    for cat, (alist, blist, templates) in CATEGORIES.items():
        assert len(templates) == 25, (cat, len(templates))
        assert len(alist) == 20 and len(blist) == 10
        prefix = {"marketing": "mkt", "graphic-designing": "gfx"}[cat]
        n = 0
        for ti, tpl in enumerate(templates):
            for ai, A in enumerate(alist):
                for bi, B in enumerate(blist):
                    n += 1
                    pid = f"bulk2-{prefix}-{ti+1:02d}-{ai+1:02d}-{bi+1:02d}"
                    if pid in existing_ids: continue
                    title = f"{tpl['title']} — {A} / {B}"
                    slug_ = f"{tpl['slug_base']}-{slug(A)}-{slug(B)}"
                    prompt = tpl["prompt"].replace("{A}", A).replace("{B}", B)
                    summ = prompt.split(". ")[0].strip()
                    if not summ.endswith("."): summ += "."
                    if len(summ) > 160: summ = summ[:157] + "..."
                    d["prompts"].append({"id": pid, "slug": slug_, "title": title, "category": cat, "summary": summ, "prompt": prompt, "variables": [], "tags": tpl["tags"] + ["bulk"]})
                    existing_ids.add(pid); added += 1
        print(cat, "generated", n)
    d["version"] = "1.4.0"
    DATA.write_text(json.dumps(d, indent=2) + "\n")
    print(f"added={added} total={len(d['prompts'])}")
    slugs = [x["slug"] for x in d["prompts"]]; prompts = [x["prompt"] for x in d["prompts"]]
    assert len(slugs) == len(set(slugs)), "duplicate slugs"
    assert len(prompts) == len(set(prompts)), "duplicate prompts"
    print("uniqueness OK")
if __name__ == "__main__":
    main()
