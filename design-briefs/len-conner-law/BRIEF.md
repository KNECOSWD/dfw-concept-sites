# Law Office of Len Conner — design brief

**Live:** https://www.lonestarlaw.net/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/len-conner-law/  
**Vibe match: 8/10** — Sell-as-is target is **navy/gold law firm**. Rebuild hero is deep navy `#0f2744` family + gold CTA `#b08948` / `#c5a572` — correct. Live Enterprise WP is **maroon/burgundy** chrome (`#77080a` nav + CTAs) on white with a bright beach family photo — not navy. Do **not** retune primary to maroon or scraped WP blues; keep navy/gold and keep the maroon **logo** as-is.

## Color tokens (LIVE — reference only)
| Token | Hex | Notes |
| --- | --- | --- |
| `--brand` (live nav/CTA) | `#77080a` | Maroon bar + “learn more” — **don’t make rebuild primary** |
| Logo maroon | `#6b1a19` | Keep in logo asset only |
| Badge gold | `#f3ae05` / `#ffbe01` | Super Lawyers / Best in Irving — accent only |
| Badge blue | `#0259b1` | Award seal only |
| `--ink` | `#333333` | Body |
| `--bg` | `#f5f5f5` / cream | Below hero |
| `--surface` | `#ffffff` | Header |
| `--hero-ink` | `#77080a` on light beach photo | Live places maroon type on photo |

## Target tokens (rebuild / Eng)
| Token | Hex |
| --- | --- |
| `--brand` | `#0f2744` |
| `--brand-2` / accent | `#c5a572` |
| `--accent` (CTA fill) | `#b08948` |
| `--bg` | `#eef2f6` |
| `--surface` | `#fbfcfe` |
| `--ink` | `#122033` |
| `--muted` | `#5a6573` |
| `--hero-ink` | `#f4efe4` |

## Layout intent
- Authoritative family-law marketing: navy hero, gold primary Call, white header with existing diamond logo, trust badges, five homepage testimonials, cities chips.
- Live pattern to borrow (optional): soft family/beach photography as a **secondary** band or muted hero underlay — never recolor the whole site maroon.
- Phone `(972) 445-1500` in header, hero primary, and callbar.
- Keep existing logo (`assets/logo.jpg`).

## Eng change list (concrete CSS/HTML)
1. `theme.css`: lock `--brand:#0f2744`, `--brand-2:#c5a572`, `--accent:#b08948`; ensure `.btn-primary` uses gold fill + dark navy or white text that passes contrast (prefer `#122033` on gold if white fails).
2. `.header-cta.btn-dark`: navy fill (not maroon); active nav link gold or navy underline — not live burgundy.
3. `.hero`: keep navy radial; optional subtle photo underlay at ≤30% opacity; keep gold `.eyebrow` (“Divorce & family law”).
4. `.badge-row`: keep Best in Irving / Super Lawyers / Avvo images; don’t recolor badges gold-wash the page.
5. Testimonials: five published quotes only (Marie, Marc and Jill, David, Dena, Kelly); remove meta copy about `/testimonials/` 404 from visible UI.
6. Soften duplicate brand text next to logo (logo already says Len Conner & Associates) — one clear wordmark.
7. Practice/areas: sober navy headings on light cards; avoid gold gradient overload on interior pages.

## Keep
- Logo/marks; badge assets; Irving address; cities/counties list; homepage testimonials only; Texas marketing disclaimer in footer; no invented email/hours.

## 508 notes
- White on `#0f2744`: pass. Gold `#b08948` on white fails for small text — large CTAs only, or dark ink on gold.
- Maroon logo on white: OK; don’t use `#77080a` for body links on cream without checking ≥4.5:1.
- Badge `alt` must include award name + year; portrait in Super Lawyers graphic is informative.
- Skip link present; focus ring on navy/gold buttons needs light outline on dark hero and dark outline on white header.
- One `h1`; testimonials as `h2` + quote markup; don’t rely on gold alone for emphasis.
