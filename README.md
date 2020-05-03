# 0. repl.it einrichten
- bei repl.it anmelden
- Auf -> my repls -> Multiplayer Repls (nur 1 Person pro team!) -> new repl gehen und ein eigenes repl anlegen (dort wird euer code gespeichert)
- im repl auf "share" klicken und eure teampartnerin, **nadjaobenaus** und **lotterleben** einladen
    * Effekt: Ihr könnt gemeinsam an einer Datei arbeiten und Nadja und ich können sehen was ihr da macht :)

- ☝️ Falls ihr etwas nachschlagen wollt, könnt ihr zB bei https://py-tutorial-de.readthedocs.io/de/python-3.3/index.html (auf Deutsch) oder https://www.w3schools.com/python/ (auf Englisch) suchen.

# 1. Aus- und Eingabe
## Aufgabe
Begrüße deine Benutzerin und frage sie nach ihrem Namen.
Gib ihn danach wieder aus.
Der Gesamtdialog könnte z.B. so aussehen:

```console
🐹🌸  WILLKOMMEN BEIM HAMSTERQUIZ! 🌸🐹
Wer bist du?
Lotte
Hallo Lotte ! :)
```
Natürlich kannst du dein Quiz zu allen möglichen Themen machen und die Begrüßung so gestalten wie es zu deinem Quiz passt.

## Befehle, die du dafür brauchst:
- `print()`
- `input()`

## Tips
- text schreibt man in `"Anführungszeichen"`
- wenn du dir notizen im code machen willst, beginne die Zeile mit `#`.

--------------------

# 2. Informationen abspeichern mit Variablen und Datentypen
## Aufgabe
1. Überlege dir mindestens zwei Quizfragen und deren Antworten
2. Erstelle eine Liste von Frage-Antwort-Tupeln
3. Speichere diese Liste von Tupeln als Variable. Du kannst die Variable z.B. `quizfrage` nennen.
4. Gebe dein erstes frage-antwort-tupel mit print() aus
4. Gebe nur die erste Antwort mit print() aus

## Tips
- `[ ]` schreibt man so:
    - auf Windows: `strg + alt + 8` und `strg + alt + 9`
    - auf Mac OS:  `alt + 5` und `alt + 6`
- In python fängt man bei 0 an zu zählen! das heißt, das 0. Element aus der Liste `[x, y, z]` ist `x`, das 1. Element ist `y` und das 2. Element `z`

## Bonusaufgabe
Da Fragen immer an der Ersten udn Antworten immer an der zweiten Stelle eines Tupels stehen, kannst du deinen code leichter lesbar machen, indem du 0 und 1 als Variable "einen Namen gibst".

## Spickzettel

```python
zahl = 12
zahl = 15   # diese variable hat nun einen neuen wert
text = "hallo ich bin ein stück text. im Programmierjargon heiße ich 'string'."
liste = ["stranger things", "mad men",
         "the great british bakeoff",
         "die sendung mit der maus"]
tupel = ("salz", "pfeffer")
liste_von_tupeln = [paar, (zahl, text)]
erstes_paar_aus_der_liste = liste_von_paaren[0] # obacht! wir zählen ab 0!
```

--------------------

# 3. Entscheidungen treffen mit If-else
## Aufgabe
Du weißt bereits, wie man Quizfragen ausgibt und user-eingaben speichert. Wenn wir dieses Wissen mit if-else abfragen kombinieren, können wir eine Quizrunde implementieren

1. Ändere deinen Code so ab, dass nur die erste Frage ausgegeben wird– und speichere die Antwort, die du von der Benutzerin bekommst
2. Überprüfe mit einem `if ... else` Block, ob die Antwort die gleich ist wie die, die du in deinen quizfragen abgespeichert hast
3. Gebe eine passende Fehler- oder Erfolgsmeldung aus.

Der Gesamtdialog könnte z.B. so aussehen:

```console
🐹🌸  WILLKOMMEN BEIM HAMSTERQUIZ! 🌸🐹
Wer bist du?
Lotte
Hallo Lotte! :)
Worin hamstern Hamster ihr Essen?
Vorratsschrank
🛑 Leider falsch. Die richtige Antwort war: Backentaschen
```

## Tips
- erinnere dich an `input()`

--------------------
# Bonus: Mehrere Antwortmöglichkeiten mit `or`

## Aufgabe
- überlege dir wie man die richtige Antwort auf deine erste Quizfrage noch schreiben kann (zum Beispiel ist neben "nein" auch "Nein",richtig)
- Packe diese schreibweise als einzelnen Text mit in dein Frage-Antworten-Tupel
- Überprüfe nun jede einzelne Schreibweise in deiner `if`-abfrage mit einem `or`

## Spickzettel
```python
quizfragen = [("Frage 1", "Nein", "nö"), ("Frage 2", "ja")]
frage_1 = quizfragen[0] # ergibt ("Frage 1", "Nein", "nö")
richtige_antwort_1 = quizfragen[1] # ergibt "Nein"
richtige_antwort_2 = quizfragen[2] # ergibt "nö"

if benutzerinnen_antwort == richtige_antwort_1 or benutzerinnen_antwort == richtige_antwort_2:
    print("richtig!")
```

--------------------

# Wiederholung: Variablen.
## Aufgabe
schaue auf deinen Code von gestern. Findest du stellen, die du durch die Nutzung von Variablen vereinfachen kannst?

## Tips
Variablen kannst du auch nutzen, um Daten einen verständlicheren Namen zu geben. Zum Beispiel:

```python
gruppen_von_freunden = [("Ernie", "Bert"), ("Tick", "Trick", "Track")]
entenfreunde = gruppen_von_freunden[1]     # ergibt ("Tick", "Trick", "Track")
entenfreund_1 = zweite_gruppe[0]           # ergibt "Tick"

print(gruppen_von_freunden[0][0])
print(entenfreund_1)
```

beide `print()`s geben `Tick` aus, aber wenn man `print(entenfreund_1)` liest ist schneller klar, wer gemeint ist. Das macht deinen code leichter zu verstehen.

--------------------
# 4. Alle Fragen durchquizzen mit Schleifen
## Aufgabe
- Verwende eine for-schleife, um alle deine Quizfragen auszugeben.
- wenn das klappt, kannst du auch deinen code der überprüft ob die Antworten richtig sind in die for-schleife verschieben
- nun hast du ein vollständiges quiz!

## Tips:
- denke an die korrekte einrückung!

```python
for elemente in liste:
    print("ich erscheine öfter auf dem Bildschirm")

print("ich nur ein mal")
```


--------------------
### BONUSAUFGABEN (Vorschläge!):
- wenbiger umständlich überprüfen ob die gegebene Antwort eine der Richtigen ist mit `antwort in [anfang:ende]`
- spielstand speichern und ausgeben
    * nächste erweiterung: multiplayermodus
- wenn die falsche antwort gegeben wurde, noch mal raten lassen
- Versuche durch googlen herauszufinden: wie kann ich verhindern, dass eine Antwort nur wegen anderer Groß- und Kleinschreibung als falsch gezählt wird? (tip: .lower())
- mehrere Antwortmöglichkeiten vorgeben und eine auswählen lassen– wie bekommt man das hin? (tip: es gibt mehrere wege, sei kreativ)
