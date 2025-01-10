import os
import json
from models.cadastro import Cadastrador
from models.conferencia import Conferencia
from models.movimento_mensal import Caixa
from models.cadastro import Membro

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

        saldo_anterior = self.caixa.dados_mensais.get(mes - 1, {}).get('saldo_final', 0)
        if mes not in self.caixa.dados_mensais:
            self.caixa.dados_mensais[mes] = {}
        self.caixa.dados_mensais[mes]['saldo_anterior'] = saldo_anterior

        receitas_data = self.caixa.receitas()  # Função existente para receber receitas
        self.caixa.dados_mensais[mes]['receitas_detalhadas'] = receitas_data

        pagamentos_data = self.caixa.pagamentos()  # Função existente para receber despesas
        self.caixa.dados_mensais[mes]['despesas_detalhadas'] = pagamentos_data

        saldo_final = self.caixa.saldo_a_transp()
        self.caixa.dados_mensais[mes]['saldo_final'] = saldo_final
        print(f"Caixa do mês {mes} atualizado.")

    def exibir_relatorios(self):
        print("\n=== Relatórios ===")
        print("1. Relatório Financeiro")
        print("2. Relatório de Membros")
        print("3. Relatório de Assistidos")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            self.relatorio_financeiro()
        elif escolha == "2":
            self.relatorio_membros()
        elif escolha == "3":
            self.relatorio_assistidos()
        else:
            print("Opção inválida. Tente novamente.")

    def relatorio_financeiro(self):
        print("\n=== Relatório Financeiro ===")
        mes = int(input("Digite o mês do relatório (1-12): "))
        if mes not in self.caixa.dados_mensais:
            print(f"Nenhum dado financeiro encontrado para o mês {mes}.")
            return

        total_membros = len(self.cadastrador.get_membros())
        total_confrades = len(self.cadastrador.get_confrades())
        total_consocias = len(self.cadastrador.get_consocia())
        total_familias_assistidas = len(self.cadastrador.get_assistidos())
        total_pessoas_assistidas = sum(a.membros_assistidos for a in self.cadastrador.get_assistidos())

        dados_mes = self.caixa.dados_mensais[mes]
        receitas = dados_mes.get('receitas_detalhadas', {})
        despesas = dados_mes.get('despesas_detalhadas', {})
        saldo_anterior = dados_mes.get('saldo_anterior', 0)
        saldo_final = dados_mes.get('saldo_final', 0)

        print("\n=== Relatório Financeiro ===")
        print(f"Mês: {mes}")
        print(f"Total de Membros: {total_membros}")
        print(f"  Confrades: {total_confrades}")
        print(f"  Consócias: {total_consocias}")
        print(f"Famílias Assistidas: {total_familias_assistidas}")
        print(f"Pessoas Assistidas: {total_pessoas_assistidas}")
        print("\n--- Dados Financeiros ---")
        print(f"Saldo Anterior: R$ {saldo_anterior:.2f}")
        print("Receitas:")
        for key, value in receitas.items():
            print(f"  {key.replace('_', ' ').capitalize()}: R$ {value:.2f}")
        print("Despesas:")
        for key, value in despesas.items():
            print(f"  {key.replace('_', ' ').capitalize()}: R$ {value:.2f}")
        print(f"Saldo Final: R$ {saldo_final:.2f}")

    def relatorio_membros(self):
        print("\n=== Relatório de Membros ===")
        membros = self.cadastrador.get_membros()
        for membro in membros:
            print(membro)

    def relatorio_assistidos(self):
        print("\n=== Relatório de Assistidos ===")
        assistidos = self.cadastrador.get_assistidos()
        for assistido in assistidos:
            print(assistido)
