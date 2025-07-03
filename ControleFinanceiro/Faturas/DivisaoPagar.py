# Libs
import pandas as pd
# Leitura dos dados

df = pd.read_excel(r'C:\Users\feh_s\Downloads\Faturas\Fatura-Excel.xls', engine='xlrd', sheet_name='Planilha2')

#Dados filtrados
df_filtrado = df.loc[~df['Tipo'].isnull()]

# Total a pagar
total_pagar = df_filtrado['valor'].sum()

# Calcular a soma da categoria 'Divide'
soma_divide = df_filtrado.loc[df_filtrado['Tipo'] == 'Divide']['valor'].sum()

# Dividir o valor de 'Divide' igualmente entre os dois
valor_dividido = soma_divide / 2

# Adicionar o valor dividido a cada categoria original
total_felipe = df_filtrado.loc[df_filtrado['Tipo'] == 'Felipe']['valor'].sum() + valor_dividido
total_lina = df_filtrado.loc[df_filtrado['Tipo'] == 'Lina']['valor'].sum() + valor_dividido

# Exibir o resultado
print(
    f"Total Felipe: {total_felipe} \n"
    f"Total Lina: {total_lina} \n"
    f"Total a pagar: {total_pagar}"
)
