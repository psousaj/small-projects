#!/bin/bash

set -e

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

echo "Serviço configurado e iniciado!"
