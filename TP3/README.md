# TPC3

## Metadata

| Title | Date | AuthorId | AuthorName | UcSigla | UcNome |
|:-----:|:----:|:--------:|:----------:|:-------:|:------:|
| TPC3 |      | PG57897  | Pedro Azevedo  | SPLN    | Scripting no Processamento de Linguagem Natural |

## Resumo

Este trabalho envolve a construção de uma ferramenta de contagem de palavras e cálculo de frequências em ficheiros de texto. O módulo `base.py` realiza a tokenização e contabiliza as ocorrências de cada palavra, exportando o resultado em JSON. O módulo `count.py` lê múltiplos ficheiros JSON de contagens parciais, soma os totais e calcula frequências absolutas e relativas, apresentando também uma tabela com percentagens. Estes scripts são disponibilizados como comandos `ftk-occ` e `ftk-cnt` via `pyproject.toml`.
