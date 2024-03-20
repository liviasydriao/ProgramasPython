from abc import ABC, abstractclassmethod

class HoraTrabalhadaError(Exception):
    def __init__(self, _valor_da_hora_trabalhada):
        self._valor_da_hora_trabalhada = _valor_da_hora_trabalhada
        super().__init__(
             f'valor da hora trabalhada inaceitável segundo a CLT ({self._valor_da_hora_trabalhada}< R$ 6.42)'
        )
        
        

class Funcionarios(ABC):
    def __init__(self, nome, cpf, data_de_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        self._valor_da_hora_trabalhada = 0   #como coloca o erro no construtor?

    @abstractclassmethod
    def calcular_salário_mes(self):
        pass

    def deﬁnir_hora_trabalhada(self, _valor_da_hora_trabalhada):
    #Se o valor dado de entrada da hora trabalhada for menor que R$ 6,42, o sistema deve lançar uma exceção (HoraTrabalhadaError), tanto no construtor como em deﬁnir_hora_trabalhada.
        
            self._valor_da_hora_trabalhada = _valor_da_hora_trabalhada
            if self._valor_da_hora_trabalhada < 6.42:
                raise HoraTrabalhadaError(_valor_da_hora_trabalhada)

    def __str__(self):
         return f"Nome: {self.nome} | CPF: {self.cpf} | Nascimento: {self.data_de_nascimento} "

class Gerente(Funcionarios):
        def __init__(self, nome, cpf, data_de_nascimento):
             super().__init__(nome, cpf, data_de_nascimento)

        def calcular_salário_mes(self):
             salario = self._valor_da_hora_trabalhada* 8 * 20 * 1.5
             return salario
        
        def __str__(self):
         return f"Nome: {self.nome} | CPF: {self.cpf} | Nascimento: {self.data_de_nascimento} | Função: Gerente | Salário Mês: R$ {self.calcular_salário_mes()}"
        
class Desenvolvedor(Funcionarios):
        def __init__(self, nome, cpf, data_de_nascimento):
             super().__init__(nome, cpf, data_de_nascimento)

        def calcular_salário_mes(self):
             salario = self._valor_da_hora_trabalhada* 8 * 20 * 1.2
             return salario
        
        def __str__(self):
            return f"Nome: {self.nome} | CPF: {self.cpf} | Nascimento: {self.data_de_nascimento} | Função: Desenvolvedor | Salário Mês: R$ {self.calcular_salário_mes()}"
        
class Analista(Funcionarios):
        def __init__(self, nome, cpf, data_de_nascimento):
             super().__init__(nome, cpf, data_de_nascimento)

        def calcular_salário_mes(self):
             salario = self._valor_da_hora_trabalhada* 8 * 20 * 1.3
             return salario
        def __str__(self):
            return f"Nome: {self.nome} | CPF: {self.cpf} | Nascimento: {self.data_de_nascimento} | Função: Analista | Salário Mês: R$ {self.calcular_salário_mes()}"