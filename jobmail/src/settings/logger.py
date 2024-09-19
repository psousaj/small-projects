import logging
from pathlib import Path
import os


def setup_logger(name: str = __name__) -> logging.Logger:
    log_file_path = os.path.join(os.path.abspath(Path().parent), "app.log")

    # Configuração básica do logger
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file_path),  # Arquivo de log
            logging.StreamHandler(),  # Console
        ],
    )

    # Ajustar o nível de log do httpx
    logging.getLogger("httpx").setLevel(
        logging.ERROR
    )  # Ou logging.ERROR para ainda menos logs

    return logging.getLogger(name)


# Instancie o logger ao carregar o módulo
logger = setup_logger()
