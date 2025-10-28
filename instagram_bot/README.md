# Projeto II - Bot de Login e Scraper de Bio Instagram

Este projeto cria um bot que faz login no Instagram, navega até um perfil específico e extrai informações da bio.

## Funcionalidades
- Faz login no Instagram
- Trata as telas de "Salvar Informações" e "Notificações"
- Navega até o perfil `@computacaounifavip_`
- Extrai informações da bio e outros dados do perfil
- Salva os dados em um arquivo JSON

## Dependências
- Python 3.x
- selenium
- ChromeDriver (instalado e configurado no PATH)

## Como executar
1. Instale as dependências:
   ```bash
   pip install selenium
   ```

2. Faça download e instale o ChromeDriver:
   - Baixe o ChromeDriver compatível com sua versão do Chrome em: https://chromedriver.chromium.org/
   - Adicione o ChromeDriver ao seu PATH do sistema

3. Execute o script:
   ```bash
   python bot.py
   ```

## Importante
- O script abrirá o navegador Chrome automaticamente
- Você precisará fornecer credenciais reais do Instagram para fazer login
- Após fazer login manualmente no navegador, pressione Enter no console para continuar a execução

## Exemplo de saída
O script irá imprimir as informações extraídas e salvará um arquivo `instagram_bio.json` com os dados.

```
Extracted data:
  Profile: computacaounifavip_
  Username: Computação - UNIFAVIP
  Bio: Centro Acadêmico de Bacharelado em Sistemas de Informação - UNIFAVIP/XV
  Followers: 187
  Following: 189
  Posts: 56
```