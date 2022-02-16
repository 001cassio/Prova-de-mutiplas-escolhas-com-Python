#! python3
#este codigo pega as capitais das cidades e cria uma avaliao com perguntas sobre os mesmos e tambem cria o seu gabarito

import random

capitais ={"Acre":"Rio Branco","Alagoas":"Maceió","Amapá":"Macapá","Amazonas":"Manaus","Bahia":"Salvador",
"Ceará":"Fortaleza","Espírito Santo":"Vitória","Minas Gerais":"Belo Horizonte","Rio de Janeiro":"Rio de Janeiro",
"Rio Grande do Norte":"Natal","Distrito Federal":"Brasília","Tocantins":"Palmas","São Paulo":"São Paulo"}

#AQUI GERAMOS OS ARQUIVOS DA PROVAS
for numero_da_prova in range(10):
    questoes = open("questoes_prova%s.txt" %(numero_da_prova + 1),"w")
    gabarito = open("gabarito%s.txt"%(numero_da_prova + 1),"w")

#aqui fazemos o cabecalho da prova

    questoes.write("Name:\n\nData:\n\nTurma:\n\n")
    questoes.write((" "*20)+"Prova sobre capitais (prova %s)" %(numero_da_prova + 1))
    questoes.write("\n\n")

    #embaralha a ordem dos estados
    estados = list(capitais.keys())
    random.shuffle(estados)

    for numero_da_questao in range(len(capitais)):

        #obtem as repostas corretas e incorretas
        resposta_correta = capitais[estados[numero_da_questao]]
        resposta_errada = list(capitais.values())
        del resposta_errada[resposta_errada.index(resposta_correta)]
        resposta_errada = random.sample(resposta_errada, 3)
        opcao_resposta = resposta_errada + [resposta_correta]
        random.shuffle(opcao_resposta)

        #este trecho de codigo acima pega a resposta correta
        #depois lista todos os valores das capitais 
        #acha o indice da resposta certa e o deleta
        #retorna tres valores errados e um correto
        #embaralha a posiçao dos itens corretos e errados
        questoes.write("%s. qual e a capital de %s?\n" %(numero_da_questao +1, estados[numero_da_questao]))
        for i in range(4):
            questoes.write(" %s.%s\n"%("ABCD"[i], opcao_resposta[i]))
            questoes.write("\n")

        #este pedaco acima cria o enunciado da questao e distribui as opcoes de resposta de A a D e grava no arquivo da prova 
        gabarito.write(" %s %s \n " %(numero_da_questao +1, "ABCD"[opcao_resposta.index(resposta_correta)]))
questoes.close()
gabarito.close() 

    

