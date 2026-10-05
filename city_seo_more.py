"""Distinct practical copy for the remaining existing place pages."""
from html import escape

PLACES = {
    'breda': {
        'name': 'Breda',
        'description': 'Loodgieter nodig in Breda? Lees wat helpt bij lekkage, een verstopte afvoer of een nieuwe aansluiting en stuur je vraag via WhatsApp.',
        'heading': 'Van een druppelende kraan tot werk bij een verbouwing',
        'sections': [
            ('Water bij de gootsteen of achter een kast', 'Zie je water onder het keukenblad? Geef aan of het druppelt bij een zichtbare aansluiting, rond de kraan of alleen na gebruik van de afvoer. Beschrijf ook of de ruimte onder de gootsteen toegankelijk is. Een overzichtsfoto van het kastje en een foto van de natte plek geven meer context dan een losse foto van de vloer.'),
            ('Een afvoer die telkens opnieuw traag wordt', 'Bij een terugkerende verstopping helpt de volgorde van de klachten. Begon het bij de keuken, of werden douche en toilet tegelijk trager? Noteer of het probleem na hetzelfde gebruik terugkomt en wat je al hebt geprobeerd. Je hoeft geen leidingen los te maken om een aanvraag te kunnen doen.'),
            ('Sanitair veranderen in jouw Bredase woning', 'Wil je een kraan, wastafel of toilet laten vervangen? Vermeld welke onderdelen blijven staan, waar de bestaande aansluitingen zitten en wat je wilt veranderen. Een klus in het centrum, Ginneken of Haagse Beemden begint met dezelfde informatie: woningtype, werkruimte en bereikbaarheid. Geef ook aan of er al werk aan de keuken of badkamer is gepland.')
        ],
        'faqs': [
            ('Welke foto helpt bij water onder mijn gootsteen?', 'Maak, als dat veilig kan, een overzicht van het kastje en de aansluitingen. Voeg ook een foto toe van de plek waar het water zichtbaar is. Vermeld of dit bij gebruik van de kraan of de afvoer gebeurt.'),
            ('Kan ik een terugkerende verstopping melden?', 'Ja. Geef aan hoe vaak het probleem terugkomt, welke afvoer het betreft en of andere afvoeren in huis dezelfde klachten hebben.'),
            ('Wat als de klus nog onderdeel is van een verbouwing?', 'Beschrijf de huidige aansluitingen, de gewenste verandering en wanneer het werk gepland is. Het contact daarna bepaalt of en onder welke voorwaarden de klus kan worden opgepakt.')
        ]
    },
    'rotterdam': {
        'name': 'Rotterdam',
        'description': 'Lekkage, verstopping of sanitairwerk in Rotterdam? Geef verdieping, woningtype en klachten door en stuur je aanvraag via WhatsApp.',
        'heading': 'Een loodgietersvraag in een woning of appartement',
        'sections': [
            ('Lekkage en gevolgen voor een andere verdieping', 'In een appartement kan een vochtplek ook in een onderliggende ruimte zichtbaar worden. Geef je eigen verdieping door, waar je water ziet en of buren eveneens iets merken. Noteer of het water blijft lopen of na gebruik van de badkamer verschijnt. De plek van de schade vertelt op zichzelf nog niet waar een lek zit.'),
            ('Meerdere afvoeren die tegelijk reageren', 'Borrelt de wastafel wanneer je een andere afvoer gebruikt, of komt er water in de douche terug? Vertel welke afvoeren meedoen en welke nog wel normaal functioneren. In een gedeeld gebouw is het nuttig te melden of andere woningen dezelfde klacht hebben. De oorzaak hoeft bij je eerste bericht nog niet vast te staan.'),
            ('Bereikbaarheid van leidingwerk en sanitair', 'Voor een kraanreparatie of aanpassing van sanitair geef je aan hoe de aansluiting bereikbaar is. Noem of die in een keukenkast, achter een wand of in een gezamenlijke ruimte ligt. Bij een Rotterdamse bovenwoning of hoogbouwappartement helpt ook informatie over de toegang en wie de werkplek kan openen.')
        ],
        'faqs': [
            ('Wat vermeld ik als benedenburen water zien?', 'Noem beide verdiepingen en de ruimtes waar vocht zichtbaar is. Geef aan wanneer het begon en of er op dat moment water werd gebruikt.'),
            ('Moet ik weten of de verstopping in een gedeelde leiding zit?', 'Nee. Beschrijf de klachten en vermeld wat andere bewoners merken. Schrijf ook op of de gebouwbeheerder al is geïnformeerd.'),
            ('Kan ik een foto van een ingebouwde aansluiting sturen?', 'Stuur een foto van wat zichtbaar is en beschrijf wat achter de ombouw ligt, als je dat weet. Open geen wand of installatie alleen voor het aanvraagbericht.')
        ]
    },
    'utrecht': {
        'name': 'Utrecht',
        'description': 'Een loodgietersklus in Utrecht? Beschrijf lekkage, verstopping of een sanitairaanpassing, inclusief bereikbaarheid, en stuur je vraag via WhatsApp.',
        'heading': 'Wat moet er in je woning worden onderzocht of aangepast?',
        'sections': [
            ('Vocht dat verschijnt na het douchen', 'Schrijf op waar het vocht zit en hoe snel het na gebruik zichtbaar wordt. Is het een plek op het plafond, langs een wand of onder een aansluiting? Vermeld of de plek terugkomt en of er op andere momenten ook water te zien is. Een beschrijving van het verloop helpt om je vraag af te bakenen.'),
            ('Een afvoer in een gedeelde woning', 'Als meerdere bewoners een keuken of badkamer gebruiken, geef dan aan welke ruimte problemen geeft en of alle gebruikers dezelfde klachten merken. Vertel of het probleem bij één afvoer begon. Maak onderscheid tussen langzaam weglopend water, borrelen en water dat terugkomt; je hoeft de oorzaak niet zelf te bepalen.'),
            ('Leidingen achter een kast of wand', 'Een bestaande aansluiting verplaatsen vraagt andere informatie dan een kraan vervangen. Geef aan welke verandering je wilt en wat van de huidige installatie zichtbaar is. Vermeld bij een Utrechtse woning je buurt en woningtype, bijvoorbeeld een appartement of woonhuis. Beschrijf ook of de werkplek tijdens een verbouwing al vrij toegankelijk is.')
        ],
        'faqs': [
            ('Wat als de vochtplek alleen na douchen verschijnt?', 'Vermeld na welk gebruik je de plek ziet, in welke ruimte en of de plek groter wordt. Voeg een foto van de omgeving toe zodra WhatsApp opent.'),
            ('Kan één bewoner de aanvraag namens een gedeeld huis sturen?', 'Ja. Vermeld wie contactpersoon is, welke gezamenlijke ruimte betrokken is en wie toegang tot de werkplek kan geven.'),
            ('Welke gegevens helpen bij het verplaatsen van een aansluiting?', 'Beschrijf de bestaande plek, de gewenste nieuwe plek en wat er nu zichtbaar is. Foto’s helpen bij de eerste vraag; de uiteindelijke werkzaamheden worden na contact besproken.')
        ]
    },
    'denhaag': {
        'name': 'Den Haag',
        'description': 'Loodgieter nodig in Den Haag? Meld lekkage, verstopping of sanitairwerk met de juiste gegevens en verstuur je aanvraag zelf via WhatsApp.',
        'heading': 'Een aanvraag voor je keuken, badkamer of leidingwerk',
        'sections': [
            ('Vocht in een bovenwoning', 'Bij een lekkage in een bovenwoning is het nuttig te vertellen of benedenburen een plek zien. Beschrijf waar in jouw woning water zichtbaar is en of het na gebruik van keuken of badkamer verschijnt. Noem ook of er nog water stroomt en of de watertoevoer is afgesloten. Een aanvraag geeft geen directe afspraak of spoedgarantie.'),
            ('Water dat in een andere afvoer omhoogkomt', 'Komt er water terug in de douche wanneer je een andere afvoer gebruikt? Noteer wat je precies deed toen het gebeurde. Vermeld welke afvoeren betrokken zijn en of het toilet normaal doorspoelt. Geef ook door welke middelen of hulpmiddelen eerder zijn gebruikt; verschillende chemische middelen mogen niet worden gecombineerd.'),
            ('Een reparatie aan sanitair voorbereiden', 'Noem het onderdeel dat je wilt laten repareren of vervangen en beschrijf de bestaande aansluiting. In een Haags appartement kan toegang tot een gezamenlijke ruimte nodig zijn. Vermeld dan of de beheerder al is benaderd en wie toegang kan geven. Bij een werkplek in een eigen keuken of badkamer helpt een foto van de aansluiting.')
        ],
        'faqs': [
            ('Welke informatie hebben jullie nodig over benedenburen?', 'Vermeld of zij vocht of druppels zien, in welke ruimte dat is en wanneer het begon. Je hoeft geen persoonlijke gegevens van buren mee te sturen.'),
            ('Wat als water terugkomt bij het doorspoelen?', 'Beschrijf waar het water omhoogkomt en welke handeling eraan voorafgaat. Gebruik de betreffende afvoer niet extra om het probleem voor een foto te herhalen.'),
            ('Kan ik een klus in een gemeenschappelijke ruimte melden?', 'Ja. Noem de ruimte en geef aan wie de beheerder is of wie toegang kan regelen. Afspraken over werkzaamheden worden in het verdere contact besproken.')
        ]
    },
    'eindhoven': {
        'name': 'Eindhoven',
        'description': 'Lekkage, verstopte afvoer of een aansluiting in Eindhoven? Lees welke details helpen en stuur je loodgietersvraag via WhatsApp.',
        'heading': 'Van een bestaande aansluiting tot nieuw sanitair',
        'sections': [
            ('Water bij een aangesloten apparaat', 'Zie je water bij een wasmachine, vaatwasser of andere aansluiting? Geef aan waar het nat is en of de klacht tijdens gebruik verschijnt. Vermeld of het toestel onlangs is aangesloten of verplaatst. Beschrijf alleen wat je ziet; een lekkage aan een leiding en een probleem in een apparaat zijn niet zonder onderzoek van elkaar te onderscheiden.'),
            ('Eén of meerdere trage afvoeren', 'Een langzaam leeglopende gootsteen is een andere situatie dan meerdere afvoeren die tegelijk water teruggeven. Zet daarom in je bericht welke plekken problemen hebben en wanneer de klachten begonnen. Geef aan of er recent iets is veranderd aan de keuken of badkamer en wat je al hebt geprobeerd.'),
            ('Een nieuwe aansluiting of kraan', 'Wil je sanitair laten vervangen of een aansluiting laten aanpassen in je Eindhovense woning? Geef aan wat er nu aanwezig is, wat je wilt aansluiten en hoe de leidingen bereikbaar zijn. Een foto van de bestaande aansluitpunten is nuttig bij de aanvraag. Eventuele werkzaamheden en kosten worden vervolgens besproken.')
        ],
        'faqs': [
            ('Wat vermeld ik als de lekkage na installatiewerk begon?', 'Noem welk onderdeel recent is aangesloten of verplaatst, wanneer dit gebeurde en waar je nu water ziet. Voeg zo mogelijk een foto van de zichtbare aansluiting toe.'),
            ('Kan ik vragen naar een aansluiting die nog niet aanwezig is?', 'Ja. Beschrijf welk toestel of sanitair je wilt plaatsen en wat er in de ruimte al beschikbaar is. Je aanvraag wordt daarna besproken.'),
            ('Moet ik zelf een apparaat demonteren voor een foto?', 'Nee. Een overzichtsfoto van de bereikbare onderdelen en een beschrijving van de klachten zijn voldoende voor een eerste bericht.')
        ]
    },
    'tilburg': {
        'name': 'Tilburg',
        'description': 'Loodgieter nodig in Tilburg? Beschrijf een terugkerende verstopping, lekkage of sanitairklus en stuur je aanvraag via WhatsApp.',
        'heading': 'Een terugkerend probleem duidelijk beschrijven',
        'sections': [
            ('Een kraan of koppeling die druppelt', 'Druppelt het terwijl de kraan dicht staat, of wordt het onder de gootsteen alleen nat na gebruik? Noteer dat verschil en vertel welke aansluiting zichtbaar is. Een foto van de kraan en de ruimte eronder helpt om de situatie te tonen. Geef ook aan hoe lang dit speelt en of het druppelen erger wordt.'),
            ('Een verstopping die steeds terugkomt', 'Vertel hoe vaak de afvoer problemen geeft en wat er vlak daarvoor werd gebruikt: keuken, douche of een aangesloten apparaat. Meld of een eerdere ingreep tijdelijk hielp. Maak in je aanvraag duidelijk of één afvoer langzaam leegloopt of meerdere plekken tegelijk reageren. Zo beschrijf je het patroon in plaats van alleen de huidige klacht.'),
            ('Leidingwerk bij een verbouwing', 'Bij aanpassingen in keuken of badkamer helpt een overzicht van de bestaande situatie. Geef je Tilburgse wijk, woningtype en het gewenste werk door. Noem welke aansluitingen blijven en wat verplaatst of vervangen moet worden. Als er een planning voor andere werkzaamheden is, zet die erbij zodat het gewenste moment duidelijk is.')
        ],
        'faqs': [
            ('Wat als de afvoer na een paar dagen weer verstopt raakt?', 'Vermeld wanneer het probleem terugkomt en wat er eerder is gedaan. Geef ook aan of het altijd dezelfde afvoer betreft.'),
            ('Welke foto stuur ik van een lekkende keukenkraan?', 'Een overzicht van de kraan en, indien veilig bereikbaar, de aansluitingen onder de gootsteen helpt. Schrijf erbij wanneer het druppelt.'),
            ('Kan ik een gewenste werkdatum doorgeven?', 'Ja. Kies het passende moment in het formulier en licht je planning toe. Beschikbaarheid wordt na ontvangst van je bericht besproken.')
        ]
    },
    'groningen': {
        'name': 'Groningen',
        'description': 'Een loodgietersklus in Groningen? Beschrijf lekkage, verstopping of sanitairwerk in je woning en stuur de gegevens via WhatsApp.',
        'heading': 'Een klus in een eigen of gedeelde woning',
        'sections': [
            ('Lekkage in een gezamenlijk gebruikte ruimte', 'In een gedeeld huis kan de melding over een keuken, badkamer of afzonderlijke kamer gaan. Vertel welke ruimte wateroverlast heeft en welke bewoners dat merken. Noteer of het water continu zichtbaar is of alleen tijdens gebruik. Geef aan wie de ruimte kan openen en of de watertoevoer al is afgesloten.'),
            ('Problemen met een gezamenlijke afvoer', 'Wanneer verschillende bewoners dezelfde afvoer gebruiken, helpt het om de klachten per plek te beschrijven. Is alleen de douche traag of loopt ook de keuken slecht door? Komt er water in een andere ruimte terug? Schrijf op sinds wanneer dit gebeurt en wat eerder is geprobeerd. Eén contactpersoon kan deze informatie verzamelen voor de aanvraag.'),
            ('Sanitair in een woning of appartement', 'Wil je een kraan of ander sanitair laten repareren of vervangen? Noem het onderdeel en de bereikbaarheid van de aansluiting. Geef bij een Groningse woning ook de buurt, verdieping en het woningtype door. Als een verhuurder of beheerder betrokken is, vermeld dan of je de gewenste werkzaamheden al met die persoon hebt besproken.')
        ],
        'faqs': [
            ('Kan ik een aanvraag doen voor een gedeelde keuken?', 'Ja. Geef aan welke aansluiting of afvoer problemen geeft en wie de contactpersoon is. Vermeld ook wie toegang tot de keuken kan regelen.'),
            ('Moeten alle bewoners een afzonderlijk bericht sturen?', 'Dat hoeft niet. Eén bericht met de klachten in de verschillende ruimtes kan de situatie overzichtelijk beschrijven.'),
            ('Wat als de hoofdkraan niet bekend is?', 'Zet dat in je bericht. Beschrijf wat je wel weet over de plek van het water en de betrokken ruimte; ga geen onbekende afsluiters uitproberen om de aanvraag in te vullen.')
        ]
    }
}

def additional_content():
    result = {}
    for slug, data in PLACES.items():
        name = data['name']
        sections = ''.join(f'<h3>{escape(title)}</h3><p>{escape(text)}</p>' for title, text in data['sections'])
        faqs = ''.join(f'<details><summary>{escape(question)}</summary><p>{escape(answer)}</p></details>' for question, answer in data['faqs'])
        body = (f'<section class="section" id="klussen-{slug}"><div class="wrap content">'
                f'<span class="kicker">Lekkage, verstopping en sanitair</span><h2>{escape(data["heading"])}</h2>{sections}'
                f'<p>Voor een gerichte aanvraag kun je ook de pagina over <a href="/lekkage-{slug}/">lekkage in {name}</a> '
                f'of <a href="/verstopping-{slug}/">verstopping in {name}</a> bekijken.</p></div></section>'
                f'<section class="section soft"><div class="wrap content faq"><span class="kicker">Praktische vragen</span>'
                f'<h2>Veelgestelde vragen over loodgieterswerk in {name}</h2>{faqs}'
                f'<p>Na het invullen opent WhatsApp met je bericht. Je verstuurt het daar zelf. Beschikbaarheid, werkzaamheden '
                f'en eventuele kosten worden na contact besproken. Bekijk ook de <a href="/veelgestelde-vragen/">algemene vragen over aanvragen</a>.</p>'
                f'</div></section>')
        result[slug] = {'name': name, 'description': data['description'], 'body': body}
    return result
