# Best Price Tires & Auto — design notes

**Slug:** `best-price-tires`  
**Live:** https://bestpricetireandauto.com/  
**Rebuild:** `sites/best-price-tires/`  
**Path:** $500 independent sales unit (do not batch with Princeton Car Care, Flavia’s, or Smiles)  
**Date:** 2026-09-06

Mitchell1 twin of Princeton Car Care in *structure only*. Brand, NAP, nav, specials, warranty, and hero treatment are this shop’s. Do not copy Car Care copy, blue-gray hero wash, phone, or address.

## Vault NAP / truth

| Field | Value |
| --- | --- |
| Business | Best Price Tires & Auto |
| Address | 790 E Princeton Dr, Princeton, TX 75407 |
| Phone | (972) 736-2027 |
| Hours | Mon–Sat 8am–6pm; Sunday closed |
| Email | None published (Vault found none). Do not invent. |
| Facebook | https://www.facebook.com/bestpricetiresauto/ |
| Reviews host | https://www.surecritic.com/reviews/best-price-tires--auto (linked; quotes not scraped into HTML) |

**Not Car Care:** 2170 W Princeton Dr / (972) 736-0202 / 12-month warranty / “since 2008” stay off this unit.

## Hard locks (FAIL if missed)

1. **Generic media only.** Logo, favicon, and photos are generic/stock. No live shop logo (`LSWL3119913-…`), no shop photos (`Untitled-2-1.jpg`, `werg.jpg`, `78.jpg`), no Snap/Acima/Kornerstone badges, no live wrench favicon.
2. **Safe preview forms.** Contact + appointment forms stay on-page (`site.js` preventDefault). No business email. No live booking.
3. **Exp 3 hero:** dark/black scrim `rgba(0,0,0,0.66)` over the full hero, plus `rgba(0,0,0,0.78)` panel under the **full heading bounds**. Stronger than live `rgba(0,0,0,0.38)`. Not Car Care blue-gray.
4. **CTA:** primary **Schedule Appointment** → `appointments.html`. Secondary **Call (972) 736-2027** once in the hero, once in finished sticky header, once in the mobile callbar. No Mitchell1 CTA pile-up.
5. **Nav:** Home / Services / Appointments / Specials / Reviews / Contact + Vehicles Serviced. **No Gallery** page, section, or nav item.
6. No invented email. Facebook footer uses the published URL.
7. Financing: generic sentence only (“Ask about available financing options.”).
8. Responsive; local assets; no lorem; no invented reviews; no dead UI.

## Colors

| Token | Hex | Use |
| --- | --- | --- |
| Mid blue | `#2a4d85` | Secondary navy / cards on navy band |
| Deep blue | `#1b3257` | Nav bar, brand |
| Primary CTA | `#111111` | Black Schedule / Call buttons |
| Gold | `#c9a227` | Icon accents, nav underline, callbar Schedule on mobile |

Omit Mitchell1 chrome (LayerSlider, triangle separators, double-line headings, CRM “click images to redirect”, partner badge row).

## IA

| Page | Source |
| --- | --- |
| Home | Live welcome, tire-forward service list, amenities, why/trust, recently serviced vehicles as published work records |
| Services | Live `/services/` category copy and bullet lists |
| Appointments | Live request + estimate copy; safe form |
| Specials | Live five offers (no `%ExpiresIn30%` token) |
| Reviews | Live 3Rs copy + SureCritic link. No invented quotes or star widgets |
| Contact | Live contact copy + NAP + safe form |
| Vehicles | Live Foreign / Domestic / popular make names on one page (not 50 Mitchell1 archive pages) |

## Media inventory (generic)

- `assets/logo.png` / `logo.svg` — generic tire mark + wordmark (not the customer file)
- `assets/favicon.png` / `apple-touch-icon.png` — generic tire icon
- `assets/hero-bay.jpg` — stock service-bay interior
- `assets/stock-tires.jpg` — stock tire stack
- `assets/stock-bay.jpg` — stock wheel/balancer bay

## 508 notes

- White text only on the black hero panel (`#000` at 0.78).
- Black buttons with white labels.
- Gold is large-icon / underline only — not small body text on white.
- Visible labels on forms; errors not color-only.
- One `h1` per page; skip link present.
