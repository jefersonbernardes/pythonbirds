class Pessoa:
    def __init__(self, nome, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    p = Pessoa('Jeferson')
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)



