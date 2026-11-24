// One-Line Roast: The Gadget You Use Every Day.
// Writes a single original roast line (1-200 characters) to /output/entry.txt.

import { mkdirSync, writeFileSync } from "node:fs";

const ROAST =
  "My microwave beeps five times when dinner's done — one to inform me, four more to imply I'm deaf, lazy, or dead in the next room.";

const text = ROAST.trim();

if (text.length < 1 || text.length > 200) {
  throw new Error(`roast must be 1-200 characters, got ${text.length}`);
}

mkdirSync("/output", { recursive: true });
writeFileSync("/output/entry.txt", text, "utf8");
console.log(`wrote /output/entry.txt (${text.length} chars)`);
