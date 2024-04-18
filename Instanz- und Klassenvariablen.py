class MyClass:
    zahl = 42
    string = "zeichenkette"
    list = []
    # Liste Mutable

    def __init__(self, buchstabeneu='a'):
        self.buchstabe = buchstabeneu

    def do_something(self, neuezahl):
        self.zahl = neuezahl
        self.list.append(neuezahl)


instanz = MyClass('z')
instanz2 = MyClass('a')
# Self wird nur genommen wenn "z" nicht angegeben ist
instanz.do_something(1337)

print(instanz2.list)

