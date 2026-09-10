# 1.opdracht voor smartapp het input gedeelte
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
gevoel = celsius - (Luchtvochtigheid / 100 * Windsnelheid)
gem = (print(F"De gemiddelde Temperatuur is: {celsius} C = {fahrenheit} F"))
print(gevoel)
print("het temperatuur vandaag is", celsius)
print("het windsnelheid vandaag is", Windsnelheid)
print("het luchtvochtigheid vandaag is", Luchtvochtigheid)


