# 1.opdracht voor smartapp het input gedeelte
while True:
    celsius = input ("Temperatuur Celsius ")
    Windsnelheid = input("Windsnelheid meter per seconde ")
    Luchtvochtigheid = input("Luchtvochtigheid als geheel percentage ")
    if int(Luchtvochtigheid) <0 or int(Luchtvochtigheid) > 100 :
         print("luchtvochtigheid moet een nummer hebben tussen 0-100"),
         continue

    try:
        int(celsius)
        int(Windsnelheid)
        int(Luchtvochtigheid)
        break
    except:
        print("dit is geen nummer")

print("het temperatuur vandaag is", celsius)
print("het windsnelheid vandaag is", Windsnelheid)
print("het luchtvochtigheid vandaag is", Luchtvochtigheid)


