#!/usr/bin/env python3

import random

# hier speichern wir alle quizfragen und deren antworten.
quizfragen = [("Worin hamstern Hamster ihr Essen?", "Backentaschen"),
              ("Haben Hamster Höhenangst?", "Nein"),
              ("Wann sind Hamster wach?", "nachts")]

print("\n🐹🌸  WILLKOMMEN BEIM HAMSTERQUIZ! 🌸🐹")
name = input("Wer bist du?\n")
print("Hallo " + name + "! :)\n")

# gehe alle Quizfragen durch und stelle sie
for frage_und_antwort in quizfragen:

    # indem wir variablen verwernden, machen wir den Code leichter zu lesen
    frage = frage_und_antwort[0]
    richtige_antwort = frage_und_antwort[1]

    # stelle die Frage
    print("~~~~~~~~~~~~\nHAMSTERFRAGE:")
    print(frage)

    # frage die benutzerin nach ihrer antwort und speichere sie ab
    user_antwort = input("\nDEINE ANTWORT:\n")

    # überprüfe ob die antwort stimmmt
    if user_antwort == richtige_antwort:
        print("✅ Richtig! \n")
    else:
        print("🛑 Leider falsch. Die richtige Antwort war: " + richtige_antwort + "\n")

    input("Bereit für die nächste Frage?\n")