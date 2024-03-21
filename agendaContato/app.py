from main import*

agenda = Agenda()
contato1 = ContatoProfissional('Livia','85999773136','empresa A','Analista')
contato2 = ContatoPessoal('Saulo','85999773026','26/05/1992')
contato3 = ContatoProfissional('Mel','85999773027','empresa B','Gerente')

agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
agenda.adicionar_contato(contato3)

agenda.exibir_info()