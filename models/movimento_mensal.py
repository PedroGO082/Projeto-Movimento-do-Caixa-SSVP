import json
import os

class Caixa:
    def __init__(self, mes):
        self.mes = int(mes)
        self.mesant = 12 if self.mes == 1 else self.mes - 1
        self.anterior = 0  # Saldo do mês anterior
        self.saldo_anterior = {"anterior": self.anterior, "mes_anterior": self.mesant}
        self.subtotal1 = 0  # Inicializa subtotal1 (Receitas com Dízimas)
        self.subtotal2 = 0  # Inicializa subtotal2 (Receitas sem Dízimas)
        self.subtotal3 = 0  # Inicializa subtotal3 (Despesas)
        self.subtotal4 = 0  # Inicializa subtotal4 (Repasses)
        self.total_receitas = 0
        self.total_pag = 0
        self.dados_mensais = {}
        self.serialized_saldo_anterior = json.dumps(self.saldo_anterior) 
    
    def salvar_dados(self, arquivo="caixa.json"):
        """Salva os dados do dicionário dados_mensais em um arquivo JSON."""
        try:
            with open(arquivo, "w", encoding="utf-8") as file:
                json.dump(self.dados_mensais, file, ensure_ascii=False, indent=4)
            print("Dados do caixa salvos com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

    def carregar_dados(self, arquivo="caixa.json"):
   
      if os.path.exists(arquivo):
        try:
            with open(arquivo, "r", encoding="utf-8") as file:
                self.dados_mensais = json.load(file)
            print("Dados do caixa carregados com sucesso!")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
      else:
        print("Nenhum dado encontrado. Iniciando um novo arquivo.")

    def receitas_decimas(self, coleta, subscricoes_beneficios, doacoes, eventos, outras_fontes):
        self.coleta = coleta
        self.subscricoes_beneficios = subscricoes_beneficios
        self.doacoes = doacoes
        self.eventos = eventos
        self.outras_fontes = outras_fontes
        self.entradas_decima = {
            "coleta": coleta,
            "subscricoes_beneficios": subscricoes_beneficios,
            "doacoes": doacoes,
            "eventos": eventos,
            "outras_fontes": outras_fontes,
        }
        self.serialized_decimas = json.dumps(self.entradas_decima)  # Serialização
        self.subtotal1 = sum(self.entradas_decima.values())
        self.serialized_subtotal1 = json.dumps({"subtotal1": self.subtotal1})  # Serialização
        return self.subtotal1

    def receitas_semdecimas(self, subvencao_oficial, ozanam_solidariedade, uniao_fraternal, contri_cc, contri_cmb):
        self.subvencao_oficial = subvencao_oficial
        self.ozanam_solidariedade = ozanam_solidariedade
        self.uniao_fraternal = uniao_fraternal
        self.contri_cc = contri_cc
        self.contri_cmb = contri_cmb
        self.entradas_semdecimas = {
            "subvencao_oficial": subvencao_oficial,
            "ozanam_solidariedade": ozanam_solidariedade,
            "uniao_fraternal": uniao_fraternal,
            "contri_cc": contri_cc,
            "contri_cmb": contri_cmb,
        }
        self.serialized_semdecimas = json.dumps(self.entradas_semdecimas)  # Serialização
        self.subtotal2 = sum(self.entradas_semdecimas.values())
        self.serialized_subtotal2 = json.dumps({"subtotal2": self.subtotal2})  # Serialização
        return self.subtotal2

    def movimento_receitas(self):
        self.total_receitas = self.anterior + self.subtotal1 + self.subtotal2
        self.serialized_total_receitas = json.dumps({"total_receitas": self.total_receitas})  # Serialização
        return self.total_receitas

    def despesas(self, cesta_basica, moradia, contas_assistidos, despesas_oe, repasse_uniao, despesas_adm):
        self.cesta_basica = cesta_basica
        self.moradia = moradia
        self.contas_assistidos = contas_assistidos
        self.despesas_oe = despesas_oe
        self.repasse_uniao = repasse_uniao
        self.despesas_adm = despesas_adm
        self.decima_cp = round(self.subtotal1 * 0.1, 2)
        self.entradas_despesas = {
            "cesta_basica": cesta_basica,
            "moradia": moradia,
            "contas_assistidos": contas_assistidos,
            "despesas_oe": despesas_oe,
            "repasse_uniao": repasse_uniao,
            "despesas_adm": despesas_adm,
        }
        self.serialized_despesas = json.dumps(self.entradas_despesas)  # Serialização
        self.subtotal3 = sum(self.entradas_despesas.values())
        self.serialized_subtotal3 = json.dumps({"subtotal3": self.subtotal3})  # Serialização
        return self.subtotal3

    def repasses(self, ozanam_solidariedade, contri_cc, contri_cmb):
        self.rep_ozanam_solidariedade = ozanam_solidariedade
        self.rep_contri_cc = contri_cc
        self.rep_contri_cmb = contri_cmb
        self.entradas_repasses = {
            "ozanam_solidariedade": ozanam_solidariedade,
            "contri_cc": contri_cc,
            "contri_cmb": contri_cmb,
        }
        self.serialized_repasses = json.dumps(self.entradas_repasses)  # Serialização
        self.subtotal4 = sum(self.entradas_repasses.values())
        self.serialized_subtotal4 = json.dumps({"subtotal4": self.subtotal4})  # Serialização
        return self.subtotal4

    def total_pagamentos(self):
        self.total_pag = self.subtotal3 + self.subtotal4
        self.serialized_total_pag = json.dumps({"total_pag": self.total_pag})  # Serialização
        return self.total_pag

    def saldo_a_transp(self):
        self.saldo_transp = self.total_receitas - self.total_pag
        self.serialized_saldo_transp = json.dumps({"saldo_transp": self.saldo_transp})  # Serialização
        return self.saldo_transp

    def movimento_des(self):
        self.movimento_des = self.total_pag + self.saldo_transp
        self.serialized_movimento_des = json.dumps({"movimento_des": self.movimento_des})  # Serialização
        return self.serialized_movimento_des

    def carregar_dados(self, arquivo="caixa.json"):
    
      if os.path.exists(arquivo):
          with open(arquivo, "r", encoding="utf-8") as file:
              self.dados_mensais = json.load(file)
          print("Dados do caixa carregados com sucesso!")
      else:
          print("Nenhum dado de caixa encontrado. Será iniciado um novo arquivo.")
      #coleta,subsc_e_Ben, doacoes, eventos, outras_fontes, subvencao_oficial, ozanam_solidariedade, uniao_fraternal, contri_cc, contri_cmb
    def receitas(self):
      while True:
        anterior = (input("Digite o valor do Saldo do Mês anterior: "))
        try:
          anterior = float(anterior)
          break
        except ValueError:
          print("Valor inválido. Por favor, digite um número.")
      while True:
        coleta = (input("Digite o valor da coleta: "))
        try:
          coleta = float(coleta)
          break
        except ValueError:
          print("Valor inválido. Por favor, digite um número.")
      while True:
        subsc_e_Ben = (input("Digite o valor da receita de Subscritores e Benfeitores: "))
        try:
          subsc_e_Ben = float(subsc_e_Ben)
          break
        except ValueError:
          print("Valor inválido. Por favor, digite um número.")
      while True:
        doacoes = (input("Digite o valor das doações: "))
        try:
          doacoes = float(doacoes)
          break
        except ValueError:
          print("Valor inválido. Por favor, digite um número.")
      while True:
        eventos = (input("Digite o valor dos eventos: "))
        try:
          eventos = float(eventos)
          break
        except ValueError:
          print("Valor inválido. Por favor, digite um número.")
      while True:
        outras_fontes = (input("Digite o valor das Outras Fontes de Receita: "))
        try:
          outras_fontes = float(outras_fontes)
          break
        except ValueError:
          print("Valor inválido. Por favor, digite um número.")
      while True:
        subvencao_oficial = (input("Digite o valor da Subvenção Oficial: "))
        try:
          subvencao_oficial = float(subvencao_oficial)
          break
        except ValueError:
          print("Valor inválido. Por favor, digite um número.")
      while True:
        ozanam_solidariedade = (input("Digite o valor da Coleta de Ozanam ou da Contribuição da Solidariedade: "))
        try:
          ozanam_solidariedade = float(ozanam_solidariedade)
          break
        except ValueError:
          print("Valor inválido. Por favor, digite um número.")
      while True:
        uniao_fraternal = (input("Digite o valor da União Fraternal: "))
        try:
          uniao_fraternal = float(uniao_fraternal)
          break
        except ValueError:
          print("Valor inválido. Por favor, digite um número.")
      while True:
        contri_cc = (input("Digite o valor da Contribuição ao CC: "))
        try:
          contri_cc = float(contri_cc)
          break
        except ValueError:
          print("Valor inválido. Por favor, digite um número.")
      while True:
        contri_cmb = (input("Digite o valor da Contribuição ao CMB: "))
        try:
          contri_cmb = float(contri_cmb)
          break
        except ValueError:
          print("Valor inválido. Por favor, digite um número.")
      instancia_caixa = Caixa(self.mes)
      receitas_decimas = instancia_caixa.receitas_decimas(coleta, subsc_e_Ben, doacoes, eventos, outras_fontes)
      receitas_semdecimas = instancia_caixa.receitas_semdecimas(subvencao_oficial, ozanam_solidariedade, uniao_fraternal, contri_cc, contri_cmb)
      instancia_caixa.movimento_receitas()
      return {
        "coleta": coleta,
        "subscritores_bemfeitores": subsc_e_Ben,
        "doacoes": doacoes,
        "eventos": eventos,
        "outras_fontes": outras_fontes,
        "subvencao_oficial": subvencao_oficial,
        "ozanam_solidariedade": ozanam_solidariedade,
        "uniao_fraternal": uniao_fraternal,
        "contri_cc": contri_cc,
        "contri_cmb": contri_cmb,
    }


    def pagamentos(self):

      while True:
          cesta_basica = input("Digite o valor gasto com Cesta Básica: ")
          try:
              cesta_basica = float(cesta_basica)
              break
          except ValueError:
              print("Valor inválido. Por favor, digite um número.")

      while True:
          moradia = input("Digite o valor gasto com Moradia: ")
          try:
              moradia = float(moradia)
              break
          except ValueError:
              print("Valor inválido. Por favor, digite um número.")

      while True:
          contas_assistidos = input("Digite o valor gasto com Contas dos Assistidos: ")
          try:
              contas_assistidos = float(contas_assistidos)
              break
          except ValueError:
              print("Valor inválido. Por favor, digite um número.")

      while True:
          despesas_oe = input("Digite o valor das Despesas OE: ")
          try:
              despesas_oe = float(despesas_oe)
              break
          except ValueError:
              print("Valor inválido. Por favor, digite um número.")

      while True:
          repasse_uniao = input("Digite o valor do Repasse União Fraternal: ")
          try:
              repasse_uniao = float(repasse_uniao)
              break
          except ValueError:
              print("Valor inválido. Por favor, digite um número.")

      while True:
          despesas_adm = input("Digite o valor das Despesas Administrativas: ")
          try:
              despesas_adm = float(despesas_adm)
              break
          except ValueError:
              print("Valor inválido. Por favor, digite um número.")

      # Calcular despesas
            #print(f"Subtotal de despesas: {despesas}")

      # Capturar entradas para repasses
      while True:
          ozanam_solidariedade = input("Digite o valor do Repasse da Coleta de Ozanam ou da Contribuição da Solidariedade: ")
          try:
              ozanam_solidariedade = float(ozanam_solidariedade)
              break
          except ValueError:
              print("Valor inválido. Por favor, digite um número.")

      while True:
          contri_cc = input("Digite o valor da Contribuição ao CC: ")
          try:
              contri_cc = float(contri_cc)
              break
          except ValueError:
              print("Valor inválido. Por favor, digite um número.")

      while True:
          contri_cmb = input("Digite o valor da Contribuição ao CMB: ")
          try:
              contri_cmb = float(contri_cmb)
              break
          except ValueError:
              print("Valor inválido. Por favor, digite um número.")
      instancia_caixa = Caixa(self.mes)
      despesas = instancia_caixa.despesas(cesta_basica, moradia, contas_assistidos, despesas_oe, repasse_uniao, despesas_adm)
      repasses = instancia_caixa.repasses(ozanam_solidariedade, contri_cc, contri_cmb)
      return {
          "cesta_basica": cesta_basica,
          "moradia": moradia,
          "contas_assistidos": contas_assistidos,
          "despesas_oe": despesas_oe,
          "repasse_uniao": repasse_uniao,
          "despesas_adm": despesas_adm,
          "ozanam_solidariedade": ozanam_solidariedade,
          "contri_cc": contri_cc,
          "contri_cmb": contri_cmb,
      }