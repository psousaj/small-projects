import logging

def use(name: str = __name__) -> logging.Logger:
    # Configuração básica do logger
    logging.basicConfig(
        level=logging.INFO,  # Define o nível mínimo de severidade que será registrado
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Formato da mensagem de log
        handlers=[
            logging.FileHandler("app.log"),  # Registrar em um arquivo chamado app.log
            logging.StreamHandler()  # Registrar no console (stdout)
        ]
    )

    # Retorna uma instância do logger com o nome do módulo
    return logging.getLogger(name)
