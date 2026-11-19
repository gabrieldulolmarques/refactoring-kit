"""Prepare _docs for mkdocs: copy the tracked files, and make README the home page.
Usage: python .github/build_site.py  (run from the repository root)"""
import pathlib, shutil, subprocess

root = pathlib.Path.cwd()
docs = root / "_docs"
shutil.rmtree(docs, ignore_errors=True)
skip = (".github/", "mkdocs.yml", ".gitignore")
for name in subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout.splitlines():
    if not name.startswith(skip):
        (docs / name).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(root / name, docs / name)

(docs / "README.md").rename(docs / "index.md")
