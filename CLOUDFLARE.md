# Loodgieter Vakmannen — externe deployment

De website is statische HTML/CSS/JavaScript. `dist/` bevat de volledige,
ingecheckte website en alle afbeeldingen. De Python-contentbuilders gebruiken
`dist/index.html` als template; `dist/` mag daarom niet worden verwijderd of
uit Git worden uitgesloten. Er zijn geen externe Python-pakketten, Node-modules,
serverfuncties, databases of secrets nodig.

## Cloudflare Pages via GitHub

| Instelling | Waarde |
| --- | --- |
| Framework preset | None |
| Production branch | main |
| Root directory | leeg (repository-root) |
| Build command | `python3 build_cloudflare.py` |
| Build output directory | `cloudflare-dist` |
| Environment variable | `PYTHON_VERSION=3.12` |

De build controleert sitemap, routes, metadata, lokale verwijzingen en JSON-LD.
Hij kopieert alle bestaande bestanden byte voor byte en voegt uitsluitend een
404-pagina aan de externe output toe. GitHub Actions voert dezelfde controle
uit, maar deployt niets. Koppel de repository later rechtstreeks aan Pages.

## Wat behouden blijft

34 pagina's met bestaande URL's, titles, descriptions, canonicals, social
metadata, schema, sitemap, robots, afbeeldingen, logo's en AdSense-code.
Formulieren maken een WhatsApp-bericht voor `31684002350`; de bezoeker
verstuurt het zelf. Er is geen servergestuurde formuliermail.

Absolute SEO- en deelafbeeldings-URL's blijven `https://loodgietervakmannen.nl`.
Op een tijdelijke Pages-preview verwijzen die dus bewust naar het live domein.

## Contentbeheer

Wijzig content en run waar nodig achtereenvolgens `python3 build_pages.py`,
`python3 build_service_pages.py` en `python3 build_blog.py`.
Controleer de resulterende diff en commit ook `dist/`. De migratiebuild draait
deze generators bewust niet: de huidige pagina's zijn de gezaghebbende bron.
`migration/baseline.json` bewaart de SHA-256-hashes van de oorspronkelijke
bestanden. Latere bewuste contentwijzigingen hoeven niet dezelfde hash te houden.

## Veilig vervolg

1. Importeer het voorbereide pakket in een eigen GitHub-repository.
2. Maak een Pages-project met bovenstaande instellingen, zonder custom domain.
3. Controleer de Pages-preview: desktop/mobiel, alle routes, formulieren,
   gemeenteselectie, WhatsApp, logo's en afbeeldingen; controleer ook de 404.
4. Beslis pas daarna over het verbinden van het domein en DNS.

Deze voorbereiding heeft niets gedeployd, geen DNS gewijzigd en geen domein
losgekoppeld. Laat de huidige Sites-hosting beschikbaar tot een migratie later
volledig is gecontroleerd. MX/SPF/DKIM voor e-mail vallen buiten deze migratie.

## GitHub-export

Het exportpakket bevat source, `dist/`, buildcontrole, baseline en deze uitleg,
maar geen Sites-projectidentiteit, Git-historie, tokens, oude archieven of cache.
De bestaande Sites-checkout en zijn Git-remote blijven intact.
