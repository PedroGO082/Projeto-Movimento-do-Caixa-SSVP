from models.cadastro import Cadastrador

class Conferencia:
    def __init__(self, nome, codigo, data_fundacao, conselho_particular, Cadastrador):
        self.nome = nome
        self.codigo = codigo
        self.data_fundacao = data_fundacao
        self.conselho_particular = conselho_particular
        self.cadastrador = Cadastrador

    def total_familias_assistidas(self):
        return len(self.cadastrador.assistidos)

    def total_pessoas_assistidas(self):
        return sum(assistido.membros_assistidos for assistido in self.cadastrador.assistidos)

    def __str__(self):
        return (
            f"Conferência {self.nome} Código: {self.codigo}\n"
            f"Fundada em: {self.data_fundacao}\n"
            f"Conselho Particular: {self.conselho_particular}\n"
            f"Membros: {len(self.cadastrador.membros)} "
            f"(Confrades: {len(self.cadastrador.confrades)}, "
            f"Consócias: {len(self.cadastrador.consocia)})\n"
            f"Assistidos: {self.total_familias_assistidas()} famílias, "
            f"{self.total_pessoas_assistidas()} pessoas\n"
        )

        