from FolhaDePagamento.funcionarios import Funcionarios, Gerente, Desenvolvedor, Analista
from FolhaDePagamento.sistemaFolha import SistemaDeFolha

funcionario1 = Gerente('Lívia', '04409306340', '26/05/1992')
funcionario2 = Analista('Mariana', '04409306341', '15/10/1985')
funcionario3 = Desenvolvedor('Saulo', '04409306342', '19/09/1984')

funcionario1.definir_hora_trabalhada(8.9)
funcionario2.definir_hora_trabalhada(6.43)
funcionario3.definir_hora_trabalhada(10)

'''print(funcionario1.calcular_salário_mes())
print(funcionario2.calcular_salário_mes())
print(funcionario3.calcular_salário_mes())'''

#--------- no sistema da folha de pagamento-----------
sistema = SistemaDeFolha()
sistema.adicionar_novo_funcionario(funcionario1)  #como add vários funcionários de uma vez? tipo vários livros em uma biblioteca tbm
sistema.adicionar_novo_funcionario(funcionario2)
sistema.adicionar_novo_funcionario(funcionario3)

sistema.mostrar_folha_do_mes()


