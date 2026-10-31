# How to add prompts — send raw data, get back categorised prompts

This site is built so you never have to write the final prompt yourself.
You send raw material, Muse turns it into a clean prompt, picks its
category, and adds it to `src/data/prompts.json`. The download files
regenerate from that one file, so the site and the downloads never drift.

## 1. Send Muse any of these

- A pasted note, voice-note transcript, or rough idea ("make reels from
  long videos, but keep my voice natural")
- A screenshot, link, or document with the workflow in it
- A list: "I need prompts for X, Y, Z"
- An existing prompt that needs tightening or splitting in two

No format required. If you do want a template, copy this:

```
Title (or working idea):
What it should do:
Who it is for:
What to avoid:
Example input / output (if you have one):
Category guess (optional — Muse will correct it):
```

## 2. What Muse does with it

1. Rewrites it as one copy-ready prompt, in the same voice as the
   library (direct, specific, no filler).
2. Pulls out the `[VARIABLES]` — the bits you fill in per job.
3. Writes a one-line summary, tags, and format (if it has one, e.g.
   1080 × 1350).
4. Picks a category. Existing categories: Design & Graphics,
   Digital Products, Video Editing. New categories are created only
   when a batch genuinely doesn't fit — not one prompt per category.
5. Adds it to `src/data/prompts.json`, runs `npm run data:build`,
   rebuilds, and pushes to GitHub so Cloudflare redeploys.

## 3. Rules that keep the library clean

- One prompt = one job. If a note contains three jobs, it becomes
  three prompts.
- No invented claims, stats, or guarantees in a prompt.
- Variables are always `[BRACKETED]` and listed separately.
- Duplicates are merged, not stacked.

## 4. If you edit by hand

Edit ONLY `src/data/prompts.json`, then run:

```
npm run data:build
npm run build
```

Never hand-edit `public/downloads/*` — they are generated.
