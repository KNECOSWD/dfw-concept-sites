# Law Office of Len Conner — design brief

**Live:** https://www.lonestarlaw.net/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/len-conner-law/  
**Vibe match: 4/10** — Rebuild invented navy/gold “prestige firm.” Live is **maroon `#77080a`** chrome (nav bar, CTAs, logo type), **white header**, **beach family photo hero** with maroon headline. Standing rule: match live — do **not** keep navy/gold as primary.

## Color tokens (LIVE — use these)
| Token | Hex |
| --- | --- |
| `--brand` | `#77080a` |
| Logo maroon | keep in `assets/logo.jpg` (don’t recolor mark) |
| Badge gold | `#ffbe01` / `#f3ae05` — Super Lawyers / Best in Irving **only** |
| Badge blue | award seals only |
| `--ink` | `#333333` |
| `--muted` | `#666666` |
| `--bg` | `#f5f5f5` / cream |
| `--surface` | `#ffffff` |
| `--hero-ink` | `#77080a` on light photo (or white if overlay darkens) |
| `--font-display` | serif for firm name/headings; sans for nav/CTAs |

## Layout intent
- Traditional family-law site: white header + diamond LC logo + phone, full-width maroon nav, lifestyle beach hero, practice copy, trust badges, five homepage testimonials only.
- Phone `972-445-1500` everywhere it matters.
- No public email/hours invent. `/testimonials/` 404 — don’t add fake page.

## Eng change list
1. `theme.css`: `--brand` → `#77080a`; drop navy `#0f2744` as primary; gold only on badges/eyebrows.
2. Header: white bar; maroon phone; maroon nav strip with white links (scaffold needs a maroon-nav modifier).
3. Hero: beach/family photo underlay (published asset if available) + maroon headline/CTA — not solid navy wash.
4. `.btn-primary` → maroon fill, white text.
5. Keep five quotes (Marie, Marc and Jill, David, Dena, Kelly); keep badge images with alts.
6. Strip any “404” meta/debug copy if present.

## Keep
- Cities served; Irving address; logo; badges; homepage quotes only.

## 508 notes
- Maroon `#77080a` on white: verify body links ≥4.5:1 (darken if needed).
- Maroon nav + white links: OK if ≥4.5:1.
- Hero maroon on beach photo: ensure overlay/shadow for contrast.
- Badge `alt` includes award name + year.
- Form labels; focus visible on maroon controls (light ring).
