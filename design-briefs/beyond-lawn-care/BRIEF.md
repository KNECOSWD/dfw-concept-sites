# Beyond Lawn Care — design brief

**Live:** https://www.beyondlawncares.com/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/beyond-lawn-care/  
**Vibe match: 5/10** — Orange accent is in the ballpark, but rebuild’s forest Georgia look misses live’s brighter green `#18793f` + orange `#f27c21`, Montserrat/Work Sans, and Duda marketing density (gallery + packages).

## Color tokens (LIVE)
| Token | Hex |
| --- | --- |
| `--brand` | `#18793f` |
| `--brand-2` / accent | `#f27c21` (hover/secondary `#ff5029`) |
| `--ink` | `#3a3a3a` |
| `--muted` | `#666666` |
| `--bg` | `#fcfcfc` / `#eef5ee` light |
| `--surface` | `#ffffff` |
| `--hero-ink` | `#ffffff` |
| `--font-display` | `Montserrat, "Work Sans", system-ui, sans-serif` |

## Layout intent
- Fresh outdoor marketing site: green brand, orange CTAs, photo-forward gallery.
- Top nav with Services / Packages / Gallery / Contact.
- Hero with lawn imagery energy (not dark woodsy serif).
- Keep Elfsight reviews as widget only — no invented quotes.
- Keep `BEYOND` logo asset only.

## Eng change list
1. `theme.css`: `--brand` → `#18793f`; `--brand-2`/`--accent` → `#f27c21` (not `#e85d04` only — close but live uses `#f27c21`).
2. Drop Georgia display font → Montserrat/Work Sans stack.
3. Lighten `--bg`; hero pattern softer or photo-backed.
4. Primary buttons orange; links/nav green.
5. Gallery page: grid denser, photo-first cards (match live gallery feel).
6. Packages page: price bands as clear cards with strong orange CTA.

## Keep
- Published service tree, package bands, gallery CDN photos, Elfsight only.

## 508 notes
- Orange `#f27c21` on white may fail small text — use for large buttons only; body links use green `#18793f`.
- Orange button text must be white and ≥4.5:1 (or darken orange to `#d45f10` if needed).
- Gallery images: meaningful `alt` from published captions; empty alt only if decorative.
- Focus ring high-contrast on green/orange fields.
- Form labels on Contact.
