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
    print("infelizmente você não tem escolha.")

HP_draco = 200
HP_seu = 100

while True:
        numeroA = random.randint(1, 2)
        numeroB = random.randint(1,3)

        XcolhaDR = random.randint(1,3)

        print("")
        Xcolha = int(input("(1)ATAQUE (2)CURA (3)DEFESA: "))
        print("")

#1 ATAQUE
        if Xcolha == 1 and numeroA == 1:
                print("OK, (10) de dano foram causados.")
                HP_draco -=10
        elif Xcolha == 1 and numeroA == 2:
            print("")
            print("você não tem sorte")
#2 CURA
        if Xcolha == 2 and numeroA == 1:
                print("OK, (10) de cura foram caudos.")
                HP_seu +=10
        elif Xcolha == 2 and numeroA == 2:
            print("")
            print("você não tem sorte")
#3 DEFESA
        if Xcolha == 3 and numeroA == 1:
                print("OK, ... você se defendeu.")
                HP_seu == HP_seu
        elif Xcolha == 3 and numeroA == 2:
            print("")
            print("você não tem sorte")
#1 dragão ATAQUE
        if XcolhaDR == 1 and numeroB == 1:
                print("")
                print("AH. o dragão te atacou")
                print("ele te causou (20) de dano")
                HP_seu -=20
        elif XcolhaDR == 1 and numeroB == 2 or numeroB == 3 or Xcolha == 3 :
            print("")
            print("ele não teve sorte")
#2 dragão SCRATCH
        if XcolhaDR == 2 and numeroB == 1:
                print("")
                print("AH. o dragão te arranhou")
                print("ele te causou (5) de dano")
                HP_seu -=5
        elif XcolhaDR == 2 and numeroB == 2 or numeroB == 3 or Xcolha == 3 :
            print("")
            print("ele não teve sorte")
#3 dragão CURA
        if XcolhaDR == 3 and numeroB == 1:
                print("")
                print("AH. o dragão se curou")
                HP_draco +=5
        elif XcolhaDR == 3 and numeroB == 2 or numeroB == 3 or Xcolha == 3 :
            print("")
            print("ele não teve sorte")

        print("")
        print(f"DRAGÃO = {HP_draco}")
        print(f"DRAGÃO = {HP_seu}")
        if HP_seu <= 0:
            print("\nVocê perdeu! Fim de jogo.")
            break
        elif HP_draco <= 0:
            print("\nVocê venceu! o dragão foi derrotado.")
            print("AGORA RECEBA!!!!")
            print("$$$  5.000.000.000  $$$")
            break
    