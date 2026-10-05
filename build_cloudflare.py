"""Prepare the checked-in static site for Cloudflare Pages; never deploy."""
from pathlib import Path
import hashlib
import json
import re
import shutil
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
source = ROOT / 'dist'
output = ROOT / 'cloudflare-dist'
baseline = json.loads((ROOT / 'migration/baseline.json').read_text())
for name, digest in baseline.items():
    path = source / name
    if not path.is_file():
        raise SystemExit(f'Ontbrekend bestaand bestand: {name}')
pages = sorted(source.rglob('index.html'))
routes = {'/' + str(p.parent.relative_to(source)).strip('.') .strip('/') + '/' for p in pages}
routes.discard('//')
routes.add('/')
locations = [n.text for n in ET.parse(source / 'sitemap.xml').getroot().findall('{*}url/{*}loc')]
assert {urlsplit(u).path for u in locations} == routes, 'Sitemap en routes verschillen'
for page in pages:
    html = page.read_text()
    assert len(re.findall(r'<h1\b', html)) == 1, page
    assert '<link rel="canonical"' in html and '<meta name="description"' in html, page
    for ref in re.findall(r'(?:href|src)=["\']([^"\']+)', html) + re.findall(r'url\(["\']?([^\)"\']+)', html):
        parsed = urlsplit(ref)
        if parsed.scheme or parsed.netloc or not parsed.path.startswith('/'):
            continue
        target = source / unquote(parsed.path).lstrip('/')
        assert target.is_file() or (target / 'index.html').is_file(), f'{page}: ontbrekend {ref}'
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        json.loads(block)
if output.exists():
    shutil.rmtree(output)
shutil.copytree(source, output)
# A real 404 prevents Pages from treating this multi-page site as an SPA.
(output / '404.html').write_text('<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pagina niet gevonden | Loodgieter Vakmannen</title></head><body><h1>Pagina niet gevonden</h1><p><a href="/">Terug naar Loodgieter Vakmannen</a></p></body></html>\n')
for path in source.rglob('*'):
    if path.is_file():
        assert path.read_bytes() == (output / path.relative_to(source)).read_bytes()
unchanged = sum(hashlib.sha256((source / name).read_bytes()).hexdigest() == digest for name, digest in baseline.items())
print(f'OK: {len(pages)} pagina\u2019s, {len(locations)} sitemap-URL\u2019s; alle bestanden exact gekopieerd. {unchanged}/{len(baseline)} bestanden gelijk aan migratiebaseline.')
