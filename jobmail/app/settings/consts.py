import os
import enum
from dotenv import load_dotenv

from helpers.filter_spreadsheet import filter_planilha1, filter_planilha2

load_dotenv()


class finalColumnsEnum(enum.Enum):
    ORIGEM = "Origem"
    EMPRESA = "Empresa"
    DATA = "Data"
    VAGA = "Vaga"
    LINK = "Link"
    LOCALIDADE = "Localidade"


FINAL_COLUMNS = [
    finalColumnsEnum.EMPRESA.value,
    finalColumnsEnum.DATA.value,
    finalColumnsEnum.VAGA.value,
    finalColumnsEnum.LINK.value,
    finalColumnsEnum.LOCALIDADE.value,
    finalColumnsEnum.ORIGEM.value,
]


XLSX_ORIGIN_INFO = {
    "jornada_tech": {
        "link": "https://docs.google.com/spreadsheets/d/1fLFZpjJbqFpur1ak4uvBGDQAPlXK3ZD9k7O1ji8YAW8/export?format=xlsx&gid=1199615731",
        "bytes": None,
        "columns": [
            finalColumnsEnum.VAGA.value,
            "Tipo",
            finalColumnsEnum.LOCALIDADE.value,
            "Uf",
            finalColumnsEnum.EMPRESA.value,
            finalColumnsEnum.LINK.value,
            finalColumnsEnum.DATA.value,
        ],
        "skiprows": 1,
        "filter_function": filter_planilha1,
    },
    "remotinho_dos_sonhos": {
        "link": "https://docs.google.com/spreadsheets/d/1dfr964jwUw4GcjQACKaRpCnXM4uKbChskQ8vwjap9wk/export?format=xlsx&gid=0",
        "columns": [
            finalColumnsEnum.EMPRESA.value,
            finalColumnsEnum.DATA.value,
            finalColumnsEnum.VAGA.value,
            finalColumnsEnum.LINK.value,
            finalColumnsEnum.LOCALIDADE.value,
        ],
        "skiprows": 4,
        "filter_function": filter_planilha2,
    },
}
MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAIN", os.getenv("MAILGUN_DOMAIN"))
MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY", os.getenv("MAILGUN_API_KEY"))
MAILGUN_API_URL = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"

DATABASE_NAME = os.environ.get("DATABASE_NAME", os.getenv("DATABASE_NAME"))
DATABASE_HOST = os.environ.get("DATABASE_HOST", os.getenv("DATABASE_HOST"))
DATABASE_PORT = os.environ.get("DATABASE_PORT", os.getenv("DATABASE_PORT"))
DATABASE_USER = os.environ.get("DATABASE_USER", os.getenv("DATABASE_USER"))
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", os.getenv("DATABASE_PASSWORD"))
