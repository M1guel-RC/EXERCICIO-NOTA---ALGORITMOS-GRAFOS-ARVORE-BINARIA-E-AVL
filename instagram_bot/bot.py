from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import time
import os

def scrape_instagram_bio():
    """
    Instagram bot that:
    1. Logs in to Instagram
    2. Navigates to a specific profile (@computacaounifavip_)
    3. Extracts bio information
    4. Saves to JSON file
    """
    
    # Set up Chrome options
    chrome_options = Options()
    # Uncomment the next line if you want to run in headless mode
    # chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        print("Opening Instagram...")
        driver.get("https://www.instagram.com/")
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        
        # Find login fields and enter credentials
        # Note: You need to provide actual Instagram credentials for this to work
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        
        # For this example, we'll use placeholders
        # In a real scenario, you'd need to provide actual credentials
        # or prompt the user for them
        print("Please enter Instagram credentials manually in the browser...")
        input("Press Enter in this console after logging in manually...")
        
        # Handle "Save Info" dialog if it appears
        try:
            not_now_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
            )
            not_now_button.click()
            print("Clicked 'Not Now' on save info dialog")
        except:
            print("No save info dialog appeared or already handled")
        
        # Handle "Turn on Notifications" dialog if it appears
        try:
            not_now_notifications = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
            )
            not_now_notifications.click()
            print("Clicked 'Not Now' on notifications dialog")
        except:
            print("No notifications dialog appeared or already handled")
        
        # Navigate to the target profile
        target_profile = "computacaounifavip_"
        driver.get(f"https://www.instagram.com/{target_profile}/")
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//header//section//div//h2"))
        )
        
        # Extract bio information
        bio = None
        try:
            bio_element = driver.find_element(By.XPATH, "//header//section//div//div[2]")
            bio = bio_element.text
        except:
            print("Could not find bio element")
        
        # Extract other profile information
        username = None
        followers = None
        following = None
        posts_count = None
        
        try:
            # Get username
            username_element = driver.find_element(By.XPATH, "//header//section//div//h2")
            username = username_element.text
        except:
            print("Could not find username")
        
        try:
            # Get followers count
            followers_element = driver.find_element(By.XPATH, "//header//section//ul//li[2]//a//span")
            followers = followers_element.get_attribute("title") or followers_element.text
        except:
            print("Could not find followers count")
        
        try:
            # Get following count
            following_element = driver.find_element(By.XPATH, "//header//section//ul//li[3]//a//span")
            following = following_element.text
        except:
            print("Could not find following count")
        
        try:
            # Get posts count
            posts_element = driver.find_element(By.XPATH, "//header//section//ul//li[1]//span")
            posts_count = posts_element.text
        except:
            print("Could not find posts count")
        
        # Save data to JSON
        bio_data = {
            "profile": target_profile,
            "username": username,
            "bio": bio,
            "followers": followers,
            "following": following,
            "posts_count": posts_count,
            "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        output_file = "instagram_bio.json"
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(bio_data, json_file, ensure_ascii=False, indent=4)
        
        print(f"Successfully extracted Instagram bio and saved to {output_file}")
        print("Extracted data:")
        print(f"  Profile: {bio_data['profile']}")
        print(f"  Username: {bio_data['username']}")
        print(f"  Bio: {bio_data['bio']}")
        print(f"  Followers: {bio_data['followers']}")
        print(f"  Following: {bio_data['following']}")
        print(f"  Posts: {bio_data['posts_count']}")
        
        return bio_data
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    scrape_instagram_bio()