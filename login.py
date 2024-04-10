def verificar_acesso(login, senha):
    try:
        arquivo = open(f"{login}.txt", "r")
        linhas = arquivo.readlines()
        arquivo.close()
        
        if linhas and linhas[2].strip() == f"Senha: {senha}":
            nome = linhas[0].strip().split(":")[1].strip()
            print(f"Acesso permitido. Bem-vindo, {nome}!")
        elif not linhas:
            print("Usuário inexistente.")
        else:
            print("Senha incorreta.")
    except FileNotFoundError:
        print("Usuário inexistente.")
    except Exception as e:
        print(f"Ocorreu um erro ao verificar o acesso: {str(e)}")


while True:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")


    verificar_acesso(login, senha)


    continuar = input("Deseja tentar novamente? (s/n): ")
    if continuar.lower() != 's':
        break