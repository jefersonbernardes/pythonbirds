class Pessoa:
    def __init__(self, *filhos, nome, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    rayan = Pessoa(nome='Rayan', idade=17)
    jeferson = Pessoa(rayan, nome='Jeferson')
    print(jeferson.cumprimentar())
    print(jeferson.nome)
    print(jeferson.idade)
    for filho in jeferson.filhos:
        print(filho.nome, filho.idade)
    jeferson.sobrenome = 'Bernardes'
    del jeferson.filhos
    print(jeferson.sobrenome)
    print(jeferson.__dict__)
    print(rayan.__dict__)






