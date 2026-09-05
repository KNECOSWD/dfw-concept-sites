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

## Content / nav / image / favicon parity (Scout fold — authoritative)

_Folded from `/workspace/dfw-parity/ferraro-dds.md` (Scout public HTML inventory, 2026-09-05). Supersedes thinner nav/image lists above for Eng._

## ferraro-dds

Source: https://www.grandprairie-arlingtondental.com/ (public homepage HTML via curl, 2026-09-05). URLs below are copied as present in live markup. Never invented.

**Live title:** Grand Prairie Dentist | Dr. Daniel Ferraro, DDS

### Primary nav (with dropdown children)

Header `<nav id="navigation_header" class="navigation">` — top-level items in DOM order (nested `ul.navigation__list--sub`):

1. **Welcome** → `https://www.grandprairie-arlingtondental.com`
2. **About Us** → `https://www.grandprairie-arlingtondental.com/about`
   - **Meet the Doctor** → `https://www.grandprairie-arlingtondental.com/doctor`
   - **Meet The Staff** → `https://www.grandprairie-arlingtondental.com/staff`
3. **Our Services** → `https://www.grandprairie-arlingtondental.com/our-services`
   - **Dental Hygiene** → `https://www.grandprairie-arlingtondental.com/dental-hygiene`
   - **Implants** → `https://www.grandprairie-arlingtondental.com/implants`
     - **Dental Implants** → `https://www.grandprairie-arlingtondental.com/dental-implants`
     - **Mini Implants** → `https://www.grandprairie-arlingtondental.com/mini-implants`
     - **Dental Implant FAQ's** → `https://www.grandprairie-arlingtondental.com/dental-implant-faq`
   - **Cosmetic** → `https://www.grandprairie-arlingtondental.com/cosmetic-services`
     - **Beautiful Veneers** → `https://www.grandprairie-arlingtondental.com/veneers`
     - **Whitening** → `https://www.grandprairie-arlingtondental.com/whitening`
     - **Bonding** → `https://www.grandprairie-arlingtondental.com/bonding-and-white-fillings`
   - **Endodontics** → `https://www.grandprairie-arlingtondental.com/endodontics`
     - **Root Canal** → `https://www.grandprairie-arlingtondental.com/root-canal`
     - **Retreatment** → `https://www.grandprairie-arlingtondental.com/retreatment`
   - **Restorative** → `https://www.grandprairie-arlingtondental.com/restorative`
     - **Bridges** → `https://www.grandprairie-arlingtondental.com/bridges`
     - **Crowns** → `https://www.grandprairie-arlingtondental.com/crowns`
     - **Dentures** → `https://www.grandprairie-arlingtondental.com/dentures`
     - **Bonding** → `https://www.grandprairie-arlingtondental.com/bonding-and-white-fillings`
   - **Pediatric** → `https://www.grandprairie-arlingtondental.com/pediatric`
     - **Sealants** → `https://www.grandprairie-arlingtondental.com/sealants`
     - **Mouth Guards** → `https://www.grandprairie-arlingtondental.com/mouth-guards`
   - **Periodontics** → `https://www.grandprairie-arlingtondental.com/periodontic`
     - **Crown Lengthening** → `https://www.grandprairie-arlingtondental.com/crown-lengthening`
     - **Frenectomy** → `https://www.grandprairie-arlingtondental.com/frenectomy`
     - **Occlusal Adjustment** → `https://www.grandprairie-arlingtondental.com/occlusal-adjustment`
     - **Cosmetic Periodontal Surgery** → `https://www.grandprairie-arlingtondental.com/cosmetic-periodontal-surgery`
     - **Periodontal (gum) disease** → `https://www.grandprairie-arlingtondental.com/periodontal-gum-disease`
     - **Scaling & Root Planing** → `https://www.grandprairie-arlingtondental.com/scaling-and-root-planing`
   - **Oral Surgery** → `https://www.grandprairie-arlingtondental.com/oral-surgery`
     - **Dental Implants** → `https://www.grandprairie-arlingtondental.com/dental-implants`
     - **Mini Implants** → `https://www.grandprairie-arlingtondental.com/mini-implants`
     - **Extractions** → `https://www.grandprairie-arlingtondental.com/extractions`
     - **Wisdom Teeth** → `https://www.grandprairie-arlingtondental.com/wisdom-teeth`
     - **Extraction Site Preservation** → `https://www.grandprairie-arlingtondental.com/extraction-site-preservation`
   - **TMJ** → `https://www.grandprairie-arlingtondental.com/tmj`
   - **Night Guards** → `https://www.grandprairie-arlingtondental.com/night-guards`
4. **Our Technology** → `https://www.grandprairie-arlingtondental.com/our-technology`
   - **Panorex** → `https://www.grandprairie-arlingtondental.com/panorex`
   - **Rotary Endodontics** → `https://www.grandprairie-arlingtondental.com/rotary-endodontics`
   - **Oral Cancer Screenings** → `https://www.grandprairie-arlingtondental.com/oral-cancer-screenings`
5. **Patient Resources** → `https://www.grandprairie-arlingtondental.com/about`
   - **Print New Patient Form** → `https://www.grandprairie-arlingtondental.com/new-patient-forms`
   - **Q & A** → `https://www.grandprairie-arlingtondental.com/q-and-a`
   - **Links** → `https://www.grandprairie-arlingtondental.com/links`
   - **Post-Op Instructions** → `https://www.grandprairie-arlingtondental.com/post-op-instructions`
   - **Surgical Instructions** → `https://www.grandprairie-arlingtondental.com/surgical-instructions`
     - **Before Anesthesia** → `https://www.grandprairie-arlingtondental.com/before-anesthesia`
     - **After Wisdom Tooth Removal** → `https://www.grandprairie-arlingtondental.com/after-wisdom-tooth-removal`
     - **After Dental Implant Surgery** → `https://www.grandprairie-arlingtondental.com/after-dental-implant-surgery`
     - **After Impacted Tooth** → `https://www.grandprairie-arlingtondental.com/after-impacted-tooth`
     - **Multiple Tooth Extractions** → `https://www.grandprairie-arlingtondental.com/multiple-tooth-extractions`
6. **Testimonials** → `https://www.grandprairie-arlingtondental.com/testimonials`
7. **Gallery** → `https://www.grandprairie-arlingtondental.com/gallery`
8. **Appointment Request** → `https://www.grandprairie-arlingtondental.com/appointment`
9. **Contact Us** → `https://www.grandprairie-arlingtondental.com/contact`

**Header logo text (no header logo `<img>`):** title “Grand Prairie - Arlington Dental”; description “Daniel L. Ferraro, DDS”.

### Key images / heroes

| Role | Absolute URL | Notes from live HTML |
| --- | --- | --- |
| **Schema / brand logo (PNG)** | `https://www.grandprairie-arlingtondental.com/storage/app/media/5728ddd39e644_00551Dentallogodesignfreelogosonline02.png` | JSON-LD `MedicalBusiness.logo` (same asset family as favicons) |
| **Hero slider 1** | `https://cdcssl.ibsrv.net/ibimg/smb/1280x1920_80/webmgr/00/k/9/01.jpg.webp?b0e8b24084a66dac05eed4d55a95b440` | `li.slider__item` bg; aria-label “Happy patient with Dentist”; title “Your Brightest Smile”; caption “Implant Specials $2400”. Responsive variants also in `image-set` (2200 / 1400 / 1023 / 767 widths). |
| **Hero slider 2** | `https://cdcssl.ibsrv.net/ibimg/smb/1280x1920_80/webmgr/00/k/9/02.jpg.webp?a3de308a164edc7548cdb03db7eb366d` | Title “Healthy Teeth for a Lifetime” |
| **Hero slider 3** | `https://cdcssl.ibsrv.net/ibimg/smb/1280x1920_80/webmgr/00/k/9/03.jpg.webp?6b9e253c5d0566a7a443f9cffc36d3e9` | Title “Protect Your Teeth” |
| **Hero slider 4** | `https://cdcssl.ibsrv.net/ibimg/smb/1280x1920_80/webmgr/00/k/9/04.jpg.webp?53ddf7f3869b322c79182469e8b2b45f` | Title “A Team You Can Rely On”; caption “Quality, compassionate care.” |
| **Doctor portrait (`<picture>` / `dan.jpg`)** | `https://cdcssl.ibsrv.net/ibimg/smb/926x928_80/webmgr/00/k/9/dan.jpg.webp?632d17e6c07e998bb4135d71aebf3b3a` | Homepage `<img>` alt `dan.jpg`; also `767x769` source for max-width 767 |
| **Featured block — Meet the Doctor** | `https://cdcssl.ibsrv.net/ibimg/smb/784x784_80/webmgr/00/k/9/dan2.jpg.webp?b033ea847f1ff2e6a7027d1bc88e9d49` | `featuredblock__image` bg; aria-label “Dr Daniel Ferraro”; links to `/doctor` |
| **Featured block — Contact Us** | `https://cdcssl.ibsrv.net/ibimg/smb/401x261_80/webmgr/00/k/9/582dd2bcebc50_OliviaSerivceDental1.jpg.webp?915743038d004b9b0b4c02eeab6a815a` | aria-label “Contact Us” |
| **Featured block — Our Services** | `https://cdcssl.ibsrv.net/ibimg/smb/401x261_80/webmgr/00/k/9/582dd2ca6e261_OliviaSerivceDental3.jpg.webp?1e751932ba0b280d5d5571d97defed8e` | aria-label “Our Services” |
| **Featured block — Patient Testimonials** | `https://cdcssl.ibsrv.net/ibimg/smb/401x261_80/webmgr/00/k/9/582dd2d827cce_OliviaSerivceDental2.jpg.webp?c76fd9436e7d6cdac65c5d946d2bc178` | aria-label “Patient Testimonials” |

### Favicon

- **shortcut icon (16x16 webp):** `https://cdcssl.ibsrv.net/ibimg/smb/16x16_80/webmgr/00/k/9/5728ddd39e644_00551Dentallogodesignfreelogosonline02.png.webp?d5d3159013fc2ae272e4328c671da234`
- **apple-touch-icon** (same asset, sized CDN paths):
  - 57×57: `https://cdcssl.ibsrv.net/ibimg/smb/57x57_80/webmgr/00/k/9/5728ddd39e644_00551Dentallogodesignfreelogosonline02.png.webp?d5d3159013fc2ae272e4328c671da234` *(also listed without `sizes`)*
  - 72×72: `https://cdcssl.ibsrv.net/ibimg/smb/72x72_80/webmgr/00/k/9/5728ddd39e644_00551Dentallogodesignfreelogosonline02.png.webp?d5d3159013fc2ae272e4328c671da234`
  - 76×76: `https://cdcssl.ibsrv.net/ibimg/smb/76x76_80/webmgr/00/k/9/5728ddd39e644_00551Dentallogodesignfreelogosonline02.png.webp?d5d3159013fc2ae272e4328c671da234`
  - 114×114: `https://cdcssl.ibsrv.net/ibimg/smb/114x114_80/webmgr/00/k/9/5728ddd39e644_00551Dentallogodesignfreelogosonline02.png.webp?d5d3159013fc2ae272e4328c671da234`
  - 120×120: `https://cdcssl.ibsrv.net/ibimg/smb/120x120_80/webmgr/00/k/9/5728ddd39e644_00551Dentallogodesignfreelogosonline02.png.webp?d5d3159013fc2ae272e4328c671da234`
  - 144×144: `https://cdcssl.ibsrv.net/ibimg/smb/144x144_80/webmgr/00/k/9/5728ddd39e644_00551Dentallogodesignfreelogosonline02.png.webp?d5d3159013fc2ae272e4328c671da234`
  - 152×152: `https://cdcssl.ibsrv.net/ibimg/smb/152x152_80/webmgr/00/k/9/5728ddd39e644_00551Dentallogodesignfreelogosonline02.png.webp?d5d3159013fc2ae272e4328c671da234`
  - 180×180: `https://cdcssl.ibsrv.net/ibimg/smb/180x180_80/webmgr/00/k/9/5728ddd39e644_00551Dentallogodesignfreelogosonline02.png.webp?d5d3159013fc2ae272e4328c671da234`

### Capture notes

- Platform: Internet Brands SMB / ibsrv CDN (`cdcssl.ibsrv.net`).
- Captured from public homepage HTML only. No invented labels or URLs.
- Header uses text logo (title + description), not an `<img>`; brand PNG appears in schema + favicon set.
- Deep nested services live under **Our Services**; **Patient Resources** nests **Surgical Instructions**.


### Parity emphasis
- Restore full nested IA: Welcome, About Us (+Doctor/Staff), Our Services (deep tree), Our Technology, Patient Resources (+Surgical Instructions nest), Testimonials, Gallery, Appointment Request, Contact Us.
- Brand PNG from schema/favicon set; hero is 4-slide dental photo slider + doctor portrait.


