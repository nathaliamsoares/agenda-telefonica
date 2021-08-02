lista_contatos = []


def adicionar(nome, telefone, email):
    contato = {nome, telefone, email}
    lista_contatos.append(contato)


def deletar(posicao):
    if posicao <= len(lista_contatos):
        del(lista_contatos[posicao])
    else:
        print('Não existe essa posição')


opcao = 100
while opcao != 0:

    print('##### AGENDA TELEFÔNICA #####')
    print('1- Listar\n2- Adicionar\n3- Deletar\n0- Fechar agenda')
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        print('--- LISTAR ---')
        print(lista_contatos)

    if opcao == 2:
        print('--- ADICIONAR ---')
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        email = input('Email: ')
        adicionar(nome, telefone, email)
        print('Lista Atualizada: ', lista_contatos)

    if opcao == 3:
        print('--- DELETAR ---')
        posicao_deletar = int(input('Digite a posição a ser deletada: '))
        deletar(posicao_deletar)
        print('Lista Atualizada: ', lista_contatos)
