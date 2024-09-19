FROM ubuntu:22.04

# Argumentos para o domínio e chave da Mailgun
ARG MAILGUN_DOMAIN
ARG MAILGUN_API_KEY

# Variáveis de ambiente para o Poetry
ENV POETRY_HOME="/usr/src/poetry"
ENV PATH="${POETRY_HOME}/bin:${PATH}"

# Atualiza o sistema e instala as dependências
RUN apt-get update && apt-get install -y \
    curl \
    python3 \
    python3-pip \
    libpq-dev \
    locales

RUN locale-gen pt_BR.UTF-8
ENV LANG=pt_BR.UTF-8
ENV LANGUAGE=pt_BR:pt
ENV LC_ALL=pt_BR.UTF-8

# Instala o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Define o diretório de trabalho
WORKDIR /usr/src/app/src

# Copia os arquivos necessários para o contêiner
COPY pyproject.toml .
COPY . .

# Instala as dependências do projeto usando o Poetry
RUN poetry install --no-root

ENV PYTHONPATH="/usr/src/app/src"

# Define o comando padrão para iniciar a aplicação
CMD ["poetry", "run", "python", "app.py"]
