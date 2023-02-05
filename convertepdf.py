import tabula
import pandas as pd

# Leitura das tabelas do PDF usando a biblioteca tabula
dfs = tabula.read_pdf("PDF/Seu_PDF-Aqui", pages="all")

# Loop para cada dataframe na lista
for i, df in enumerate(dfs):
    # Salva o dataframe em um arquivo Excel
    df.to_excel("Excel/tabela_extraída_" + str(i) + ".xlsx", index=False)