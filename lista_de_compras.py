compra=[]

def carregarLIsta():
    with open('lista_compras.txt', 'r') as arquivo:
            for item in arquivo:
                if item == ' ':
                    pass
                else:
                    x = item[:-1]
                    compra.append(x)

def lista():
    print(compra)

def adcionar():
    novoItem = input('qual item?')
    compra.append(novoItem)

def remover():
    numero = int(input('qual item deseja remover? (selecione o numero)'))
    compra.pop(numero-1)

def salvarLista():
    with open('lista_compras.txt', 'w') as arquivo:
        for i in compra:
            arquivo.writelines(f'{i}\n')

def play():
     
    carregarLIsta()
    while True:
        print('adcionar item - 1')
        print('remover item - 2')
        print('visualizar lista - 3')
        print('sair - 4')
        acao = input('oq pretende fazer?')


        if acao == '1':
            adcionar()
        elif acao == '2':
            remover()
        elif acao == '3':
            lista()
        elif acao == '4':
            salvarLista()
            break
        else:
            print('perdao, poderia repetir?')


play()

