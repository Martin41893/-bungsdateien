class MyClass:
    zahl = 42
    string = "zeichenkette"

    def __init__(self, buchstabeneu='a'):
        self.buchstabe = buchstabeneu

    def do_something(self, neuezahl):
        self.zahl = neuezahl


instanz = MyClass("z")
# Self wird nur genommen wenn "z" nicht angegeben ist
instanz.do_something(1337)

print(instanz.buchstabe)



