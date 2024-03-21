class Contato:
  def __init__(self, nome, telefone):
    self.nome = nome
    self.telefone = telefone
  def exibir_info(self):
    print(f"o nome do contato é {self.nome} e seu telefone é {self.telefone}. ")
  '''def __str__(self):
    return f"\n-------------\n o nome do contato é {self.nome} e seu telefone é {self.telefone}\n---------------"'''

class ContatoProﬁssional(Contato):
  def __init__(self, nome, telefone, empresa, cargo):
    super().__init__(nome, telefone)
    self.empresa = empresa
    self.cargo = cargo
  def exibir_info(self):
    super().exibir_info()
    print(f"Seu cargo é {self.cargo} e Sua empresa é {self.empresa}")

class ContatoPessoal(Contato):
  def __init__(self, nome, telefone, aniversario):
    super().__init__(nome, telefone)
    self.aniversario = aniversario

  def exibir_info(self):
    super().exibir_info()
    print(f"Seu aniversário é {self.aniversario}.")

class Agenda:
  def __init__(self):
    self.contatos = []
  def adicionar_contato(self, contato):
    self.contatos.append(contato)
  def exibir_info(self):
    print("******************** AGENDA ***********************")
    for contato in self.contatos:
        contato.exibir_info()
        print("***************************************************")