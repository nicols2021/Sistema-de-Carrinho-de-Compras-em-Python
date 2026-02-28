
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    # calcula o valor total daquele produto
    def subtotal(self):
        return self.preco * self.quantidade