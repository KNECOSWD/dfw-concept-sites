# Ferraro DDS — design brief

**Live:** https://www.grandprairie-arlingtondental.com/ (Cloudflare often challenges bots; content historically from Oct 2025 archive + practice CDN)  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/ferraro-dds/  
**Vibe match: 7/10** — Teal dental (`#0d7377` / bright `#3bc0e1`) is the right family. Polish toward cleaner clinical white + teal; avoid muddy greens.

## Color tokens (LIVE/archive-informed)
| Token | Hex |
| --- | --- |
| `--brand` | `#0d7377` |
| `--brand-2` | `#14919b` / highlight `#3bc0e1` |
| `--ink` | `#16333a` |
| `--muted` | `#547077` |
| `--bg` | `#eef6f6` |
| `--surface` | `#ffffff` |
| `--hero-ink` | `#ffffff` or dark on light hero |
| `--font-display` | Georgia or clean serif for doctor name; body sans |

## Layout intent
- Calm dental practice: logo + doctor photo, services, one published testimonial (Mrs. Conger), hours Mon–Thu 8–5.
- Soft teal gradients ok; clinical whitespace.
- Keep published dental logo asset only.

## Eng change list
1. Keep teal tokens; optionally brighten accents with `#3bc0e1` for chips/icons.
2. Hero: light clinical or soft teal — less “ornate radial.”
3. Doctor photo prominent on About; respectful crop.
4. Testimonials page: single real quote — no filler cards.
5. Contact: email + hours; Friday blank stays blank (don’t invent).

## Keep
- Archive-sourced copy rules; Top Rated Doctors 2016 if published; no fake reviews.

## 508 notes
- Teal on white: verify `#0d7377` ≥4.5:1 for body links.
- Light teal `#3bc0e1` on white fails for text — large UI only.
- Doctor photo: descriptive `alt`.
- Appointment form labels; required fields announced.
- If live CF blocks Eng QA, test against rebuild + archive screenshots.
