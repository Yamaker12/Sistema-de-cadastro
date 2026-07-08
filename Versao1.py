Lista_de_nome = []
Lista_de_idade = []
Lista_de_Email = []
Lista_de_numero_de_telefone = []



def lista_de_adicionar(): # Vai adicionar os dados na lista
    
    # Nome
    Adicionar_nome = input("Digite seu nome: ")
    if Adicionar_nome.isalpha():
      Lista_de_nome.append(Adicionar_nome)
    
    # Idade
    Adicionar_idade = int(input("Digite sua Idade: "))
    Lista_de_idade.append(Adicionar_idade)
    
    # Email
    Adicionar_Email = input("Adicione seu Email: ")
    if "@"  in Adicionar_Email and "." in Adicionar_Email:
     Lista_de_Email.append(Adicionar_Email)
    
    # Telefone
    Adicionar_telefone = int(input("Adicione seu telefone: "))
    Lista_de_numero_de_telefone.append(Adicionar_telefone)

    return 


def lista_de_dados (): # Vai mostrar a lista de um certo nome da pessoa que for citado
    print("Lista de nomes: ", Lista_de_nome)
    Pergunta_nome = input("Qual é o nome do usuario:")
    

    #checar se o nome tem só letras
    if Pergunta_nome.isalpha():
      
      #checar se o nome esta na lista de nomes
      if Pergunta_nome in Lista_de_nome:
        index_nome = Lista_de_nome.index(Pergunta_nome)
        nome = Pergunta_nome
        idade = Lista_de_idade[index_nome]
        email = Lista_de_Email[index_nome]
        telefone = Lista_de_numero_de_telefone[index_nome]
        print(f'\n\nNome: {nome} \nIdade: {idade} \nEmail: {email} \nTelefone: {telefone}\n\n')
    
    return


while True:
 
 Pergunta = int(input("""Você Deseja: 
 (1)Adicionar Dados
 (2)Olhar os Dados
 (3)Acabou
 Resposta: """ ))
 
 
    
 if Pergunta == 1:
   lista_de_adicionar()

 if Pergunta == 2:
   lista_de_dados()

 if Pergunta == 3:
   print("Acabado")
   break