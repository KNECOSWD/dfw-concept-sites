# B&B Complete Auto Repair — design brief

**Live:** https://bbcompleteautorepair.com/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/bb-complete-auto/  
**Vibe match: 6/10** — Black + red `#c1121f` is plausible for auto. Live WordPress also shows utility blues (`#3279BB`) and bright reds in theme CSS — verify visually; avoid making it “luxury black/red agency” if live is simpler shop WP.

## Color tokens (LIVE-informed)
| Token | Hex |
| --- | --- |
| `--brand` | `#1a1a1a` / `#202020` |
| `--brand-2` / accent | `#c1121f` or live `#ee0101` / `#cf2e2e` family — pick one red and stick |
| Support | `#3279BB` for secondary links if present on live header |
| `--ink` | `#1b1b1b` |
| `--muted` | `#5c5854` |
| `--bg` | `#f1eeea` / `#eeeeee` |
| `--surface` | `#fffaf6` / `#ffffff` |
| `--hero-ink` | `#ffffff` |
| `--font-display` | sans-serif (Segoe/system) |

## Layout intent
- Auto shop: strong Call phone, services list, areas, FAQ; Elfsight reviews widget only; empty gallery stays empty.
- Header with logo + red CTA Call.
- Keep license CO16-0388 in copy.

## Eng change list
1. Confirm red against live screenshot — unify `--accent` to exact live CTA red.
2. Hero: darker photo/black wash + red CTA; avoid fancy diagonal pattern if live is flat.
3. Service cards denser, mechanic-practical (not boutique).
4. Ensure Elfsight script only for reviews — no fake stars in HTML.
5. Areas/FAQ pages: match live information architecture.

## Keep
- No invented reviews/photos; real services and contact.

## 508 notes
- Red on black: check contrast for buttons; prefer white text on `#c1121f`.
- Red links on white: may need darker red `#a50e18` for small text.
- Map/embed iframes: title attribute.
- Form labels; focus visible on dark header (light ring).
