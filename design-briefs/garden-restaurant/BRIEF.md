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


---

## Content / nav parity (HARD GATE)

**Parity status:** FAIL — Gallery + Order PickUp|Delivery missing from rebuild nav.

### Live nav map
- **Home** → `https://gardenrestaurantgarland.com/`
- **About Us** → `https://gardenrestaurantgarland.com/about.php`
- **Menu** → `https://gardenrestaurantgarland.com/menu.php`
- **Gallery** → `https://gardenrestaurantgarland.com/gallery.php`
- **Contact** → `https://gardenrestaurantgarland.com/contact.php`
- **Order PickUp | Delivery** → `https://zingmyorder.com/restaurants/garden-restaurant-3555-w-walnut-st-garland-t`



### Rebuild nav map (current)
- Home → `index.html`
- About Us → `about.html`
- Menu → `menu.html`
- Contact → `contact.html`

### Eng requirement
Restore **full live header IA** (every top item + dropdown children). Collapsing only OK if every destination stays reachable with the **same labels**. Do not strip Financing / service-area / deep service pages into a thin 4–5 link bar.

## Image inventory (Eng must incorporate)

Homepage (and linked gallery/team) assets from live — download into `assets/` and place in matching sections (hero / gallery / team / services). Do not leave pages image-thin vs live.

1. **logo** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/112515226/logo/UVXZFh3yQh7WE5ForJIgmGreBvkghbn5wnYi26dj.png` alt="logo"
2. **hero/banner** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113302335/banner_image/SCdpmHt0xRYj25VJnZVwGgAwWPwTrSMpx8Qmm31V.jpg`
3. **hero/banner** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113302335/banner_image/3HdKB1JWeOk45SyFq9qMQAkxWVhejjpwFio8FutE.jpg`
4. **hero/banner** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113319427/banner_image/BtsCC44nhJv9qrf1uv9xw7RIzLn3vSkchoy4DME6.jpg`
5. **hero/banner** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113509679/banner_mobile_image/1DMe6BYF9M4ZRDsIE54Om8brUQvwVcwffKTKSN17.jpg`
6. **hero/banner** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113509679/banner_mobile_image/n2xHn7KYjUHKzEPXUbv5X7o5ZVhlZ9ioDg3kPq2j.jpg`
7. **hero/banner** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113509679/banner_mobile_image/q6yXNfTegyhKbnLm6zjKZu3huyuEv8W11H6ComBW.jpg`
8. **content** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/112435541/specialities_image/MDjO6KqHxioEBRe4U9UserH3HPmsjhvUksDbPHzq.jpg` alt="gallery bg image"
9. **content** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113727813/website_gallery/jvetvaa6rMyomfUpc0YDeGIRTT03fnpLCgHy7YIH.jpg` alt="gallery image"
10. **content** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113727813/website_gallery/G3x5gchafpjj7lFFuIZDHWc594rehgB922cQWdbq.jpg` alt="gallery image"
11. **content** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113727813/website_gallery/vlKUOjnag5ekM3LSFcclnKzedldDd7Jrb0260rQ5.jpg` alt="gallery image"
12. **content** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113727813/website_gallery/hsHfVHAvyApT4ngdgzeOYAwUgVDvdfGi0UuZjXrF.jpg` alt="gallery image"
13. **content** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113727813/website_gallery/7aIOGvwcxjLItdtBHrmg00p0pw5WaHNGDecER1Gz.jpg` alt="gallery image"
14. **content** — `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113727813/website_gallery/wZCA6xOr0YyoZPzjv51lHaUJEQBYjyVruNtnA9pt.jpg` alt="gallery image"

Parsed homepage image count (raw): **15**. Also pull gallery/inner-page images when those routes are restored.

## Favicon

- **Live source:** `https://gardenrestaurantgarland.com/favicon.ico`
- **Local capture:** `/workspace/dfw-design-briefs/favicons/garden-restaurant.ico`
- **Note:** Ship this favicon (or logo-derived 32/180) — never invent a new mark.

