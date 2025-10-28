import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_news():
    """
    Scraper for news from Books to Scrape (as example) or G1
    Extracts title, link, and summary when available
    Saves data to manchetes.json
    """
    # Using Books to Scrape as example site
    base_url = "http://books.toscrape.com/"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('article', class_='product_pod')
        
        news_data = []
        
        for book in books:
            title_element = book.find('h3').find('a')
            title = title_element['title'] if title_element else "No title"
            
            link_element = book.find('h3').find('a')
            link = base_url + link_element['href'][3:] if link_element else "No link"  # Remove '../' from href
            
            price_element = book.find('p', class_='price_color')
            price = price_element.get_text() if price_element else "No price"
            
            # For books, the price can serve as a "summary" since there's no actual summary
            summary = f"Price: {price}"
            
            news_item = {
                "title": title,
                "link": link,
                "summary": summary
            }
            
            news_data.append(news_item)
        
        # Save to JSON file
        output_file = "manchetes.json"
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(news_data, json_file, ensure_ascii=False, indent=4)
        
        print(f"Successfully scraped {len(news_data)} items and saved to {output_file}")
        print("Sample data:")
        for i, item in enumerate(news_data[:3]):  # Print first 3 items as sample
            print(f"  {i+1}. Title: {item['title']}")
            print(f"     Link: {item['link']}")
            print(f"     Summary: {item['summary']}")
            print()
        
        return news_data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    scrape_news()