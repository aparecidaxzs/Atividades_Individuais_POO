#inicio questão 6
class Aluno:
    def __init__(self, nome:str, matricula:str):
        self.nome = nome
        self.matricula = matricula
        sel.notas: list[float]=[]

    def lancar_notas(self, valor:float):
        self.notas.append(valor)

    def media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def aprovado(self) -> bool:
        return self.media() >= 6

    def str(self):
        return f"{self.nome} ({self.matricula}) - media {self.media():.1f}"

#fim da questão 6

#inicio da questão 7
aluno1 = Aluno("Ana","20261234")
aluno2 = Aluno("Carlos","20261234")
aluno3 = Aluno("Maria", "20261234")

aluno1.lancar_notas(7)
aluno1.lancar_notas(8)

aluno2.lancar_notas(5)
aluno2.lancar_notas(4)

aluno3.lancar_notas(6)
aluno3.lancar_notas(9)

alunos = [aluno1, aluno2, aluno3]


for aluno in alunos:
    if aluno.aprovado():
        print(aluno)

#fim da questão 7

#inicio da questão 8
class Retangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)

    def __eq__(self, outro) -> bool:
        if not isinstance(outro, Retangulo):
            return False

        return self.base == outro.base and self.altura == outro.altura

#fim da questão 8

#inicio da questão 9
class Data:
    def __init__(self, dia: int, mes: int, ano: int):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def texto(cls, texto: str):
        dia, mes, ano = map(int, texto.split("/"))
        return cls(dia, mes, ano)

    @staticmethod
    def bissexto(ano: int) -> bool:
        return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}"


data = Data(9, 8, 2026)
print(data)