import locale
import os
import pandas as pd
import httpx
from dotenv import load_dotenv

from consts import MAILGUN_API_KEY, MAILGUN_API_URL, MAILGUN_DOMAIN
from download import get_spredsheet

# Função para enviar e-mail usando a API do Mailgun
def send_email(subject, body, recipient):
    response = httpx.post(
        MAILGUN_API_URL,
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": f"vagasremotas@{MAILGUN_DOMAIN}",
            "to": recipient,
            "subject": subject,
            "html": body,
        },
    )
    if response.status_code == 200:
        print(f"Email enviado para {recipient}")
    else:
        print(f"Falha ao enviar e-mail para {recipient}: {response.status_code} - {response.text}")

# Carregar e limpar a planilha
def load_and_clean_data(filepath):
    df = pd.read_excel(filepath, skiprows=1)
    df.columns = ["Vaga", "Tipo", "Cidade", "Uf", "Empresa", "Link", "Data"]
    df = df.drop(index=[0, 1]).reset_index(drop=True)
    df = df[df[["Cidade", "Uf"]].isna().any(axis=1)]
    df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
    df = df[df["Data"].notna()]
    df = df[(df["Tipo"] != "QA") & (df["Vaga"] != "QA")]
    return df.sort_values(by="Data", ascending=False)

# Função para enviar vagas agrupadas por data
def send_grouped_data_jobs(df: pd.DataFrame, recipient: list[str]):
    email_body = """
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; }
            table { width: 100%; border-collapse: collapse; margin: 20px 0; }
            th, td { padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }
            th { background-color: #f4f4f4; }
            h2 { color: #333; }
            .container { max-width: 800px; margin: auto; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Vagas Disponíveis Agrupadas por Data</h1>
            <p>Confira abaixo as vagas disponíveis organizadas por data:</p>
    """

    grouped = df.groupby(df['Data'].dt.date)
    for date, group in sorted(grouped, key=lambda x: x[0], reverse=True):
        email_body += f"<h2>Vagas disponíveis em {date.strftime('%d/%m/%Y')}</h2>"
        email_body += "<table><tr><th>Vaga</th><th>Tipo</th><th>Empresa</th><th>Link</th><th>Data</th></tr>"
        for _, row in group.iterrows():
            email_body += (f"<tr>"
                           f"<td>{row['Vaga']}</td>"
                           f"<td>{row['Tipo']}</td>"
                           f"<td>{row['Empresa']}</td>"
                           f"<td><a href='{row['Link']}'>{row['Link']}</a></td>"
                           f"<td>{row['Data'].strftime('%d/%m/%Y')}</td>"
                           f"</tr>")
        email_body += "</table>"
    
    email_body += "</div></body></html>"

    send_email("Vagas Disponíveis por Data", email_body, recipient)

if __name__ == "__main__":
    load_dotenv()
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    #
    get_spredsheet()
    #
    df = load_and_clean_data("files/vagas.xlsx")
    send_grouped_data_jobs(df, ["josepsousa2012@gmail.com", "arq.lucas2003@gmail.com"])
