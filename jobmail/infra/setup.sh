#!/bin/bash

set -e  # Termina o script ao encontrar um erro

# Argumentos para o domínio e chave da Mailgun
MAILGUN_DOMAIN=${MAILGUN_DOMAIN:-"seu_dominio"}
MAILGUN_API_KEY=${MAILGUN_API_KEY:-"sua_chave"}


# Atualiza o sistema e instala as dependências
echo "Atualizando o sistema e instalando dependências..."
sudo apt-get update && sudo apt-get install -y \
    curl \
    python3 \
    python3-pip \
    libpq-dev \
    locales

# Configura as localizações
echo "Configurando localizações..."
sudo locale-gen pt_BR.UTF-8
export LANG=pt_BR.UTF-8
export LANGUAGE=pt_BR:pt
export LC_ALL=pt_BR.UTF-8

# Cria o diretório para o Poetry
echo "Criando diretório para o Poetry..."
sudo mkdir -p /usr/src/poetry


# Adiciona o Poetry ao PATH
export POETRY_HOME="/usr/src/poetry"
export PATH="${POETRY_HOME}/bin:${PATH}"

# Instala o Poetry
echo "Instalando o Poetry..."
curl -sSL https://install.python-poetry.org | POETRY_HOME=$POETRY_HOME python3 -

echo "Atualizando permissões do poetry"
sudo chown $USER:$USER /usr/src/poetry  # Ajusta permissões para o diretório
sudo chmod -R 777 /usr/src/poetry

# Cria o diretório de trabalho
echo "Criando diretório de trabalho..."
WORK_DIR="/usr/src/jobmail"
[ -f $WORK_DIR ] && sudo rm -rf $WORK_DIR
sudo mkdir -p $WORK_DIR
sudo mkdir -p $WORK_DIR/src  # Cria o diretório src

# Copia os arquivos necessários
echo "Copiando arquivos..."
sudo cp -r $PWD/pyproject.toml $WORK_DIR
sudo cp -r $PWD/src/* $WORK_DIR/src/
sudo cp -r $PWD/.[!.]* $WORK_DIR/  # Copia arquivos ocultos, excluindo ..

# Ajusta as permissões dos arquivos
sudo chown -R $USER:$USER $WORK_DIR  # Muda a propriedade do diretório
sudo chmod -R 755 $WORK_DIR

# Torna o arquivo app.py executável
echo "Tornando o app.py executável..."
sudo chmod +x $WORK_DIR/src/app.py

# Instala as dependências do projeto usando o Poetry
echo "Instalando dependências do projeto..."
cd $WORK_DIR
# poetry export -f requirements.txt -o requirements.txt --without-hashes
# pip install -r requirements.txt
poetry install --no-root
