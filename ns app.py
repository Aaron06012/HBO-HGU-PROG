def standaardprijs(afstandkm):
    if afstandkm < 0:
        afstandkm = 0
    if afstandkm > 50:

        return (15 + 0.60 * afstandkm)
    else:
        return (0.80 * afstandkm)



def ritprijs(leeftijd, weekendrit, afstandkm):
    prijs = standaardprijs(afstandkm)
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit:
            prijs = prijs * 0.65
        else :
            prijs = prijs * 0.70
    else:
        if weekendrit:
            prijs = prijs * 0.60

    return prijs

leeftijd = int(input("geef je leeftijd:"))
weekendrit = str(input("Is het weekend? (ja/nee)"))
afstandkm = int(input("Hoeveel kilometer is je rit?:"))

if weekendrit == "ja":
    weekendrit = True

else:
    weekendrit = False

prijs = ritprijs(leeftijd, weekendrit, afstandkm)

print("De ritprijs is €", prijs)

# alleen nog weekend stukje duidelijk maken en zorgen voor dingen als negatieve leeftijd. km is al voor gezorgd en misschien
# ook ja of nee bij weekend dat je niet wat anders doet