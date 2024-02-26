import random
Vorname = input("Bitte Tragen Sie Ihren Vornamen ein: ")
Nachname = input("Bitte geben Sie Ihren Nachnahmen ein: ")
Hobby = input("Bitte geben Sie den Namen Ihres liebsten Hobbys ein: ")
Alter = int(input("Bitte geben Sie am Schluss noch Ihr Alter ein: "))
if Alter <= 30: 
    rnd = random.randint(Alter, Alter + 50)
elif Alter > 30:
    rnd = random.randint(Alter, Alter + 40)
elif Alter > 70:
    rnd = random.randint(Alter, Alter + 20)
print(f"Hallo, {Vorname} {Nachname}, Ich freue mich Sie kennenzulernen. Mit {Hobby}",
"habe Sie wirklich ein schönes Hobby ausgewählt." )
print(f"Da Sie {Alter} Jahre alt sind, werden Sie vermutlich ca. {rnd} Jahre alt.")