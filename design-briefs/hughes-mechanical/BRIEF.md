# Hughes Mechanical — design brief

**Assigned live URL:** https://www.hughes-mech-elect.com/ — **blocked** (TLS handshake / unreachable from box; see `live-assigned-host-attempt.png`).  
**Live reference used:** https://www.hughescontractorsllc.com/ (current brand Wix site; same phone/address/team).  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/hughes-mechanical/  
**Capture note:** browserUse Task not available to this worker; headless Chrome screenshots saved instead.

**Vibe match: 4/10** — Rebuild is polished navy scaffold with coral CTAs and a KPI panel; live is punchy trade branding: deep navy fields, **script “Hughes” wordmark**, **bright yellow** accents, yellow circular bug/logo, photo team block, and denser service cards on textured backgrounds. Same trade intent, different brand costume.

## 1. Vibe match score
**4/10** — Colors and hero/nav density diverge (coral vs yellow+orange; serif/scaffold panel vs script+photo hero).

## 2. Color tokens from LIVE (hex)
| Token | Hex | Notes |
| --- | --- | --- |
| `--brand` | `#112F5B` | Dominant navy (also `#0a192f`–`#151e2d` in hero washes) |
| `--brand-2` | `#D64000` | Orange CTA / contact accents |
| `--accent` | `#FDF102` | Yellow chips, “since 1970” line, CONTACT US buttons |
| `--cta-mid` | `#2e57a6` / `#26468b` | Medium-blue “GET IN TOUCH” pill on hero |
| `--ink` | `#152033` | Body on light surfaces |
| `--muted` | `#5f6360` | Secondary |
| `--bg` | `#F2EAE7` | Warm page wash on light sections |
| `--surface` | `#ffffff` | Cards |
| `--hero-ink` | `#ffffff` | On navy |
| `--font-display` | brush/script for “Hughes” + condensed bold sans for trade lines | Live uses decorative script for brand name; body Arial/Helvetica/system sans |

## 3. Layout intent
- Dark navy chrome + large script **Hughes** + yellow circular logo/starburst in hero (right).
- Yellow all-caps tagline under wordmark; primary CTA medium-blue or yellow (not coral).
- Next band: team photo left + stacked **FAMILY OWNED / OPERATED / ORIENTED** right on textured navy.
- Services: icon cards over industrial photo; team name cards with yellow role text.
- Footer contact/address bar; phone always visible.
- **Keep existing logo/bug assets only** (wordmark + yellow circular mark) — do not invent a new mark.

## 4. Concrete CSS/HTML change list for Eng
1. `theme.css`: set `--brand:#112F5B`; `--brand-2:#D64000`; `--accent:#FDF102`; **remove coral `#e76f51`**.
2. `.btn-primary` → orange `#D64000` + white text (or yellow `#FDF102` + navy text for secondary “CONTACT US”); drop coral fill.
3. Hero: prefer live structure — large script/wordmark treatment for “Hughes”, yellow tagline, logo mark on right; optional reduce scaffold KPI panel or restyle panel to navy/yellow border (not orange glow).
4. Remove / soften orange radial glow + technical grid if it reads “template”; live uses photo textures and solid navy.
5. Header: navy bar, white nav, Call CTA in orange or mid-blue; keep `assets/wordmark.png` / `assets/logo.png` only.
6. About band: restore two-column team photo + FAMILY OWNED stack if assets exist in rebuild `assets/`.
7. Services cards: darker navy translucent cards + yellow icons/labels; denser all-caps titles.
8. Fonts: keep sans for UI; allow script only for the published “Hughes” wordmark image (do not fake a new script webfont if wordmark PNG covers it).
9. Confirm real content: (817) 461-9241, sales@hughes-mech-elect.com, 423 Dodson Lake Drive, team names as published — no lorem.

## 5. 508 notes
- Yellow `#FDF102` on white fails for body text — use on navy only, or as button bg with `#112F5B` text and verify ≥4.5:1.
- Orange `#D64000` + white: check button contrast.
- Keep skip link (rebuild improvement over live).
- Decorative hero pattern must not drop text contrast; team photos need meaningful `alt`.
- `tel:` / `mailto:` links with visible text; focus rings light on navy.

## 6. What to keep
- Existing logo/wordmark assets only.
- Real HVAC + electrical + lighting + refrigeration service list.
- Published team names/roles; 24/7 phone messaging; Arlington address.
- Sell-as-is polish — no new brand costume, no demo copy.


---

## Content / nav / image / favicon parity (HTML inventory fold)

_Built from `/workspace/dfw-parity/` live HTML for `hughes-mechanical` (supersede if formal Scout `.md` arrives)._  
**Live:** https://www.hughescontractorsllc.com/  
**Title:** Hughes Mechanical and Electrical Contractors | Dallas-Fort Worth HVAC Contractor | Arlington, TX

### Primary nav
1. **Home** → `/`
2. **Services**
3. **About**
4. **FAQ**
5. **Contact** / Call CTA

Wix anchors may become pages if labels + published team/services content stay reachable. Host = hughescontractorsllc.com (not hughes-mech-elect.com).


### Key images / heroes
- `https://static.wixstatic.com/media/418722_1993efe25fa844e78dc0c9d5d5d1a62c~mv2.png/v1/fill/w_100,h_56,al_c,q_85,usm_0.66_1.00_0.01,blur_3,enc_avif,quality_auto/418722_1993efe25fa844e78dc0c9d5d5d1a62c~mv2.png`
- `https://static.wixstatic.com/media/418722_1095a3e8f6cf4b29a3b86fda28c8d80a~mv2.png/v1/crop/x_4335,y_3146,w_1701,h_565/fill/w_49,h_16,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/Hughes%20Mechanical%20Full%20Logo%20%E2%80%93%20White%20with%20Colored%20Bug%20%E2%80%93%20No%20LLC.png`
- `https://static.wixstatic.com/media/418722_294b4fb63f0648dcbc6231ee89f37f35~mv2.png/v1/fill/w_160,h_90,al_c,q_85,usm_0.66_1.00_0.01,blur_3,enc_avif,quality_auto/418722_294b4fb63f0648dcbc6231ee89f37f35~mv2.png`
- `https://static.wixstatic.com/media/418722_294b4fb63f0648dcbc6231ee89f37f35~mv2.png/v1/fill/w_100,h_56,al_c,q_85,usm_0.66_1.00_0.01,blur_3,enc_avif,quality_auto/418722_294b4fb63f0648dcbc6231ee89f37f35~mv2.png`
- `https://static.wixstatic.com/media/418722_53973c441a104dfb9d71612a8f068690~mv2.jpg/v1/fill/w_147,h_83,al_c,q_80,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/Profile%20(1).jpg`
- `https://static.wixstatic.com/media/418722_93e6e1ccd46d41c1906ca378aca87f07~mv2.png/v1/fill/w_100,h_56,al_c,q_85,usm_0.66_1.00_0.01,blur_3,enc_avif,quality_auto/418722_93e6e1ccd46d41c1906ca378aca87f07~mv2.png`
- `https://static.wixstatic.com/media/418722_72342bbe43d942fc9617ed8855750d63~mv2.png`
- `https://static.wixstatic.com/media/418722_72342bbe43d942fc9617ed8855750d63~mv2.png/v1/fill/w_73,h_67,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/Hughes%20Mechanical%20Logo%20Bug.png`
- `https://static.wixstatic.com/media/418722_c717935a8ed14ccf841b74587de0f812~mv2.png/v1/fill/w_160,h_73,al_c,q_85,usm_0.66_1.00_0.01,blur_3,enc_avif,quality_auto/418722_c717935a8ed14ccf841b74587de0f812~mv2.png`
- `https://static.wixstatic.com/media/418722_93e6e1ccd46d41c1906ca378aca87f07~mv2.png/v1/fill/w_160,h_90,al_c,q_85,usm_0.66_1.00_0.01,blur_3,enc_avif,quality_auto/418722_93e6e1ccd46d41c1906ca378aca87f07~mv2.png`
- `https://static.wixstatic.com/media/418722_1993efe25fa844e78dc0c9d5d5d1a62c~mv2.png/v1/fill/w_160,h_90,al_c,q_85,usm_0.66_1.00_0.01,blur_3,enc_avif,quality_auto/418722_1993efe25fa844e78dc0c9d5d5d1a62c~mv2.png`
- `https://static.wixstatic.com/media/418722_1095a3e8f6cf4b29a3b86fda28c8d80a~mv2.png/v1/crop/x_4447,y_3189,w_1582,h_468/fill/w_49,h_14,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/Hughes%20Mechanical%20Full%20Logo%20%E2%80%93%20White%20with%20Colored%20Bug%20%E2%80%93%20No%20LLC.png`

### Favicon
- `https://static.wixstatic.com/media/418722_72342bbe43d942fc9617ed8855750d63%7Emv2.png/v1/fill/w_192%2Ch_192%2Clg_1%2Cusm_0.66_1.00_0.01/418722_72342bbe43d942fc9617ed8855750d63%7Emv2.png`
- `https://static.wixstatic.com/media/418722_72342bbe43d942fc9617ed8855750d63%7Emv2.png/v1/fill/w_32%2Ch_32%2Clg_1%2Cusm_0.66_1.00_0.01/418722_72342bbe43d942fc9617ed8855750d63%7Emv2.png`
- `https://static.wixstatic.com/media/418722_72342bbe43d942fc9617ed8855750d63%7Emv2.png/v1/fill/w_180%2Ch_180%2Clg_1%2Cusm_0.66_1.00_0.01/418722_72342bbe43d942fc9617ed8855750d63%7Emv2.png`

### Capture notes
Keep published Wix logo/bug + team photos. Tokens: navy #112F5B, orange #D64000, yellow #FDF102.

