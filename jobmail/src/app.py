import locale
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from settings.db_utils import connect, create_tables, get_recipients
from lib.data_processing import load_and_clean_data
from lib.email_utils import send_grouped_data_jobs
from lib.download_spreadsheets import get_all_spredsheets


def run_task():
    load_dotenv()
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

    db = connect()
    create_tables(db)
    recipients = get_recipients(db)
    recipients_list = [recipient for recipient, name in recipients.items()]

    spreadsheet_data_and_infos = get_all_spredsheets()
    df = load_and_clean_data(spreadsheet_data_and_infos)

    send_grouped_data_jobs(df, recipients_list)


# Configurar o agendador
scheduler = BackgroundScheduler()
# Agendar para executar de segunda a sexta-feira às 12:00
scheduler.add_job(run_task, CronTrigger(hour=12, minute=0, day_of_week="mon-fri"))
scheduler.start()

if __name__ == "__main__":
    run_task()
    # Mantém o script em execução
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
