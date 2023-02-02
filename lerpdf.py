import PyPDF2
import re


pdf_file = open('arquivo.pdf', 'rb')

read_pdf = PyPDF2.PdfFileReader(pdf_file)

#Lendo a primeira página
página = read_pdf.getPage(0)

#extraindo o texto da página
dados_da_página = página.extractText()

# fazendo a junção das linhas 
verificar_dados = ''.join(dados_da_página)

# remove quebra de linha
verificar_dados = re.sub('n', '', verificar_dados)
print(verificar_dados)

print("10 primeiras linhas")
análise = verificar_dados[0:10]
print(análise)

