# Klassen oben definieren

class MyClass:
    zahl = 42
    string = "zeichenkette"
# Variabeln unter Klassen definierbar
    def do_something(self, neuezahl):
        self.zahl = neuezahl
# Self bedeutet es nimmt keine Variabel ausserhalb der Klasse auf

instanz = MyClass()
instanz.do_something(1337)
# instanz.do_something greift auf self zu
# self.zahl ermöglicht änderung der Variabel, änder lokalität
print(instanz.string)
print(instanz.zahl)


# . Ist zugriffsoperator