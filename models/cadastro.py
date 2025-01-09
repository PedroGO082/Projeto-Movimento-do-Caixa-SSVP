class Membro:
    def __init__(self, nome, sexo, data_nascimento, proclamacao, endereco, encargo, ativo):
        self.nome = nome
        self.sexo = sexo
        if self.sexo.lower() == "m":
            self.cfd_or_csc = "Confrade"
        elif self.sexo.lower() == "f":
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
    
    def to_dict(self):
        """Converte os atributos do cadastrador em um dicionário."""
        return {
            "membros": [membro.__dict__ for membro in self.get_membros()],
            "confrades": [confrade.__dict__ for confrade in self.get_confrades()],
            "consocia": [consocia.__dict__ for consocia in self.get_consocia()],
            "assistidos": [assistido.__dict__ for assistido in self.get_assistidos()],
            "inativos": [inativo.__dict__ for inativo in self.get_inativos()]
        }

    def to_json(self):
        """Serializa os atributos do cadastrador em formato JSON."""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)


def cadastro_membro():
    nome = input("Digite o nome do membro: ")
    while True:
        sexo = input("Digite o sexo do membro (M/F): ")
        if sexo.upper() == "M" or sexo.upper() == "F":
            break
        else:
            print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")
    while True:
        data_nascimento = input("Digite a data de nascimento do membro: ")
        if data_nascimento.count("/") == 2 and len(data_nascimento) == 10:
            break
        else:
            print("Data de nascimento inválida. Por favor, digite a data no formato dd/mm/aaaa.")
    while True:
        proclamacao = input("Digite a data de proclamação do membro: ")
        if proclamacao.count("/") == 2 and len(proclamacao) == 10:
            break
        else:
            print("Data de proclamação inválida. Por favor, digite a data no formato dd/mm/aaaa.")

        endereco = input("Digite o endereço do membro: ")
    while True:
        encargo = input("Digite o cargo do membro: ")
        if encargo.lower() == "presidente" or encargo.lower() == "secretária(o)" or encargo.lower() == "vice-presidente" or encargo.lower() == "vice - secretária(o)" or encargo.lower() == "tesoureiro" or encargo.lower() == "vice - tesoureiro" or encargo.lower() == "confrade" or encargo.lower() == "consocia":
            break
        else:
            print("Cargo inválido. Por favor, digite um cargo válido.")
    ativo = input("Digite o status do membro (ativo/inativo): ")
    Cadastrador.cadastrar_membro(nome, sexo, data_nascimento, proclamacao, endereco, encargo, ativo)
    print("Membro cadastrado com sucesso!")
