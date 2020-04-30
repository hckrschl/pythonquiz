#!/usr/bin/env python3

import random

# hier speichern wir alle quizfragen und deren antworten.
quizfragen = [("Worin hamstern Hamster ihr Essen?", "Backentaschen"),
              ("Haben Hamster Höhenangst?", "Nein"),
              ("Wann sind Hamster wach?", "nachts")]

print("\n🐹🌸  WILLKOMMEN BEIM HAMSTERQUIZ! 🌸🐹")

# so lange das programm nicht abgebrochen wird, quizzen wir:
while(True):
    # wähle eine zufällige frage und deren antwort aus
    frage_und_antwort = random.choice(quizfragen)
    frage = frage_und_antwort[0]
    richtige_antwort = frage_und_antwort[1]

    # stelle die Ffage
    print("~~~~~~~~~~~\nHAMSTERFRAGE:")
    print(frage)

    # frage die benutzerin nach ihrer antwort und speichere sie ab
    user_antwort = input("\nDEINE ANTWORT:\n")

    # überprüfe ob die antwort stimmmt
    if (user_antwort == richtige_antwort):
        print("Richtig! 🌸\n")
    else:
        print("Leider falsch. Die richtige Antwort war: ", richtige_antwort, "\n")