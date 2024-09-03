from dotenv import load_dotenv
import os

load_dotenv()

XLSX_FILE = "files/vagas.xlsx"
XLSX_ORIGIN_URL = "https://docs.google.com/spreadsheets/d/1fLFZpjJbqFpur1ak4uvBGDQAPlXK3ZD9k7O1ji8YAW8/export?format=xlsx&gid=1199615731"
# XLSX_ORIGIN_URL = "https://doc-10-0g-sheets.googleusercontent.com/export/54bogvaave6cua4cdnls17ksc4/8cr0s8qf3hmnbcikkdlev0btik/1723688360000/112525517457232303984/*/1fLFZpjJbqFpur1ak4uvBGDQAPlXK3ZD9k7O1ji8YAW8?format=xlsx&amp;gid=1199615731/"
MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN')
MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
MAILGUN_API_URL = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"