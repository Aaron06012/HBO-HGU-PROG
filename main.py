temp = float(input( "Wat is op dag 1 de temperatuur[C]: " ))
wind = float(input("Wat is op dag 1 de windsnelheid[m/s]: "))
vocht = float(input("Wat is op dag 1 de vochtigheid[%]: "))

fahrenheit = 32 + 1.8 * temp

print("de gemiddlede temperatuur is:", temp, "C =", fahrenheit, "F")
gevoel = temp - (vocht / 100 * wind)
print("De gevoelstemperatuur is:", (gevoel), "C")
                                             