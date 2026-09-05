# Shared scaffold

`styles.css` and `site.js` are the source files for every site.

Each folder under `sites/<slug>/` includes its own copies so that folder can be zipped and opened alone. After you edit the shared files, recopy them:

```bash
python3 scaffold/build.py
```

That rebuilds every `sites/<slug>/*.html` and refreshes the copied CSS/JS. Logos in `sites/<slug>/assets/` are left in place.
