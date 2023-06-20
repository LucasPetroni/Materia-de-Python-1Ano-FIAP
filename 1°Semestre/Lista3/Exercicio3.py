time1 = input("Escreva o nome do time 1: ")
gols1 = int(input("Quantos gols o time " + time1 + " fez? "))

time2 = input("Escreva o nome do time 2: ")
gols2 = int(input("Quantos gols o time " + time2 + " fez? "))

if gols1 > gols2:
    print("O time", time1, "ganhou o jogo!")
elif gols2 > gols1:
    print("O time", time2, "ganhou o jogo!")
else:
    print("EMPATE")
