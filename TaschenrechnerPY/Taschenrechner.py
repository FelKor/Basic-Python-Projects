def abfrage():
    x = int(input("Geben sie ihre erste Zahl ein: "))
    y = int(input("Geben sie ihre zweite Zahl ein: "))
    
    check = input("Geben sie ein wie sie die beiden Zahlen zusammen rechnen möchten. [plus][minus][mal][geteilt]")

    while check not in["plus", "minus", "mal", "geteilt"]:
        check = input("Geben sie ein wie sie die beiden Zahlen zusammen rechnen möchten. [plus][minus][mal][geteilt]")
    
    return x, y, check

    global sum

def rechne_plus(x,y):
    sum = x+y

def rechne_minus(x,y):
    sum = x-y

def rechne_mal(x,y):
    sum = x*y

def rechne_geteilt(x,y):
    if(x>y):
        sum = x/y
    else:
        print("Diese Rechenaufgabe ist nicht möglich")
        check = ""
        abfrage()

def Taschenrechner():
    if(abfrage() == "plus"):
        rechne_plus(abfrage(),abfrage())


Taschenrechner()