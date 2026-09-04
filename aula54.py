"""

Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista

Não permita que o programa quebre com erros de índices inexistentes na lista

"""

lista = ['Batata', 'Manteiga', 'Arroz']
while True:
    
    opcao = input("Selecione uma opção\n [i]nserir [a]pagar [l]istar\n")
    
    if opcao == "i":
        valor = input("Insira o valor: ")
        
        if len(valor) < 1:
            print("Digite um valor.")
            continue
        else:
            lista.append(valor)
    elif opcao == "a":
        try:
            indice = input("Digite o índice do valor para realizar a exclusão: ")
            indice = int(indice)
            if indice < 0 or indice >= len(lista):
                print("Não foi possível apagar este índice")
                continue

            lista.pop(indice)
            print("Valor apagado")
                            
        except (ValueError, IndexError, TypeError):
            print("Não foi possível apagar este índice")
            continue
            
    elif opcao == "l":
        
        if len(lista) < 1:
            print('Nada para listar')
        else:
            for i, item in enumerate(lista):
                print(i, item)
    
    else:
        print("Digite uma opção correta")
        continue