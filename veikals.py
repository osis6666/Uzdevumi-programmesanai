cenradis = {"Zobens": 45, "Vairogs": 30, "Cirvis": 55,"Lāpsta": 15,"Izskapts": 10, "Bruņas": 100}
def pirkt_lietu(Nosaukums):
    if Nosaukums in cenradis:
        cena = cenradis[Nosaukums]
        print(f"Iztērēti {cena}")
    else:
        print("Lieta nav pieejama")

lieta = input("Ievadi lietas nosaukumu: ")
cena = pirkt_lietu(lieta)
if cena != 0:
    print("Pirkums veikts")
else:    print("Pirkums nav veikts")