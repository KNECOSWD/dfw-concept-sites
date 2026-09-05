# CareMaster Building Services — design brief

**Live:** http://www.caremaster.biz/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/caremaster-building/  
**Vibe match: 3/10** — Rebuild invented teal `#2a9d8f` “clean SaaS.” Live Freemona/NationConnect site is **gray corporate + red `#E80000` + gold `#EDDB8C`** accents.

## Color tokens (LIVE)
| Token | Hex |
| --- | --- |
| `--brand` | `#383838` / `#1a2332` dark charcoal for header |
| `--brand-2` / accent | `#E80000` |
| Highlight | `#EDDB8C` (gold bar/headings sparingly) |
| `--ink` | `#383838` |
| `--muted` | `#686868` |
| `--bg` | `#f0f0f0` / `#f7f7f7` |
| `--surface` | `#ffffff` |
| `--hero-ink` | `#ffffff` |
| `--font-display` | `Open Sans, Source Sans Pro, sans-serif` |

## Layout intent
- Classic commercial janitorial brochure: horizontal text nav (Home About Services Commitment…), red email/phone strip, formal prose.
- Not trendy teal startup.
- Keep `logo-2.jpg` only.

## Eng change list
1. `theme.css`: remove teal `#2a9d8f`; set accent `#E80000`; optional gold `#EDDB8C` for eyebrow/rules.
2. Header dark charcoal; CTA red.
3. Section heads: charcoal, not teal underlines.
4. Softer corporate density — longer prose blocks ok (match live About/Commitment).
5. Fonts: Open/Source Sans — drop playful patterns.

## Keep
- Since 1982, Richard/John Lee, PO Box, phones, service list; no reviews invented.

## 508 notes
- Red `#E80000` on white for small text may fail — use for buttons/large links; body links charcoal with underline.
- Gold on white fails for text — decorative only.
- Old live tables/layout had weak semantics — rebuild should keep real headings/lists (improvement).
- Contact form labels; don’t rely on red alone for errors.
