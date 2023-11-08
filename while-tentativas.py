
print('advinhe em 3 tentativas qual o número secreto da fechadura')

tentativas = 0

while(tentativas < 3):

    numInfo = input('Digite o número: ')
    numInfoConvert = int(numInfo)
    numeroSecreto = 33

    if(numInfoConvert == numeroSecreto ):
        print('Você acertou o número, a fechadura abriu!')
        print('Tentativas utilizadas foram:{} '.format(tentativas,tentativas))
        break
    else:
        print('Você errou !! Tente novamente!')
        tentativas = tentativas + 1
        print('Tentativas utilizadas foram: ',tentativas)
        
print('Fim de Gamer !!!')

print('Fim de Gamer !!!')

print('Fim de Gamer !!!')




        
   

    