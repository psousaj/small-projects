#!/usr/bin/env python3

import locale
import time
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from settings.db_utils import connect, create_tables, get_recipients
from settings.logger import logger
from lib.data_processing import load_and_clean_data
from lib.email_utils import send_grouped_data_jobs
from lib.download_spreadsheets import get_all_spredsheets


def run_task():
    load_dotenv()
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

    logger.info("Verificando novas vagas agora")

    # db = connect()
    # create_tables(db)
    # recipients = get_recipients(db)
    # recipients_list = [recipient for recipient, name in recipients.items()]
    recipients_list = ["josepsousa2012@gmail.com", "arq.lucas2003@gmail.com"]

    logger.info("Início do download das planilhas")

    spreadsheet_data_and_infos = get_all_spredsheets()

    logger.info("Executando filtro e limpeza nas vagas")

    df = load_and_clean_data(spreadsheet_data_and_infos)

    logger.info("Enviando vagas para destinatários")

    send_grouped_data_jobs(df, recipients_list)

    logger.info("Aguardando nova execução")


scheduler = BackgroundScheduler()
# Agendar para executar de segunda a sexta-feira às 12:00
scheduler.add_job(run_task, CronTrigger(hour=12, minute=0, day_of_week="mon-fri"))
scheduler.start()

if __name__ == "__main__":
    logger.info("App iniciado")
    run_task()
    logger.info("Agendamento de Seg à Sex ao meio dia iniciado!")
    # Mantém o script em execução
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
