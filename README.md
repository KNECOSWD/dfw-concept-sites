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

## Shared scaffold

- [`scaffold/styles.css`](scaffold/styles.css) — layout, mobile nav, forms
- [`scaffold/site.js`](scaffold/site.js) — menu + on-page form confirmation (does not email the business)
- [`scaffold/build.py`](scaffold/build.py) — rebuilds all 10 folders from the shared files

```bash
python3 scaffold/build.py
```

Contact forms stay on the page. They do not email, store, or submit to the businesses. Please call so the office receives the request.

## Source notes

- **Logos** are the businesses’ existing marks downloaded from their live sites (or the public Wayback copy for Ferraro) and stored under `sites/<slug>/assets/`.
- **Beyond Lawn Care** embeds Google reviews via Elfsight. Review text is not in the HTML and was not invented.
- **Hughes Mechanical** publishes no customer reviews. None were added. Wix placeholder socials were ignored.
- **CareMaster** current pages list (469) 233-3366 and customerservice@caremaster.biz. No street address is published on those pages.
- **Ferraro DDS** live site returned Cloudflare 403. Content, the published logo (`…00551Dentallogodesign…png`), and the doctor photo come from the public October 2025 archive / practice CDN. Hours used: Monday–Thursday 8–5. Friday is blank on the source. Email: danielferrarodds@sbcglobal.net. One published quote (Mrs. Conger). Top Rated Doctors 2016.
- **B&B Complete Auto** reviews are Elfsight JS only. Gallery is empty. No reviews or photos were invented. License CO16-0388.
- **Garden Restaurant** menu is the full priced list from `/menu.php` (10 categories). No site reviews. About/Events stay thin.
- **Len Conner** homepage testimonials only (Marie, Marc and Jill, David, Dena, Kelly). `/testimonials/` is 404. No public email or hours. Super Lawyers, Avvo, and Best in Irving 2022 badges from the live site.
- **Speake's** homepage slider labels MashIt / FabuFit / YesSuits are template chrome, not used as company names.
