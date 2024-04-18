liste = [1, 2, 3, 4, 5]
liste[1]
liste[-2]
print(liste[1], liste[-2])

#Slicing

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print (liste[::3])

# Dictionary Zugriff
dictionary = {"Hallo": "Welt", 1: -3, -3: 7.0}
print(dictionary["Hallo"], dictionary[-3])

# Dictionary Wert ersetzen
dictionary = {"Hallo": "Welt", 1: -3, -3: 7.0}
dictionary["Hallo"] = "Rene"
print(dictionary)

# Indizierung
# -

#Slicing
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(liste[2:10:2])

# Konkatenation
liste1 = [0, "Ni!", 2, "Ni!"]
liste2 = [3.0, [1, "Ni!"]]

ergebnis = liste1 + liste2
print(ergebnis)
del ergebnis[1]
ergebnis.remove("Ni!")
ergebnis[-1].remove("Ni!")

print(ergebnis)

# Mutabilität
daten = ["wichtige Daten", 69, 111, "Kokosnuss"]
backup = daten
print(backup)

daten[0] = "super unwichtig"
print(daten)
print(backup)
# Lösung
import copy
daten = ["wichtige Daten", 69, 111, "Kokosnuss"]
backup = copy.deepcopy(daten)
print(backup)

daten[0] = "super unwichtig"
print(daten)
print(backup)

# join
woerter = ["Alle", "die", "mit", "uns", "auf", "Kaperfahrt", "fahren"]
neuer_text = "   ".join(woerter)
print(neuer_text)

# Tuple unpacking
name, beruf, stadt = ("Arthur", "König", "Camelot")
print(name, beruf, stadt)

# Dictionary erzeugen
dictionary = {1: "Ritter", "zwei": "Brian", "actors":{"Graham": "Chapman", "John": "Cleese"}}
print(dictionary)

# Dictionary vereinigen
dictionary.update({3: "Jabberwocky", 4: "Flying Circus"})
print(dictionary)
# Werte Ausgeben
print(dictionary.values())

# Herausforderung
vornamen = ["Captain", "Jack", "Klaus"]
nachnamen = ["Hook", "Sparrow", "Stoertebeker"]
addressen = ["Neverland", "Union Jack", "Likedeeler"]

datenbank = dict()

datenbank[vornamen[0] + " " + nachnamen[0]] = {"vorname": vornamen[0], "nachname":
nachnamen[0], "addresse": addressen[0]}

datenbank[vornamen[1] + " " + nachnamen[1]] = {"vorname": vornamen[1], "nachname":
nachnamen[1], "addresse": addressen[1]}

datenbank[vornamen[2] + " " + nachnamen[2]] = {"vorname": vornamen[2], "nachname":
nachnamen[2], "addresse": addressen[2]}
print(datenbank)