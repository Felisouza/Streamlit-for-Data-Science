import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def lePlanilha():

    # Configurar autenticação
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(".\ControleFinanceiro\TratamentoDados\credentials.json", scope)

    cliente = gspread.authorize(creds)


    # Abrir a planilha pelo ID
    SHEET_ID = "1zgDfVIVOfTDHKvxuOM8eHzQy0keTlKR3EbNabgtuA54"
    planilha = cliente.open_by_key(SHEET_ID)

    # Obter todas as abas (worksheets)
    abas = planilha.worksheets()

    # Compartilhar com seu e-mail (substitua pelo seu Gmail!)
    planilha.share("felisouza1991@gmail.com", perm_type="user", role="writer")

    # Ler os dados e converter para Pandas DataFrame
    sheet = planilha.worksheet("Sheet1")
    dados = sheet.get_all_records()
    df = pd.DataFrame(dados)

    # print(df)
    return sheet

def lePlanilhaCSV():
    df = pd.read_csv(r'./ControleFinanceiro/Debito/data.txt', sep=';')
    return df