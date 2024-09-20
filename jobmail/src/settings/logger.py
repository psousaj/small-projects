import logging
import os
from pathlib import Path


class Logger:
    def __init__(self, name: str = None):
        if name is None:
            # Atribui o nome baseado no módulo que importar essa classe
            name = __name__

        # Caminho para o arquivo de log
        log_file_path = os.path.join(os.path.abspath(Path().parent), "app.log")

        # Configurações de logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s -%(levelname)s- %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S",  # DD-MM-YYYY HH:MM:SS
            handlers=[
                logging.FileHandler(log_file_path),
                logging.StreamHandler(),
            ],
        )

        # Reduz o nível de log de bibliotecas específicas
        logging.getLogger("httpx").setLevel(logging.ERROR)

        # Cria o logger com o nome apropriado
        self.logger = logging.getLogger(name)

    def get_logger(self):
        return self.logger


# Cria uma instância global do logger
logger = Logger().get_logger()
