# COMP0428_Adicley_Adrian_Marcelo_At1

## Instruções de Configuração

### Pré-requisitos
- Gerenciador de pacotes [UV](https://docs.astral.sh/uv/getting-started/installation/)
- [Dados NLTK](https://www.nltk.org/data.html)

### Como Começar

1. Clone este repositório
2. Navegue até o diretório do projeto
3. Configure o ambiente e as dependências:

```bash
# Baixe e instale as dependências
uv sync

# Baixe os dados do NLTK
# (Isso será executado automaticamente na primeira vez que você rodar a aplicação)
# Se você quiser baixar os dados do NLTK manualmente:
uv run python -c "import nltk; nltk.download('wordnet')"

# Execute a aplicação
uv run main.py
```

## Visão Geral do Projeto

Baseado na resposta do [Stack Overflow](https://stackoverflow.com/questions/14489309/convert-words-between-verb-noun-adjective-forms).

Este projeto demonstra a lematização de palavras usando o WordNet do NLTK. Ele pode:
- Converter substantivos em verbos relacionados (verbify)
- Converter verbos em substantivos relacionados (nounify)

## Exemplos

Quando você executar a aplicação, serão mostrados exemplos de:
1. Conversão de "writer" (escritor) para verbos relacionados
2. Conversão de "written" (escrito) para substantivos relacionados
