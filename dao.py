from numpy import append
from models import *

class DaoCategoria:

    @classmethod
    def salvar(cls, categoria):
        with open('categorias.txt', 'a') as arq:
            arq.writelines(f'{categoria}\n')

    @classmethod
    def ler(cls):
        with open('categorias.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        
        return cat


class DaoVenda:

    @classmethod
    def salvar(cls, venda: Venda):
         with open('vendas.txt', 'a') as arq:
            arq.writelines(f'{venda.item_vendido.nome} | {venda.item_vendido.preco} | {venda.item_vendido.categoria} | {venda.vendedor} | {venda.comprador} | {venda.quantidade_vendida} | {venda.data}\n')

    @classmethod
    def ler(cls):
        with open('vendas.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', '').split(' | '), cls.venda))

        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], float(i[1]), i[2]), i[3], i[4], int(i[5]), i[6]))

        return vend


class DaoEstoque:

    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
         with open('estoque.txt', 'a') as arq:
            arq.writelines(f'{produto.nome} | {produto.preco} | {produto.categoria} | {quantidade}\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', '').split(' | '), cls.estoque))

        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], float(i[1]), i[2]), int(i[3])))

        return est


class DaoFornecedor:

    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
         with open('fornecedores.txt', 'a') as arq:
            arq.writelines(f'{fornecedor.nome} | {fornecedor.cnpj} | {fornecedor.telefone} | {fornecedor.categoria}\n')

    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()

        cls.fornecedores = list(map(lambda x: x.replace('\n', '').split(' | '), cls.fornecedores))

        forn = []
        if len(cls.fornecedores) > 0:
            for i in cls.fornecedores:
                forn.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return forn


class DaoPessoa:

    @classmethod
    def salvar(cls, pessoas: Pessoa):
         with open('clientes.txt', 'a') as arq:
            arq.writelines(f'{pessoas.nome} | {pessoas.telefone} | {pessoas.cpf} | {pessoas.email} | {pessoas.endereco}\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace('\n', '').split(' | '), cls.clientes))

        cli = []
        if len(cls.clientes) > 0:
            for i in cls.clientes:
                cli.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))

        return cli


class DaoFuncionario:

    @classmethod
    def salvar(cls, funcionario: Funcionario):
         with open('funcionarios.txt', 'a') as arq:
            arq.writelines(f'{funcionario.clt} | {funcionario.nome} | {funcionario.telefone} | {funcionario.cpf} | {funcionario.email} | {funcionario.endereco}\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(map(lambda x: x.replace('\n', '').split(' | '), cls.funcionarios))

        func = []
        if len(cls.funcionarios) > 0:
            for i in cls.funcionarios:
                func.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))

        return func




"""
#x = Produtos('Laranja', '2', 'Frutas')
#x = Produtos('Acerola', '5', 'Frutas')
#y = Venda(x, 'Caio', 'Gleson', 7)
#z = DaoVenda.salvar(y)

v = DaoVenda.ler()



print(v[2].item_vendido.nome)
print(v[2].item_vendido.preco)
print(v[2].item_vendido.categoria)
print(v[2].vendedor)
print(v[2].comprador)
print(v[2].quantidade_vendida)
print(v[2].data)
print(v[2].data)



#DaoCategoria.salvar('Frutas')
#DaoCategoria.salvar('Verduras')
#DaoCategoria.salvar('Legumes')

#DaoCategoria.ler()

"""