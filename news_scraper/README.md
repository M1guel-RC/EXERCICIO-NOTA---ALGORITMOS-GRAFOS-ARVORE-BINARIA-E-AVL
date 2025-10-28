# Projeto I - Scraper de Notícias

Este projeto extrai informações de notícias (título, link e resumo) de um site e as salva em um arquivo JSON.

## Funcionalidades
- Acessa um site (usando Books to Scrape como exemplo)
- Extrai título, link e resumo dos itens
- Salva os dados em um arquivo JSON chamado `manchetes.json`

## Dependências
- Python 3.x
- requests
- beautifulsoup4

## Como executar
1. Instale as dependências:
   ```bash
   pip install requests beautifulsoup4
   ```

2. Execute o script:
   ```bash
   python scraper.py
   ```

## Exemplo de saída
O script irá imprimir informações sobre os itens extraídos e salvará um arquivo `manchetes.json` com os dados.

```
Sample data:
  1. Title: A Light in the Attic
     Link: http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
     Summary: Price: £51.77
```