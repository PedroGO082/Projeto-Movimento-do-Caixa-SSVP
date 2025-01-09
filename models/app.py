import os
import json
from models.cadastro import Cadastrador
from models.conferencia import Conferencia
from models.movimento_mensal import Caixa
from models.cadastro import Membro
#from models.movimento_mens


class SistemaSSVP:
    def __init__(self):
        self.data_file = "data.json"  # Arquivo onde os dados serão salvos
        self.cadastrador = Cadastrador()
        self.caixa = Caixa(1)  # Inicializa com o mês 1
        self.conferencia = Conferencia("Conferência Rainha dos Anjos", "06.06.06.06", "27/01/2003", "Conselho Particular Rainha dos Anjos", self.cadastrador)
        self.caixa.carregar_dados("caixa.json") 
        self.load_data()  # Carrega os dados do arquivo, se existirem

    def save_data(self):
    
        data = {
            "membros": [membro.__dict__ for membro in self.cadastrador.get_membros()],
            "confrades": [confrade.__dict__ for confrade in self.cadastrador.get_confrades()],
            "consocias": [consocia.__dict__ for consocia in self.cadastrador.get_consocia()],
            "assistidos": [assistido.__dict__ for assistido in self.cadastrador.get_assistidos()],
            "caixa": {
            "saldo_anterior": self.caixa.anterior,
            "dados_mensais": self.caixa.dados_mensais  # Salva os dados mensais do caixa
            }
        }
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso!")


    def load_data(self):
   
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
            
                for membro in data.get("membros", []):
                    self.cadastrador.cadastrar_membro(
                        membro["nome"], membro["sexo"], membro["data_nascimento"],
                        membro["proclamacao"], membro["endereco"], membro["encargo"], membro["ativo"]
                )
            
                for confrade in data.get("confrades", []):
                    self.cadastrador.confrades.append(Membro(
                        confrade["nome"], confrade["sexo"], confrade["data_nascimento"],
                        confrade["proclamacao"], confrade["endereco"], confrade["encargo"], confrade["ativo"]
                 ))
            
                for consocia in data.get("consocias", []):
                    self.cadastrador.consocia.append(Membro(
                        consocia["nome"], consocia["sexo"], consocia["data_nascimento"],
                        consocia["proclamacao"], consocia["endereco"], consocia["encargo"], consocia["ativo"]
                    ))
            
                for assistido in data.get("assistidos", []):
                    self.cadastrador.cadastrar_assistido(
                        assistido["nome"], assistido["sexo"], assistido["data_nascimento"],
                        assistido["endereco"], assistido["membros_assistidos"], assistido["ativo"]
                    )
            
                self.caixa.anterior = data.get("caixa", {}).get("saldo_anterior", 0)
                self.caixa.dados_mensais = data.get("caixa", {}).get("dados_mensais", {})
                print("Dados carregados com sucesso!")
        else:
            print("Nenhum dado encontrado. Um novo arquivo será criado ao salvar.")


    def menu_principal(self):
        while True:
            print("\n=== Sistema de Gestão SSVP ===")
            print("1. Cadastrar Membro")
            print("2. Cadastrar Assistido")
            print("3. Gerenciar Caixa")
            print("4. Relatórios")
            print("5. Sair")
            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                self.cadastrar_membro()
            elif escolha == "2":
                self.cadastrar_assistido()
            elif escolha == "3":
                self.gerenciar_caixa()
            elif escolha == "4":
                self.exibir_relatorios()
            elif escolha == "5":
                self.caixa.salvar_dados("caixa.json")
                self.save_data()  
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def cadastrar_membro(self):
        print("\n=== Cadastro de Membro ===")
        nome = input("Nome: ")
        sexo = input("Sexo (M/F): ")
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        proclamacao = input("Data de Proclamação (dd/mm/aaaa): ")
        endereco = input("Endereço: ")
        encargo = input("Cargo: ")
        ativo = input("Status (ativo/inativo): ")
        self.cadastrador.cadastrar_membro(nome, sexo, data_nascimento, proclamacao, endereco, encargo, ativo)
        print("Membro cadastrado com sucesso!")

    def cadastrar_assistido(self):
        print("\n=== Cadastro de Assistido ===")
        nome = input("Nome: ")
        sexo = input("Sexo (M/F): ")
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        endereco = input("Endereço: ")
        membros_assistidos = input("Número de membros assistidos: ")
        ativo = input("Status (ativo/inativo): ")
        self.cadastrador.cadastrar_assistido(nome, sexo, data_nascimento, endereco, membros_assistidos, ativo)
        print("Assistido cadastrado com sucesso!")

    def gerenciar_caixa(self):
        print("\n=== Gerenciar Caixa ===")
        mes = input("Digite o mês (1-12): ")
        try:
            mes = int(mes)
            if mes < 1 or mes > 12:
                raise ValueError
            self.caixa.mes = mes
            print(f"Gerenciando caixa para o mês {self.caixa.mes}.")
        except ValueError:
            print("Mês inválido. Tente novamente.")
            return

         # Gerenciar receitas e despesas para o mês especificado
        minha_caixa = Caixa(self.caixa.mes)
       
        receitas_data = minha_caixa.receitas()  # Função existente para receber receitas
        #print("Receitas cadastradas com sucesso:", receitas_data)
        if mes not in self.caixa.dados_mensais:
            self.caixa.dados_mensais[mes] = {}
        self.caixa.dados_mensais[mes]['receitas_detalhadas'] = receitas_data
        self.caixa.receitas_decimas(
            receitas_data["coleta"],
            receitas_data["subscritores_bemfeitores"],
            receitas_data["doacoes"],
            receitas_data["eventos"],
            receitas_data["outras_fontes"],
        )
        self.caixa.receitas_semdecimas(
            receitas_data["subvencao_oficial"],
            receitas_data["ozanam_solidariedade"],
            receitas_data["uniao_fraternal"],
            receitas_data["contri_cc"],
            receitas_data["contri_cmb"],
        )

        print("Receitas cadastradas com sucesso.")
        #self.caixa.despesas()  # Função existente para receber despesas
        pagamentos_data =  minha_caixa.pagamentos()  # Chama a função pagamentos
        #print("Pagamentos cadastrados com sucesso:", pagamentos_data)

    # Atualizar despesas no dicionário de dados mensais
        self.caixa.dados_mensais[mes]['despesas_detalhadas'] = pagamentos_data
        self.caixa.despesas(
            pagamentos_data["cesta_basica"],
            pagamentos_data["moradia"],
            pagamentos_data["contas_assistidos"],
            pagamentos_data["despesas_oe"],
            pagamentos_data["repasse_uniao"],
            pagamentos_data["despesas_adm"],
         )
        print("Despesas cadastradas com sucesso.")
    # Calcular e armazenar o saldo final no dicionário
        saldo_anterior = self.caixa.dados_mensais.get(mes - 1, {}).get('saldo', 0)
        saldo_final = self.caixa.saldo_a_transp()
        self.caixa.dados_mensais[mes]['saldo_anterior'] = saldo_anterior
        self.caixa.dados_mensais[mes]['saldo_final'] = saldo_final
        print(f"Caixa do mês {mes} atualizado.")

    def exibir_relatorios(self):
        print("\n=== Relatórios ===")
        try:
            mes = int(input("Digite o mês do relatório (1-12): "))
            if mes < 1 or mes > 12:
                raise ValueError
        except ValueError:
            print("Mês inválido. Tente novamente.")
            return

        if mes not in self.caixa.dados_mensais:
            print(f"Nenhum dado encontrado para o mês {mes}.")
            return

        dados = self.caixa.dados_mensais[mes]
        receitas = dados.get('receitas', 0)
        despesas = dados.get('despesas', 0)
        saldo_anterior = self.caixa.dados_mensais.get(mes - 1, {}).get('saldo', 0)
        saldo = dados.get('saldo', receitas - despesas)

        print(f"\n=== Relatório do Mês {mes} ===")
        print(f"Membros: {self.cadastrador.get_membros()}")
        print(f"Assistidos: {self.cadastrador.get_assistidos()}")
        print(f"Saldo Anterior: R$ {saldo_anterior:.2f}")
        print(f"Total Receitas: R$ {receitas:.2f}")
        print(f"Total Despesas: R$ {despesas:.2f}")
        print(f"Saldo Final: R$ {saldo:.2f}")