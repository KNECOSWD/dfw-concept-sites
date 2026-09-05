# Forum Terrace Church of Christ — design brief

**Live:** http://forumterrace.org/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/forum-terrace-church/  
**Vibe match: 7/10** — Brand blue `#1d597c` matches. Rebuild adds warm parchment/Georgia that is slightly more “brochure” than live Hestia WordPress (cleaner blue/white), but direction is acceptable with polish — not a rebrand.

## Color tokens (LIVE)
| Token | Hex |
| --- | --- |
| `--brand` | `#1d597c` (keep) |
| `--brand-2` | `#4e86bf` / light blue accents |
| `--accent` | `#8b5a2b` optional; live is mostly blue — prefer blue CTAs over brown |
| `--ink` | `#363537` |
| `--muted` | `#6b5348` → better `#6b6b6b` |
| `--bg` | `#ffffff` / `#eeeeee` |
| `--surface` | `#ffffff` |
| `--hero-ink` | `#ffffff` |
| `--font-display` | `Arial, Helvetica, sans-serif` (live) — Georgia ok if softened |

## Layout intent
- Congregation WordPress: logo banner, blue nav, hero slider imagery (BoyAndBible etc. if licensed/published assets exist), service times, resource links out to live HTTP paths.
- Warm cream rebuild is fine if blue remains dominant.
- Keep cropped FTCoC logo.
- Member directory stays gated/out.

## Eng change list
1. Keep `--brand #1d597c`; make primary buttons blue (not brown `#8b5a2b`).
2. Reduce parchment if it fights logo blue — whiter `--bg`.
3. Nav: simple blue active underline.
4. Resources: clearly external links (open live tracts/sermons) with visible “opens congregation site” affordance.
5. Typography: consider Arial/system for closer match; Georgia only for headings.

## Keep
- Times, address, Dan Vess phone, resource URLs, no email invent.

## 508 notes
- Blue `#1d597c` on white: verify links ≥4.5:1.
- Hero slider images need `alt` describing content (not empty if informative).
- External resource links: indicate new context if `target=_blank` (and `rel`).
- Skip link; focus on blue header.
