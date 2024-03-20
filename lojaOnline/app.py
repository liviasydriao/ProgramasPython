# tem o código que de fato executa o programa
from main import*

#criando clientes e produtos:
cliente1 = ClientePadrao('04409306340', 'Lívia', 'Braga', '26/05/1992', '01/01/2024')
cliente2 = ClienteEspecial('1657409735', 'Regina', 'Alencar', '05/08/1958', 2)
cliente3 = ClienteEspecial('1657409737', 'José', 'Alencar', '05/08/1958', 1)
cliente4 = ClienteEspecial('1657409736', 'Saulo', 'Alencar', '05/08/1958', 3)
produto1 = Produto('Teclado', 250.00)
produto2 = Produto('Monitor', 530.00)
produto3 = Produto('Mouse', 80.00)
produto4 = Produto('CPU', 1200.00)

#criando a minha loja
lojinha = Loja()

#adicionando os clientes no cadastro da loja
lojinha.adicionar_cliente_especial(cliente2)
lojinha.adicionar_cliente_especial(cliente3)
lojinha.adicionar_cliente_especial(cliente4)
lojinha.adicionar_cliente_padrao(cliente1)

#adicionando produtos na loja
lojinha.adicionar_produto(produto1)
lojinha.adicionar_produto(produto2)
lojinha.adicionar_produto(produto3)
lojinha.adicionar_produto(produto4)
#Produto.obter_total_produtos_cadastrados()
#lojinha.exibir_produtos()

lojinha.adicionar_produto_carrinho_cliente('04409306340',0)
lojinha.adicionar_produto_carrinho_cliente('04409306340',1)
lojinha.adicionar_produto_carrinho_cliente('1657409735',1)
lojinha.adicionar_produto_carrinho_cliente('1657409737',2)
lojinha.adicionar_produto_carrinho_cliente('1657409736',3)

cliente1.mostrar_carrinho()
#cliente2.mostrar_carrinho()

lojinha.calcular_total_carrinho_cliente('04409306340')
lojinha.calcular_total_carrinho_cliente('1657409735')
lojinha.calcular_total_carrinho_cliente('1657409737')
lojinha.calcular_total_carrinho_cliente('1657409736')

