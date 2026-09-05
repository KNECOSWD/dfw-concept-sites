# CareMaster Building Services — design brief

**Live:** http://www.caremaster.biz/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/caremaster-building/  
**Vibe match: 3/10** — Rebuild is teal SaaS navy (`#2a9d8f`). Live is a traditional brochure: **white centered header**, **dark green + gold logo** (skyscraper + stars), light-gray all-caps nav, **Dallas skyline photo hero** with white slogan overlay. Red `#E80000` appears in CSS/contact accents — not the hero brand.

## Color tokens (LIVE — visual + CSS)
| Token | Hex | Notes |
| --- | --- | --- |
| `--brand` | `#0b3d2e`–`#1a4d3a` (dark green matching logo type) | Primary brand (logo serif green) |
| `--brand-2` / gold | `#C9A84C` / `#EDDB8C` | Logo stars / gold accents |
| `--accent` (optional) | `#E80000` | Contact/email strip only — not hero CTAs |
| `--ink` | `#383838` | |
| `--muted` | `#686868` / light gray nav `#a0a0a0` | |
| `--bg` | `#ffffff` / `#f0f0f0` | |
| `--surface` | `#ffffff` | |
| `--hero-ink` | `#ffffff` | On skyline photo |
| `--font-display` | serif for logo lockup only; body `Open Sans` / sans | |

## Layout intent
- Centered logo header (not left brand + right CTA like scaffold default).
- Centered all-caps text nav under logo.
- Full-bleed skyline hero with short white slogan; prose sections below.
- Formal commercial janitorial density — not trendy teal startup.
- Keep published `logo-2.jpg` / gold tower mark only.

## Eng change list
1. Remove teal `#2a9d8f` from buttons/accents.
2. Primary CTA → dark green (or charcoal); gold for thin rules/stars only; red only if matching live contact strip.
3. Header layout: center logo + center nav (scaffold `header-row` left-align needs a CareMaster modifier).
4. Hero: use published skyline photo with dark overlay + white slogan — drop teal gradient pinstripe panel.
5. Softer corporate prose blocks for About/Commitment.
6. Fonts: Open/Source Sans body; keep logo image (don’t recreate gold tower in CSS).

## Keep
- Since 1982, John Lee, phones, PO Box, service list; no invented reviews.

## 508 notes
- White text on skyline: ensure overlay dark enough (≥4.5:1).
- Gold on white fails for small text — decorative only.
- Light-gray nav on white may fail — darken active/hover to `#383838`.
- Centered nav: still a real `<nav>` with focus order.
- Form labels; don’t use red alone for errors.
