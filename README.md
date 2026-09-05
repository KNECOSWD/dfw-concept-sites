# KNECO DFW concept sites

Ten static marketing mocks for a **$500 DFW concept test**.  
Matthew Sullivan / KNECOSWD.

These pages are **concept demos / not the live business sites**.  
**$0 Azure:** no App Service, no Azure resources, no custom domains, no paid hosting.  
**No outreach:** no emails, calls, or live-site form submissions were made.

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

Each folder under `sites/` is self-contained (`index.html`, `styles.css`, `theme.css`, `site.js`).

```bash
cd sites
zip -r speakes-plumbing.zip speakes-plumbing
```

Unzip and open `index.html`. No build step, no node, no Azure.

## GitHub Pages

Publish this repo root (or `/docs` if you copy the files there). The gallery at `/` links to `/sites/<slug>/`.

## The 10 paths

| # | Business | City | Folder |
| --- | --- | --- | --- |
| 1 | Speake's Plumbing | Garland | [`sites/speakes-plumbing/`](sites/speakes-plumbing/) |
| 2 | Beyond Lawn Care | Mesquite | [`sites/beyond-lawn-care/`](sites/beyond-lawn-care/) |
| 3 | Hughes Mechanical | Arlington | [`sites/hughes-mechanical/`](sites/hughes-mechanical/) |
| 4 | Victory Pest Control | Red Oak / DeSoto | [`sites/victory-pest-control/`](sites/victory-pest-control/) |
| 5 | CareMaster Building | Dallas | [`sites/caremaster-building/`](sites/caremaster-building/) |
| 6 | Forum Terrace Church of Christ | Grand Prairie | [`sites/forum-terrace-church/`](sites/forum-terrace-church/) |
| 7 | B&B Complete Auto | Garland | [`sites/bb-complete-auto/`](sites/bb-complete-auto/) |
| 8 | Daniel L. Ferraro, D.D.S. | Grand Prairie | [`sites/ferraro-dds/`](sites/ferraro-dds/) |
| 9 | Garden Restaurant | Garland | [`sites/garden-restaurant/`](sites/garden-restaurant/) |
| 10 | Law Office of Len Conner | Irving | [`sites/len-conner-law/`](sites/len-conner-law/) |

## Shared scaffold

- [`scaffold/styles.css`](scaffold/styles.css) — layout, mobile nav, forms
- [`scaffold/site.js`](scaffold/site.js) — menu + demo form (never posts)
- [`scaffold/build.py`](scaffold/build.py) — rebuilds all 10 folders from the shared files

```bash
python3 scaffold/build.py
```

## Research notes

Public homepages were fetched for name, phone, services, and tone. Reviews on each mock are **labeled placeholders**. License numbers are included only when the business published them. If a street address was not on the public homepage, the mock marks it as a **placeholder**. Church and veteran-owned language does **not** impersonate government or VA.

Contact forms only show an on-page confirmation. They do not email, store, or submit to the businesses.
