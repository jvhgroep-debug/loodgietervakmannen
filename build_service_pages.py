from pathlib import Path
from html import escape
from html.parser import HTMLParser

ROOT = Path('dist')
home = (ROOT / 'index.html').read_text()
css = home.split('<style>', 1)[1].split('</style>', 1)[0]
header = '<header class="top">' + home.split('<header class="top">', 1)[1].split('</header>', 1)[0] + '</header>'
header = header.replace('href="/#aanvraag"', 'href="#aanvraag"')
footer = '<footer class="foot">' + home.split('<footer class="foot">', 1)[1].split('</footer>', 1)[0] + '</footer>'
floatlink = '<a class="whatsapp-float"' + home.split('<a class="whatsapp-float"', 1)[1].split('</a>', 1)[0] + '</a>'
form = '<form class="card" id="leadForm">' + home.split('<form class="card" id="leadForm">', 1)[1].split('</form>', 1)[0] + '</form>'
script = '<script>' + home.split('<script>', 1)[1].split('</script>', 1)[0] + '</script>'

# Each city has its own practical context; no availability or pricing is implied.
CITIES = {
    'breda': {
        'name': 'Breda', 'area': 'Breda heeft zowel oudere woningen rond het centrum en Ginneken als gezinswoningen in Haagse Beemden en Princenhage.',
        'leak': 'Bij een oudere woning kan water langs een muur of vloer zichtbaar worden terwijl de lekkende aansluiting ergens anders zit. Noteer in welke ruimte je het eerst zag en of het na douchen, koken of het gebruiken van een kraan erger wordt.',
        'block': 'Bij een verstopping in een Bredase woning helpt het om te vertellen of alleen de keukenafvoer traag is of ook de douche en het toilet. Dat maakt duidelijk of het probleem bij één afvoer lijkt te zitten.',
        'leak_answer': 'Meld hoe lang je de plek al ziet en of ze telkens na gebruik terugkomt. Een foto van de plek en de aansluiting kan je vraag verduidelijken.', 'block_answer': 'Schrijf in de aanvraag welke afvoer traag is en of de andere afvoeren wel normaal werken. Dat helpt de klacht af te bakenen.',
        'leak_question': 'Is het water alleen zichtbaar na gebruik van de badkamer?',
        'block_question': 'Loopt de keukenafvoer langzaam leeg terwijl de badkamer normaal werkt?',
    },
    'amsterdam': {
        'name': 'Amsterdam', 'area': 'In Amsterdam kan de klus in een smal ouder pand, een appartement op een hogere verdieping of een nieuwere woning liggen.',
        'leak': 'Geef het stadsdeel en de verdieping door. Bij een lekkage in een appartement is het nuttig te melden of er ook vocht bij buren of in een ruimte onder de lekkage te zien is.',
        'block': 'In een Amsterdams appartement is het belangrijk om te weten of een afvoer alleen in jouw woning problemen geeft of dat buren dezelfde klacht hebben. Vermeld ook of het om een gedeelde standleiding kan gaan.',
        'leak_answer': 'Geef aan op welke verdieping de vochtplek zit en of buren er ook last van hebben. Vermeld of je al contact met de beheerder hebt gehad.', 'block_answer': 'Vraag eventueel na of dezelfde klacht elders in het gebouw speelt en vermeld dat in je bericht. Je hoeft de oorzaak niet zelf vast te stellen.',
        'leak_question': 'Zien buren beneden ook vocht of druppels?',
        'block_question': 'Hebben andere woningen in het gebouw dezelfde verstopping?',
    },
    'rotterdam': {
        'name': 'Rotterdam', 'area': 'Rotterdam heeft appartementen in hoogbouw, oudere woningen in delen van de stad en gezinswoningen verder van het centrum.',
        'leak': 'Bij een lekkage op een hogere verdieping helpt het om de verdieping en de ruimte te noemen. Geef aan of het water bij de gootsteen, badkamer of een zichtbare leiding vandaan lijkt te komen.',
        'block': 'Een verstopte afvoer in een appartement vraagt soms andere informatie dan in een eengezinswoning. Noem het woningtype en of meer dan één afvoer tegelijk borrelt of langzaam wegloopt.',
        'leak_answer': 'Beschrijf of je een druppelende aansluiting ziet of alleen een vochtplek. De verdieping en bereikbaarheid van de ruimte zijn nuttig om door te geven.', 'block_answer': 'Meld welke afvoeren tegelijk reageren en of het water terugkomt. Schrijf ook op sinds wanneer dit speelt.',
        'leak_question': 'Komt het water uit een zichtbare aansluiting of verschijnt het bij een wand?',
        'block_question': 'Borrelen meerdere afvoeren tegelijk wanneer je water gebruikt?',
    },
    'utrecht': {
        'name': 'Utrecht', 'area': 'Een pand rond de Utrechtse binnenstad heeft vaak een andere indeling dan een woning in Leidsche Rijn of een appartement elders in de stad.',
        'leak': 'Beschrijf of de vochtplek bij een leiding, achter een keukenkast of langs een plafond zit. Vermeld ook of de plek groter wordt wanneer je een specifieke kraan of douche gebruikt.',
        'block': 'Geef bij een verstopping aan of de afvoer in de keuken, douche of het toilet zit en hoe bereikbaar die is. In een ouder pand kan de route van de afvoer minder zichtbaar zijn; beschrijf daarom vooral de symptomen.',
        'leak_answer': 'Noteer wanneer de plek zichtbaar wordt en welke kraan of douche je dan gebruikte. Geef aan of de leiding direct zichtbaar is.', 'block_answer': 'Vermeld de volgorde waarin klachten begonnen: eerst één afvoer of meerdere op dezelfde dag. Dat is bruikbare informatie voor je aanvraag.',
        'leak_question': 'Wordt de vochtplek groter nadat je de douche gebruikt?',
        'block_question': 'Is het probleem begonnen bij één afvoer of bij meerdere tegelijk?',
    },
    'denhaag': {
        'name': 'Den Haag', 'area': 'In Den Haag komen bovenwoningen, appartementen, oudere stadswoningen en nieuwere huizen naast elkaar voor.',
        'leak': 'Noem of je in een bovenwoning of appartement woont en of benedenburen iets merken. Geef ook aan of het water uit een kraan, afvoer of een onbekende plek lijkt te komen.',
        'block': 'Een verstopt toilet in een appartement is een andere vraag dan een langzaam leeglopende douche in een woonhuis. Beschrijf welke afvoer het betreft en of het water terugkomt in een andere ruimte.',
        'leak_answer': 'Meld of er bij benedenburen een plek zichtbaar is en in welke ruimte. Voeg pas na het openen van WhatsApp eventueel een foto toe.', 'block_answer': 'Beschrijf of terugstromend water in de douche, wastafel of het toilet verschijnt. Gebruik geen extra middelen zolang onduidelijk is wat eerder is toegepast.',
        'leak_question': 'Is er ook in de woning onder je een vochtplek te zien?',
        'block_question': 'Komt het water in een andere afvoer omhoog wanneer je doorspoelt?',
    },
    'eindhoven': {
        'name': 'Eindhoven', 'area': 'Een klus in Eindhoven kan plaatsvinden in een appartement rond het centrum of in een gezinswoning in een andere wijk.',
        'leak': 'Geef aan of de lekkage bij een apparaat, kraan of leiding zichtbaar is en of je de watertoevoer hebt kunnen afsluiten. Bij een recent aangepaste badkamer is het nuttig te melden wat er veranderd is.',
        'block': 'Vertel of het probleem bij de gootsteen, douche of het toilet begon en of je al iets hebt geprobeerd. Als meerdere afvoeren tegelijk traag worden, zet dat duidelijk in de aanvraag.',
        'leak_answer': 'Geef aan welk onderdeel recent is aangesloten en waar je nu water ziet. Dat is nuttiger dan zelf een oorzaak te raden.', 'block_answer': 'Noem welke afvoeren traag werden en of dit tegelijk gebeurde. Vermeld ook wat je al zonder succes hebt geprobeerd.',
        'leak_question': 'Is de lekkage ontstaan na werk aan een aansluiting of toestel?',
        'block_question': 'Zijn meerdere afvoeren tegelijk langzaam gaan doorlopen?',
    },
    'tilburg': {
        'name': 'Tilburg', 'area': 'Tilburg heeft uiteenlopende woningen, van oudere huizen tot appartementen en nieuwere gezinswoningen.',
        'leak': 'Vermeld je wijk en beschrijf precies waar het vocht zit. Een lekkende kraan onder een keukenblad is beter te beoordelen met een foto van de aansluiting; die kun je in WhatsApp toevoegen.',
        'block': 'Bij een terugkerende verstopping helpt het om te vermelden hoe vaak die optreedt. Schrijf ook op of het water na gebruik van de wasmachine, douche of keukenafvoer terugkomt.',
        'leak_answer': 'Een foto van de plek en de aansluiting helpt de aanvraag te verduidelijken. Beschrijf daarnaast of de kraan open of dicht staat wanneer het druppelt.', 'block_answer': 'Noteer hoe vaak het probleem terugkomt en na welk gebruik. Dan staat in je aanvraag meer dan alleen dat de afvoer nu vastzit.',
        'leak_question': 'Is de aansluiting onder de gootsteen bereikbaar voor een foto?',
        'block_question': 'Komt de verstopping telkens terug na hetzelfde gebruik?',
    },
    'groningen': {
        'name': 'Groningen', 'area': 'In Groningen kan een loodgietersklus in een appartement, gedeeld huis of oudere woning rond het centrum liggen.',
        'leak': 'Bij een gedeelde woning is het handig om te vertellen welke ruimte last heeft van water en wie toegang tot die ruimte heeft. Geef ook door of de hoofdkraan al is gevonden.',
        'block': 'Als meerdere bewoners dezelfde afvoer gebruiken, beschrijf dan of het probleem op één plek of in meerdere kamers voorkomt. Noem wat er gebeurt wanneer de douche, wasbak of keuken wordt gebruikt.',
        'leak_answer': 'Vermeld welke bewoners of kamers last hebben en wie de ruimte kan openen. Geef aan of er nog water loopt.', 'block_answer': 'Noem of de klacht in een gezamenlijke keuken, badkamer of bij één toestel speelt. Dat maakt duidelijk welke afvoer je bedoelt.',
        'leak_question': 'Hebben meerdere kamers of bewoners last van de lekkage?',
        'block_question': 'Speelt de verstopping in een gedeelde afvoer?',
    },
}

SERVICES = {
    'lekkage': {
        'label': 'Lekkage', 'option': 'Lekkage',
        'intro': 'Zie je water of een vochtplek? Beschrijf waar het probleem zichtbaar is en wanneer het optreedt. Je verstuurt de aanvraag zelf via WhatsApp.',
        'what': 'Wat helpt bij een lekkageaanvraag?',
        'points': ['De ruimte en de plek waar je water ziet', 'Sinds wanneer de lekkage zichtbaar is', 'Of het water blijft lopen of alleen na gebruik verschijnt', 'Een foto van de plek, toegevoegd in WhatsApp'],
        'note': 'Als er actief water uitstroomt, beperk dan eerst waar mogelijk de watertoevoer en voorkom verdere schade. Een aanvraag via deze site is geen spoedgarantie.',
    },
    'verstopping': {
        'label': 'Verstopping', 'option': 'Verstopping',
        'intro': 'Loopt een afvoer niet meer goed door of komt water terug? Geef aan welke afvoer het is en wat je merkt. Daarna kun je je bericht via WhatsApp versturen.',
        'what': 'Wat helpt bij een verstoppingsaanvraag?',
        'points': ['Welke afvoer problemen geeft: keuken, douche of toilet', 'Of één of meerdere afvoeren zijn getroffen', 'Wanneer het probleem is begonnen', 'Wat je al hebt geprobeerd, zonder middelen te combineren'],
        'note': 'Een beschrijving van de klachten helpt om de vraag te beoordelen. Er wordt pas na contact besproken wat mogelijk is en onder welke voorwaarden.',
    },
}

for slug, city in CITIES.items():
    city_route = f'/loodgieter-{slug}/'
    city_file = ROOT / f'loodgieter-{slug}' / 'index.html'
    city_html = city_file.read_text()
    cards = (f'<section class="section soft" id="specifieke-klussen"><div class="wrap"><div class="intro"><span class="kicker">Klus in {city["name"]}</span>'
             f'<h2>Bekijk ook deze aanvragen</h2><p class="lead">Beschrijf de situatie op de pagina die bij jouw klus past.</p></div><div class="linkcards">'
             f'<a class="linkcard" href="/lekkage-{slug}/"><strong>Lekkage in {city["name"]}</strong><p>Welke details helpen bij een lekkageaanvraag?</p><span>Bekijk lekkages ↗</span></a>'
             f'<a class="linkcard" href="/verstopping-{slug}/"><strong>Verstopping in {city["name"]}</strong><p>Beschrijf welke afvoer problemen geeft.</p><span>Bekijk verstoppingen ↗</span></a></div></div></section>')
    if 'id="specifieke-klussen"' in city_html:
        a = city_html.index('<section class="section soft" id="specifieke-klussen">')
        b = city_html.index('</section>', a) + len('</section>')
        city_html = city_html[:a] + cards + city_html[b:]
    else:
        city_html = city_html.replace('</main>', cards + '</main>', 1)
    city_file.write_text(city_html)

    for service_slug, service in SERVICES.items():
        route = f'{service_slug}-{slug}'
        canonical = f'https://loodgietervakmannen.nl/{route}/'
        image = f'https://loodgietervakmannen.nl/hero-{slug}.webp'
        title = f'{service["label"]} {city["name"]} | Beschrijf je klus | Loodgieter Vakmannen'
        description = f'{service["label"]} in {city["name"]}? Beschrijf waar het probleem zit en stuur je aanvraag via WhatsApp.'
        heading = f'{service["label"]} in {city["name"]}?'
        local_form = form.replace('placeholder="Bijv. Breda"', f'value="{escape(city["name"], quote=True)}"')
        local_form = local_form.replace(f'<option>{service["option"]}</option>', f'<option selected>{service["option"]}</option>')
        points = ''.join(f'<li>{escape(item)}</li>' for item in service['points'])
        question = city['leak_question' if service_slug == 'lekkage' else 'block_question']
        answer = city['leak_answer' if service_slug == 'lekkage' else 'block_answer']
        detail = city['leak' if service_slug == 'lekkage' else 'block']
        sibling = 'verstopping' if service_slug == 'lekkage' else 'lekkage'
        social = (f'<meta property="og:type" content="website"><meta property="og:site_name" content="Loodgieter Vakmannen">'
                  f'<meta property="og:url" content="{canonical}"><meta property="og:title" content="{escape(title, quote=True)}">'
                  f'<meta property="og:description" content="{escape(description, quote=True)}"><meta property="og:image" content="{image}">'
                  f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(title, quote=True)}">'
                  f'<meta name="twitter:description" content="{escape(description, quote=True)}"><meta name="twitter:image" content="{image}">')
        body = (f'<section class="section"><div class="wrap split"><div><span class="kicker">{service["label"]} in {city["name"]}</span>'
                f'<h2>Beschrijf wat er gebeurt</h2><p class="lead">{city["area"]} {detail}</p>'
                f'<p class="lead">{service["note"]}</p><a class="primary" href="#aanvraag">Vul je aanvraag in <span aria-hidden="true">↗</span></a></div>'
                f'<div class="card"><h3>{service["what"]}</h3><ul>{points}</ul><p class="note">Je kunt een foto zelf aan het WhatsApp-bericht toevoegen.</p></div></div></section>'
                f'<section class="section soft"><div class="wrap content faq"><span class="kicker">Praktische vraag</span><h2>Wat geef ik nog meer door?</h2>'
                f'<details open><summary>{escape(question)}</summary><p>{escape(answer)}</p></details>'
                f'<p>Gaat het om een andere klus? Bekijk de <a href="{city_route}">algemene loodgieterpagina voor {city["name"]}</a> '
                f'of de pagina over <a href="/{sibling}-{slug}/">{sibling} in {city["name"]}</a>.</p></div></section>')
        html = (f'<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<title>{escape(title)}</title><meta name="description" content="{escape(description, quote=True)}">'
                f'<link rel="canonical" href="{canonical}"><link rel="icon" type="image/svg+xml" href="/favicon.svg">'
                f'<link rel="preload" as="image" href="/hero-{slug}.webp">{social}<style>{css}</style></head><body>{header}'
                f'<main><section class="subhero form-hero city-hero city-{slug}"><div class="wrap"><div class="page-hero-copy">'
                f'<div class="bread"><a href="/">Home</a> / <a href="{city_route}">{city["name"]}</a> / {service["label"]}</div>'
                f'<h1>{heading}</h1><p>{service["intro"]}</p></div><div class="hero-form" id="aanvraag">{local_form}</div>'
                f'</div></section>{body}</main>{footer}{floatlink}{script}</body></html>')
        target = ROOT / route / 'index.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html)

routes = ['/'] + sorted('/' + str(p.parent.relative_to(ROOT)) + '/' for p in ROOT.rglob('index.html') if p != ROOT / 'index.html')
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap += ''.join(f'  <url><loc>https://loodgietervakmannen.nl{route}</loc></url>\n' for route in routes)
sitemap += '</urlset>\n'
(ROOT / 'sitemap.xml').write_text(sitemap)
print(f'Generated {len(CITIES) * len(SERVICES)} service pages; sitemap has {len(routes)} URLs')

# Retain AdSense when regenerating existing pages or adding new ones.
from adsense import install as install_adsense
install_adsense()
