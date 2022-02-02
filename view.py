from controller import *
import os.path

def criar_arquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            open(i, "w").close()


criar_arquivos(
    "categorias.txt", "clientes.txt",
    "estoque.txt", "fornecedores.txt",
    "funcionarios.txt", "vendas.txt")



if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar ( Categorias )\n"
                          "Digite 2 para acessar ( Estoque )\n"
                          "Digite 3 para acessar ( Fornecedor )\n"
                          "Digite 4 para acessar ( Cliente )\n"
                          "Digite 5 para acessar ( Funcionario )\n"
                          "Digite 6 para acessar ( Vendas )\n"
                          "Digite 7 para ver os produtos mais vendidos\n"
                          "Digite 8 para sair\n"))

        if local == 1:
            cat = ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma categoria\n"
                                    "Digite 2 para remover uma categoria\n"
                                    "Digite 3 para alterar uma categoria\n"
                                    "Digite 4 para mostrar as categorias cadastradas\n"
                                    "Digite 5 para voltar\n"))

                if decidir == 1:
                    categoria = input("Digite a categoria que deseja cadastrar\n")
                    cat.cadastrar_categoria(categoria)
                elif decidir == 2:
                    categoria = input("Digite a categoria que deseja remover\n")
                    cat.remover_categoria(categoria)
                elif decidir == 3:
                    categoria = input("Digite a categoria que deseja alterar\n")
                    nova_categoria = input("Digite a categoria para qual deseja alterar\n")
                    cat.alterar_categoria(categoria, nova_categoria)
                elif decidir == 4:
                    cat.mostrar_categoria()
                else:
                    break

        elif local == 2:
            cat = ControllerEstoque()
            while True:
                decidir = int(input("Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para remover um produto\n"
                                    "Digite 3 para alterar um produto\n"
                                    "Digite 4 para ver o estoque\n"
                                    "Digite 5 para voltar\n"))

                if decidir == 1:
                    nome = input("Digite o nome do produto: \n")
                    preco = input("Digite o preco do produto: \n")
                    categoria = input("Digite a categoria do produto: \n")
                    quantidade = input("Digite a quantidade do produto: \n")

                    cat.cadastrar_produto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    produto = input("Digite o produto que deseja remover: \n")

                    cat.remover_produto(produto)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do produto que deseja alterar: \n")
                    nome = input("Digite o novo nome do produto: \n")
                    preco = input("Digite o novo preco do produto: \n")
                    categoria = input("Digite a nova categoria do produto: \n")
                    quantidade = input("Digite a nova quantidade do produto: \n")

                    cat.alterar_produto(nomeAlterar, nome, preco, categoria, quantidade)
                elif decidir == 4:
                    cat.mostrar_estoque()
                else:
                    break

        elif local == 3:
            cat = ControllerFornecedor()
            while True:
                decidir = int(input("Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para remover um fornecedor\n"
                                    "Digite 3 para alterar um fornecedor\n"
                                    "Digite 4 para mostrar fornecedores\n"
                                    "Digite 5 para voltar"))

                if decidir == 1:
                    nome = input("Digite o nome do fornecedor: \n")
                    cnpj = input("Digite o cnpj do fornecedor: \n")
                    telefone = input("Digite o telefone do fornecedor: \n")
                    categoria = input("Digite a categoria fornecida: \n")
                    cat.cadastrar_fornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    fornecedor = input("Digite o fornecedor que deseja remover: \n")
                    cat.remover_fornecedor(fornecedor)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do fornecedor que deseja alterar: \n")
                    novoNome = input('Digite o novo nome do fornecedor: \n')
                    novoCnpj = input('Digite o novo cnpj do fornecedor: \n')
                    novoTelefone = input('Digite o novo telefone do fornecedor: \n')
                    novoCategoria = input('Digite a nova categoria fornecida: \n')

                    cat.alterar_fornecedor(nomeAlterar, novoNome, novoCnpj, novoTelefone, novoCategoria)
                elif decidir == 4:
                    cat.mostrar_fornecedores()
                else:
                    break

        elif local == 4:
            cat = ControllerCliente()
            while True:
                decidir = int(input("Digite 1 para cadastrar um cliente\n"
                                    "Digite 2 para remover um cliente\n"
                                    "Digite 3 para alterar um cliente\n"
                                    "Digite 4 para mostrar clientes\n"
                                    "Digite 5 para voltar\n"))

                if decidir == 1:
                    nome = input("Digite o nome do cliente: \n")
                    telefone = input("Digite o telefone do cliente: \n")
                    cpf = input("Digite o cpf do cliente: \n")
                    email = input("Digite o email do cliente: \n")
                    endereco = input("Digite o endereço do cliente: \n")

                    cat.cadastrar_cliente(nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    cliente = input("Digite o cliente que deseja remover: \n")

                    cat.remover_cliente(cliente)
                elif decidir == 3:
                    nome_atual = input("Digite o nome do cliente que deseja alterar: \n")
                    novo_nome = input("Digite o novo nome do cliente: \n")
                    novo_telefone = input("Digite o novo telefone do cliente: \n")
                    novo_cpf = input("Digite o novo cpf do cliente: \n")
                    novo_email = input("Digite o novo email do cliente: \n")
                    novo_endereco = input("Digite o novo endereço do cliente: \n")
                    cat.alterar_cliente(nome_atual, novo_nome, novo_telefone, novo_cpf, novo_email, novo_endereco)
                elif decidir == 4:
                    cat.mostrar_clientes()
                else:
                    break

        elif local == 5:
            cat = ControllerFuncionario()
            while True:
                decidir = int(input("Digite 1 para cadastrar um funcionario\n"
                                    "Digite 2 para remover um funcionario\n"
                                    "Digite 3 para alterar um funcionario\n"
                                    "Digite 4 para mostrar funciorios\n"
                                    "Digite 5 para voltar\n"))

                if decidir == 1:
                    clt = input("Digite a clt do funcionario: \n")
                    nome = input("Digite o nome do funcionario: \n")
                    telefone = input("Digite o telefone do funcionario: \n")
                    cpf = input("Digite o cpf do funcionario: \n")
                    email = input("Digite o email do funcionario: \n")
                    endereco = input("Digite o endereço do funcionario: \n")

                    cat.cadastrar_funcionario(clt, nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    funcionario = input("Digite o funcionario que deseja remover: \n")
                    cat.remover_funcionario(funcionario)
                elif decidir == 3:
                    nome_atual = input("Digite o nome do funcionario que deseja alterar: \n")
                    novo_clt = input("Digite a nova clt do funcionario: \n")
                    novo_nome = input("Digite o novo nome do funcionario: \n")
                    novo_telefone = input("Digite o novo telefone do funcionario: \n")
                    novo_cpf = input("Digite o novo cpf do funcionario: \n")
                    novo_email = input("Digite o novo email do funcionario: \n")
                    novo_endereco = input("Digite o novo endereço do funcionario: \n")
                    cat.alterar_funcionario(nome_atual, novo_clt, novo_nome, novo_telefone, novo_cpf, novo_email,
                                           novo_endereco)
                elif decidir == 4:
                    cat.mostrar_funcionarios()
                else:
                    break

        elif local == 6:
            cat = ControllerVenda()
            while True:
                decidir = int(input("Digite 1 para realizar uma venda\n"
                                    "Digite 2 para ver as vendas\n"
                                    "Digite 3 para voltar\n"))

                if decidir == 1:
                    nome = input('Digite o nome do produto: \n')
                    vendedor = input('Digite nome do vendedor: \n')
                    comprador = input('Digite o nome do cliente: \n')
                    quantidade = input('Digite a quantidade: \n')
                    cat.cadastrar_venda(nome, vendedor, comprador, quantidade)
                elif decidir == 2:
                    data_inicio = input("Digite a data de inicio no formato dia/mes/ano: \n")
                    data_termino = input("Digite a data de termino no formato dia/mes/ano: \n")
                    cat.mostrar_venda(data_inicio, data_termino)
                else:
                    break

        elif local == 7:
            a = ControllerVenda()
            a.relatorio_produtos()
        else:
            break
