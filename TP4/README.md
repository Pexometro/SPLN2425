# TPC4

## Metadata

| Title | Date | AuthorId | AuthorName | UcSigla | UcNome |
|:-----:|:----:|:--------:|:----------:|:-------:|:------:|
| TPC4 | | PG57897 | Pedro Azevedo | SPLN | Scripting no Processamento de Linguagem Natural |

## Resumo

Este trabalho prático consiste no desenvolvimento de um conjunto de scripts em Python para análise e processamento de texto, focando-se em tarefas de frequência, probabilidade e manipulação de corpora. Utiliza-se como base um dicionário em Tetum e um corpus de texto comprimido, com o objetivo de extrair estatísticas linguísticas e preparar dados para tarefas de PLN.

## Estrutura

O projeto está organizado da seguinte forma:
- `ftk/ftk/`: Contém os módulos principais:
  - `base.py`: Funções utilitárias e classes base.
  - `corpus.py`: Leitura e processamento de corpora.
  - `freq.py`: Cálculo de frequências de palavras.
  - `probability.py`: Cálculo de probabilidades e estatísticas.
  - `mains.py` e `__main__.py`: Pontos de entrada para execução dos scripts.
- `tetum-Dicionario_de_fundamentos_elementares_da.txt`: Dicionário utilizado para análise.
- `corpus/pt.xz`: Corpus de texto comprimido.
- `tests/`: Testes automáticos para validação das funcionalidades.

## Como correr

1. Instalar dependências:
   ```sh
   pip install -e .

