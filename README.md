# 1. Aus- und Eingabe
## Aufgabe
Begrüße deine Benutzerin und frage sie nach ihrem Namen.
Gib ihn danach wieder aus.
Der Gesamtdialog könnte z.B. so aussehen:

```
🐹🌸  WILLKOMMEN BEIM HAMSTERQUIZ! 🌸🐹
Wer bist du?
Lotte
Hallo Lotte ! :)
```
Natürlich kannst du dein Quiz zu allen möglichen Themen machen und die Begrüßung so gestalten wie es zu deinem Quiz passt.

## Befehle, die du dafür brauchst:
`print()`
`input()`

## Tips
- text schreibt man in `"Anführungszeichen"`


# 2. Informationen abspeichern mit Variablen und Datentypen
## Aufgabe
1. Überlege dir mindestens zwei Quizfragen und deren Antworten
2. Erstelle eine Liste von Frage-Antwort-Tupeln
3. Speichere diese Liste von Tupeln als Variable. Du kannst die Variable z.B. `quizfrage` nennen.
4. Gebe dein erstes frage-antwort-tupel mit print() aus
4. Gebe nur die erste Antwort mit print() aus

## Tips
- In python fängt man bei 0 an zu zählen! das heißt, das 0. Element aus der Liste `[x, y, z]` ist `x`, das 1. `y` und das 2. `z`

## Spickzettel

```
zahl = 12
zahl = 15                                       # diese variable hat nun einen neuen wert
text = "hallo ich bin ein stück text. im Programmierjargon heiße ich 'string'."
liste = ["stranger things", "mad men", "the great british bakeoff", "die sendung mit der maus"]
tupel = ("salz", "pfeffer")
liste_von_tupeln = [paar, (zahl, text)]
erstes_paar_aus_der_liste = liste_von_paaren[0] # obacht! wir zählen ab 0!
```

# 3. Entscheidungen treffen mit If-else
## Aufgabe
Du weißt bereits, wie man Quizfragen ausgibt und user-eingaben speichert. Wenn wir dieses Wissen mit if-else abfragen kombinieren, können wir eine Quizrunde implementieren

1. Ändere deinen Code so ab, dass nur die erste Frage ausgegeben wird– und speichere die Antwort, die du von der Benutzerin bekommst
2. Überprüfe mit einem `if ... else` Block, ob die Antwort die gleich ist wie die, die du in deinen quizfragen abgespeichert hast
3. Gebe eine passende Fehler- oder Erfolgsmeldung aus.

Der Gesamtdialog könnte z.B. so aussehen:

```
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