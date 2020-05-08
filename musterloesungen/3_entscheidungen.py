print("\n🐹🌸  WILLKOMMEN BEIM HAMSTERQUIZ! 🌸🐹")
name = input("Wer bist du?\n")
print("Hallo " + name + "! :)")

quizfragen = [("Worin hamstern Hamster ihr Essen?", "Backentaschen"),
              ("Haben Hamster Höhenangst?", "Nein"),
              ("Wann sind Hamster wach?", "nachts")]

erste_frage_und_antwort = quizfragen[0]

erste_antwort = erste_frage_und_antwort[1]
erste_frage = erste_frage_und_antwort[0]

benutzerinnnen_antwort = input(erste_frage + "\n")

if (benutzerinnnen_antwort == erste_antwort):
  print("✅ Richtig! \n")
else:
  print("🛑 Leider falsch. Die richtige Antwort war: "+ erste_antwort + "\n")