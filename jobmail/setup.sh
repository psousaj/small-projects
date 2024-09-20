#!/bin/bash

set -e  # Termina o script ao encontrar um erro

# Argumentos para o domínio e chave da Mailgun
MAILGUN_DOMAIN=${MAILGUN_DOMAIN:-"seu_dominio"}
MAILGUN_API_KEY=${MAILGUN_API_KEY:-"sua_chave"}

# Solicita a senha do sudo uma vez
echo "Por favor, digite sua senha de administrador."
sudo -v

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
sudo chown $USER:$USER /usr/src/poetry  # Ajusta permissões para o diretório

# Adiciona o Poetry ao PATH
export POETRY_HOME="/usr/src/poetry"
export PATH="${POETRY_HOME}/bin:${PATH}"

# Instala o Poetry
echo "Instalando o Poetry..."
curl -sSL https://install.python-poetry.org | POETRY_HOME=$POETRY_HOME python3 -

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

# Verifica se o arquivo de serviço já existe
SERVICE_FILE="/etc/systemd/system/jobmail.service"

echo "Configurando o serviço..."
cat <<EOL | sudo tee $SERVICE_FILE
[Unit]
Description=Serviço de Vagas Por Email

[Service]
ExecStart=/usr/src/poetry run python /usr/src/jobmail/src/app.py
WorkingDirectory=/usr/src/jobmail/
StandardOutput=journal
StandardError=journal
Restart=on-failure
Environment="PYTHONUNBUFFERED=1"
Environment="POETRY_HOME=/usr/src/poetry"
Environment="PATH=/usr/src/poetry/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

[Install]
WantedBy=multi-user.target
EOL

# Carrega o novo serviço
sudo systemctl daemon-reload

# Inicia e habilita o serviço
sudo systemctl start jobmail.service
sudo systemctl enable jobmail.service

echo "Instalação concluída! O serviço está rodando."
exit 0
