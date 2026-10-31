import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, '..');
const data = JSON.parse(readFileSync(join(root, 'src/data/prompts.json'), 'utf8'));

// Set SITE_URL when you know your live domain, e.g.
// SITE_URL=https://prompt-press.pages.dev npm run build
// Default is a placeholder — update it after you connect Cloudflare Pages,
// then rebuild. The site works without it; only the sitemap URLs change.
const base = (process.env.SITE_URL || 'https://prompt-press.pages.dev').replace(/\/$/, '');
const esc = (s) => s.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');

const urls = ['', ...data.prompts.map((p) => `/prompts/${p.slug}/`)];
const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map((u) => `  <url><loc>${esc(base + u)}</loc></url>`).join('\n')}\n</urlset>\n`;
writeFileSync(join(root, 'public/sitemap.xml'), xml);
console.log(`Built sitemap: ${urls.length} URLs → public/sitemap.xml (base: ${base})`);
