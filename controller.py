#from sqlalchemy import true
from models import *
from dao import *
from datetime import datetime


class ControllerCategoria:

    def cadastra_categoria(self, nova_categoria):
        existe = False
        x = DaoCategoria.ler()

        for i in x:
            if i.categoria == nova_categoria:
                existe = True
                print(f'A categoria {nova_categoria} já existe!')
                break
        
        if not existe:
            DaoCategoria.salvar(nova_categoria)
            print('Categoria cadastrada com sucesso!')

    def remover_categoria(self, categoria_remover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoria_remover, x))

        if not cat:
            print('A categoria que deseja remover não existe!!!')
        else:
            with open('categorias.txt', 'w') as arq:
                for i in x:
                    if i.categoria != categoria_remover:
                        arq.writelines(f'{i.categoria}\n')
            print('Categoria removida com sucesso!')
            #TODO: COLOCAR 'SEM CATEGORIA' NO ESTOQUE


    def alterar_categoria(self, categoria_antiga, categoria_nova):
        x = DaoCategoria.ler()
        cat_ant = list(filter(lambda x: x.categoria == categoria_antiga, x))

        if not cat_ant:
            print(f'Não existe a categoria {categoria_antiga} para ser alterada!')
        else:
            cat_nov = list(filter(lambda x: x.categoria == categoria_nova, x))
            if cat_nov:
                print(f'A categoria {categoria_nova} já existe!')
            else:
                x = list(map(lambda x: Categoria(categoria_nova) if (x.categoria == categoria_antiga) else x, x))
                with open('categorias.txt', 'w') as arq:
                    for i in x:
                        arq.writelines(f'{i.categoria}\n')
                print(f'Alteração da categoria efetuada com sucesso!')
                #TODO: ALTERAR TAMBÉM A CATEGORIA DO ESTOQUE

    def mostrar_categoria(self):
        x = DaoCategoria.ler()
        if not x:
            print('Categoria vazia!')
        else:
            print('Categorias:')
            for i in x:
                print(f'- {i.categoria}')


class ControllerEstoque:

    def cadastrar_produto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        cat = list(filter(lambda y: y.categoria == categoria, y))

        if cat:
            if not est:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Estoque cadastrado com sucesso!')
            else:
                print('Produto já existe em estoque!')
        else:
            print('Categoria inexistente!')


    def remover_produto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if est:
            open('estoque.txt', 'w').close()
            for i in x:
                if i.produto.nome != nome:
                    DaoEstoque.salvar(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade)
            print('Produto removido com sucesso!')
        else:
            print('O pruduto que deseja remover não existe!')


    def alterar_produto(self, nome_anterior, novo_nome, novo_preco, nova_categoria, nova_quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        cat = list(filter(lambda y: y.categoria == nova_categoria, y))

        if cat:
            est_ant = list(filter(lambda x: x.produto.nome == nome_anterior, x))
            if est_ant:
                est_nov = list(filter(lambda x: x.produto.nome == novo_nome, x))
                if not est_nov:
                    k = list(map(lambda x: Estoque(Produtos(novo_nome, novo_preco, nova_categoria), nova_quantidade) if (x.produto.nome == nome_anterior) else x, x))
                    open('estoque.txt', 'w').close()
                    for i in k:
                        DaoEstoque.salvar(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade)
                    print('Produto alterado com sucesso!')
                else:
                    print('Produto já cadastrado!')
            else:
                print('O produto que deseja alterar não existe!')
        else:
            print('A categoria informada não existe!')

    def mostrar_estoque(self):
        estoque = DaoEstoque.ler()

        if not estoque:
            print('Estoque vazio!')
        else:
            print('=========== Produtos ===========')
            for i in estoque:
                print(f'Nome: {i.produto.nome}\n'
                      f'Preço: {i.produto.preco}\n'
                      f'Categoria: {i.produto.categoria}\n'
                      f'Quantidade: {i.quantidade}\n'
                      f'--------------------')


class ControllerVenda:

    def cadastrar_venda(self, nome_produto, vendedor, comprador, quantidade_vendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x:
            if not existe:
                if i.produto.nome == nome_produto:
                    existe = True
                    if i.quantidade >= quantidade_vendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidade_vendida)

                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidade_vendida)
                        valor_compra = int(quantidade_vendida) * float(i.produto.preco)
                        DaoVenda.salvar(vendido)

            temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])


        if not existe:
            print('O produto não existe!')
            return None
        elif not quantidade:
            print('A quantidade vendida não contem em estoque!')
            return None
        else:
            open('estoque.txt', 'w').close()
            for i in temp:
                DaoEstoque.salvar(Produtos(i[0].nome, i[0].preco, i[0].categoria), i[1])
            print('Venda realizada com sucesso!')
            return valor_compra

    def relatorio_produtos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.item_vendido.nome
            quantidade = i.quantidade_vendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))

            if tamanho:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)} 
                if (x['produto'] == nome) else (x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': quantidade})

        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)

        print('Esses são os produtos mais vendidos:')
        a = 1
        for i in ordenado:
            print(f"Produto: {i['produto']}\nQuantidade: {i['quantidade']}\n---------------")


    def mostrar_venda(self, data_inicio, data_termino):
        vendas = DaoVenda.ler()
        inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
        termino = datetime.strptime(data_termino, '%d/%m/%Y')

        vendas_selecionadas = list(filter(lambda x: (datetime.strptime(x.data, '%d/%m/%Y') >= inicio) 
                                          and (datetime.strptime(x.data, '%d/%m/%Y') <= termino), vendas))
        
        total = 0
        for n, i in enumerate(vendas_selecionadas):
            print(f'=========== Venda {n+1} ===========\n'
                  f'Nome: {i.item_vendido.nome}\n'
                  f'Data: {i.data}\n'
                  f'Quantidade: {i.quantidade_vendida}\n'
                  f'Vendedor: {i.vendedor}\n'
                  f'Cliente: {i.comprador}')
            total += float(i.item_vendido.preco) * int(i.quantidade_vendida)

        print(f'Total vendido: R$ {total}')


class ControllerFornecedor:
    
    def cadastrar_fornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        lista_cnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        lista_telefone = list(filter(lambda x: x.telefone == telefone, x))

        if lista_cnpj:
            print('O CNPJ já existe!')
        elif lista_telefone:
            print('O telefone já está cadastrado!')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
                print('Fornecedor cadastrado com sucesso!')
            else:
                print('Digite um CNPJ ou telefone válido!')

    def alterar_fornecedor(self, nome_atual, novo_nome, novo_cnpj, novo_telefone, nova_categoria):
        x = DaoFornecedor.ler()
        fornecedor = list(filter(lambda x: x.nome == nome_atual, x))

        if fornecedor:
            cnpj = list(filter(lambda x: x.cnpj == novo_cnpj, x))
            if not cnpj:
                x = list(map(lambda x: Fornecedor(novo_nome, novo_cnpj, novo_telefone, nova_categoria) if x.nome == nome_atual else x, x))

                open('fornecedores.txt', 'w').close()
                for i in x:
                    DaoFornecedor.salvar(Fornecedor(i.nome, i.cnpj, i.telefone, i.categoria))
                print('Fornecedor alterado com sucesso!')
            else:
                print('CNPJ já existe!')
        else:
            print('O fornecedor que deseja alterar não existe!')

    def remover_fornecedor(self, nome):
        x = DaoFornecedor.ler()
        fornecedor = list(filter(lambda x: x.nome == nome, x))

        if fornecedor:
            open('fornecedores.txt', 'w').close()
            for i in x:
                if i.nome != nome:
                    DaoFornecedor.salvar(Fornecedor(i.nome, i.cnpj, i.telefone, i.categoria))
            print('Fornecedor removido com sucesso!')    


    def mostrar_fornecedores(self):
        x = DaoFornecedor.ler()

        if not x:
            print('Lista de fornecedores vazia!')
        else:
            for n, i in enumerate(x):
                print(f'======== Fornecedor {n+1} ========\n'
                      f'Nome: {i.nome}\n'
                      f'CNPJ: {i.cnpj}\n'
                      f'Fone: {i.telefone}\n'
                      f'Categoria: {i.categoria}\n')


class ControllerCliente:

    def cadastrar_cliente(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()

        verifica_cpf = list(filter(lambda x: x.cpf == cpf, x))
        verifica_telefone = list(filter(lambda x: x.telefone == telefone, x))

        if not verifica_cpf:
            if not verifica_telefone:
                if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                    DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                    print('Cliente cadastrado com sucesso!')
                else:
                    print('CPF ou telefone incorretos!')
            else:
                print('Já existe um cliente com esse telefone cadastrado!')
        else:
            print('Já existe um cliente com esse cpf cadastrado!')

    def alterar_cliente(self, nome_atual, novo_nome, novo_telefone, novo_cpf, novo_email, novo_endereco):
        x = DaoPessoa.ler()
        verifica_nome = list(filter(lambda x: x.nome == nome_atual, x))

        if verifica_nome:
            x = list(map(lambda x: Pessoa(novo_nome, novo_telefone, novo_cpf, novo_email, novo_endereco) 
                         if x.nome == nome_atual else x, x))
            open('clientes.txt', 'w').close()
            for i in x:
                DaoPessoa.salvar(Pessoa(i.nome, i.telefone, i.cpf, i.email, i.endereco))                
            print('Cliente alterado com sucesso!')
        else:
            print('Cliente não encontrado!')

    def remover_cliente(self, nome):
        x = DaoPessoa.ler()
        verifica_nome = list(filter(lambda x: x.nome == nome, x))

        if verifica_nome:
            open('clientes.txt', 'w').close()
            x = [i for i in x if i.nome != nome]
            for i in x:
                DaoPessoa.salvar(Pessoa(i.nome, i.telefone, i.cpf, i.email, i.endereco))                
            print('Cliente removido com sucesso!')
        else:
            print('Cliente não encontrado!')

    def mostrar_clientes(self):
        x = DaoPessoa.ler()

        if x:
            for n, i in enumerate(x):
                print(f'======== Cliente {n+1} ========\n'
                      f'nome: {i.nome}\n'
                      f'telefone: {i.telefone}\n'
                      f'cpf: {i.cpf}\n'
                      f'email: {i.email}\n'
                      f'endereco: {i.endereco}\n')
        else:
            print('Lista de clientes vazia!')


class ControllerFuncionario:

    def cadastrar_funcionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()
        verifica_cpf = list(filter(lambda x: x.cpf == cpf, x))
        verifica_clt = list(filter(lambda x: x.clt == clt, x))

        if verifica_cpf:
            print('Já existe um funcionário com esse CPF!')
        elif verifica_clt:
            print('Já existe um funcionário com essa CLT!')
        elif len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
            DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
            print('Funcionário cadastrado com sucesso!')
        else:
            print('Digite um CPF ou telefone válido!')

    def alterar_funcionario(self, nome_atual, nova_clt, novo_nome, novo_telefone, novo_cpf, novo_email, novo_endereco):
        x = DaoFuncionario.ler()

        verifica_nome = list(filter(lambda x: x.nome == nome_atual, x))
        if not verifica_nome:
            print('Funcionário não encontrado!')
        elif len(novo_cpf) == 11 and len(novo_telefone) >= 10 and len(novo_telefone) <= 11:
            x = list(map(lambda x: Funcionario(nova_clt, novo_nome, novo_telefone, novo_cpf, novo_email, novo_endereco) 
                         if x.nome == nome_atual else x, x))
            open('funcionarios.txt', 'w').close()
            for i in x:
                DaoFuncionario.salvar(Funcionario(i.clt, i.nome, i.telefone, i.cpf, i.email, i.endereco))
            print('Funcionário alterado com sucesso!')
        else:
            print('Digite um CPF ou telefone válido!')

    def remover_funcionario(self, nome):
        x = DaoFuncionario.ler()

        verifica_nome = list(filter(lambda x: x.nome == nome, x))
        if not verifica_nome:
            print('Funcionário não encontrado!')
        else:
            x = [i for i in x if i.nome != nome]
            open('funcionarios.txt', 'w').close()
            for i in x:
                DaoFuncionario.salvar(Funcionario(i.clt, i.nome, i.telefone, i.cpf, i.email, i.endereco))
            print('Funcionário removido com sucesso!')            

    def mostrar_funcionarios(self):
        x = DaoFuncionario.ler()

        if not x:
            print('Lista de funcionarios vazia!')
        else:
            for n, i in enumerate(x):
                print(f'======== Funcionário {n+1} ========\n'
                      f'CLT: {i.clt}\n'
                      f'Nome: {i.nome}\n'
                      f'Telefone: {i.telefone}\n'
                      f'CPF: {i.cpf}\n'
                      f'Email: {i.email}\n'
                      f'Endereco: {i.endereco}\n')

