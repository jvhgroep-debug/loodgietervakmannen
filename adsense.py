"""Keep the owner's AdSense snippet in every generated page head."""
from pathlib import Path

CLIENT = 'ca-pub-1125623842987786'
SNIPPET = f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={CLIENT}" crossorigin="anonymous"></script>'

def install(root=Path('dist')):
    for path in root.rglob('index.html'):
        html = path.read_text()
        if SNIPPET not in html:
            assert '</head>' in html, path
            path.write_text(html.replace('</head>', SNIPPET + '</head>', 1))

if __name__ == '__main__':
    install()
