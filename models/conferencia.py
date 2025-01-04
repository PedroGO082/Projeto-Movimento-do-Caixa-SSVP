from cadastro import Assistido
from cadastro import Membro
from cadastro import Cadastrador

class Conferencia:
    def __init__(self, nome, codigo, data_fundacao, conselho_particular):
        self.nome = nome
        self.codigo = codigo
        self.data_fundacao = data_fundacao
        self.conselho_particular = conselho_particular
        self.membros = {"Confrades": 0, "Consócias": 0, "Auxiliares": 0}
        self.familias_assistidas = len(cadastro.assistidos)
        self.pessoas_assistidas = Cadastrador.total_membros_assistidos()

        