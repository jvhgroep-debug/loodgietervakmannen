"""Build the editorial section after build_pages.py and build_service_pages.py."""
from pathlib import Path
from html import escape
import json
from urllib.parse import quote

ROOT = Path('dist')
DOMAIN = 'https://loodgietervakmannen.nl'
home = (ROOT / 'index.html').read_text()
css = home.split('<style>', 1)[1].split('</style>', 1)[0]
header = '<header class="top">' + home.split('<header class="top">', 1)[1].split('</header>', 1)[0] + '</header>'
header = header.replace('href="/#aanvraag"', 'href="#aanvraag"')
footer = '<footer class="foot">' + home.split('<footer class="foot">', 1)[1].split('</footer>', 1)[0] + '</footer>'
floatlink = '<a class="whatsapp-float"' + home.split('<a class="whatsapp-float"', 1)[1].split('</a>', 1)[0] + '</a>'
form = '<form class="card" id="leadForm">' + home.split('<form class="card" id="leadForm">', 1)[1].split('</form>', 1)[0] + '</form>'
form = form.replace('placeholder="Bijv. Breda"', 'value="Amsterdam"').replace('<option>Lekkage</option>', '<option selected>Lekkage</option>')
script = '<script>' + home.split('<script>', 1)[1].split('</script>', 1)[0] + '</script>'

article_css = '''
.article-grid{display:grid;grid-template-columns:minmax(0,1fr) 275px;gap:65px;align-items:start}
.article{max-width:750px}.article p,.article li{color:#47586b;font-size:1.05rem;line-height:1.8}
.article h2{font-size:clamp(1.65rem,2.7vw,2.2rem);margin:40px 0 12px}
.article h3{font-size:1.25rem;color:#132438;margin:24px 0 8px}
.article ul,.article ol{padding-left:24px}.article li{margin:7px 0}
.article-meta{font-size:.9rem;color:#68798a;margin:0 0 22px}
.article-aside{background:#eaf0f4;border-radius:12px;padding:26px;position:sticky;top:24px}
.article-aside h2{font-size:1.35rem;margin:0 0 15px}.article-aside p{line-height:1.65;color:#47586b}
.article-aside a{display:block;margin:12px 0;color:#975229}
.article-callout{background:#eaf0f4;border-left:4px solid #b96f3a;padding:18px 22px;margin:27px 0;border-radius:0 8px 8px 0}
.article-callout p{margin:0}.article-sources{font-size:.9rem;border-top:1px solid #dce5eb;margin-top:45px;padding-top:20px}
.article-sources a{color:#975229}.blog-card{max-width:720px;margin-top:30px}
.blog-cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin-top:28px}
.blog-cards .blog-card{margin:0;max-width:none}.blog-cards .blog-card span{color:#975229;font-weight:750}
.partner-hero{background:#101f30;position:relative;overflow:hidden}.partner-hero:before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(16,31,48,.98),rgba(16,31,48,.88) 48%,rgba(16,31,48,.65)),url('/loodgieter.webp') center/cover}
.partner-hero .wrap{position:relative}.partner-hero .bread{margin-bottom:18px}.partner-hero .primary{margin-top:20px}
.partner-card{background:white;border-radius:12px;border:1px solid #dce5eb;padding:28px;box-shadow:0 15px 45px rgba(16,31,48,.08)}
.partner-card h2{font-size:1.5rem;margin:0 0 10px}.partner-card p{line-height:1.65;color:#47586b}.partner-card .primary{margin-top:9px}
@media(max-width:860px){.article-grid{grid-template-columns:1fr;gap:30px}.article-aside{position:static}}
@media(max-width:760px){.blog-cards{grid-template-columns:1fr}}
'''

def page(path, title, description, main, *, image=None, article=False, partner=False, hero_asset=None, published='2026-09-27'):
    canonical = DOMAIN + path
    image = image or DOMAIN + '/og.png'
    social = (f'<meta property="og:type" content="{"article" if article else "website"}">'
              f'<meta property="og:site_name" content="Loodgieter Vakmannen">'
              f'<meta property="og:url" content="{canonical}"><meta property="og:title" content="{escape(title, quote=True)}">'
              f'<meta property="og:description" content="{escape(description, quote=True)}"><meta property="og:image" content="{image}">'
              f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(title, quote=True)}">'
              f'<meta name="twitter:description" content="{escape(description, quote=True)}"><meta name="twitter:image" content="{image}">')
    if article:
        social += f'<meta property="article:published_time" content="{published}">'
    local_header = header.replace('>Doe een aanvraag</a>', '>Meld je bedrijf aan</a>') if partner else header
    partner_message = quote('Hallo, ik heb een loodgietersbedrijf en wil meer weten over een eigen gemeentepagina op Loodgieter Vakmannen.')
    local_float = (floatlink.replace('https://wa.me/31684002350?text=Hallo%2C%20ik%20heb%20een%20vraag%20over%20een%20loodgietersklus.',
                                    f'https://wa.me/31684002350?text={partner_message}')
                   .replace('Stel je vraag via WhatsApp', 'Vraag informatie over een gemeentepagina via WhatsApp')) if partner else floatlink
    html = (f'<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{escape(title)}</title><meta name="description" content="{escape(description, quote=True)}">'
            f'<link rel="canonical" href="{canonical}"><link rel="icon" type="image/svg+xml" href="/favicon.svg">'
            f'<link rel="preload" as="image" href="/{hero_asset or ("loodgieter.webp" if partner else "hero-amsterdam.webp")}">{social}<style>{css}{article_css}</style></head>'
            f'<body>{local_header}<main>{main}</main>{footer}{local_float}{"" if partner else script}</body></html>')
    target = ROOT / path.lstrip('/') / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html)

slug = '/blog/lekkage-appartement-amsterdam/'
title = 'Lekkage in een Amsterdams appartement: wat doe je eerst? | Loodgieter Vakmannen'
description = 'Vochtplek of water in je appartement in Amsterdam? Lees wat je veilig kunt controleren en welke gegevens helpen bij een lekkageaanvraag.'
image = DOMAIN + '/hero-amsterdam.webp'
structured = json.dumps({
    '@context': 'https://schema.org', '@type': 'BlogPosting',
    'headline': 'Lekkage in een Amsterdams appartement: wat doe je eerst?',
    'description': description, 'datePublished': '2026-09-27', 'dateModified': '2026-09-27',
    'author': {'@type': 'Organization', 'name': 'Loodgieter Vakmannen'},
    'publisher': {'@type': 'Organization', 'name': 'Loodgieter Vakmannen'},
    'image': image, 'mainEntityOfPage': DOMAIN + slug
}, ensure_ascii=False)

article_main = f'''<section class="subhero form-hero city-hero city-amsterdam"><div class="wrap"><div class="page-hero-copy">
<div class="bread"><a href="/">Home</a> / <a href="/blog/">Blog</a> / Amsterdam</div>
<span class="eyebrow">Praktische gids · Amsterdam</span>
<h1>Lekkage in een Amsterdams appartement: wat doe je eerst?</h1>
<p>Zie je water bij een leiding of verschijnt er een vochtplek aan de muur of het plafond? Met een paar gerichte controles kun je de situatie duidelijk beschrijven.</p>
</div><div class="hero-form" id="aanvraag">{form}</div></div></section>
<section class="section"><div class="wrap article-grid"><article class="article">
<p class="article-meta">Gepubliceerd op <time datetime="2026-09-27">27 september 2026</time> · Loodgieter Vakmannen</p>
<p>In een appartement is de plek waar je water ziet niet altijd de plek waar het probleem begint. Een vochtplek bij jouw plafond kan samenhangen met een ruimte erboven; water onder de gootsteen is soms direct bij een aansluiting zichtbaar. Ga daarom niet meteen uit van één oorzaak. Noteer wat je ziet, op welk moment het gebeurt en welke ruimtes betrokken zijn.</p>
<h2>1. Beperk wateroverlast waar dat veilig kan</h2>
<p>Stroomt er zichtbaar water uit een leiding of aansluiting? Sluit de toevoer naar dat onderdeel af als je weet waar de kraan zit. Lukt dat niet en is het veilig bereikbaar, sluit dan de hoofdkraan van jouw woning. Bij sommige appartementen bevindt de meter of kraan zich in een algemene ruimte. <a href="https://www.waternet.nl/veelgestelde-vragen/problemen-met-water/waar-vind-ik-de-hoofdkraan/" target="_blank" rel="noopener noreferrer">Waternet legt uit waar de hoofdkraan vaak zit</a>. Gebruik een gedeelde hoofdkraan niet zonder afstemming met de beheerder of andere bewoners.</p>
<p>Komt water bij stopcontacten, verlichting of elektrische apparatuur? Blijf uit de buurt van natte elektrische delen en laat een deskundige beoordelen wat veilig is. Voorkom daarnaast waar mogelijk verdere schade met een emmer of doeken; stel een noodzakelijke melding niet uit om eerst foto's te maken.</p>
<div class="article-callout"><p><strong>Watermeter zelf nat?</strong> Waternet behandelt meldingen over een lekkende watermeter apart. Bij andere lekkages in huis verwijst Waternet naar een loodgieter. <a href="https://www.waternet.nl/service-en-contact/problemen-met-water/lekkage/" target="_blank" rel="noopener noreferrer">Bekijk de uitleg van Waternet</a>.</p></div>
<h2>2. Leg vast wanneer en waar het vocht verschijnt</h2>
<p>Noteer het stadsdeel, de verdieping en de ruimte. Maak, als het veilig kan, een foto van de vochtplek en een overzichtsfoto van de omgeving. Schrijf op wanneer je de plek voor het eerst zag en of hij groter wordt na douchen, na gebruik van de keuken of juist zonder watergebruik. Dat helpt om een gerichte aanvraag te doen, zonder zelf een diagnose te hoeven stellen.</p>
<p>Voorbeelden van nuttige details zijn een druppelende koppeling onder de gootsteen, een natte muur achter de douche of een plek aan het plafond onder de badkamer van een bovenwoning. Zie je alleen verkleuring en geen stromend water? Vermeld dat ook. Een vochtplek kan verschillende oorzaken hebben.</p>
<h2>3. Stem af bij een huurwoning of gedeeld gebouw</h2>
<p>Woon je in een huurwoning, meld een lekkage ook bij de verhuurder of beheerder. De Rijksoverheid adviseert om onderhoudsproblemen eerst bij de verhuurder te melden en bij een dringend probleem om spoed te vragen. <a href="https://www.rijksoverheid.nl/vraag-en-antwoord/woning-huren/hoe-zorg-ik-ervoor-dat-de-verhuurder-slecht-onderhoud-aanpakt" target="_blank" rel="noopener noreferrer">Lees de uitleg voor huurders</a>.</p>
<p>Bij een gedeelde leiding of vocht bij benedenburen is het handig de gebouwbeheerder of VvE te informeren. Vertel welke verdieping last heeft van water en of buren hetzelfde merken. Wie verantwoordelijk is voor onderzoek of herstel hangt af van de situatie en de afspraken rond het gebouw; trek daar niet op basis van alleen de zichtbare plek een conclusie over.</p>
<h2>4. Stuur een duidelijke aanvraag</h2>
<p>Je hoeft de oorzaak niet te kennen. Met deze gegevens kan je vraag wel sneller worden begrepen:</p>
<ul><li>Amsterdamse wijk of stadsdeel, verdieping en type woning;</li>
<li>de precieze plek van water of vocht, en sinds wanneer je het ziet;</li>
<li>of het water continu stroomt of alleen na bepaald gebruik verschijnt;</li>
<li>of buren ook vocht zien en of de beheerder al is ingelicht;</li>
<li>wat je al hebt afgesloten of gecontroleerd.</li></ul>
<p>Vul het formulier bovenaan in en voeg een foto toe zodra WhatsApp opent. Je verstuurt het bericht daar zelf. De beschikbaarheid en eventuele vervolgstappen worden na contact besproken; via deze website wordt geen directe hulp gegarandeerd.</p>
<p>Meer informatie over een <a href="/lekkage-amsterdam/">lekkageaanvraag in Amsterdam</a> of een andere <a href="/loodgieter-amsterdam/">loodgietersklus in Amsterdam</a> vind je op de bijbehorende pagina's.</p>
<div class="article-sources"><strong>Gebruikte bronnen</strong><ul>
<li><a href="https://www.waternet.nl/service-en-contact/problemen-met-water/lekkage/">Waternet: lekkage in huis</a></li>
<li><a href="https://www.waternet.nl/veelgestelde-vragen/problemen-met-water/waar-vind-ik-de-hoofdkraan/">Waternet: waar vind ik de hoofdkraan?</a></li>
<li><a href="https://www.rijksoverheid.nl/vraag-en-antwoord/woning-huren/hoe-zorg-ik-ervoor-dat-de-verhuurder-slecht-onderhoud-aanpakt">Rijksoverheid: onderhoud bij een huurwoning melden</a></li>
</ul></div></article><aside class="article-aside" aria-label="Verder lezen"><h2>Verder lezen</h2>
<p>Beschrijf de lekkage zo duidelijk mogelijk en stuur je vraag via WhatsApp.</p>
<a href="#aanvraag">Naar het aanvraagformulier ↗</a><a href="/lekkage-amsterdam/">Lekkage Amsterdam</a>
<a href="/loodgieter-amsterdam/">Loodgieter Amsterdam</a><a href="/blog/">Alle blogs</a></aside></div></section>
<script type="application/ld+json">{structured}</script>'''
page(slug, title, description, article_main, image=image, article=True)

partner_slug = '/blog/loodgietersbedrijven-gezocht-per-gemeente/'
partner_title = 'Loodgietersbedrijven gezocht in heel Nederland | Loodgieter Vakmannen'
partner_description = 'Loodgieter Vakmannen zoekt loodgietersbedrijven per gemeente. Laat je bedrijf zien met een eigen logo, foto’s en WhatsApp-knop op jouw gemeentepagina.'
partner_wa = 'https://wa.me/31684002350?text=' + quote('Hallo, ik heb een loodgietersbedrijf en wil meer weten over een eigen gemeentepagina op Loodgieter Vakmannen.')
partner_structured = json.dumps({
    '@context': 'https://schema.org', '@type': 'BlogPosting',
    'headline': 'Loodgietersbedrijven gezocht in heel Nederland',
    'description': partner_description, 'datePublished': '2026-09-27', 'dateModified': '2026-09-27',
    'author': {'@type': 'Organization', 'name': 'Loodgieter Vakmannen'},
    'publisher': {'@type': 'Organization', 'name': 'Loodgieter Vakmannen'},
    'image': DOMAIN + '/loodgieter.webp', 'mainEntityOfPage': DOMAIN + partner_slug
}, ensure_ascii=False)
partner_main = f'''<section class="subhero partner-hero" id="aanvraag"><div class="wrap">
<div class="bread"><a href="/">Home</a> / <a href="/blog/">Blog</a> / Voor loodgietersbedrijven</div>
<span class="eyebrow">Samenwerken per gemeente</span><h1>Loodgietersbedrijven gezocht in heel Nederland</h1>
<p>Wil jij met jouw bedrijf zichtbaar zijn op een eigen gemeentepagina? Loodgieter Vakmannen zoekt loodgietersbedrijven die hun werkgebied en bedrijf rechtstreeks aan bezoekers willen laten zien.</p>
<a class="primary" href="{partner_wa}" target="_blank" rel="noopener noreferrer">Vraag informatie via WhatsApp <span aria-hidden="true">↗</span></a>
</div></section><section class="section"><div class="wrap article-grid"><article class="article">
<p class="article-meta">Gepubliceerd op <time datetime="2026-09-27">27 september 2026</time> · Loodgieter Vakmannen</p>
<p>Van Breda en Amsterdam tot Rotterdam, Utrecht en andere gemeenten: bezoekers zoeken vaak een loodgieter voor een specifieke plaats en klus. Op Loodgieter Vakmannen bouwen we pagina's voor gemeenten en veelvoorkomende loodgietersvragen. We zoeken bedrijven die op een gemeentepagina met hun eigen gegevens zichtbaar willen worden.</p>
<h2>Jouw bedrijf herkenbaar op de gemeentepagina</h2>
<p>Een aangesloten bedrijf kan zijn <strong>eigen logo</strong> en <strong>foto's van het bedrijf of uitgevoerde werkzaamheden</strong> laten plaatsen. Daarbij hoort een beschrijving van de diensten en het werkgebied. Zo zien bezoekers welk bedrijf achter de vermelding staat en voor welke klussen zij contact kunnen opnemen.</p>
<p>Heb je foto's van bijvoorbeeld een badkamerrenovatie, leidingwerk of een gerepareerde lekkage? Dan kunnen die de pagina concreter maken. We bespreken samen welke beelden en teksten passen en plaatsen alleen materiaal waarvoor jouw bedrijf toestemming heeft.</p>
<h2>Contact via je eigen WhatsApp-knop</h2>
<p>Voor jouw gemeentepagina kan de contactknop naar het <strong>eigen WhatsApp-nummer van je bedrijf</strong> verwijzen. Een bezoeker die daar een vraag stelt, komt dan rechtstreeks bij jouw bedrijf terecht. Je kunt zelf reageren, de situatie beoordelen en afspraken maken over beschikbaarheid en eventuele kosten.</p>
<p>De algemene aanvragen op de site lopen momenteel via Loodgieter Vakmannen. Een persoonlijk nummer op jouw gemeentepagina stellen we in wanneer we de samenwerking en de juiste plaatsgegevens hebben afgestemd.</p>
<h2>Welke gemeente past bij jouw werkgebied?</h2>
<p>Je kunt interesse doorgeven voor de gemeente waarin je gevestigd bent, of voor een plaats die je vanuit jouw bedrijf bedient. Werk je in meerdere gemeenten, noem die dan ook. We bekijken per gemeente welke pagina's al bestaan en welke gegevens nodig zijn om jouw bedrijf goed te presenteren. Een vermelding of positie is pas afgesproken zodra we de voorwaarden samen hebben bevestigd.</p>
<div class="article-callout"><p><strong>Stuur bij je eerste bericht mee:</strong> je bedrijfsnaam, website, de gemeenten waarin je werkt en het WhatsApp-nummer waarop klanten je mogen bereiken. Je logo en foto's kunnen daarna volgen.</p></div>
<h2>Interesse om mee te doen?</h2>
<p>Stuur ons een WhatsApp-bericht met je bedrijfsnaam en gewenste gemeente of gemeenten. We vertellen je welke mogelijkheden er zijn en hoe jouw logo, foto's en WhatsApp-knop op de gemeentepagina kunnen worden verwerkt.</p>
<p><a class="primary" href="{partner_wa}" target="_blank" rel="noopener noreferrer">Meld je bedrijf aan via WhatsApp <span aria-hidden="true">↗</span></a></p>
<p>Bekijk als voorbeeld de huidige <a href="/loodgieter-breda/">pagina voor Breda</a> of <a href="/loodgieter-amsterdam/">pagina voor Amsterdam</a>. De persoonlijke bedrijfsvermelding wordt ingericht zodra een samenwerking is afgesproken.</p>
</article><aside class="partner-card" aria-label="Samenwerken"><h2>Jouw bedrijf per gemeente</h2>
<p>Een eigen logo, foto's en een WhatsApp-knop voor jouw bedrijf op de gemeentepagina.</p>
<p>Vertel ons in welke plaatsen je werkt. We bespreken de mogelijkheden en voorwaarden persoonlijk.</p>
<a class="primary" href="{partner_wa}" target="_blank" rel="noopener noreferrer">Stuur een WhatsApp ↗</a></aside></div></section>
<script type="application/ld+json">{partner_structured}</script>'''
page(partner_slug, partner_title, partner_description, partner_main, image=DOMAIN + '/loodgieter.webp', article=True, partner=True)

klundert_slug = '/blog/loodgietersklus-klundert/'
klundert_title = 'Loodgietersklus in Klundert? Dit kun je aanvragen | Loodgieter Vakmannen'
klundert_description = 'Lekkage, verstopping of werk aan sanitair in Klundert? Lees welke gegevens helpen en stuur je klus via WhatsApp naar Loodgieter Vakmannen.'
klundert_image = DOMAIN + '/hero-klundert.webp'
klundert_form = form.replace('value="Amsterdam"', 'value="Klundert"').replace('<option selected>Lekkage</option>', '<option>Lekkage</option>')
klundert_structured = json.dumps({
    '@context': 'https://schema.org', '@type': 'BlogPosting',
    'headline': 'Loodgietersklus in Klundert? Dit kun je aanvragen',
    'description': klundert_description, 'datePublished': '2026-09-28', 'dateModified': '2026-09-28',
    'author': {'@type': 'Organization', 'name': 'Loodgieter Vakmannen'},
    'publisher': {'@type': 'Organization', 'name': 'Loodgieter Vakmannen'},
    'image': klundert_image, 'mainEntityOfPage': DOMAIN + klundert_slug
}, ensure_ascii=False)
klundert_main = f'''<section class="subhero form-hero city-hero city-klundert"><div class="wrap"><div class="page-hero-copy">
<div class="bread"><a href="/">Home</a> / <a href="/blog/">Blog</a> / Klundert</div>
<span class="eyebrow">Loodgieter Vakmannen · Klundert</span>
<h1>Loodgietersklus in Klundert? Dit kun je aanvragen</h1>
<p>Een lekkage, verstopte afvoer of klus aan je sanitair? Beschrijf wat er in jouw woning gebeurt en stuur je aanvraag zelf via WhatsApp.</p>
</div><div class="hero-form" id="aanvraag">{klundert_form}</div></div></section>
<section class="section"><div class="wrap article-grid"><article class="article">
<p class="article-meta">Gepubliceerd op <time datetime="2026-09-28">28 september 2026</time> · Loodgieter Vakmannen</p>
<p>Klundert is een vestingstad binnen de gemeente Moerdijk, met een historische kern en andere woonbuurten. Een loodgietersvraag kan overal in de plaats spelen. Voor de aanvraag zijn vooral de precieze plek in huis, de klachten en de bereikbaarheid van de leiding of afvoer van belang. Je hoeft de oorzaak niet zelf vast te stellen.</p>
<h2>Lekkage aan een kraan, leiding of aansluiting</h2>
<p>Zie je druppels onder de gootsteen, een natte vloer bij het toilet of een vochtplek in de badkamer? Vermeld waar je het water voor het eerst zag en of het blijft doorlopen of alleen na gebruik van een kraan of douche verschijnt. Geef ook aan of je de watertoevoer hebt kunnen afsluiten. Bij actief stromend water beperk je eerst waar mogelijk verdere schade.</p>
<h2>Een afvoer die niet goed doorloopt</h2>
<p>Een verstopping kan zich laten merken bij de gootsteen, douche, wastafel of het toilet. Schrijf op welke afvoer problemen geeft, sinds wanneer het speelt en of andere afvoeren in de woning nog normaal werken. Komt water ergens terug of borrelt een andere afvoer mee? Dat is nuttige informatie voor je bericht. Combineer geen verschillende chemische ontstoppingsmiddelen.</p>
<h2>Werk aan sanitair en aansluitingen</h2>
<p>Ook voor een andere loodgietersklus kun je een vraag sturen, bijvoorbeeld over een kraan, leidingaansluiting of sanitair. Beschrijf wat er nu aanwezig is en wat je wilt laten aanpassen of repareren. Als een aansluiting lastig bereikbaar is achter een kast of wand, vermeld dat dan. Een foto kun je in WhatsApp toevoegen nadat je het formulier hebt ingevuld.</p>
<div class="article-callout"><p><strong>Handig om mee te sturen:</strong> Klundert als plaats, je straat of buurt, de betreffende ruimte, wanneer het probleem begon, wat je al hebt geprobeerd en wanneer je hulp zoekt.</p></div>
<h2>Zo werkt een aanvraag vanuit Klundert</h2>
<p>In het formulier bovenaan staat Klundert alvast ingevuld. Kies het soort klus, schrijf een korte omschrijving en open het bericht in WhatsApp. Je controleert het bericht en drukt daar zelf op verzenden. Een aanvraag is nog geen afspraak; beschikbaarheid, werkzaamheden en eventuele kosten worden pas na contact besproken.</p>
<p>Wil je direct naar de lokale pagina? Bekijk <a href="/loodgieter-klundert/">Loodgieter Klundert</a>. Een loodgietersbedrijf dat zich voor Klundert wil presenteren, kan ook lezen hoe <a href="/blog/loodgietersbedrijven-gezocht-per-gemeente/">samenwerking per plaats</a> werkt.</p>
</article><aside class="article-aside" aria-label="Aanvraag in Klundert"><h2>Jouw klus in Klundert</h2>
<p>Beschrijf de situatie bovenaan en voeg daarna eventueel een foto toe in WhatsApp.</p>
<a href="#aanvraag">Naar het aanvraagformulier ↗</a><a href="/loodgieter-klundert/">Loodgieter Klundert</a><a href="/blog/">Alle blogs</a></aside></div></section>
<script type="application/ld+json">{klundert_structured}</script>'''
page(klundert_slug, klundert_title, klundert_description, klundert_main,
     image=klundert_image, article=True, hero_asset='hero-klundert.webp', published='2026-09-28')

index_main = '''<section class="subhero form-hero city-hero city-amsterdam"><div class="wrap"><div class="page-hero-copy">
<div class="bread"><a href="/">Home</a> / Blog</div><span class="eyebrow">Loodgieter Vakmannen</span><h1>Nieuws en praktische tips</h1>
<p>Lees praktische gidsen voor je klus en nieuws over samenwerken met Loodgieter Vakmannen.</p></div></div></section>
<section class="section"><div class="wrap"><span class="kicker">Onze blogs</span><h2>Recente artikelen</h2><div class="blog-cards">
<a class="linkcard blog-card" href="/blog/loodgietersklus-klundert/"><strong>Loodgietersklus in Klundert? Dit kun je aanvragen</strong>
<p>Van een lekkage of verstopping tot werk aan sanitair: lees wat je kunt doorgeven.</p><span>Lees het artikel ↗</span></a>
<a class="linkcard blog-card" href="/blog/loodgietersbedrijven-gezocht-per-gemeente/"><strong>Loodgietersbedrijven gezocht in heel Nederland</strong>
<p>Presenteer je bedrijf per gemeente met je eigen logo, foto's en WhatsApp-knop.</p><span>Lees het artikel ↗</span></a>
<a class="linkcard blog-card" href="/blog/lekkage-appartement-amsterdam/"><strong>Lekkage in een Amsterdams appartement: wat doe je eerst?</strong>
<p>Wat je veilig kunt controleren, welke informatie helpt en wie je in een gedeeld gebouw informeert.</p><span>Lees het artikel ↗</span></a></div></div></section>'''
# The overview has no form, so use only the shared script's form listener when a form exists.
page('/blog/', 'Blog | Praktische loodgieterstips | Loodgieter Vakmannen',
     'Nieuws voor loodgietersbedrijven en praktische gidsen over lekkages en loodgietersklussen op Loodgieter Vakmannen.',
     index_main.replace('</div></div></section>', f'</div><div class="hero-form" id="aanvraag">{form}</div></div></section>', 1))

# Surface the editorial section without changing existing routes or replacing city content.
for target in ROOT.rglob('index.html'):
    html = target.read_text()
    footer_start = html.index('<div class="footerlinks">')
    footer_end = html.index('</div>', footer_start)
    if 'href="/blog/">Blog</a>' not in html[footer_start:footer_end]:
        html = html[:footer_end] + '<a href="/blog/">Blog</a>' + html[footer_end:]
    target.write_text(html)

city_file = ROOT / 'loodgieter-amsterdam' / 'index.html'
city = city_file.read_text()
section = ('<section class="section" id="blog-amsterdam"><div class="wrap"><div class="intro">'
           '<span class="kicker">Lees ook</span><h2>Lekkage in een Amsterdams appartement?</h2>'
           '<p class="lead">Wat controleer je eerst en wat meld je aan de beheerder? Lees de praktische gids.</p>'
           '<a class="primary" href="/blog/lekkage-appartement-amsterdam/">Lees het artikel <span aria-hidden="true">↗</span></a>'
           '</div></div></section>')
if 'id="blog-amsterdam"' not in city:
    city = city.replace('</main>', section + '</main>', 1)
city_file.write_text(city)

klundert_file = ROOT / 'loodgieter-klundert' / 'index.html'
klundert = klundert_file.read_text()
klundert_section = ('<section class="section soft" id="blog-klundert"><div class="wrap"><div class="intro">'
                    '<span class="kicker">Lees ook</span><h2>Welke klus kun je in Klundert aanvragen?</h2>'
                    '<p class="lead">Lees welke informatie helpt bij lekkage, een verstopping of werk aan sanitair.</p>'
                    '<a class="primary" href="/blog/loodgietersklus-klundert/">Lees het artikel <span aria-hidden="true">↗</span></a>'
                    '</div></div></section>')
if 'id="blog-klundert"' not in klundert:
    klundert = klundert.replace('</main>', klundert_section + '</main>', 1)
klundert_file.write_text(klundert)

routes = ['/'] + sorted('/' + str(p.parent.relative_to(ROOT)) + '/' for p in ROOT.rglob('index.html') if p != ROOT / 'index.html')
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap += ''.join(f'  <url><loc>{DOMAIN}{route}</loc></url>\n' for route in routes)
(ROOT / 'sitemap.xml').write_text(sitemap + '</urlset>\n')
print(f'Built blog and updated sitemap: {len(routes)} URLs')

# Retain AdSense when regenerating existing pages or adding new ones.
from adsense import install as install_adsense
install_adsense()
