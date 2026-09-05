# Ferraro DDS — design brief

**Live:** https://www.grandprairie-arlingtondental.com/ (**Cloudflare 403** from this environment — `live-home.png` / `live-hero.png` are 403 stubs)  
**Archive (Oct 2025):** https://web.archive.org/web/20251013053238/https://www.grandprairie-arlingtondental.com/ → `archive-home.png`, `archive-hero.png`  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/ferraro-dds/ → `rebuild-home.png`, `rebuild-hero.png`  
**Vibe match: 5/10** — Both are “dental teal,” but **live/archive is bright cyan-teal `#3bc0e1` on clinical white** (airy, SMB dental template). Rebuild is **deep teal `#0d7377` on dark charcoal header** with radial hero — reads premium medical, not the published bright/clean vibe. Align rebuild toward live’s light teal + white.

## Color tokens (LIVE / archive `:root` + screenshots)
| Token | Hex | Notes |
| --- | --- | --- |
| `--brand` / primary | `#3bc0e1` | Live `--color1` / `--color2`; nav bar + CTA |
| Highlight | `#5dd5f3` | Live `--color4` — chips/hover only (not body text) |
| `--brand-deep` (optional) | `#0d7377` | OK as footer/ink support — **not** full-page hero fill |
| `--ink` | `#000000` / `#16333a` | Headings / body |
| `--muted` | `#646464` | Live `--color6` secondary |
| `--bg` | `#ffffff` / `#f7f7f7` | Clinical white (`--color3`) |
| `--surface` | `#ffffff` | Cards |
| `--hero-ink` | `#000000` on white hero; white only on teal buttons |
| `--font-display` | Serif for hero titles (“Your Brightest Smile”); sans for nav/body |

Rebuild `theme.css` deep teal (`#0d7377` / `#14919b`) should **shift primary brand/CTA/nav toward `#3bc0e1`** to match live dental teal/clean.

## Layout intent
- **Live/archive:** Top contact strip (address/email | phone/email) → **centered text logo** “Grand Prairie - Arlington Dental / Daniel L. Ferraro, DDS” → **bright teal full-width nav** (WELCOME, ABOUT US, OUR SERVICES, …) → **white centered hero** (“Your Brightest Smile” / implant special / teal “CALL TODAY…” button) → 4 featured cards → doctor photo welcome block.
- Rebuild dark header + deep teal gradient hero + “Call the office” KPI panel is scaffold-OK but **too dark/ornate** vs live airy white.
- Calm clinical whitespace; keep published logo graphic (tooth/D mark + name).
- Hours: Mon–Thu published; **do not invent Friday**.

## Eng change list
1. **Brighten brand:** `--brand` / primary buttons / nav accents → `#3bc0e1`; reserve deep teal for footer or small accents only.
2. **Hero:** light clinical white (or soft teal band) with dark serif headline — reduce ornate radial dark hero.
3. Restyle or drop `theme-dark-header` charcoal chrome → light header or teal nav bar feel.
4. Featured path: restore visual density of 4 info cards (Meet the Doctor / Contact / Services / Testimonials) if content exists.
5. About: doctor photo prominent with respectful crop + descriptive `alt`.
6. Testimonials: only published quotes (e.g. archive-sourced) — no filler cards.
7. Implant pricing copy: keep published specials; note `$2400` vs `$1100/$2100` inconsistency — “call to confirm,” don’t invent a single number.
8. **Keep published logo** asset only (`assets/logo.png` / live dental mark) — do not replace with generic icon.

## Keep
- Practice name + Dr. Ferraro identity, Emerald Square / Hwy 360 address, `(972) 988-8044`, 30+ years / UT San Antonio / 3M mini-implant facts as published.
- Archive-sourced welcome copy; no fake reviews; no outreach forms beyond existing contact patterns.

## 508 notes
- `#3bc0e1` on white **fails** for small body text — use for large buttons/nav only; body links use darker teal (~`#0a6b70` / `#0d7377`).
- White text on `#3bc0e1` buttons: verify contrast; darken button fill if needed.
- Doctor / slider images: meaningful `alt` (archive slider alts exist for some slides).
- Skip link present on rebuild — keep visible on focus.
- If live CF blocks Eng QA, regress against `archive-*.png` + rebuild screenshots.
- Form labels on appointment/contact; required fields announced; errors not color-only.


---

## Content / nav parity (HARD GATE)

**Parity status:** FAIL — live deep service tree (40+ pages) collapsed to 5; must restore dropdown IA with every destination.

### Live nav map
- **Welcome** → `https://www.grandprairie-arlingtondental.com`
- **About Us** (dropdown)
  - Meet the Doctor → `https://www.grandprairie-arlingtondental.com/doctor`
  - Meet The Staff → `https://www.grandprairie-arlingtondental.com/staff`
- **Our Services** (dropdown)
  - Dental Hygiene → `https://www.grandprairie-arlingtondental.com/dental-hygiene`
  - Implants / Dental Implants / Mini Implants / FAQ → `https://www.grandprairie-arlingtondental.com/implants`
  - Cosmetic (Veneers, Whitening, Bonding) → `https://www.grandprairie-arlingtondental.com/cosmetic-services`
  - Endodontics (Root Canal, Retreatment) → `https://www.grandprairie-arlingtondental.com/endodontics`
  - Restorative (Bridges, Crowns, …) → `https://www.grandprairie-arlingtondental.com/restorative`

_Note: Full live service tree is deep (40+ destinations). Eng must keep every published service URL reachable with same labels — collapse only with dropdown children._

### Rebuild nav map (current)
- Home → `index.html`
- About → `about.html`
- Services → `services.html`
- Testimonials → `testimonials.html`
- Contact → `contact.html`

### Eng requirement
Restore **full live header IA** (every top item + dropdown children). Collapsing only OK if every destination stays reachable with the **same labels**. Do not strip Financing / service-area / deep service pages into a thin 4–5 link bar.


### Full live destinations (must stay reachable)

- Welcome → `https://www.grandprairie-arlingtondental.com`
- About Us → `https://www.grandprairie-arlingtondental.com/about`
- Meet the Doctor → `https://www.grandprairie-arlingtondental.com/doctor`
- Meet The Staff → `https://www.grandprairie-arlingtondental.com/staff`
- Our Services → `https://www.grandprairie-arlingtondental.com/our-services`
- Dental Hygiene → `https://www.grandprairie-arlingtondental.com/dental-hygiene`
- Implants → `https://www.grandprairie-arlingtondental.com/implants`
- Dental Implants → `https://www.grandprairie-arlingtondental.com/dental-implants`
- Mini Implants → `https://www.grandprairie-arlingtondental.com/mini-implants`
- Dental Implant FAQ's → `https://www.grandprairie-arlingtondental.com/dental-implant-faq`
- Cosmetic → `https://www.grandprairie-arlingtondental.com/cosmetic-services`
- Beautiful Veneers → `https://www.grandprairie-arlingtondental.com/veneers`
- Whitening → `https://www.grandprairie-arlingtondental.com/whitening`
- Bonding → `https://www.grandprairie-arlingtondental.com/bonding-and-white-fillings`
- Endodontics → `https://www.grandprairie-arlingtondental.com/endodontics`
- Root Canal → `https://www.grandprairie-arlingtondental.com/root-canal`
- Retreatment → `https://www.grandprairie-arlingtondental.com/retreatment`
- Restorative → `https://www.grandprairie-arlingtondental.com/restorative`
- Bridges → `https://www.grandprairie-arlingtondental.com/bridges`
- Crowns → `https://www.grandprairie-arlingtondental.com/crowns`
- Dentures → `https://www.grandprairie-arlingtondental.com/dentures`
- Pediatric → `https://www.grandprairie-arlingtondental.com/pediatric`
- Sealants → `https://www.grandprairie-arlingtondental.com/sealants`
- Mouth Guards → `https://www.grandprairie-arlingtondental.com/mouth-guards`
- Periodontics → `https://www.grandprairie-arlingtondental.com/periodontic`
- Crown Lengthening → `https://www.grandprairie-arlingtondental.com/crown-lengthening`
- Frenectomy → `https://www.grandprairie-arlingtondental.com/frenectomy`
- Occlusal Adjustment → `https://www.grandprairie-arlingtondental.com/occlusal-adjustment`
- Cosmetic Periodontal Surgery → `https://www.grandprairie-arlingtondental.com/cosmetic-periodontal-surgery`
- Periodontal (gum) disease → `https://www.grandprairie-arlingtondental.com/periodontal-gum-disease`
- Scaling & Root Planing → `https://www.grandprairie-arlingtondental.com/scaling-and-root-planing`
- Oral Surgery → `https://www.grandprairie-arlingtondental.com/oral-surgery`
- Extractions → `https://www.grandprairie-arlingtondental.com/extractions`
- Wisdom Teeth → `https://www.grandprairie-arlingtondental.com/wisdom-teeth`
- Extraction Site Preservation → `https://www.grandprairie-arlingtondental.com/extraction-site-preservation`
- TMJ → `https://www.grandprairie-arlingtondental.com/tmj`
- Night Guards → `https://www.grandprairie-arlingtondental.com/night-guards`
- Our Technology → `https://www.grandprairie-arlingtondental.com/our-technology`
- Panorex → `https://www.grandprairie-arlingtondental.com/panorex`
- Rotary Endodontics → `https://www.grandprairie-arlingtondental.com/rotary-endodontics`

## Image inventory (Eng must incorporate)

Homepage (and linked gallery/team) assets from live — download into `assets/` and place in matching sections (hero / gallery / team / services). Do not leave pages image-thin vs live.

1. **content** — `https://cdcssl.ibsrv.net/ibimg/smb/926x928_80/webmgr/00/k/9/dan.jpg.webp?632d17e6c07e998bb4135d71aebf3b3a` alt="dan.jpg"
2. **hero/banner** — `https://cdcssl.ibsrv.net/ibimg/smb/1280x1920_80/webmgr/00/k/9/01.jpg.webp?b0e8b24084a66dac05eed4d55a95b440`
3. **hero/banner** — `https://cdcssl.ibsrv.net/ibimg/smb/1280x1920_80/webmgr/00/k/9/02.jpg.webp?a3de308a164edc7548cdb03db7eb366d`
4. **content** — `https://cdcssl.ibsrv.net/ibimg/smb/1280x1920_80/webmgr/00/k/9/03.jpg.webp?6b9e253c5d0566a7a443f9cffc36d3e9`
5. **content** — `https://cdcssl.ibsrv.net/ibimg/smb/1280x1920_80/webmgr/00/k/9/04.jpg.webp?53ddf7f3869b322c79182469e8b2b45f`
6. **content** — `https://cdcssl.ibsrv.net/ibimg/smb/784x784_80/webmgr/00/k/9/dan2.jpg.webp?b033ea847f1ff2e6a7027d1bc88e9d49`
7. **content** — `https://cdcssl.ibsrv.net/ibimg/smb/401x261_80/webmgr/00/k/9/582dd2bcebc50_OliviaSerivceDental1.jpg.webp?915743038d004b9b0b4c02eeab6a815a`
8. **content** — `https://cdcssl.ibsrv.net/ibimg/smb/401x261_80/webmgr/00/k/9/582dd2ca6e261_OliviaSerivceDental3.jpg.webp?1e751932ba0b280d5d5571d97defed8e`
9. **content** — `https://cdcssl.ibsrv.net/ibimg/smb/401x261_80/webmgr/00/k/9/582dd2d827cce_OliviaSerivceDental2.jpg.webp?c76fd9436e7d6cdac65c5d946d2bc178`

Parsed homepage image count (raw): **9**. Also pull gallery/inner-page images when those routes are restored.

## Favicon

- **Live source:** `https://cdcssl.ibsrv.net/ibimg/smb/16x16_80/webmgr/00/k/9/5728ddd39e644_00551Dentallogodesignfreelogosonline02.png.webp?d5d3159013fc2ae272e4328c671da234`
- **Local capture:** `/workspace/dfw-design-briefs/favicons/ferraro-dds.png`
- **Note:** Ship this favicon (or logo-derived 32/180) — never invent a new mark.

