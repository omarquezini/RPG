import random



print("[]========================[]")
print("[]                        []")
print("[]     *O_MARQUEZINI*     []")
print("[]      a aula final.     []")
print("[]                        []")
print("[]========================[]")

print("")
print("Um monstro terrivel a anos")
print("atrai pesouas para uma")
print("caverna misteriosa.")
print("")
print("missão: matar a criatura!")
print("$$$   5.000.000.000   $$$")

escolha = int(input("você aseita a missão? / (1) SIM (2) NÃO :"))

if escolha == 1:
    print(" blz intão.")
else:
    print("isso acaba aqui intão.")

HPdraco = 200
seuHP = 100

while True:
    numeroA = random.randint(1, 2)
    print("")
    Xcolha = int(input("(1)ATK (2)CURA (3)DEFESA: "))
    print("")

    if Xcolha == 1 and numeroA == 1:
        print("OK, (10) de dano foram causados.")
        HPdraco -10
    elif Xcolha == 1 and numeroA == 2:
        print("OK, você não teve sorte")
    print(HPdraco)
