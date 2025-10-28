project:
  name: "Algoritmo Projects"
  description: >
    Este repositório contém duas aplicações Python distintas, desenvolvidas
    para fins de estudo e prática em automação e web scraping.

  applications:
    - name: "Scraper de Notícias"
      description: "Coleta automaticamente manchetes de portais de notícias."
    - name: "Bot de Login e Scraper de Bio do Instagram"
      description: "Realiza login automatizado e extrai biografias de perfis."

structure:
  root: "AlgoritmoProject/"
  files:
    - "main.py              # Menu principal para selecionar os projetos"
    - "requirements.txt     # Dependências do projeto"
  directories:
    - name: "news_scraper"
      description: "Projeto I - Scraper de Notícias"
      files:
        - "scraper.py"
        - "README.md"
    - name: "instagram_bot"
      description: "Projeto II - Instagram Bot"
      files:
        - "bot.py"
        - "README.md"

installation:
  steps:
    - "Clone este repositório:"
    - command: |
        git clone https://github.com/seu-usuario/AlgoritmoProjects.git
        cd AlgoritmoProjects
    - "Instale as dependências necessárias:"
    - command: |
        pip install -r requirements.txt

execution:
  description: "Execute o programa principal para acessar o menu interativo."
  command: "python main.py"
  options:
    - "Projeto I: Scraper de Notícias"
    - "Projeto II: Bot de Login e Scraper de Bio do Instagram"

outputs:
  description: "Após a execução, cada projeto gera um arquivo JSON com os resultados obtidos."
  files:
    - project: "Scraper de Notícias"
      file: "manchetes.json"
      content: "Contém as manchetes coletadas"
    - project: "Instagram Bot"
      file: "instagram_bio.json"
      content: "Contém as biografias extraídas dos perfis"

technologies:
  - "Python 3.x"
  - "Selenium"
  - "Requests"
  - "JSON"
