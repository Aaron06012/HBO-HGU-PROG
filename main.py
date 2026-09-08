temp = float(input( "Wat is op dag 1 de temperatuur[C]: " ))
wind = float(input("Wat is op dag 1 de windsnelheid[m/s]: "))
vocht = float(input("Wat is op dag 1 de vochtigheid[%]: "))

fahrenheit = 32 + 1.8 * temp

gem = (print(F"De gemiddelde Temperatuur is: {temp} C = {fahrenheit} F"))
gevoel = temp - (vocht / 100 * wind)
print(gevoel)