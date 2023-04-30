import PySimpleGUI as sg

personagens = ["Buzz Lightear", "Dexter", 
               "Dick Vigarista", "Doutora Brinquedos", 
               "Edna Moda", "Eustácio", 
               "Fred Flinstone", "Girafales", 
               "Guido", "Johnny Bravo", 
               "Linguini", "Lula Molusco",
               "Mario", "Popeye",
               "Policial", "Prefeito", 
               "Sherlock Holmes", "Vicky",
               "Woody", "Homer Simpson"]


# Seu personagem está usando óculos?
# Seu personagem está usando chapéu?
# Seu personagem tem bigode?
# Seu personagem é masculino?
# Seu personagem é careca?
# Seu personagem é loiro?
# Seu personagem tem cabelo marrom?
# Seu personagem tem cabelo preto?

# Oq falta:
 # - Adicionar segunda lista com as perguntas;
 # - Fazer validação por pergunta e resposta até achar o personagem solicitado;
 # - Adicionar parte do Jogador adivinhar o personagem escolhido pelo robô (import random);
 # - Adicionar a interface ao jogo.



print("=======================")
print(personagens)
print("=======================")

while len(personagens) != 1:
                
        pergunta = str(input("Seu personagem está usando óculos?"))        
        if pergunta.lower() == "s":
                pass
        elif pergunta.lower() == "n":
                itens_a_remover = ["Buzz Lightear", "Dick Vigarista", "Edna Moda", "Fred Flinstone", "Girafales", "Guido", "Linguini", "Lula Molusco", "Mario", "Popeye", "Policial", "Sherlock Holmes", "Woody", "Homer Simpson"]
                for item in itens_a_remover:
                        if item in personagens:
                                personagens.remove(item)
                        else:
                                pass             
                pass
        else:
                print("tente novamente")

        print(personagens)
        pergunta = str(input("Seu personagem está usando chapéu?"))        
        if pergunta.lower() == "s":
                pass
        elif pergunta.lower() == "n":
                itens_a_remover = ["Buzz Lightear", "Dick Vigarista", "Doutora Brinquedos", "Dexter", "Fred Flinstone", "Girafales", "Guido", "Johnny Bravo", "Lula Molusco", "Vicky", "Homer Simpson"]
                for item in itens_a_remover:
                        if item in personagens:
                                personagens.remove(item)
                        else:
                                pass
        else:
                print("tente novamente")
                
        print(personagens)
        pergunta = str(input("Seu personagem tem bigode?"))        
        if pergunta.lower() == "s":
                pass
        elif pergunta.lower() == "n":
                itens_a_remover = ["Eustácio"]
                for item in itens_a_remover:
                        if item in personagens:
                                personagens.remove(item)
                        else:
                                pass
                print(personagens)
        else:
                print("tente novamente")                

print(f"O personagem que você escolheu é {personagens}!")
