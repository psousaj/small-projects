import psycopg2

from settings.consts import (
    DATABASE_HOST,
    DATABASE_NAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_USER,
)


def connect():
    # Conectar ao banco de dados
    conn = psycopg2.connect(
        dbname=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
    )

    return conn


def add_default_users(connection):
    # Criar um cursor a partir da conexão
    cur = connection.cursor()

    # Comando SQL para inserir usuários padrão com verificação de unicidade
    insert_query = """
    INSERT INTO recipients (recipient, name)
    VALUES (%s, %s)
    ON CONFLICT (recipient) DO NOTHING;
    """

    users = [
        ("josepsousa2012@gmail.com", "José Pinheiro"),
        ("arq.lucas2003@gmail.com", "Lucas Antonio"),
    ]

    for user in users:
        cur.execute(insert_query, user)

    connection.commit()


def create_tables(conn, should_close_connection=False):
    create_recipients_table = """
    CREATE TABLE IF NOT EXISTS recipients (
        id SERIAL PRIMARY KEY,
        recipient VARCHAR(255) UNIQUE NOT NULL,
        name VARCHAR(255) NOT NULL
    );
    """

    create_envios_table = """
    CREATE TABLE IF NOT EXISTS envios (
        id SERIAL PRIMARY KEY,
        data_de_envio TIMESTAMP NOT NULL
    );
    """

    cur = conn.cursor()

    cur.execute(create_recipients_table)
    cur.execute(create_envios_table)

    add_default_users(conn)

    conn.commit()

    if should_close_connection:
        cur.close()
        conn.close()


def get_recipients(conn, should_close_connection=True):
    select_recipients_query = """
    SELECT id, recipient, name
    FROM recipients;
    """

    cur = conn.cursor()

    cur.execute(select_recipients_query)

    rows = cur.fetchall()

    recipients_dict = {row[0]: {"recipient": row[1], "name": row[2]} for row in rows}

    if should_close_connection:
        cur.close()
        conn.close()

    return recipients_dict


def get_envios(conn, should_close_connection=False):
    select_envios_query = """
    SELECT id, data_de_envio
    FROM envios;
    """

    cur = con.cursor()

    cur.execute(select_envios_query)

    rows = cur.fetchall()

    recipients_dict = {row[0]: {"data": row[1]} for row in rows}

    if should_close_connection:
        cur.close()
        conn.close()

    return recipients_dict
