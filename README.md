# Algoritmo Projects

Este projeto contém duas aplicações distintas:
1. Scraper de Notícias
2. Bot de Login e Scraper de Bio Instagram

## Estrutura do Projeto
```
AlgoritmoProject/
├── main.py              # Menu principal para selecionar os projetos
├── requirements.txt     # Dependências do projeto
├── news_scraper/        # Projeto I - Scraper de Notícias
│   ├── scraper.py
│   └── README.md
└── instagram_bot/       # Projeto II - Instagram Bot
    ├── bot.py
    └── README.md
```

## Instalação

1. Clone ou baixe este repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução

Execute o programa principal para acessar o menu:
```bash
python main.py
```

No menu, você poderá escolher entre:
- Projeto I: Scraper de Notícias
- Projeto II: Bot de Login e Scraper de Bio Instagram

## Documentação dos Projetos

Para detalhes específicos sobre cada projeto, consulte os READMEs individuais:
- [News Scraper README](./news_scraper/README.md)
- [Instagram Bot README](./instagram_bot/README.md)

## Prints dos JSONs

Após a execução de cada projeto, arquivos JSON serão gerados:
- Projeto I gera `manchetes.json`
- Projeto II gera `instagram_bio.json`