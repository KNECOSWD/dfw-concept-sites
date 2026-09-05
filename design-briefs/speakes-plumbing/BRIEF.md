# Speake's Plumbing — design brief

**Live:** https://www.speakesplumbing.com/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/speakes-plumbing/  
**Vibe match: 4/10** — Rebuild is navy+copper serif “premium contractor.” Live is burgundy/maroon Duda site (Acme + Open Sans), white/light panels, top unified nav, burgundy CTAs.

## Color tokens (from LIVE — use these)
| Token | Hex | Notes |
| --- | --- | --- |
| `--brand` | `#7a001a` | Primary burgundy (inline rgb(122,0,26); #990021/#7a001a in home CSS) |
| `--brand-2` / accent | `#990021` | Buttons, nav accents, links |
| `--ink` | `#333333` | Body |
| `--muted` | `#617379` | Secondary text |
| `--bg` | `#faf9f9` / `#f5f5f5` | Page wash |
| `--surface` | `#ffffff` | Cards/panels |
| `--hero-ink` | `#ffffff` | On burgundy hero bands |
| `--font-display` | `Acme, "Open Sans", sans-serif` | Not Palatino |

## Layout intent
- Top horizontal nav (Home / About / Services / Testimonials / Contact) on light or burgundy bar — not a dark “executive” header.
- Hero: welcoming photo or solid burgundy band + short welcome copy; phone prominent.
- Density: medium; service list as bullets/cards; testimonials carousel ok.
- Keep existing logo `assets/logo.png` only.

## Eng change list (concrete)
1. `theme.css`: replace `--brand/#16324f` and `--brand-2/#c47a3a` with burgundy tokens above; drop copper entirely.
2. Remove `theme-dark-header` OR restyle `.theme-dark-header .site-header` to white/light with burgundy text/links (live is not navy chrome).
3. `.btn-primary` → burgundy fill, white text; `.btn-dark` header CTA same family.
4. `--font-display`: Acme or system sans stack; body Open Sans/system-ui — drop Palatino.
5. Hero: reduce decorative radial pattern; prefer solid `--brand` or live photo treatment if assets exist.
6. Strip “premium panel” visual if it reads hotel/spa — keep practical plumber density.

## Keep
- Real copy, license #16836, address, hours, published testimonials only.
- Skip link, tel: CTAs, existing logo.

## 508 notes
- Burgundy on white: check `#7a001a` on `#fff` (≥4.5:1); white on `#7a001a` for buttons.
- Focus: ensure burgundy outline on light header (scaffold gold focus may vanish on burgundy).
- Logo `alt` already set — keep.
- Heading order: one `h1` in hero; services as `h2`/`h3` — avoid skipping.
- Contact form: visible `<label>` for every input; error text not color-only.
- Skip link already present — verify visible on focus.
