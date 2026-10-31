# Launch Prompt Press yourself — Cloudflare Pages

Muse does NOT deploy this — you do, in Cloudflare. Everything else is ready.

## What is ready

- Astro static site, 15,085 prompts, paginated homepage (24 at a time)
- Per-prompt pages, search + category filter, copy buttons
- Downloads: JSON / CSV / Markdown / TXT + one all-data ZIP
- SEO: sitemap, robots.txt, 404 page, Open Graph tags
- Repo: https://github.com/goalxpro26-debug/prompt-library

## Deploy in Cloudflare Pages (5 minutes)

1. Cloudflare Dashboard → Pages → Create application → Pages → Connect to Git
2. Select repo: `goalxpro26-debug/prompt-library`, branch: `main`
3. Framework preset: Astro (or leave blank and set manually below)
4. Build command: `npm run build`
5. Build output directory: `dist`
6. Save and Deploy — first deploy takes a few minutes (15,086 pages)

Every future push to `main` redeploys automatically. No Wrangler login
needed for this path.

## After your first deploy (optional, recommended)

1. Note your `*.pages.dev` URL from Cloudflare.
2. If you want the sitemap to use that exact URL, rebuild once with:
   ```
   SITE_URL=https://YOUR-SITE.pages.dev npm run build
   ```
   Then push — the sitemap regenerates. The site works fine without this step.
3. Optional custom domain: Pages → Custom domains → Set up a custom domain,
   then follow Cloudflare's DNS instructions for your domain.

## If a build fails

- Check the Cloudflare build log for the failing step first.
- Local check that must pass before re-deploying:
  ```
  npm install
  npm run build
  ```
- Never hand-edit `public/downloads/*` or `public/sitemap.xml` — both are
  generated from `src/data/prompts.json` on every build.

## Single download — all data at once

One ZIP with everything, in the repo:
`public/downloads/prompt-press-all-data.zip`
(contains prompts.json, prompts.csv, prompts.md, prompts.txt)

Direct link (after this push):
https://github.com/goalxpro26-debug/prompt-library/raw/main/public/downloads/prompt-press-all-data.zip
