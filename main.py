import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "turma_d"
)
meucursor = banco.cursor()
opcao = 0
while opcao != 3:
    opcao = int(input("\nDigite uma opção:\n1 - Consultar \n2 - Inserir \n3 - Sair \nOpção desejada:"))
    if opcao == 1:
        pesquisa = 'select * from alunos;'
        meucursor.execute(pesquisa)
        # fetchall recebe tudo da pesquisa e retorna através de uma tupla
        resultado = meucursor.fetchall()
        for x in resultado:
            print(x)
        opcao = 0

    elif opcao == 2:
        nome1 = input("Digite seu nome:")
        telefone1 = input("Digite seu número: ")

        sql = "INSERT INTO alunos (nome, telefone) VALUES (%s, %s)"
        data = (nome1, telefone1)
        meucursor.execute(sql, data)
        banco.commit()

    elif opcao == 3:
        print("Programa encerrado.")
        meucursor.close()
        banco.close()

    else:
        print("Opção inválida.")

