#!/bin/bash

set -e

# Função para verificar se o git está instalado
check_git_installed() {
    if ! command -v git &> /dev/null; then
        echo "Erro: Git não está instalado."
        echo "Instalando git..."
        
        # Verifica qual é o gerenciador de pacotes e instala o git
        if command -v apt-get &> /dev/null; then
            apt-get update && apt-get install -y git
        elif command -v yum &> /dev/null; then
            yum install -y git
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

echo "Setando workdir"
WORKDIR=$TEMP_DIR/jobmail

echo "Movendo para a pasta temporária e executando setup.sh..."
cd $WORKDIR

# Torna o setup.sh executável
chmod +x $WORKDIR/infra/setup.sh
chmod +x $WORKDIR/infra/setup_service.sh

# Executa o setup.sh, pedindo senha do sudo se necessário
if [ "$#" -gt 0 ]; then
    echo "Executando setup.sh com senha do sudo..."
    echo "$1" | sudo -S ./setup.sh
else
    echo "Executando setup.sh com solicitação de senha do sudo."
    /usr/bin/sudo ./setup.sh 
fi
echo "Configurando o serviço..." \
setup_service.sh


# Limpa a pasta temporária após a instalação
echo "Limpando a pasta temporária..."
rm -rf $TEMP_DIR

echo "Instalação concluída! O serviço está rodando."

