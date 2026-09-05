# Victory Pest Control — design brief

**Live:** https://www.victorypestcontrol.com/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/victory-pest-control/  
**Vibe match: 3/10** — Rebuild is olive/gold “outdoorsy.” Live Hibu brand tokens are **navy `#001A54` + gold `#D4AF37` / yellow `#F7D000`** (plus dark teal `#11414B` in home CSS). Green forest palette invents a different brand.

## Color tokens (LIVE)
| Token | Hex |
| --- | --- |
| `--brand` | `#001A54` |
| `--brand-2` | `#D4AF37` |
| `--accent` | `#F7D000` |
| `--ink` | `#2e2e2d` / `#333333` |
| `--muted` | `#888787` |
| `--bg` | `#f5f5f5` |
| `--surface` | `#ffffff` |
| `--hero-ink` | `#ffffff` |
| Secondary bar | `#11414B` (optional dark teal sections) |
| `--font-display` | `Righteous, Muli, system-ui, sans-serif` (logo-adjacent); body Muli/sans |

## Layout intent
- Pest-control marketing: bold navy + gold/yellow CTAs, specials, wildlife + pest services.
- Top nav; phone dual lines; 24h messaging.
- Keep VPC logo asset — not Hibu gen-logo.
- Do not copy live “Lorem Ipsum” / placeholder tokens.

## Eng change list
1. Replace green `--brand/#2d4a22` with navy `#001A54`.
2. Gold/yellow accents as above; primary CTA yellow or gold on navy (check contrast) or navy button with gold outline.
3. Drop Georgia “estate” feel → sans (Muli/system).
4. Hero: navy field + gold accent stripe; reduce diagonal green pattern.
5. Specials page: yellow price callouts on navy cards.
6. Reviews: only the three published names already in build.

## Keep
- Owner John Gaines, phones, Red Oak address, published specials copy cleaned of lorem.

## 508 notes
- Yellow `#F7D000` on white fails for text; use on navy only with dark text, or large UI.
- Gold `#D4AF37` on navy: verify link/button contrast.
- Dual phone links as real `tel:` with visible text.
- Form labels; focus visible on navy backgrounds (light focus ring).
