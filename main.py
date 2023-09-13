# Importação das bibliotecas necessárias
import pandas as pd  # Para manipulação de dados em formato tabular
import datetime  # Para trabalhar com datas e horários
from lista_livro import lista_livros  # Importação da lista de livros
from reportlab.lib.pagesizes import letter  # Tamanho da página para o PDF
from reportlab.pdfgen import canvas  # Para criar o arquivo PDF
import os # Para verificar se existe PDF e Excel existente


# Função para adicionar um livro à lista de livros
def adicionar_livro(nome, editora=None):
    if editora is None or editora.strip() == "":
        editora = 'desconhecida'  # Define 'desconhecida' como editora padrão se não for fornecida ou se for uma string vazia

    livro = {
        'Nome': nome.lower(),  # Converte o nome para minúsculas
        'Editora': editora,
    }

    lista_livros.append(livro)  # Adiciona o livro à lista


#Função para retirar livro
def escolher_livro(nome):
    nome = nome.lower()  # Converte o nome fornecido para minúsculas
    for livro in lista_livros:
        if livro['Nome'] == nome:
            lista_livros.remove(livro)
            print(f"O livro '{nome}' foi removido da biblioteca com sucesso às {datetime.datetime.now()}.")
            return
    print(f"Não temos o livro '{nome}' na biblioteca!")

# Função para criar um arquivo Excel com a lista de livros
def criar_arquivo_excel():
    num = 1
    while True:
        arquivo_excel = f'biblioteca{num}.xlsx'  # Define o nome do arquivo Excel com número incrementado
        if not os.path.exists(arquivo_excel):
            break  # O arquivo não existe, podemos usá-lo
        num += 1

    df = pd.DataFrame(lista_livros)  # Cria um DataFrame a partir da lista de livros

    df.to_excel(arquivo_excel, index=False)  # Salva o DataFrame como um arquivo Excel

# Função para criar um arquivo PDF com a lista de livros
def criar_pdf_lista_livros():
    # Verifique se o arquivo PDF já existe
    num = 1
    while True:
        arquivo_pdf = f'lista_livros_{num}.pdf'  # Nome do arquivo PDF com número incrementado
        if not os.path.exists(arquivo_pdf):
            break  # O arquivo não existe, podemos usá-lo
        num += 1

    df = pd.DataFrame(lista_livros)  # Cria um DataFrame a partir da lista de livros

    c = canvas.Canvas(arquivo_pdf, pagesize=letter)  # Cria um objeto canvas para o PDF

    # Configurações de fonte e tamanho
    c.setFont("Helvetica", 12)

    # Título
    c.drawString(100, 750, "Lista de Livros")

    # Cabeçalhos da tabela
    c.drawString(100, 720, "Nome")
    c.drawString(300, 720, "Editora")

    y = 700
    for _, row in df.iterrows():
        nome = row['Nome']
        editora = row['Editora']
        y -= 20
        c.drawString(100, y, nome)
        c.drawString(300, y, editora)

    c.save()  # Salva o arquivo PDF

# Mensagem de boas-vindas
print("-" * 40)
print("Seja bem-vindo à Biblioteca Nacional!")

while True:
    # Menu interativo
    print("\nEscolha uma opção:\n"
          "1 - Escolher um livro\n"
          "2 - Verificar a quantidade de livros na biblioteca\n"
          "3 - Adicionar um livro\n"
          "4 - Lista no excel\n"
          "5 - Lista em pdf\n"
          "6 - sair")

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        nome = input("Nome do livro: ")
        escolher_livro(nome)

    elif opcao == 2:
        nome_a_contar = input("Nome do livro: ").lower()  # Converte o nome fornecido para minúsculas
        contagem = sum(1 for livro in lista_livros if livro['Nome'] == nome_a_contar)
        print(f"O livro '{nome_a_contar}' ocorre {contagem} vezes na biblioteca.")

    elif opcao == 3:
        nome = input("Nome do livro: ")
        editora = input("Editora: ")
        adicionar_livro(nome, editora)

    elif opcao == 4:
        criar_arquivo_excel()

    elif opcao == 5:
        criar_pdf_lista_livros()

    elif opcao == 6:
        break  # Encerra o loop e sai do programa quando o usuário escolhe '6 - sair'


