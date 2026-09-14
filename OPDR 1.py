def standaardprijs(afstandKM):

    if afstandKM < 0 :
        afstandKM = 0
    if afstandKM < 50:
        return (afstandKM * 0.80)
    else :
        return (afstandKM * 0.60 + 15)

def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd < 12 or leeftijd > 65 :
        Prijs * 0.70
        if weekendrit is True :
            Prijs * 0.65
    else :
        if weekendrit is True :
            Prijs * 60
    print("Uw prijs is $",Prijs)


while True:
    weekend_input = input("Is it the weekend? (yes/no): ").lower()

    if weekend_input == "yes":
        is_weekend = True
        break
    elif weekend_input == "no":
        is_weekend = False
        break
    else:
        print("Please enter yes or no.")


age= int(input("wat is je leeftijd?"))
num1 = float(input("voer hiet KM in"))
Prijs = standaardprijs(num1)

ritprijs(age,is_weekend,Prijs)



