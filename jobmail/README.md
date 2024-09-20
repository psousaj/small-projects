# JobMail Setup

Este repositório contém um script de instalação automatizada para o JobMail. O script baixa todas as dependências, instala e configura o serviço para rodar em segundo plano.

## Requisitos

- **Git**: Certifique-se de que o Git esteja instalado na máquina. O script de instalação tentará instalá-lo automaticamente, caso não esteja disponível.
- **sudo**: O script precisará de permissões administrativas para instalar dependências.

## Instalação

Siga os passos abaixo para instalar o JobMail no seu sistema Linux.

### 1. Baixar e executar o `install.sh`

O script de instalação irá:

- Verificar se o Git está instalado e instalá-lo se necessário.
- Clonar o repositório em uma pasta temporária.
- Navegar até o diretório do projeto clonado e executar o `setup.sh`.

Para executar a instalação, basta rodar o seguinte comando no terminal:

```bash
curl -s https://raw.githubusercontent.com/psousaj/small-projects/main/jobmail/install.sh | bash
```
