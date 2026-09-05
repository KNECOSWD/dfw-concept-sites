# Hughes Mechanical — design brief

**Live:** https://www.hughescontractorsllc.com/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/hughes-mechanical/  
**Vibe match: 5/10** — Rebuild guessed coral `#e76f51` + navy `#1d3557`. Live Wix is **navy `#112F5B` + orange `#D64000` + yellow `#FDF102`** (trade contractor punch). Wrong domain was hughes-mech-elect.com — do not use.

## Color tokens (LIVE)
| Token | Hex |
| --- | --- |
| `--brand` | `#112F5B` |
| `--brand-2` | `#D64000` |
| `--accent` | `#FDF102` (use for highlights/badges sparingly; text on yellow needs dark ink) |
| `--ink` | `#152033` |
| `--muted` | `#5f6360` / `#8d8d8d` |
| `--bg` | `#f2eae7` / `#eef2f6` |
| `--surface` | `#ffffff` |
| `--hero-ink` | `#ffffff` |
| `--font-display` | `Arial, Helvetica, sans-serif` (Wix default — keep clean sans) |

## Layout intent
- Wix Studio contractor: bold navy header, orange CTAs, yellow accents, team/services blocks.
- Single-page-ish energy with clear Call / Contact.
- Keep published Wix logo/bug assets only.

## Eng change list
1. `theme.css`: `--brand` `#112F5B`; `--brand-2`/`btn-primary` `#D64000`; add `--accent` `#FDF102` for chips/highlights only.
2. Remove coral `#e76f51`.
3. Header: navy bar, white/light nav, orange Call button.
4. Hero: photo or navy with orange CTA; yellow only as accent bar/chip (never yellow body text).
5. Fonts: Segoe/Arial sans — drop heavy “Semibold display” if it feels off-brand.
6. Confirm content still matches hughescontractorsllc.com (phone 817-461-9241, Dodson Lake address).

## Keep
- HVAC+electrical+lighting+refrigeration scope; team names as published; no fake reviews.

## 508 notes
- Yellow `#FDF102` on white fails — never use for text; if used as button bg, pair with `#112F5B` text and verify contrast.
- Orange `#D64000` + white: verify ≥4.5:1.
- Wix live may lack skip link — rebuild keep skip link (improvement ok).
- Decorative grid hero pattern: ensure it doesn’t reduce text contrast.
