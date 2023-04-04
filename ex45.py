import random
from time import sleep
lista = [0,1,2]
randomizar = random.choice(lista)
print('\033[1;34mPEDRA, PAPEL,TESOURA!!!\033[m')
print("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
opt = int(input('\033[0;32mQual é a sua opção?:\033[m '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=-' * 15)
if randomizar == 0:
    print('\033[1;31mO COMPUTADOR\033[m escolheu: PEDRA')
elif randomizar == 1:
    print('\033[1;31mO COMPUTADOR\033[m escolheu: PAPEL')
elif randomizar == 2:
    print('\033[1;31mO COMPUTADOR\033[m escolheu: TESOURA')
if opt == 0:
    print('\033[0;32mO JOGADOR \033[m escolheu: PEDRA')
elif opt ==1:
    print('\033[0;32mO JOGADOR \033[mescolheu: PAPEL')
elif opt ==2:
    print('\033[0;32mO JOGADOR \033[m escolheu: TESOURA')
else:
    print('OPÇÃO INVÁLIDA')
print('-=-' * 15)
if randomizar == opt:
    print('\033[1;36mEMPATE!\033[m')
elif randomizar == 0 and opt ==1 or randomizar == 1 and opt == 2 or randomizar == 2 and opt == 0:
    print('\033[0;32mJOGADOR VENCE\033[m')
else:
    print('\033[1;31mCOMPUTADOR VENCE\033[m')












