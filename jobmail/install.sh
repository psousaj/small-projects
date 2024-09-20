#!/bin/bash

set -e

# Solicita a senha do sudo uma vez
echo "Por favor, digite sua senha de administrador."
sudo -v

# Função para verificar se o git está instalado
check_git_installed() {
    if ! command -v git &> /dev/null; then
        echo "Erro: Git não está instalado."
        echo "Instalando git..."
        
        # Verifica qual é o gerenciador de pacotes e instala o git
        if command -v apt-get &> /dev/null; then
            sudo apt-get update && sudo apt-get install -y git
        elif command -v yum &> /dev/null; then
            sudo yum install -y git
        else
            echo "Por favor, instale o Git manualmente e execute o script novamente."
            exit 1
        fi
    else
        echo "Git já está instalado."
    fi
}

# Verifica se o git está instalado
check_git_installed

# Define a URL do repositório Git e a pasta temporária
REPO_URL="https://github.com/psousaj/small-projects.git"
TEMP_DIR=$(mktemp -d)

# Clona o repositório na pasta temporária
echo "Clonando o repositório na pasta temporária..."
git clone $REPO_URL $TEMP_DIR

# Verifica se o clone foi bem-sucedido e se a pasta 'jobmail' existe
if [ ! -d "$TEMP_DIR/jobmail" ]; then
    echo "Erro: Não foi possível clonar o repositório ou encontrar a pasta 'jobmail'."
    exit 1
fi

# Move para o diretório temporário onde está o 'jobmail'
echo "Movendo para a pasta temporária e executando setup.sh..."
cd $TEMP_DIR/jobmail

# Torna o setup.sh executável
chmod +x setup.sh

# Executa o setup.sh a partir da pasta temporária
./setup.sh

# Limpa a pasta temporária após a instalação
echo "Limpando a pasta temporária..."
rm -rf $TEMP_DIR

echo "Instalação concluída!"
