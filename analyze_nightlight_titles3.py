# -*- coding: utf-8 -*-
import re, sys
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

titles = [
"Gemmac Bij Nachtlampje voor Kinderen, 3 Helderheidsniveaus 7 Kleuren",
"Gemmac Siliconen Nachtlampje Kikker Led Bedlampje USB-Oplaad en Timingfunctie Touch-bediening Borstvoeding 3 Helderheidsaanpassing 7 kleuren Tafellamp Slaapkamerdecoratie Kerst- en Verjaardagscadeaus",
"FAMIDUO Voetbal Nachtlampje voor Kinderen, Lucky 7 Rood Groen",
"ZKLiLi Bunny Nachtlampje voor Kinderen, 16 Kleuren Lamp Schattig, Dimbare Baby Nachtlampjes voor Kinderkamer, Siliconen Oplaadbare Nachtlampje voor Kinderkamer, Kawaii Kamerdecoratie",
"Diboniur Nachtlampje voor kinderen, oplaadbaar, nachtlampje voor baby's, 7 kleuren, led, nachtlampje voor meisjes, siliconen, bedlampje, touchscreen, voor kinderen, volwassenen, slaapkamer, decoratie,",
"URAQT Siliconen Nachtlampje Kinderen, Eend Led Bedlampje USB-Oplaad en Timingfunctie 1200 mAh Kawaii Nachtlampje met Aanraakschakelaar en Helderheidsaanpassing 3 Niveaus Houder voor Mobiele Telefoon",
"FAMIDUO Axolotl Kindernachtlampje, Roze Axolotl Lamp, Zacht LED Nachtlampje voor Kinderkamer, Zachte Siliconen Dierenbedlamp van Voedselkwaliteit, Schattige Kamerdecoratie voor Moeder, Meisjes, Baby",
"Nachtlampje voor kinderen, Kawaii, nachtlampje voor kinderen, met timerfunctie, USB-oplaadbaar, siliconen lamp voor kinderen, voor woonkamer, kinderkamer, slaapkamer",
"Diboniur Nachtlampje voor kinderen, wolk, nachtlampje voor baby's",
"Nachtlampje voor kinderen, 7 kleuren, zacht siliconen nachtlampje voor kinderen met 3 dimbare niveaus, oplaadbaar, niet-verblindend, zacht en schattig, leeuwenvorm, nachtlampje touch",
"AUAUY Nachtlampje eenhoorn nachtlampje siliconen dier met timer",
"Gemmac Nachtlampje voor Kinderen, LED Siliconen Nachtlampje, LED-Nachtlampje met 7 Kleuren 3 Lichtmodi Timer Dimbaar Touch USB Oplaadbaar Bedlampje, Dierentouch-Lamp voor Slaapkamer Verjaardagscadeau",
"Pinguïn nachtlampje voor kinderen, Kawaii nachtlampje voor kinderen, met timerfunctie, oplaadbare siliconen nachtlampje, draagbaar, cadeau voor jongens en meisjes",
"Tremdwoto Nachtlampje voor kinderen, schattig kat nachtlampje op batterijen voor de kinderkamer, draagbaar nachtlampje van zachte siliconen, verjaardagscadeau voor meisjes en jongens",
"Amaredom Nachtlampje vos siliconen led dimbare timer voor kinderen",
"HOTUT Ster nachtlampje voor kinderen, USB oplaadbaar Siliconen Nachtlampje Kinderen, Kawaii Kid-nachtlampje, 3 lichtmodi, Magnetische muurophanging, draagbaar aanraakdimmend kindernachtlampje",
"FAMIDUO Pinguïn Nachtlampje, Schattige Roze Pinguïn Lamp met Gebreide Muts, Zacht Siliconen Daglicht voor Baby, Oplaadbaar/Dimbaar/Timer, Zacht LED Nachtlampje, Leuke Cadeaus voor Kinderen",
"URAQT Schattig smileygezicht Peer Nachtlampje, Zacht Kinderkamer Siliconen lamp, USB-opladen Squishy nachtlampje, LED-aanraaklicht Geschikt voor Kinderen, Peuters, Vrouwen en Tienermeisjes",
"URAQT Capybara nachtlampje voor kinderen, Capybara nachtlampje met aanraakbediening, opladen via USB en timer, dimbaar siliconen nachtlampje, nachtlampje voor pasgeborenen voor meisjeskamers cadeau",
"AmmToo Eenhoorn nachtlampje voor kinderen, 3 lichtmodi, instelbaar met timer, touch-bediening, siliconen, oplaadbaar via USB",
"Schattige siliconen Kung Fu Panda nachtlamp, 3-standen dimbare helderheid met 30 min timer, oplaadbare zachte siliconen nachtlamp, perfecte kinderkamer decoratie voor kinderen, vrouwen",
"Siliconen Nachtlamp Dimbaar Tik Sensor Kinderen Kat Silicone Nachtlampje",
"Siliconen Nachtlampje voor Kinderen, Oplaadbare Schattige",
"Veilleuse Kind in de Vorm van de Paar, Veilleuse Oplaadbare USB met Minuter, Tactiele Schakelaar, Bedlamp voor Slaapkamer, Kinderkamer en Woonkamer",
"URAQT Kindernachtlampje, siliconen nachtlampje met aanraaksensor, schattig konijn kinderslaapkamerverlichting met 30 minuten timerfunctie, USB oplaadbaar, voor kinderkamer, pasgeboren cadeau",
"Aigostar Uil nachtlampje kinderen, 7 kleuren & warm wit, touch-bediening",
"Nachtlampje voor kinderen, ultrazachte siliconen haas, nachtlampje voor baby's, met klokbediening, 30 minuten timer en 1200 mAh, USB-oplaadbaar, 3 helderheidsniveaus, dimbaar, voor meisjes, cadeau",
"GIBOHOM Eenhoorn nachtlampje voor kinderen, led, dimbare touch-bediening, siliconen nachtlampje voor kinderkamer met 30 minuten timer, USB-oplaadbaar, 3 lichtmodi, nachtlampje baby, eenhoorn, cadeau",
"Nachtlampje voor kinderen, touch-bediening, dimbare nachtlamp met 3 helderheidsniveaus en automatische uitschakeling van 20 minuten, zachte siliconen bedlamp voor",
"HOTUT wolken nachtlampje voor kinderen, USB oplaadbaar Siliconen Nachtlampje Kinderen, Kawaii Kid-nachtlampje, 3 lichtmodi, Magnetische muurophanging, draagbaar aanraakdimmend kindernachtlampje",
"Gemmac Nachtlampje voor Kinderen Siliconen Kawaii Nachtlampje Zacht Dimbare Oplaadbare LED 7 Kleur Licht Kinderkamer, Siliconen Dierenbedlamp van Voedselkwaliteit Slaapkamerdecoratie Cadeau",
"Ainiv Wolk Nachtlampje, Schattige Siliconen Kinderkamer Nachtlamp, Aanraakbediening Nachtlampjes USB Oplaadbaar Nachtkastje Lamp, 3 Niveaus Helderheid, 30 Minuten Timer, Schattige Kamerdecoratie",
"xinrongda Capybara Nachtlampje voor kinderen, bedlampje voor kinderen, Capybara-lamp, dimbaar, siliconen nachtlampje, USB-oplaadbaar, 2 helderheidsniveaus, nachtlampje voor slaapkamer",
"Nachtlampje voor kinderen, oplaadbaar siliconen LED-nachtlampje in de vorm van een haai met 7 kleuren, ideaal als verjaardagscadeau voor babyjongens, kinderen, peuters, tienermeisjes en de kinderkamer",
"IHALO Nachtlampje voor kinderen en kinderkamer, USB-oplaadbaar, dimbaar, led-nachtlamp met schattig kampvuur design, slaaphulp en borstvoedingslicht voor baby's en kinderen, decoratie",
"SOLIDEE Bunny Nachtlampje voor kinderen, siliconen voedingslicht voor baby's, met 7 lichtwisselingen, dimbaar, tap control, opladen via USB en timerfunctie, bedlampje voor kinderkamer, decoratie",
"Tremdwoto Bier Nachtlampje voor kinderen, schattig nachtlampje op batterijen voor kinderkamer, draagbaar nachtlampje van zachte siliconen ，Cadeaus voor jongens en meisjes",
"Nachtlampje voor kinderen, 7 kleuren, zacht siliconen nachtlampje voor kinderen met 3 dimbare niveaus, oplaadbaar, niet-verblindend, zacht en schattig, wolkenvorm, nachtlampje touch",
"One Fire Nachtlampje voor kinderen, 16 kleuren, 5 helderheidsniveaus, eenhoorn, cadeau voor meisjes, 1200 mAh, siliconen, roze",
"Led-nachtlampje voor kinderen, USB-oplaadbaar, nachtlampje voor kinderen, van siliconen, helderheidsinstelling door klikken en kan worden getimed, babynachtlampje, verjaardags- en kerstcadeaus",
"Mewaii Eenhoorn Nachtlampje voor Kinderen, Oplaadbaar, Zacht Siliconen",
"DoDo Duck Kinderverlichting, USB-oplaadbaar nachtlampje met timer, touch-schakelaar, draagbaar nachtlampje voor slaapkamer, kinderkamer en woonkamer",
"Gemmac Basketbal Nachtlampje voor Kinderen, Dimbare Silicone Nachtlampje",
"Schattige Eendenlamp, LED Nachtlicht voor Kinderen, Oplaadbaar Draagbaar Dodo Eend Nachtlampje, Nachtlamp Kinderkamer Decoratie, Slaapkamerdecoratie, Draagbaar Cadeau voor Meisjes/Jongens",
"BONNYCO Nachtlampje voor Kinderen met Afstands- & Aanraakbediening en 16 Kleuren. Nachtlamp Kinderkamer met Timer, Konijn Siliconen Kinder Bedlampje BPA-vrij. Geschenk voor Meisjes en Jongens",
"Gemmac Krokodil Siliconen Nachtlampje Witte Ruis Stil Licht Dimbaar Touch USB Oplaadbaar LED-Nachtlampje 30 Timer 5 Witte Ruis Zachte Siliconen Dierenbedlamp Schattige Kamerdecoratie Cadeau Meisjes",
"IHALO Schattig nachtlampje voor kinderen, borstvoedingslicht voor babyverzorging in de kinderkamer, nachtlampje baby, zachte siliconen touch-nachtlampje, RGB-licht, nachtlamp bij voor pasgeborenen",
"Huggwaii Sponsachtig dinosaurusnachtlampje voor kinderen, dimbaar siliconen nachtlampje met 4 witte geluiden, oplaadbare dinosauruslamp met lange levensduur, nachtlampje voor",
"AUAUY Axolotl nachtlampje, oplaadbaar, USB, touch-nachtlampje van siliconen",
"FAMIDUO Schedel nachtlampje, knijpbaar siliconen met antipp-functie, warmwit en 7 kleuren RGB, BPA-vrij, blauw lichtvrij oogvriendelijk nachtlampje voor babyvoeding, kinderkamerdecoratie, camping",
"Leuke Baby Nachtlampje Kids Lamp, Eend Slaaplichten met Touch Sensor Baby Siliconen Nachtlampje Oplaadbare Batterij Dimbare Nachtlamp Kerstcadeaus voor Baby, Kinderen, Tiener Slaapkamer (Beer)",
"Auxmir Babynachtlampje Touch met 6 Kleuren, LED Kindernachtlampje van Zachte Siliconen, USB Oplaadbaar 2000mAh, Draadloos Schattig Bedlampje met Dimfunctie voor Jongens, Meisjes en Pasgeborenen",
"One Fire Nachtlampje voor kinderen, 16 kleuren, instelbare helderheid, dinosaurus met afstandsbediening, oplaadbare siliconen lamp voor baby's en jongens",
"One Fire Kawaii Nachtlampje voor Kinderen, 16 Kleuren + Dimbaar + Afstandsbediening, Veilig en Energiezuinig, USB-oplaadbaar, Haas, Silicone, Meerkleurig",
"kindernachtlampje, draagbaar oplaadbaar, 4 instelbare helderheid cloud-nachtlampje, nachtlamp voor meisjesslaapkamer, babycadeau (blauw)",
"Sxhlseller Siliconen Nachtlampje, Schattige Maanvormige Oplaadbare",
"Siliconen eend nachtlampje, kinderkamer nachtlampje eend, Schattige",
"Silicone Nachtlampje voor Kinderen Schattige Tenniesball Nachtlampen",
"Siliconen nachtlampje met aanraaksensor voor kinderkamer, kinderkamer en bed",
"Nachtlampje voor kinderen, oplaadbaar siliconen LED-nachtlampje in de vorm van een haai met 7 kleuren, ideaal als verjaardagscadeau voor babyjongens, kinderen, peuters, tienermeisjes en de kinderkamer",
"BONNYCO Nachtlampje voor Kinderen met Afstands- en Aanraakbediening en 16 Kleuren. Nachtlamp Kinderkamer Timer, Pinguïn Siliconen Kinder Bedlampje BPA-vrij. Geschenk voor Jongens en Meisjes",
"FAMIDUO Voetbal Nachtlampje voor Kinderen, Siliconen Nachtlampje Babykamer BPA-Vrij, Oplaadbaar Warm & RGB Licht met Timer, Voetbal Cadeau Jongens Meisjes, Rood-Blauw Teamkleuren Voetballampje",
"IHALO Schattig nachtlampje voor kinderen, borstvoedingslicht voor babyverzorging in de kinderkamer, nachtlampje baby, zachte siliconen touch-nachtlampje, RGB-licht, nachtlamp bij voor pasgeborenen",
"Nachtlampje voor kinderen, siliconen borstvoedingslamp voor baby's met 7 kleuren, USB-opladen en timer, dimbaar borstvoedingsnachtlampje, bedlampje voor kinderkamer, geschenken",
"kindernachtlampje, draagbaar oplaadbaar, 4 instelbare helderheid cloud-nachtlampje, nachtlamp voor meisjesslaapkamer, babycadeau (wit)",
"Nachtlampje eend, siliconen, led, touchscreen, oplaadbaar, kinderen",
"TFA Dostmann Nachtlampje Pinguïn, oplaadbaar led-babynachtlampje | 43.2043 | BPA-vrije siliconen | kinderkamerlamp met 2 helderheidsniveaus | 20 minuten timer | grijs",
"FAMIDUO nachtlampje voor kinderen, siliconen Konijn nachtlampje, nachtlampje voor de kinderkamer, 7 kleurveranderingen, dimbare/oplaadbare voedingslamp met touchfunctie, cadeau voor kinderen",
"HOTUT maan nachtlampje voor kinderen, USB oplaadbaar Siliconen Nachtlampje Kinderen, Kawaii Kid-nachtlampje, 3 lichtmodi, Magnetische muurophanging, draagbaar aanraakdimmend kindernachtlampje",
"Koala Nachtlampje voor kinderen, dimbaar, USB-nachtlampje met timer",
"TFA Dostmann CAPYBARA LED nachtlampje kinderen, 43.2042, bruin",
"Gemmac Zebra LED siliconen Nachtlampje Stil Licht Dimbaar Touch USB Oplaadbaar LED-Nachtlampje Dimbaar met 30 Timer Zachte Siliconen Dierenbedlamp Schattige Kamerdecoratie Cadeau voor Moeder Meisjes",
"MERTTURM Capybara Nachtlampje voor Kinderen, Oplaadbare Babykamerlamp met Aanraakbediening/Dimbaar, Voedselveilig Siliconen Tafellampje voor Borstvoeding, Bedtijd, Cadeau",
"7 kleuren baby nachtlampje zachte siliconen baby nachtlampje met 3 helderheidsniveaus, oplaadbaar nachtlampje voor kinderkamer, woonkamer en slaapkamer",
"Macchiatto Voedingslicht baby nachtlampje ei, dimbare aanraaklamp met batterij, nachtlampje kinderen 2600 mAh, 7 kleuren RGB, 30/60 minuten timer, geheugenfunctie, klaphaak, voor borstvoeding in de",
"2 stuks Bubu Dudu Nachtlampje, LED Panda Nachtlampje Kinderen, Siliconen Nachtlampje Baby USB Oplaadbaar, Wit En Bruin",
"URAQT kindernachtlampje, siliconen nachtlampje met aanraaksensor, Panda schattig kinderslaapkamerlampje met 30 minuten timerfunctie, dimbaar en oplaadbaar, geschikt voor kinderen, pasgeboren cadeau",
"ZKLiLi Nachtlampje voor kinderkamer, 16 kleuren kattenlamp, schattige dimbare verlichting, siliconen oplaadbaar lampje, Kawaii decoratie",
"Ainiv Led-nachtlampje voor baby's, dinosaurus, siliconen nachtlampje",
"Sxhlseller Siliconen Nachtlampje, Schattige Maanvormige Oplaadbare (ster)",
"Konijn siliconen nachtlampje | het schattige konijn kinderkamer",
"RiToEasysports Siliconen Nachtlamp, Oplaadbare Touchlamp met 3 (Pompoen",
"Spooklamp Siliconen Nachtlampjes met Timer",
"FAMIDUO Eendenlamp, Schattig Eend Nachtlampje, Dimbaar Eendennachtlampje in 2 standen, LED Squishy Dierenlamp voor Kinderen om mee te Slapen, Oplaadbare Siliconen Nachtlamp, Uniek Cadeau Speelgoed",
"BUBU DUDU Schattig panda nachtlampje - 3-standen dimbare batterij-LED-lamp met siliconen touch, draagbare slaapkamerdecoratie en kinderkamercadeau voor meisjes/jongens-(BUBU)",
"Hama Led-nachtlampje voor kinderen, RGB, dimbaar en oplaadbaar, nachtlampje met timer (1 uur), batterij, zachte siliconen, borstvoeding, babylicht & kinderkamer lamp met kleurverandering",
"AUAUY Nachtlampje Walvis, Oplaadbaar USB Tactiel Nachtlampje van Siliconen",
"Nachtlampje voor kinderen, decoratief, van siliconen, oplaadbaar via USB, nachtlampje voor kinderen, nachtlampje, nachtlampje voor kinderen.",
"Puppy nachtlampje voor kinderen, siliconen, nachtlampje voor pasgeborenen, nachtlamp, Puppy Lu-ce nachtlampje voor kinderen, 7 kleuren, oplaadbaar via USB, zacht oppervlak",
"Star Nachtlampje voor kinderen, nachtlampje voor baby's, siliconen sterren, nachtlampje voor kinderen, 7 kleuren, ster-nachtlampje, via USB oplaadbaar, soft-touch-oppervlak, zachte",
"Winkee Mini nachtlampje kinderen beer, touch borstvoedingslicht 7 kleuren, USB oplaadbaar, BPA-vrij silicone, babykinderkamer cadeau (beer)",
"Draak nachtlampje, schattig cadeau voor kinderen, met 3 niveaus warm licht en RGB-kleurverandering, zachte siliconen led-touch-lamp, voor jongens en meisjes",
"Winkee Mini nachtlampje kinderen beer, touch borstvoeding licht 7 kleuren, USB oplaadbaar, BPA-vrij silicone, baby kinderkamer cadeau",
"AmmToo Nachtlamp voor kinderen, panda dimbaar, timer, touch-bediening, siliconen, USB-oplaadbaar, schattige lamp, kinderkamer, decoratie",
"Zacht nachtlampje voor kinderen, aanraakbediening met 16 dimniveaus, timer van 30/60 minuten, schattig oplaadbaar nachtlampje van siliconen in de vorm van een kat, decoratieve lamp voor de slaapkamer",
"Nachtlamp voor kinderen, panda, nachtlampje voor kinderen, 7 kleuren, borstvoedingslicht, dimbaar, met timer, touch-bediening, siliconen nachtlampje voor baby's, USB-oplaadbaar",
"Draken Nachtlampje Kinderen, LED Nachtlampje 7 Kleuren Dimbaar met Timer, Zachte Silicone & Oplaadbaar via USB, Magnetische Functie en Aanraakbediening, Cadeau voor Baby's, Jongens en Meisjes",
"Nachtlampje voor kinderen, stil licht met 7 kleuren en kleurverandering, 30 minuten timer, USB-C batterij, voedselveilige siliconen, zacht en inklapbaar, aanraaksensor, dimbaar, voor kinderkamer",
"Leuke Eendenlamp, Dierenkwekerij Siliconen Nachtlampje met Draagbare USB Oplaadbare Timer Dimbaar, Perfect voor Thuis Slaapkamer Woonkamer, Vakantie Verjaardag Xmas Pasen Decor Geschenken aan",
"Kindernachtlampje, panda-lamp, dimbaar, schattige panda, led-bedlamp, oplaadbaar met timer, slaaplamp voor kinderen, siliconen nachtlamp voor kinderkamer",
"LOVERUIS Nachtlampje voor Kinderen Schattige Eend Lamp Wit Siliconen Kinderslaapkamer Licht",
"Nachtlampje voor baby's, dinosaurus, siliconen lamp, nachtlampje voor",
"Gemmac Krokodil Siliconen Nachtlampje Witte Ruis Stil Licht Dimbaar Touch USB Oplaadbaar LED-Nachtlampje 30 Timer 5 Witte Ruis Zachte Siliconen Dierenbedlamp Schattige Kamerdecoratie Cadeau Meisjes",
"Ainiv Siliconen nachtlampje voor kinderen, nachtlampje voor baby's, dimbaar nachtlampje, voedingslicht, USB-oplaadbaar led-nachtlampje, kinderkamerdecoratie, slaapverlichting, babykamerdecoratie",
]

def tok(t):
    t = t.lower()
    t = re.sub(r"[\|\(\)\[\],\.;:&+/\\\-—–\u3000]", " ", t)
    t = re.sub(r"\d+(\.\d+)?", " ", t)
    return t.split()

# animal / shape terms
animals = ['kikker','voetbal','bunny','axolotl','eenhoorn','pinguïn','pinguin','vos','ster','kat','peer','capybara','kung','panda','uil','haas','konijn','wolk','wolken','haai','kampvuur','bier','basketbal','krokodil','schedel','dinosaurus','dino','walvis','beer','draak','draken','koala','zebra','maan','ei','pompoen','spook','squishy','tennisbal','tenniesball','dierenbedlamp','eend','eendenlamp','dodo','duck','smileygezicht','baby','leeuwen','leeuwenvorm','maanvormige','cloud']
acnt = Counter()
for t in titles:
    for w in tok(t):
        if w in animals:
            acnt[w]+=1
print("=== ANIMAL/SHAPE WORDS ===")
for w,c in acnt.most_common(40):
    print(f"{c}\t{w}")

# specific feature terms raw counts (substring)
feat = ['bpa','rgb','afstandsbediening','afstands','afstands-','magnetische','muurophanging','draagbaar','voedsel','voedselkwaliteit','voedselveilig','borstvoeding','witte ruis','ruis','squishy','draadloos','nachtkastje','oplaadbaar','usb','timer','minuten','helderheid','niveaus','lichtmodi','kleur','kawaii','decoratie','cadeau','geschenk','aanraak','touch','tactiel','dim','led','rgb','blauw lichtvrij','oogvriendelijk','geheugen','klaphaak','inklapbaar','stil licht']
print("\n=== FEATURE TERM SUBSTRING COUNTS ===")
fcnt = Counter()
lowtitles = [t.lower() for t in titles]
for f in feat:
    n = sum(1 for t in lowtitles if f in t)
    fcnt[f]=n
for f,c in fcnt.most_common(40):
    print(f"{c}\t{f}")
