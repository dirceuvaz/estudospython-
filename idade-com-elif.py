
idade = input('informe a sua idade: ')

print('Idade informada é:', idade)

idadeInt = int(idade)

if(idadeInt >= 10):
    print('É necessário autorização dos pais para acessar as redes sociais')
elif(idadeInt >= 14 ):
    print('Você tem acesso as redes sociais com supervisão dos pais')
else:
    print('Tem acesso completo')

    