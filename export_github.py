"""Create a clean GitHub import archive without touching either Git remote."""
from pathlib import Path
import subprocess
import sys
import zipfile

root = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(root / 'build_cloudflare.py')], check=True)
target = root / 'github-export.zip'
files = list((root / 'dist').rglob('*'))
files += list((root / 'migration').rglob('*'))
files += list((root / '.github').rglob('*'))
files += list(root.glob('*.py'))
files += [root / 'CLOUDFLARE.md', root / '.gitignore']
with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(files):
        if path.is_file():
            archive.write(path, path.relative_to(root))
print(f'GitHub-import gereed: {target.name}')
