from cadastro import assistido

class Conferencia:
    def __init__(self, nome, codigo, data_fundacao, conselho_particular):
        self.nome = nome
        self.codigo = codigo
        self.data_fundacao = data_fundacao
        self.conselho_particular = conselho_particular
        self.membros = {"Confrades": 0, "Consócias": 0, "Aspirantes": 0, "Auxiliares": 0}
        #self.familias_assistidas = cadasto.assistido()
        self.pessoas_assistidas = 0


    def add_membro(self, membro):
        