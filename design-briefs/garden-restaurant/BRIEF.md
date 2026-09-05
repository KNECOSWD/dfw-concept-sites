# Garden Restaurant — design brief

**Live:** https://gardenrestaurantgarland.com/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/garden-restaurant/  
**Vibe match: 3/10** — Rebuild invented banquet red `#8b1e1e`. Live is **teal `#18A687` CTAs + gold `#B8A51C`** on a **dark food-photo hero** with outlined “GARDEN RESTAURANT” wordmark and Order PickUp | Delivery. Standing rule: match live vibe/colors — do **not** keep Chinese-red invent.

## Color tokens (LIVE — use these)
| Token | Hex |
| --- | --- |
| `--brand` | `#18A687` |
| `--brand-2` / accent | `#B8A51C` |
| `--ink` | `#343a40` / `#334152` |
| `--muted` | `#495057` |
| `--bg` | `#ffffff` / `#f7f7f7` |
| `--surface` | `#ffffff` |
| `--hero-ink` | `#ffffff` |
| `--font-display` | `"Nunito Sans", system-ui, sans-serif` |

## Layout intent
- Modern order-forward restaurant: food photography hero, teal Order CTAs, Menu / About / Gallery / Contact.
- Keep existing logo asset; keep full priced menu content.
- About/Events stay thin as live — don’t pad.

## Eng change list
1. `theme.css`: replace `--brand #8b1e1e` with `#18A687`; gold `#B8A51C` (not only `#d4a017`).
2. `.btn-primary` / header Order CTA → teal fill, white text.
3. Hero: published food photo + dark wash (not solid red gradient); white wordmark energy.
4. Add “Order PickUp | Delivery” text/button pattern linking to live order path if already in content — no new outreach forms.
5. Fonts → Nunito Sans stack; drop deep-red banquet vibe.
6. Gallery nav only if real assets exist.

## Keep
- Menu prices; phone (972) 487-8289; email; logo; no fake reviews.

## 508 notes
- Gold `#B8A51C` on white fails for small text — dark ink for prices; gold for large accents.
- Teal buttons + white text: verify ≥4.5:1.
- Food hero: descriptive `alt` or empty if pure decorative under text.
- Form labels; keyboardable any carousel.
