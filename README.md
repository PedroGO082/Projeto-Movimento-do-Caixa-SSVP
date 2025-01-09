# Projeto-Movimento-do-Caixa-SSVP

# Sistema de Gestão SSVP

## Descrição
Este é um sistema de gestão desenvolvido para apoiar as atividades da Sociedade de São Vicente de Paulo (SSVP), facilitando o gerenciamento de membros, assistidos e finanças de uma conferência. A aplicação é baseada em Python e utiliza persistência de dados em arquivos JSON para manter o histórico das operações.

---

## Funcionalidades

- **Gerenciamento de Membros:**
  - Cadastro de Confrades e Consócias.
  - Organização por status (ativo/inativo).
  - Consulta e exportação de dados.

- **Gerenciamento de Assistidos:**
  - Cadastro de assistidos com informações detalhadas.
  - Registro do número de membros assistidos.

- **Controle Financeiro (Caixa):**
  - Registro de receitas e despesas mensais.
  - Cálculo automático de saldo e repasses.
  - Armazenamento de movimentações financeiras por mês.

- **Relatórios:**
  - Relatórios detalhados de membros e assistidos.
  - Relatórios financeiros por mês, incluindo receitas, despesas e saldo final.

- **Persistência de Dados:**
  - Dados de membros, assistidos e movimentações financeiras são salvos automaticamente em arquivos JSON.

---

## Tipos de Dados Aceitos pelo Programa

### **Membros**
| Campo              | Tipo      | Formato ou Valores Aceitos                                                         |
|--------------------|-----------|------------------------------------------------------------------------------------|
| `nome`             | `str`     | Texto livre                                                                        |
| `sexo`             | `str`     | `"M"` para masculino ou `"F"` para feminino                                        |
| `data_nascimento`  | `str`     | `dd/mm/aaaa`                                                                       |
| `proclamacao`      | `str`     | `dd/mm/aaaa`                                                                       |
| `endereco`         | `str`     | Texto livre                                                                        |
| `encargo`          | `str`     | `"Presidente"`, `"Secretária(o)"`, `"Tesoureiro"`, `"Confrade"`, `"Consócia"`, etc.|
| `ativo`            | `str`     | `"ativo"` ou `"inativo"`                                                           |

### **Assistidos**
| Campo                 | Tipo      | Formato ou Valores Aceitos                                                      |
|--------------------   |-----------|---------------------------------------------------------------------------------|
| `nome`                | `str`     | Texto livre                                                                     |
| `sexo`                | `str`     | `"M"` para masculino ou `"F"` para feminino                                                                           |
| `data_nascimento`     | `str`     | `dd/mm/aaaa`                                                                    |
| `endereco`            | `str`     | Texto livre                                                                     |
| `membros_assistidos`  | `int`     | Número inteiro                                                                  |
| `ativo`               | `str`     | `"ativo"` ou `"inativo"`                                                        |

### **Caixa (Receitas e Despesas)**
 --> Todos os dados financeiros são numéros reais, atribuidos a variáveis do tipo float.

## Pré-requisitos

- Python 3.8 ou superior.
- Bibliotecas nativas do Python:
  - `os`
  - `json`

---

## Como Executar

1. **Clone o Repositório:**
   ```bash
   
   git clone https://github.com/seu-usuario/sistema-ssvp.git
   
   cd sistema-ssvp
   
2. **Execute o Sistema:**
   ```bash

      python main.py






##Estrutura do Projeto

**sistema-ssvp/**
                ├── models/
                
                │   ├── cadastro.py          # Classes relacionadas a membros e assistidos
                
                │   ├── conferencia.py       # Classe da conferência
                
                │   ├── movimento_mensal.py  # Controle financeiro (Caixa)
                
                ├── main.py                  # Arquivo principal do sistema
                
                ├── data.json                # Dados persistidos (membros e assistidos)
                
                ├── caixa.json               # Dados persistidos (movimentações financeiras)
                
                ├── README.md                # Documentação do projeto
                
# Casos de Uso
Gerenciamento de Membros
Cadastro de membros da conferência (Confrades e Consócias).
Consulta de membros por tipo (ativo/inativo).
Gerenciamento de Assistidos
Registro de famílias assistidas, com número de membros e status.
Controle de Caixa
Registro de receitas e despesas mensais.
Cálculo de saldo final e movimentações financeiras.
Relatórios
Visualização de dados financeiros por mês.
Relatórios de membros e assistidos.


# Contato
Desenvolvedor: Pedro Gomes Oliveira
GitHub: https://github.com/PedroGO082
