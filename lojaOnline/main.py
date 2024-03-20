# tem as classes do projeto
#adicionar os métodos __string___
#perguntar à Ana pq ela n add método mostrar carrinho no Cliente

from abc import ABC, abstractclassmethod

class Cliente(ABC):
    def __init__(self, cpf, nome, sobrenome, nascimento):   
        self.nome = nome
        self.cpf = cpf
        self.sobrenome = sobrenome
        self.nascimento = nascimento
        self.carrinho_compras = []             #lista que armazena os produtos no carrinho

    @abstractclassmethod
    def calcular_valor_ﬁnal_venda(self):
        pass

    def adicionar_produto_carrinho(self, produto):
        self.carrinho_compras.append(produto)
    
    def mostrar_carrinho(self):
        for produto in self.carrinho_compras:
            print(produto)

#----------------------------------------------------------------------------------------------------------------
        
class ClientePadrao (Cliente):
    def __init__(self, cpf, nome, sobrenome, nascimento, data_cadastro_loja):
        super().__init__(cpf, nome, sobrenome, nascimento)
        self.data_cadastro_loja = data_cadastro_loja

    def calcular_valor_ﬁnal_venda(self):    #método da classe abstrata, tem que ser implementado nas filhas /// retorna a soma de todos os produtos
        total = 0
        for cada_produto in self.carrinho_compras:     #a lista carrinho_compras guarda os produtos na classe pai Cliente, e dentro do Produto tem o atributo preço
            total += float(cada_produto.preco)
        return total

#----------------------------------------------------------------------------------------------------------------
  
class ClienteEspecial (Cliente):
    def __init__(self, cpf, nome, sobrenome, nascimento, nivel_ﬁdelidade):  #nivel_ﬁdelidade de 1 a 3
        super().__init__(cpf, nome, sobrenome, nascimento)

        if nivel_fidelidade in [1,2,3]:
            self.nivel_ﬁdelidade = nivel_ﬁdelidade
        else:  
            print("nível de fidelidade inexistente!")
            raise Exception

    def calcular_valor_ﬁnal_venda(self):
        total = 0
        #etorna a soma de todos os produtos com desconto de 10% e 30%, de acordo com o nivel_ﬁdelidade
        for cada_produto in self.carrinho_compras:
            total += cada_produto.preco

        if self.nivel_fidelidade == 1:   
            return (total) * 0.9
        
        elif self.nivel_fidelidade == 2:
            return  total * 0.8
        
        if self.nivel_fidelidade == 3:
            return  total * 0.7

#----------------------------------------------------------------------------------------------------------------
  
class Produto:
    total_produtos = 0

    def __init__(self, nome_produto, preco):
        self.id = Produto.total_produtos
        self.nome_produto = nome_produto
        self.preco = preco
        Produto.total_produtos += 1                   
  
    @staticmethod
    def obter_total_produtos_cadastrados():
        print(f"O total de produtos cadastrados é {Produto.total_produtos}")
    
    def __str__(self):
        return f"ID = {self.id} | Nome = {self.nome_produto} | Preço = {self.preco}"
        
#----------------------------------------------------------------------------------------------------------------
  
class Loja:
    def __init__(self):
        self.lista_clientes = []
        self.lista_produtos = []
    
    def adicionar_cliente_padrao(self, ClientePadrao):  #não posso receber só a classe ao invés de toooodos os argumentos da classe?
        self.lista_clientes.append(ClientePadrao)

    def adicionar_cliente_especial(self, ClienteEspecial):    #não posso receber só a classe ao invés de toooodos os argumentos da classe?
        self.lista_clientes.append(ClienteEspecial)

    def adicionar_produto(self, Produto):              #não posso receber só a classe ao invés de toooodos os argumentos da classe?
        self.lista_produtos.append(Produto)

    def adicionar_produto_carrinho_cliente(self, cpf, id):
        for cliente in self.lista_clientes:
            if cpf == cliente.cpf:
                for produto in self.lista_produtos:
                    if id == produto.id:
                        cliente.carrinho_compras.append(produto)

    def calcular_total_carrinho_cliente(self, cpf):
        for cliente in self.lista_clientes:
            if cpf == cliente.cpf:
                print(f"o total do carrinho do cliente {cliente.nome} é {cliente.calcular_valor_ﬁnal_venda()}")
    
    def exibir_produtos(self):
        for produto in self. lista_produtos:
            print(produto)