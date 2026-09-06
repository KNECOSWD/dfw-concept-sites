# Flavia's Beauty Salon & Barber Shop — independent sales unit

**Slug:** `flavias-beauty`  
**Offer path:** $500 rebuild  
**Live:** https://flaviasbeautysalonandbarbershop.com/  
**Rebuild:** `sites/flavias-beauty/` → https://knecoswd.github.io/dfw-concept-sites/sites/flavias-beauty/  
**Platform (live):** GoHighLevel / LeadConnector website (omit GHL chrome in the static rebuild)  
**Cap:** GitHub Pages static only. $0 Azure.

This is an **independent sales unit**. Do not fold it into the original 10 DFW rebuilds. Matthew merges.

---

## Sketch notes

Sticky chrome → hero (stock photo + **full plate/scrim under the entire heading block** + **one** Book) → dual location cards → barber / salon pathways → services → specials → team grids → contact / maps / footer.

Exp 3 hard fails:

1. Hero/media text needs a plate or scrim under the **full heading bounds** (not a thin wash that leaves the H1 on the photo).
2. Finished, consistent **sticky nav chrome** on every page.
3. **No CTA pile-up** — one primary Book path (`book.html`). Header + hero (and service “Reserva tu Cita” labels) all point there. Pathway cards use VER MAS → services, not a second Book.

## Vault notes (content truth)

Fetched 2026-09-06 from the live homepage and `/services`.

### Nav

Live homepage: **Products** · **Services** · **Team** · **Contact us** + primary **RESERVAR CITA / BOOK NOW**.

| Label | Live target |
| --- | --- |
| Products | `#section-gc7P24ByG` (specials on the home page). Funnel step `/products` exists in GHL JSON but **404s**. |
| Services | `/services` (funnel step “Servicios”) |
| Team | `#section-0sw7qQHp7` |
| Contact us | `#section-H86u0I4h3` |
| RESERVAR CITA / BOOK NOW / Get a Appointment | `scroll-to-element` → `#section-6jXnPTJG5` (location picker) |
| Reservar Aqui (on each location card) | `click-to-call` for that shop |
| VER MAS | `go-to-funnel-step` → `/services` |

Rebuild nav uses the same four labels as real pages (so Products is not a dead 404) plus **one** Book control.

### Dual locations (equal cards; phone paired with address)

- **West:** 275 West Princeton Drive, Princeton, Texas. `tel:+14693783098` · +1 469 378 3098  
- **East:** 691 East Princeton Drive, Princeton, Texas. `tel:+12149740534` · +1 214 974 0534  
- **Hours (both):** Mon – Sat 10:00am – 7:00pm; Sunday – 10:00am - 4:00pm

### Services (live `/services`)

- **Cortes para Mujeres:** Regular; Blow Dry / Secado; Corte, Shampoo; Curly; Girl / Niña; Flat Iron / Planchado  
- **Cortes para Hombres:** Regular; Fade; Haircut & Beard; Kid / Niño; Kid Fade; Beard / Barba; Mustache / Bigote; Design / Diseño; Eyebrows / Cejas; Wax  
- **Color y Tratamientos:** Retouch / Retoque; Retouch & Blowdry; Full Color; Highlights; Balayage; Keratina; Botox; Perms  
- **Maquillaje y Peinados:** Make Up; Up Do / Peinado; Quinceañera  

Homepage category blurbs (Spanish) are copied from the live home page. No service prices are published — none invented.

### Specials / Products

Keep **UP** wording. No invented fixed prices.

1. Especial 1 **$75UP** — Shampoo, Deep Treatment, Haircut, Style  
2. Especial 2 **$95UP** — Retoque de Color, Shampoo, Tratamiento, Estilizado  
3. Especial 3 **$185UP** — Color, Highlights, Treatment, Style  

### Team (generic avatars only)

- Beauty: Carmen, SILVIA, DIANA, GRACE, ONDINA  
- Barber: CELINA, VICTOR, SAMUEL, LETICIA, ALHANA, flavia  

### Colors & type (live `:root`)

| Token | Hex |
| --- | --- |
| Rose / primary | `#EB639C` |
| Sky | `#639EDB` |
| Soft | `#DBE5F5` |
| Muted | `#697785` |
| Ink | `#292929` |
| Headline | Lora |
| Body | Open Sans |

### Booking destination (LeadConnector wiring)

Confirmed from the homepage Nuxt payload (2026-09-06):

- Location ID `hDMS1l5GNup1DNZ2x998`
- **No public calendar / widget / `api.leadconnectorhq.com/widget/booking` URL**
- Every Book control is `scroll-to-element` → location picker `#section-6jXnPTJG5`
- Location-card “Reservar Aqui” is `click-to-call`

**Single rebuild Book path:** `book.html` (that picker). Preview-safe: no GHL widget, no live booking, `mailto:disabled` + `preventDefault` on forms.

### Footer domain lock

Live footer currently prints the typo host `falviasbeautysalonandbarbershop.com`.  
**Never ship that string.** Footer and copy use **flaviasbeautysalonandbarbershop.com** only.

## Beacon notes

- Generic media lock: generated “F” wordmark + stock salon/barber photos + CSS initial avatars. **Hard fail** if customer logo, headshots, storefront photos, or the live favicon ship.
- Live favicon is the generic GHL icon (`stcdn.leadconnectorhq.com/funnel/icon/favicon.ico`) — still replaced with a generated mark so we do not copy live chrome.
- Safe preview forms: `action="mailto:disabled"`, JS `preventDefault`, KNECO preview notice. Must not email the shop or create a booking.
- Omit GHL / LeadConnector chrome (cart, funnel UI, default GHL favicon, widgets).
- Local fonts + images for GitHub Pages preview parity.
- No lorem, no invented reviews / prices / awards, no dead nav, no unfinished placeholders.

## 508

- Rose `#EB639C` is for large buttons and kickers, not small body text on white.
- Sky `#639EDB` links on white: large/bold; body uses ink for paragraphs.
- Skip link kept. Form errors are text, not color-only. 44px targets on nav and CTAs.
- Hero text sits on an opaque plate (contrast vs photo).

## Files

- `sites/flavias-beauty/` — static site  
- `sites-data.json` + gallery `index.html`  
- `design-briefs/flavias-beauty/` — this brief  
