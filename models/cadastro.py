cfd = 0
csc = 0
assistidos = 0

class membro:
    def __init__(self, nome, sexo, data_nascimento, proclamacao, endereco, encargo, ativo):
        global cfd, csc
        self.nome = nome
        self.sexo = sexo
        if self.sexo == "M":
            self.cfd_or_csc = "Confrade"
            cfd += 1
            
        else:
            self.cfd_or_csc = "Consócia"
            csc += 1
        self.data_nascimento = data_nascimento
        self.proclamacao = proclamacao
        self.endereco = endereco
        self.encargo = encargo
        if ativo == True or ativo == "ativo" or ativo == "Ativo" or ativo == "ATIVO":   
            self.ativo = "ativo"
        else:
            self.ativo = "inativo"
    
    def __str__(self):
        return f"{self.cfd_or_csc} {self.nome} - {self.encargo}, membro {self.ativo}, proclamado em {self.proclamacao}."
    
    def __repr__(self):
        return f"{self.cfd_or_csc} {self.nome} - {self.encargo}, membro {self.ativo}, proclamado em {self.proclamacao}."

class assistido:
    def __init__(self, nome, sexo, data_nascimento, endereco, membros, ):
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.enderenco = endereco
        self.membros = membros
        self.ativo = True
        if self.ativo == True:
            assistidos += 1
membros = []
#Pedro = membro("Pedro Gomes", "M", "01/01/1990", "01/01/2010", "Rua 1, 123", "Presidente", "ativo")
membros.append(Pedro)



print(Pedro); 
print(membros)
print(f"A conferência possui {cfd} confrade(s) e {csc} consócia(s).")