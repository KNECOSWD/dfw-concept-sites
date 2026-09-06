# Princeton Car Care — acquisition design brief

**Live:** https://princetoncarcare.com/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/princeton-car-care/  
**Slug:** `princeton-car-care`  
**Path:** independent $500 sales unit (not one of the original ten DFW rebuilds)

## Hard locks (this unit)

1. **Generic media only.** Typeset generic logo + generic favicon + stock shop/auto imagery. No customer logo, live favicon, gallery photos, partner/affiliate badges, or Mitchell1 marks. Customer marks swap after approval.
2. **Safe preview forms.** Contact and appointment forms stay on the page. They do not email the shop (Vault found none) and do not create appointments.
3. **Exp 3 chrome.** Blue-gray plate under the **full** hero heading bounds. Finished sticky header. No CTA pile-up.
4. **CTA hierarchy.** Primary **Schedule Appointment** → `appointments.html` once in header + once in hero. Secondary **Call (972) 736-0202** once in hero + sticky callbar. No Mitchell1 Schedule / Specials / Reviews button stack.
5. **Nav.** Home / Services / Appointments / Specials / Gallery / Reviews / Contact + collapsible Vehicles Serviced. **About is soft-missing** — do not hard-link `/about/` or `/about-us/`.
6. `appointment.html` aliases to `appointments.html`. One booking product only.
7. Financing badges omitted; generic text only until approval.
8. Responsive; local assets; no lorem; no invented facts or reviews; no dead UI; no capability loss vs published live IA.

## Vault NAP / truth

| Field | Value |
| --- | --- |
| Business | Princeton Car Care |
| Address | 2170 W Princeton Dr, Princeton, TX 75407 |
| Phone | (972) 736-0202 |
| Hours | Mon–Sat 8am–6pm; Sunday Closed |
| Since | Serving Princeton since 2008 |
| Warranty (as published) | 12 Month/12,000 Mile; Lifetime on brake pads & shoes |
| Colors | Navy `#043f69` / blue `#0055a0` / gold `#ffc200` |

## Live IA (published)

| Label | Live path | Rebuild |
| --- | --- | --- |
| Home | `/` | `index.html` |
| Services | `/services/` | `services.html` |
| Appointments | `/appointments/` | `appointments.html` |
| Appointment alias | `/appointment/` | `appointment.html` → appointments |
| Specials | `/specials/` | `specials.html` |
| Gallery | `/gallery/` | `gallery.html` |
| Reviews | `/reviews/` | `reviews.html` |
| Contact | `/contact/` | `contact.html` |
| Privacy | `/privacy-policy/` | `privacy-policy.html` |
| Vehicles Serviced | published make list | `vehicles-serviced.html` + make pages |
| About | soft-missing | **not linked** |

**Vehicles Serviced children (published “We Service” list + GEO page):** Audi, BMW, Chevrolet, Dodge, Ford, GEO (`service-repair-geo.html`), GMC, Honda, Lexus, Mazda, Mercedes-Benz, Subaru, Toyota, Volkswagen.

**Service categories (live `/services/`):** maintenance, engine, HVAC, electrical, exhaust, alignment, transmission — lists copied as published.

## Media

- Logo / favicon: generic navy + gold mark (`assets/logo.svg`, `assets/favicon.svg` / PNG). **Not** the live `princeton-logo-copy-resized.png`.
- Hero / gallery: Unsplash + Pexels stock shop, engine, lounge, and coffee imagery. Captions say stock stand-in.
- Omitted: customer gallery (coffee station / waiting area / shop in action photos), financing badge images, Mitchell1 Schedule/Specials/Reviews buttons, WP Engine chrome.

## Reviews

- Reviews page copy (3Rs) as published.
- SureCritic outbound link as published: https://www.surecritic.com/reviews/princeton-car-care
- Homepage recently-serviced notes (GARY K., KARLA, TIBURCIO A., TERRY C.) as published. No invented quotes or star widgets.

## Specials (published; expire 10/6/2026)

Back to School $149.99 · Heat–A/C check $24.99 · Oil change $24.99 / $42.99 · 4-wheel alignment from $59.99 · State inspection $18.50.

## 508

- Skip link; `:focus-visible`; 44×44 nav/form/CTA targets.
- Gold CTAs use navy `#043f69` label (not white-on-gold).
- Hero plate is opaque blue-gray under the full H1 so white heading meets AA.
- Forms have visible labels; errors are not color-only.
- Mobile header hides the Schedule pill so the generic lockup does not overflow; sticky callbar is Call only.

## Out of scope

- Flavia’s, Princeton Smiles, Best Price (separate agents).
- Do not merge. Matthew merges.
