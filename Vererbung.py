class Lebewesen:
    augen = 3
    def __init__(self):
        self.klasse = "säuger"

    def lebe(self):
        self.augen = 4

class Hund(Lebewesen):
    beine = 42
    name = "bulldogge"
    augen = 2

    def __init__(self, buchstabeneu='a'):
        Lebewesen.__init__(self)
        self.buchstabe = buchstabeneu
        self.list = []

    def do_something(self, neuezahl):
        self.augen = neuezahl
        self.lebe()

    def lebe(self):
        print(Lebewesen.augen)
        self.beine = 43

fiffi = Hund()
fiffi.do_something(42)
fiffi.lebe()
print(fiffi.augen)