# Shared scaffold

`styles.css` and `site.js` are the source files for every concept site.

Each folder under `sites/<slug>/` already includes its own copies so that folder can be zipped and opened alone. After you edit the shared files, recopy them:

```bash
python3 scaffold/build.py
```

That rebuilds every `sites/<slug>/index.html` and refreshes the copied CSS/JS.
