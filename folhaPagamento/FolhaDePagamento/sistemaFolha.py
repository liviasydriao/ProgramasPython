from FolhaDePagamento.funcionarios import*

class SistemaDeFolha:
    def __init__(self):
        self.total_folha_pagmnt = 0
        self.lista_de_funcionários = []

    def adicionar_novo_funcionario(self, Funcionarios):
        self.lista_de_funcionários.append(Funcionarios)

    def mostrar_folha_do_mes(self):
        for funcionario in self.lista_de_funcionários:
            print(funcionario)
            self.total_folha_pagmnt += funcionario.calcular_salário_mes()
        print(f"Total a ser pago no mês: R$ {round(self.total_folha_pagmnt,2)}")
