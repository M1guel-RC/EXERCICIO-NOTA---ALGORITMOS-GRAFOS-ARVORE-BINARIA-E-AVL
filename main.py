import os
import sys

def print_menu():
    # Display the main menu
    print('\n' + '='*50)
    print('           MENU DE PROJETOS')
    print('='*50)
    print('1. Projeto I - Scraper de Notícias')
    print('2. Projeto II - Bot de Login e Scraper de Bio Instagram')
    print('3. Sair')
    print('='*50)

def run_news_scraper():
    # Run the news scraper project
    print('\nExecutando Projeto I - Scraper de Notícias...')
    try:
        from news_scraper.scraper import scrape_news
        scrape_news()
    except ImportError as e:
        print(f'Erro ao importar o scraper de notícias: {e}')
        print('Certifique-se de que as dependências estão instaladas:')
        print('pip install requests beautifulsoup4')
    except Exception as e:
        print(f'Ocorreu um erro ao executar o scraper de notícias: {e}')

def run_instagram_bot():
    # Run the Instagram bot project
    print('\nExecutando Projeto II - Bot de Login e Scraper de Bio Instagram...')
    try:
        from instagram_bot.bot import scrape_instagram_bio
        print('ATENÇÃO: Este script irá abrir o navegador Chrome para fazer login no Instagram.')
        print('Você precisará fornecer credenciais reais para fazer login.')
        print('Após o login, pressione Enter no console para continuar a execução.')
        input('Pressione Enter para continuar...')
        scrape_instagram_bio()
    except ImportError as e:
        print(f'Erro ao importar o bot do Instagram: {e}')
        print('Certifique-se de que as dependências estão instaladas:')
        print('pip install selenium')
        print('Também é necessário ter o ChromeDriver instalado e configurado corretamente.')
    except Exception as e:
        print(f'Ocorreu um erro ao executar o bot do Instagram: {e}')

def main():
    # Main function to run the menu
    while True:
        print_menu()
        choice = input('\nEscolha uma opção (1-3): ').strip()
        
        if choice == '1':
            run_news_scraper()
        elif choice == '2':
            run_instagram_bot()
        elif choice == '3':
            print('\nSaindo do programa. Até logo!')
            sys.exit(0)
        else:
            print('\nOpção inválida! Por favor, escolha uma opção válida (1-3).')

        # Prompt to continue
        input('\nPressione Enter para voltar ao menu...')

if __name__ == '__main__':
    main()

    
    