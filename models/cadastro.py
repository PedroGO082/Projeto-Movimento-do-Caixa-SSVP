
class Membro:
    def __init__(self, nome, sexo, data_nascimento, proclamacao, endereco, encargo, ativo):
        self.nome = nome
        self.sexo = sexo
        if self.sexo == "M":
            self.cfd_or_csc = "Confrade"
        elif self.sexo == "F":
            self.cfd_or_csc = "Consócia"
        else:
            raise ValueError("Sexo deve ser 'M' para masculino ou 'F' para feminino.")
        self.data_nascimento = data_nascimento
        self.proclamacao = proclamacao
        self.endereco = endereco
        self.encargo = encargo
        self.ativo = "ativo" if ativo.lower() == "ativo" else "inativo"
    
    def __str__(self):
        return f"{self.cfd_or_csc} {self.nome} - {self.encargo}, membro {self.ativo}, proclamado em {self.proclamacao}."
    
    def __repr__(self):
        return self.__str__()

class Assistido:
    def __init__(self, nome, sexo, data_nascimento, endereco, membros_assistidos, ativo):
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        try:
            self.membros_assistidos = int(membros_assistidos)
        except ValueError:
            raise ValueError("O número de membros assistidos deve ser um número inteiro.")
        self.ativo = "ativo" if ativo.lower() == "ativo" else "inativo"

    def __str__(self):
          return f"O(A) {self.nome} com {self.membros_assistidos} membros residente em {self.endereco} está ativo."
    
    def __repr__(self):
        return self.__str__()

class Cadastrador:
    def __init__(self):
        self.membros = []
        self.confrades = []
        self.consocia = []
        self.assistidos = []
        self.inativos = []
    
    def cadastrar_membro(self, nome, sexo, data_nascimento, proclamacao, endereco, encargo, ativo):
        membro_novo = Membro(nome, sexo, data_nascimento, proclamacao, endereco, encargo, ativo)
        self.membros.append(membro_novo)
        if membro_novo.cfd_or_csc == "Confrade":
            self.confrades.append(membro_novo)
        else:
            self.consocia.append(membro_novo)
    
    def cadastrar_assistido(self, nome, sexo, data_nascimento, endereco, membros_assistidos, ativo):
        assistido_novo = Assistido(nome, sexo, data_nascimento, endereco, membros_assistidos, ativo)
        self.assistidos.append(assistido_novo)
    
    def __str__(self):
        return f"A conferência possui {len(self.confrades)} confrade(s) e {len(self.consocia)} consócia(s), {len(self.assistidos)} assistido(s).\n"

    def __repr__(self):
        return self.__str__()
    
    def get_membros(self):
        return self.membros

    def get_confrades(self):
        return self.confrades

    def get_consocia(self):
        return self.consocia

    def get_assistidos(self):
        return self.assistidos
    def get_inativos(self):
        return self.inativos
    def imprime_assistidos(self):
      for assistido in Cadastrador.assistidos:
         print(assistido)

    def total_membros_assistidos(self):
        qtdade = 0
        for assistido in self.cadastrador.assistidos:
            qtdade += assistido.membros_assistidos
        return qtdade