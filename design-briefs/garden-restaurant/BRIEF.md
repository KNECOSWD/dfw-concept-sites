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

## Content / nav / image / favicon parity (Scout fold — authoritative)

_Folded from `/workspace/dfw-parity/garden-restaurant.md` (Scout public HTML inventory, 2026-09-05). Supersedes thinner nav/image lists above for Eng._

## garden-restaurant

Source: https://gardenrestaurantgarland.com/ (public homepage HTML via curl, 2026-09-05). URLs below are copied as present in live markup (including `//about.php` double-slash paths). Never invented.

**Live title:** Garden Restaurant3555 W Walnut St, Garland, TX 75042, USAChinese Restaurant

### Primary nav (with dropdown children)

**Desktop primary** — `<nav class="d-none d-xl-flex">` → `<ul class="d-flex">` (no dropdown children in HTML):

1. **Home** → `https://gardenrestaurantgarland.com/`
2. **About Us** → `https://gardenrestaurantgarland.com//about.php`
3. **Menu** → `https://gardenrestaurantgarland.com//menu.php`
4. **Gallery** → `https://gardenrestaurantgarland.com//gallery.php`
5. **Contact** → `https://gardenrestaurantgarland.com//contact.php`

**Mobile primary** — `<nav class="list-bk">` → `<ul class="js-mob-list">`: same five labels/hrefs as desktop (no dropdown children).

**Mobile social row** (sibling `<ul class="social-menu">`, not a page nav item): Facebook → `https://www.facebook.com/profile.php?id=100060537861254`

**Header CTA (outside primary `<ul>`, present in header chrome):** **Order PickUp | Delivery** → `https://zingmyorder.com/restaurants/garden-restaurant-3555-w-walnut-st-garland-tx-75042-usa` *(absolute ZingMyOrder order URL; also appears in mobile chrome)*

**Footer menu** — `ul.footer-menu` (distinct from primary; includes pages not in header nav):

1. **Home** → `https://gardenrestaurantgarland.com/`
2. **About Us** → `https://gardenrestaurantgarland.com//about.php`
3. **Menu** → `https://gardenrestaurantgarland.com//menu.php`
4. **Events** → `https://gardenrestaurantgarland.com//events.php`
5. **Order PickUp | Delivery** → `https://gardenrestaurantgarland.com//online.php`
6. **Contact** → `https://gardenrestaurantgarland.com//contact.php`

**Dropdown children:** none in primary nav DOM (flat lists only).

### Key images / heroes

| Role | Absolute URL | Notes from live HTML |
| --- | --- | --- |
| **Logo** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/112515226/logo/UVXZFh3yQh7WE5ForJIgmGreBvkghbn5wnYi26dj.png` | `img` alt `logo` (header + repeats overlaying banners / footer) |
| **Hero / banner slide 1 (desktop)** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113302335/banner_image/SCdpmHt0xRYj25VJnZVwGgAwWPwTrSMpx8Qmm31V.jpg` | Homepage `banner_image` |
| **Hero / banner slide 2 (desktop)** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113302335/banner_image/3HdKB1JWeOk45SyFq9qMQAkxWVhejjpwFio8FutE.jpg` | Homepage `banner_image` |
| **Hero / banner slide 3 (desktop)** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113319427/banner_image/BtsCC44nhJv9qrf1uv9xw7RIzLn3vSkchoy4DME6.jpg` | Homepage `banner_image` |
| **Hero / banner mobile 1** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113509679/banner_mobile_image/1DMe6BYF9M4ZRDsIE54Om8brUQvwVcwffKTKSN17.jpg` | `banner_mobile_image` |
| **Hero / banner mobile 2** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113509679/banner_mobile_image/n2xHn7KYjUHKzEPXUbv5X7o5ZVhlZ9ioDg3kPq2j.jpg` | `banner_mobile_image` |
| **Hero / banner mobile 3** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113509679/banner_mobile_image/q6yXNfTegyhKbnLm6zjKZu3huyuEv8W11H6ComBW.jpg` | `banner_mobile_image` |
| **About / specialties side image** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/112435541/specialities_image/MDjO6KqHxioEBRe4U9UserH3HPmsjhvUksDbPHzq.jpg` | `section.about-section` `img` alt `gallery bg image` |
| **Homepage gallery thumb 1** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113727813/website_gallery/jvetvaa6rMyomfUpc0YDeGIRTT03fnpLCgHy7YIH.jpg` | alt `gallery image` |
| **Homepage gallery thumb 2** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113727813/website_gallery/G3x5gchafpjj7lFFuIZDHWc594rehgB922cQWdbq.jpg` | alt `gallery image` |
| **Homepage gallery thumb 3** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113727813/website_gallery/vlKUOjnag5ekM3LSFcclnKzedldDd7Jrb0260rQ5.jpg` | alt `gallery image` |
| **Homepage gallery thumb 4** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113727813/website_gallery/hsHfVHAvyApT4ngdgzeOYAwUgVDvdfGi0UuZjXrF.jpg` | alt `gallery image` |
| **Homepage gallery thumb 5** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113727813/website_gallery/7aIOGvwcxjLItdtBHrmg00p0pw5WaHNGDecER1Gz.jpg` | alt `gallery image` |
| **Homepage gallery thumb 6** | `https://site.zingmyorder.com/image/original/website/website/2024/12/12/113727813/website_gallery/wZCA6xOr0YyoZPzjv51lHaUJEQBYjyVruNtnA9pt.jpg` | alt `gallery image` |

**Present but not brand/hero:** `https://site.zingmyorder.com/image-captcha` (`img.img-fluid` captcha endpoints).

### Favicon

- **No `<link rel="icon">`, `shortcut icon`, or `apple-touch-icon` in homepage HTML.**
- **Site-root probe:** `https://gardenrestaurantgarland.com/favicon.ico` → HTTP **404** (checked via HEAD).
- No favicon URL declared on the public homepage markup.

### Capture notes

- Platform: ZingMyOrder website builder (`site.zingmyorder.com` / `website.zingmyorder.com`, design33 theme).
- Captured from public homepage HTML only. No invented labels or URLs.
- Many internal page hrefs use a literal double slash after the host (`…com//about.php`); reported as in source.
- Footer adds **Events** and a site-relative **Order** URL (`//online.php`) not in the desktop primary five.


### Favicon (Eng — logo-derived)
- Live declares **no** favicon link; `favicon.ico` → 404.
- **Derive favicon from published logo** (do not invent a mark):
  - Logo URL: `https://site.zingmyorder.com/image/original/website/website/2024/12/12/112515226/logo/UVXZFh3yQh7WE5ForJIgmGreBvkghbn5wnYi26dj.png`
  - Local capture already at: `/workspace/dfw-design-briefs/favicons/garden-restaurant.png`
  - Ship 16/32/180 from that logo asset.


