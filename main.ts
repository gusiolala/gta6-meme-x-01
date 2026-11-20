// gta6-meme-x-01 entry (Node 22, standard library only).
//
// The entry is the X post itself: an agent-made GTA 6 meme (meme.png) posted
// from a public X account with make.fun and the entrant's play code in its
// text. This program only copies POST.json from the repository root to
// /output/POST.json, where the house gate reads it. Nothing this program
// writes about the post is judged: the house reads the post from X (its
// first picture and its text) and hands that to the judge.
//
// POST.json as shipped here holds a placeholder address, so the gate refuses
// it as it stands (valid 0). Replace it with the real post's address
// ({"url": "https://x.com/<handle>/status/<id>"}) before submitting.
//
// The program is deterministic and network-free: it only reads POST.json
// from the repository and writes the same bytes to /output, so its two
// grader runs produce identical output.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(join(BOT_DIR, 'POST.json'), join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
