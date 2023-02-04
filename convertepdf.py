import tabula
import pandas as pd

# Lê o PDF usando a biblioteca tabula
dfs = tabula.read_pdf("PDF/ResultadoVale.pdf", pages="all")

# Loop para cada dataframe na lista
for i, df in enumerate(dfs):
    # Salva o dataframe em um arquivo Excel
    df.to_excel("Excel/tabela_extraída_" + str(i) + ".xlsx", index=False)