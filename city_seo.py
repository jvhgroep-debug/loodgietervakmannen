"""Editorial additions for existing city routes; no new service claims."""
from html import escape
import json
from city_seo_more import additional_content

CONTENT = {
    'amsterdam': {
        'name': 'Amsterdam',
        'description': 'Loodgieter nodig in Amsterdam? Lees wat je doorgeeft bij lekkage, verstopping of sanitairwerk en stuur je aanvraag via WhatsApp.',
        'body': '''<section class="section" id="klussen-amsterdam"><div class="wrap content">
<span class="kicker">Lekkage, verstopping en sanitair</span><h2>Welke loodgietersklus heb je in Amsterdam?</h2>
<h3>Lekkage in een appartement of bovenwoning</h3><p>Bij water onder de gootsteen, een druppelende aansluiting of een vochtplek aan het plafond zijn de zichtbare klachten het startpunt. Geef aan op welke verdieping je woont en of boven- of benedenburen hetzelfde merken. Vertel of de plek na douchen of ander watergebruik groter wordt. De oorzaak hoeft nog niet bekend te zijn: een foto van de plek en de omgeving kun je in WhatsApp toevoegen.</p>
<p>Op de pagina over <a href="/lekkage-amsterdam/">lekkage in Amsterdam</a> lees je welke gegevens bij zo'n aanvraag helpen.</p>
<h3>Verstopte keukenafvoer, douche of toilet</h3><p>Vermeld welke afvoer langzaam leegloopt en of er water terugkomt. Wanneer meerdere afvoeren tegelijk reageren, zet dat erbij. In een gedeeld gebouw helpt het om te weten of andere bewoners dezelfde klacht hebben. Meld ook wat je al hebt geprobeerd, zodat er geen onduidelijkheid is over eerder gebruikte middelen of ingrepen.</p>
<p>Bekijk ook de aanvraagpagina voor een <a href="/verstopping-amsterdam/">verstopping in Amsterdam</a>.</p>
<h3>Een kraan, aansluiting of sanitair aanpassen</h3><p>Beschrijf wat er nu aanwezig is en wat je wilt laten repareren of veranderen. Gaat het om een kraan, wastafel, toilet of aansluiting van een apparaat? Geef aan of de leidingen zichtbaar zijn en of de werkplek achter een keukenblok of tegelwand ligt. Dat maakt de vraag concreter dan alleen 'nieuw sanitair plaatsen'.</p>
<h2>De locatie en toegang in jouw stadsdeel</h2><p>Een klus in Centrum, West of Noord kan in een appartement, bovenwoning of ander type pand liggen. Geef je stadsdeel, verdieping en woningtype door, plus wie toegang tot de werkplek kan geven. Woon je in een huurwoning of gaat het om een gemeenschappelijke ruimte? Vermeld of je de verhuurder of gebouwbeheerder al hebt gesproken.</p>
</div></section><section class="section soft"><div class="wrap content faq"><span class="kicker">Voor je een aanvraag doet</span><h2>Veelgestelde vragen over loodgieterswerk in Amsterdam</h2>
<details><summary>Kan ik een lekkage melden als de oorzaak onbekend is?</summary><p>Ja. Beschrijf waar je water of vocht ziet, sinds wanneer het speelt en wanneer de klachten optreden. Geef aan of er nog water stroomt. Een foto van de plek kun je zelf aan je WhatsApp-bericht toevoegen.</p></details>
<details><summary>Wat is handig bij een klus op een hogere verdieping?</summary><p>Noem de verdieping, de bereikbaarheid van de werkplek en of andere woningen last hebben. Vermeld wie het pand of een gezamenlijke ruimte kan openen.</p></details>
<details><summary>Krijg ik meteen een prijs en afspraak?</summary><p>Het formulier verstuurt een vraag. De werkzaamheden, beschikbaarheid en eventuele kosten worden na contact besproken. Vraag vooraf welke kosten en werkzaamheden bij een eventuele afspraak horen.</p></details>
<p>Meer praktische uitleg vind je in de blog <a href="/blog/lekkage-appartement-amsterdam/">Lekkage in een Amsterdams appartement: wat doe je eerst?</a></p>
</div></section>'''
    },
    'klundert': {
        'name': 'Klundert',
        'description': 'Loodgieter nodig in Klundert? Beschrijf je lekkage, verstopte afvoer of sanitairklus en stuur je vraag via WhatsApp naar Loodgieter Vakmannen.',
        'body': '''<section class="section" id="klussen-klundert"><div class="wrap content">
<span class="kicker">Jouw woning in Klundert</span><h2>Lekkage, verstopping of sanitairwerk?</h2>
<h3 id="lekkage-klundert">Een lekkage beschrijven</h3><p>Zie je vocht achter een keukenkast, water bij een toilet of een plek aan het plafond? Schrijf op waar je het eerst zag en of het alleen na gebruik van een kraan of douche verschijnt. Vermeld of de aansluiting zichtbaar is en of je de watertoevoer hebt afgesloten. De zichtbare plek is niet altijd de oorzaak; je hoeft daarom geen diagnose te geven.</p>
<h3 id="verstopping-klundert">Een afvoer die niet goed doorloopt</h3><p>Vertel of het om de gootsteen, douche, wastafel of het toilet gaat. Noteer of het water langzaam wegloopt, helemaal blijft staan of elders terugkomt. Werken de andere afvoeren wel? Zet dat in je aanvraag. Bij een terugkerend probleem is het nuttig te vertellen hoe vaak het gebeurt en na welk gebruik.</p>
<h3 id="sanitair-klundert">Een kraan of aansluiting repareren of aanpassen</h3><p>Voor werk aan sanitair helpt een korte beschrijving van de bestaande situatie. Noem het onderdeel, de gewenste verandering en of leidingen en afsluiters bereikbaar zijn. Geef bij een verbouwing aan welke onderdelen blijven staan en wat je wilt vervangen. Foto's van de aansluiting kun je later in WhatsApp meesturen.</p>
<h2>Geef Klundert als plaats door</h2><p>Klundert is een vestingstad binnen de gemeente Moerdijk. Voor je aanvraag is de precieze locatie van de klus belangrijk: vermeld Klundert en je straat of buurt. Bij een klus in de oudere kern of een andere woonbuurt geef je ook het woningtype en de betreffende ruimte door. Vertel of de leiding achter een wand ligt of direct zichtbaar is.</p>
<p>De vestingwerken en het oude stadhuis horen bij het karakter van Klundert. Meer informatie over de plaats staat op de <a href="https://www.moerdijk.nl/mijn-woonplaats/klundert-2/" target="_blank" rel="noopener noreferrer">website van de gemeente Moerdijk</a>.</p>
</div></section><section class="section soft"><div class="wrap content faq"><span class="kicker">Voor je een aanvraag doet</span><h2>Veelgestelde vragen over een loodgieter in Klundert</h2>
<details><summary>Wat als ik alleen een vochtplek zie?</summary><p>Vermeld waar de plek zit, wanneer je hem voor het eerst zag en of hij groter wordt na watergebruik. Een overzichtsfoto en een foto van de plek helpen om je vraag te verduidelijken.</p></details>
<details><summary>Kan ik foto's meesturen van een verstopte afvoer?</summary><p>Ja. Het formulier opent een tekstbericht in WhatsApp. Daar kun je zelf foto's toevoegen en het bericht versturen. Vermeld ook welke andere afvoeren nog normaal werken.</p></details>
<details><summary>Hoe worden kosten en beschikbaarheid bepaald?</summary><p>Dat wordt besproken na ontvangst van je vraag. Het invullen van het formulier is nog geen afspraak of prijsopgave. Vraag vooraf welke werkzaamheden en kosten bij een eventuele afspraak horen.</p></details>
<p>Lees de lokale blog <a href="/blog/loodgietersklus-klundert/">Loodgietersklus in Klundert: dit kun je aanvragen</a> voor meer uitleg over de aanvraagroute.</p>
</div></section>'''
    }
}

CONTENT.update(additional_content())

def city_details(slug):
    entry = CONTENT.get(slug)
    if not entry:
        return None
    name = entry['name']
    canonical = f'https://loodgietervakmannen.nl/loodgieter-{slug}/'
    title = f'Loodgieter {name} | Lekkage, verstopping & sanitair'
    schema = {
        '@context': 'https://schema.org', '@graph': [
            {'@type': 'WebPage', '@id': canonical + '#webpage', 'url': canonical,
             'name': title, 'description': entry['description'], 'inLanguage': 'nl-NL'},
            {'@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://loodgietervakmannen.nl/'},
                {'@type': 'ListItem', 'position': 2, 'name': f'Loodgieter {name}', 'item': canonical}
            ]}
        ]
    }
    accountability = '''<section class="section"><div class="wrap content"><span class="kicker">Over deze aanvraagroute</span>
<h2>Contact via Loodgieter Vakmannen</h2><p>Loodgieter Vakmannen is een initiatief van Star Local. Je gebruikt deze site om je klus te beschrijven en je bericht via WhatsApp te versturen. Beschikbaarheid en afspraken worden in het verdere contact besproken.</p>
<p>Lees <a href="/over-ons/">meer over Loodgieter Vakmannen</a> of bekijk de <a href="/contact/">contactgegevens van Star Local</a>.</p></div></section>'''
    markup = entry['body'] + accountability + '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + '</script>'
    return title, entry['description'], markup
