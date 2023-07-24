import os

tentativa1= []
acertos1= []
print("\033[33m                                  JOGO DA FORCA                                     ")
for x in range(0,6):
    print("\033[39mDICA:Vende na padaria")
    per=input("Adivinhe a palavra _ _ _ , escolha uma letra:  ")
    if per != "A" and per != "P" and per != "O":
        os.system("clear")
        tentativa1.append(per)
        print("Você errou uma letra")
        print(tentativa1)
        if len(tentativa1) == 3:
            os.system("clear")
            print("\033[31mGame over")
            break
    else:
        os.system("clear")
        acertos1.append(per)
        print("Você acertou uma letra")
        print(acertos1)
    if len(acertos1) == 3:
        os.system("clear")
        print("\033[35mWinner, a palavra é PÃO")
        break 
tentativa2= []
acertos2= []
for y in range(0,8):
    print("\033[39mDICA:É algo falso")
    per2=input("Adivinhe a palavra _ _ _ _ _ , escolha uma letra:  ")
    os.system("clear")
    if per2 != "M" and per2 != "I" and per2 != "O" and per2 != "T" and per2 != "S":
        os.system("clear")
        tentativa2.append(per2)
        print("Você errou uma letra")
        print(tentativa2)
        if len(tentativa2) == 3:
            os.system("clear")
            print("\033[31mGame over")
            break
    else:
        os.system("clear")
        acertos2.append(per2)
        print("Você acertou uma letra")
        print(acertos2)
    if len(acertos2) == 5:
        os.system("clear")
        print("\033[35mWinner, a palavra é MITOS")
        break 
tentativa3= []
acertos3= []
for p in range(0,7):
    print("\033[39mDICA:Um evento")
    per3=input("Adivinhe a palavra _ _ _ _  , escolha uma letra:  ")
    os.system("clear")
    if per3 != "S" and per3 != "H" and per3 != "O" and per3 != "W":
        os.system("clear")
        tentativa3.append(per3)
        print("Você errou uma letra")
        print(tentativa3)
        if len(tentativa3) == 3:
            os.system("clear")
            print("\033[31mGame over")
            break
    else:
        os.system("clear")
        acertos3.append(per3)
        print("Você acertou uma letra")
        print(acertos3)
    if len(acertos3) == 4:
        os.system("clear")
        print("\033[35mWinner, a palavra é SHOW")
        break 
tentativa4= []
acertos4= []
for u in range(0,8):
    print("\033[39mDICA:É um inseto")
    per4=input("Adivinhe a palavra _ _ _ _ _ , escolha uma letra:  ")
    os.system("clear")
    if per4 != "M" and per4 != "C" and per4 != "O" and per4 != "A" and per4 != "S":
        os.system("clear")
        tentativa4.append(per4)
        print("Você errou uma letra")
        print(tentativa4)
        if len(tentativa4) == 3:
            os.system("clear")
            print("\033[31mGame over")
            break
    else:
        os.system("clear")
        acertos4.append(per4)
        print("Você acertou uma letra")
        print(acertos4)
    if len(acertos4) == 5:
        os.system("clear")
        print("\033[35mWinner, a palavra é MOSCA")
        break 
tentativa5= []
acertos5= []
for r in range(0,9):
    print("\033[39mDICA:É uma linguagem de programação")
    per5=input("Adivinhe a palavra _ _ _ _ _ _, escolha uma letra:  ")
    os.system("clear")
    if per5 != "P" and per5 != "Y" and per5 != "O" and per5 != "T" and per5 != "H" and per5 != "N":
        os.system("clear")
        tentativa5.append(per5)
        print("Você errou uma letra")
        print(tentativa5)
        if len(tentativa5) == 3:
            os.system("clear")
            print("\033[31mGame over")
            break
    else:
        os.system("clear")
        acertos5.append(per5)
        print("Você acertou uma letra")
        print(acertos5)
    if len(acertos5) == 6:
        os.system("clear")
        print("\033[35mWinner, a palavra é PYTHON")
        break 