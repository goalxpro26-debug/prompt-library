import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, '..');
const data = JSON.parse(readFileSync(join(root, 'src/data/prompts.json'), 'utf8'));

const outDir = join(root, 'public/downloads');
mkdirSync(outDir, { recursive: true });

// JSON — exact source of truth, pretty-printed
writeFileSync(join(outDir, 'prompts.json'), JSON.stringify(data, null, 2) + '\n');

// CSV — one row per prompt
const esc = (v) => `"${String(v ?? '').replaceAll('"', '""')}"`;
const rows = [
  ['id', 'slug', 'title', 'category', 'summary', 'format', 'variables', 'tags', 'prompt'].join(','),
  ...data.prompts.map((p) => [
    p.id, p.slug, p.title, p.category, p.summary, p.format ?? '',
    (p.variables ?? []).join('; '), (p.tags ?? []).join('; '), p.prompt,
  ].map(esc).join(',')),
];
writeFileSync(join(outDir, 'prompts.csv'), rows.join('\n') + '\n');

// Markdown — readable, copy-friendly, grouped by category
const catLabel = Object.fromEntries(data.categories.map((c) => [c.id, c.label]));
let md = `# Prompt Library\n\n${data.prompts.length} prompts. Source of truth: \`src/data/prompts.json\`.\n\n`;
for (const cat of data.categories) {
  md += `## ${cat.label}\n\n${cat.description}\n\n`;
  for (const p of data.prompts.filter((x) => x.category === cat.id)) {
    md += `### ${p.title}\n\n${p.summary}\n\n`;
    if (p.format) md += `Format: ${p.format}\n\n`;
    if (p.variables?.length) md += `Fill in: ${p.variables.map((v) => `[${v}]`).join(', ')}\n\n`;
    md += `${p.prompt}\n\n---\n\n`;
  }
}
writeFileSync(join(outDir, 'prompts.md'), md);

// Plain text — one prompt per block, for pasting anywhere
const txt = data.prompts.map((p) => `${p.title} [${catLabel[p.category]}]\n${p.prompt}`).join('\n\n---\n\n');
writeFileSync(join(outDir, 'prompts.txt'), txt + '\n');

console.log(`Built downloads: ${data.prompts.length} prompts → public/downloads/ (json, csv, md, txt)`);
