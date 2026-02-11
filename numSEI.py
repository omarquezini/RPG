import random
from colorama import init, Fore, Back, Style

init()

print(Fore.BLACK +"[]========================[]")
print(Fore.BLACK +"[]                        []")
print(Fore.BLACK +"[]     *O_MARQUEZINI*     []")
print(Fore.BLACK +"[]      a aula final.     []")
print(Fore.BLACK +"[]                        []")
print(Fore.BLACK +"[]========================[]")

print("")
print("Um monstro terrivel a anos")
print("atrai pessoas para uma")
print("caverna misteriosa.")
print("")
print("missão: matar a criatura!")
print("$$$   5.000.000.000   $$$")

escolha = int(input(Fore.RED +"você aseita a missão? / (1) SIM (2) NÃO :"))


if escolha == 1:
        print("")
        print("Blz, então.")
elif escolha == 2:
        print("")
        print(Fore.RED+"Blz.")
        exit()
      
HP_draco = 200
HP_seu = 100
mana = 5

while True:
        numeroA = random.randint(1, 2)
        numeroB = random.randint(1,3)
        critcal = random.randint(1,5)

        XcolhaDR = random.randint(1,3)

        

        print("")
        print(Fore.GREEN + "$ MANA:"+ Fore.BLUE + f"{mana}")
        Xcolha = int(input(Fore.GREEN + " (1)ATAQUE /// (2)CURA -5 MANA /// (3) ESPERAR +10 MANA: "))
        print("")


#1 ATAQUE
        if Xcolha == 1 and numeroA == 1:
                print(Fore.GREEN +"OK, (10) de dano foram causados.")
                HP_draco -=10
        elif critcal == 5 and Xcolha == 1 and numeroA == 1:
                print(Fore.RED +"CRITICO! (20) de dano foram causados.")
                HP_draco -=20
        elif Xcolha == 1 and numeroA == 2:
            print("")
            print(Fore.BLACK +"você não tem sorte")

#2 CURA
        if Xcolha == 2 and numeroA == 1 and mana > 0:
                print(Fore.GREEN +"OK, (10) de cura foram causados.")
                HP_seu +=10
                mana -= 5

        elif Xcolha == 2 and numeroA == 2:
            print("")
            print(Fore.BLACK +"você não tem sorte")

#3 ESPERAR
        if Xcolha == 3 and numeroA == 1 :
                print(Fore.BLUE +"OK...")
                mana += 10

        
#1 dragão ATAQUE
        if XcolhaDR == 1 and numeroB == 1:
                print("")
                print(Fore.RED + "AH. o dragão te atacou")
                print("ele te causou (20) de dano")
                HP_seu -=20
        elif XcolhaDR == 1 and numeroB == 2 or numeroB == 3:
            print("")
            print(Fore.BLACK +"ele não teve sorte")

#2 dragão "SCRATCH"
        if XcolhaDR == 2 and numeroB == 1:
                print("")
                print(Fore.RED +"AH. o dragão te arranhou")
                print("ele te causou (5) de dano")
                HP_seu -=5
        elif XcolhaDR == 2 and numeroB == 2 or numeroB == 3 :
            print("")
            print(Fore.BLACK +"ele não teve sorte")

#3 dragão CURA
        if XcolhaDR == 3 and numeroB == 1:
                print("")
                print(Fore.RED + "AH. o dragão se curou")
                HP_draco +=5
        elif XcolhaDR == 3 and numeroB == 2 or numeroB == 3 :
            print("")
            print(Fore.BLACK +"ele não teve sorte")


        print("")
        print(Fore.RED + f"DRAGÃO = {HP_draco}")
        if HP_seu >= 100:
                print(Fore.BLUE + f"Você = {HP_seu}")

        elif HP_seu < 70 < HP_seu:
              print(Fore.YELLOW + f"Você = {HP_seu}")

        elif HP_seu < 50:
              print(Fore.RED + f"Você = {HP_seu}")

#NUM SEI...

        if Xcolha > 3:
              print (Fore.LIGHTRED_EX + "Você morreu porque você é " + Fore.LIGHTMAGENTA_EX + "BURRO!")
              HP_seu == 100  
              HP_seu -= 1000

        elif Xcolha < 1:
              print (Fore.LIGHTRED_EX + "Você morreu porque você é " + Fore.LIGHTMAGENTA_EX + "INDIOTA!")
              HP_seu == 100
              HP_seu -= 1000




        if HP_seu <= 0 :
            print("\nVocê perdeu! Fim de jogo.")
            break
        elif HP_draco <= 0:
            print("\nVocê venceu! o dragão foi derrotado.")
            print("AGORA RECEBA!!!!")
            print("$$$  5.000.000.000  $$$")
            break
    