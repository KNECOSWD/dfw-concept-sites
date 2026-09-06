# DFW site rebuilds

Ten static website rebuilds for local Dallas–Fort Worth businesses.  
Each folder under `sites/` is a finished site Matthew can open or zip and sell as-is.

**$0 Azure.** No App Service, no custom domains, no paid hosting.  
**No outreach.** Public pages were fetched only. No emails, calls, or live-site form submissions.

## Open locally

From this repo root:

```bash
python3 -m http.server 8080
```

Then open [http://127.0.0.1:8080/](http://127.0.0.1:8080/).

Or open any file directly:

- Gallery: `index.html`
- A single site: `sites/<slug>/index.html`

## Zip one site

Each folder under `sites/` is self-contained (`index.html`, extra pages, `styles.css`, `theme.css`, `site.js`, `assets/`).

```bash
cd sites
zip -r speakes-plumbing.zip speakes-plumbing
```

Unzip and open `index.html`. No build step, no Node, no Azure.

## GitHub Pages

Publish this repo root. Keep `.nojekyll`. The gallery at `/` links to `/sites/<slug>/`.

Preview URLs:

1. https://knecoswd.github.io/dfw-concept-sites/sites/speakes-plumbing/
2. https://knecoswd.github.io/dfw-concept-sites/sites/beyond-lawn-care/
3. https://knecoswd.github.io/dfw-concept-sites/sites/hughes-mechanical/
4. https://knecoswd.github.io/dfw-concept-sites/sites/victory-pest-control/
5. https://knecoswd.github.io/dfw-concept-sites/sites/caremaster-building/
6. https://knecoswd.github.io/dfw-concept-sites/sites/forum-terrace-church/
7. https://knecoswd.github.io/dfw-concept-sites/sites/bb-complete-auto/
8. https://knecoswd.github.io/dfw-concept-sites/sites/ferraro-dds/
9. https://knecoswd.github.io/dfw-concept-sites/sites/garden-restaurant/
10. https://knecoswd.github.io/dfw-concept-sites/sites/len-conner-law/
11. https://knecoswd.github.io/dfw-concept-sites/sites/princeton-smiles/
12. https://knecoswd.github.io/dfw-concept-sites/sites/best-price-tires/
13. https://knecoswd.github.io/dfw-concept-sites/sites/flavias-beauty/

## The 10 sites

| # | Business | City | Folder |
| --- | --- | --- | --- |
| 1 | Speake's Plumbing, Inc. | Garland | [`sites/speakes-plumbing/`](sites/speakes-plumbing/) |
| 2 | Beyond Lawn Care & Landscaping | Mesquite | [`sites/beyond-lawn-care/`](sites/beyond-lawn-care/) |
| 3 | Hughes Mechanical and Electrical | Arlington | [`sites/hughes-mechanical/`](sites/hughes-mechanical/) |
| 4 | Victory Pest Control LLC | DFW | [`sites/victory-pest-control/`](sites/victory-pest-control/) |
| 5 | CareMaster Building Services | Dallas / Fort Worth | [`sites/caremaster-building/`](sites/caremaster-building/) |
| 6 | Forum Terrace Church of Christ | Grand Prairie | [`sites/forum-terrace-church/`](sites/forum-terrace-church/) |
| 7 | B&B Complete Auto Repair | Garland | [`sites/bb-complete-auto/`](sites/bb-complete-auto/) |
| 8 | Daniel L. Ferraro, D.D.S. | Grand Prairie | [`sites/ferraro-dds/`](sites/ferraro-dds/) |
| 9 | Garden Restaurant | Garland | [`sites/garden-restaurant/`](sites/garden-restaurant/) |
| 10 | Law Office of Len Conner | Irving | [`sites/len-conner-law/`](sites/len-conner-law/) |
| — | Princeton Smiles Dentistry (independent sales unit) | Princeton | [`sites/princeton-smiles/`](sites/princeton-smiles/) |
| — | Best Price Tires & Auto (independent sales unit) | Princeton | [`sites/best-price-tires/`](sites/best-price-tires/) |
| — | Flavia's Beauty Salon & Barber Shop (independent sales unit) | Princeton | [`sites/flavias-beauty/`](sites/flavias-beauty/) |

## Shared scaffold

- [`scaffold/styles.css`](scaffold/styles.css) — layout, mobile nav, forms
- [`scaffold/site.js`](scaffold/site.js) — menu + on-page form confirmation (does not email the business)
- [`scaffold/build.py`](scaffold/build.py) — rebuilds all 10 folders from the shared files

```bash
python3 scaffold/build.py
```

Contact forms stay on the page. They do not email, store, or submit to the businesses. Please call so the office receives the request.

## Source notes

- **Logos** are the businesses’ existing marks, downloaded from the specified live URLs and stored under `sites/<slug>/assets/`.
- **Speake's** logo is `077-162h.png`. Grant Speake, Master Plumber #16836, est. 1987. 633 N 5th St, Garland; 972-271-9144; Mon–Fri 7–5; spi87@icloud.com and grantspeake@verizon.net. Testimonials are published quotes only. MashIt / FabuFit / YesSuits slider labels were not used.
- **Beyond Lawn Care** logo is `BEYOND-1920w.png`. 972-803-7495; Info@beyondlawncares.com; Mon–Fri 8–5, Sat 9–2; no street on Contact. Full commercial/residential service tree, published package price bands, and the live gallery photos. Google reviews load via the published Elfsight widget only — review text was not invented.
- **Hughes Mechanical** live site is hughescontractorsllc.com (not hughes-mech-elect.com). Wordmark and bug are the published Wix files. 817-461-9241; the live page still lists sales@hughes-mech-elect.com; 423 Dodson Lake Dr, Arlington. HVAC plus electrical, lighting, and refrigeration. Team names as published. No reviews. Wix Studio social placeholders ignored.
- **Victory Pest Control** uses the brand VPC logo (`victory-pest-control-llc-logo-0510bb09-1920w.jpg`), not the Hibu template gen-logo. Owner John Gaines. (972) 230-5526 / mobile (214) 543-6357. 234 Paradise Way, Red Oak, TX 75154. 24 hours. No email. Reviews only: Taylor Akin, Camille Henderson, Michelle Owens. Live “Lorem Ipsum” tagline and `{{placeholder_*}}` tokens were not copied.
- **CareMaster** logo is `logo-2.jpg` from nccdn. Since 1982; Richard Lee / President John Lee. 469.233.3366; customerservice@caremaster.biz; PO Box 29303, Dallas, TX 75229. No reviews. Street hours are not published.
- **Forum Terrace** logo is `cropped-FTCoC_Logo_646x200.png`. 2446 Arkansas Lane; Dan Vess (972) 922-3249; Sun 9:30 / 10:30 / 5:00 and Wed 7:30. Tracts, sermons, workbooks, and bulletins are links to the live HTTP pages. Member directory is gated and skipped. No reviews or email.
- **Ferraro DDS** live site returned Cloudflare 403. Content, the published logo (`…00551Dentallogodesign…png`), and the doctor photo come from the public October 2025 archive / practice CDN. Hours used: Monday–Thursday 8–5. Friday is blank on the source. Email: danielferrarodds@sbcglobal.net. One published quote (Mrs. Conger). Top Rated Doctors 2016.
- **B&B Complete Auto** reviews are Elfsight JS only. Gallery is empty. No reviews or photos were invented. License CO16-0388.
- **Garden Restaurant** menu is the full priced list from `/menu.php` (10 categories). No site reviews. About/Events stay thin.
- **Len Conner** homepage testimonials only (Marie, Marc and Jill, David, Dena, Kelly). `/testimonials/` is 404. No public email or hours. Super Lawyers, Avvo, and Best in Irving 2022 badges from the live site.
- **Princeton Smiles** is an independent $500 sales unit (not one of the original ten). Generic wordmark + Unsplash clinical stock only — no live logo, doctor photo, or live favicon. Form does not email princetonsmiles@gmail.com. Live Wylie emergency blurb omitted (NAP conflict). Four homepage quotes only. Do not confuse with NJ princetonsmile.com.
- **Best Price Tires & Auto** is an independent $500 sales unit (not one of the original ten). Generic tire wordmark + stock bay/tire photos only — no customer logo, shop photos, financing badges, or live favicon. Forms stay on-page. No published shop email.
- **Flavia's Beauty** is an independent $500 sales unit. Generic “F” wordmark + stock salon/barber photos only — no customer logo, headshots, storefront photos, or live favicon. Dual Princeton Drive locations. Forms do not email the salon or create a LeadConnector booking. Footer uses flaviasbeautysalonandbarbershop.com only.
