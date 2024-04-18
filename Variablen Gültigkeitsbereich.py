def f():
    def local():
        var = "local text"
    def dononlocal():
        nonlocal var
        var = "non local text"
    def doglobal():
        global var
        var = "global text"
# Variabel Local gilt nur im Block, Nonlocal in Unterfunktion

    var = "text"
    local()
    dononlocal()
    doglobal()
    print("after init: ", var)
    # Local am kleinsten, nonlocal etwas größer, global am größten

f()
print("global", var)

# localvar = local text
# nonlocalvar = nonlocal text
# globalvar = global text

# Main Funktion Ganzes Script, Local nur Funktion , Nonlocal Unterfunktionen, ganze Funktion
#