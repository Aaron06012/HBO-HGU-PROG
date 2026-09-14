# 1.opdracht voor smartapp het input gedeelte

def weerstation()
    while True:
        celsius = float(input ("Temperatuur Celsius "))
        Windsnelheid = float(input("Windsnelheid meter per seconde "))
        Luchtvochtigheid = float(input("Luchtvochtigheid als geheel percentage "))
        if int(Luchtvochtigheid) <0 or int(Luchtvochtigheid) > 100 :
             print("luchtvochtigheid moet een nummer hebben tussen 0-100"),
             continue
        if int(celsius) <= 0 or int(Windsnelheid) <= 0 : exit
        try:
            int(celsius)
            int(Windsnelheid)
            int(Luchtvochtigheid)
            break
        except:
            print("dit is geen nummer")
def(temp_celsius)
    fahrenheit = 32 + 1.8 * celsius
    gevoel = celsius - (Luchtvochtigheid / 100) * Windsnelheid

    gemidelde = str(celsius) +"C" + " " + str(fahrenheit) +"F"




dagen = 0
while dagen != 7 :
    while True:
        celsius = float(input ("Temperatuur Celsius "))
        Windsnelheid = float(input("Windsnelheid meter per seconde "))
        Luchtvochtigheid = float(input("Luchtvochtigheid als geheel percentage "))
        if int(Luchtvochtigheid) <0 or int(Luchtvochtigheid) > 100 :
             print("luchtvochtigheid moet een nummer hebben tussen 0-100"),
             continue
        if int(celsius) <= 0 or int(Windsnelheid) <= 0 : exit
        try:
            int(celsius)
            int(Windsnelheid)
            int(Luchtvochtigheid)
            break
        except:
            print("dit is geen nummer")

    fahrenheit = 32 + 1.8 * celsius
    gevoel = celsius - (Luchtvochtigheid / 100) * Windsnelheid

    gemidelde = str(celsius) +"C" + " " + str(fahrenheit) +"F"
    print("het gemmidelde is", gemidelde)
    print("het voelt", gevoel)
    print("het temperatuur vandaag is", celsius)
    print("het windsnelheid vandaag is", Windsnelheid)
    print("het luchtvochtigheid vandaag is", Luchtvochtigheid)

    dagen += 1
    print(dagen)
    #if dagen == 3 :
        #break
    #meerdere IF statements gebruiken voor de beslisingsrapport
    #Als de gevoelstemperatuur tussen 0 en 10 ligt (0 inclusief, 10 exclusief) en de windsnelheid groter is dan 12 → “Het is best koud en het waait; verwarming aan en roosters dicht!”
    #Als de gevoelstemperatuur tussen 0 en 10 ligt (0 inclusief, 10 exclusief) en de windsnelheid 12 of lager → “Het is een beetje koud, elektrische kachel op de benedenverdieping aan!”
    #Als de gevoelstemperatuur tussen 10 en 22 ligt (10 inclusief, 22 exclusief) → “Heerlijk weer, niet te koud of te warm.”
    #In alle overige gevallen → “Warm! Airco aan!”
        #if gevoel < 0 and Windsnelheid > 10 :
            #print("Het is heel koud en het stormt")
        #if gevoel < 0 and Windsnelheid < 10 :
            #print("het is erg koud")

