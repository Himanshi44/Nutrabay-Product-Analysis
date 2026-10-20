from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Setup headless browser
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load the URL
url = "https://nutrabay.com/product-category/bodybuilding/proteins/"
driver.get(url)

# Wait for full content to load
time.sleep(5)

# Parse the rendered HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# ✅ Find the "Brand" filter section using a unique attribute
brand_section = soup.find('article', attrs={'data-title': 'Brand'})

# Extract brand names from inside checkboxes
brand_list = []
if brand_section:
    labels = brand_section.find_all('label')
    for label in labels:
        span = label.find('span')
        if span:
            brand_name = span.get_text(strip=True)
            brand_list.append(brand_name)

# ✅ Output results
if brand_list:
    print(f"\n✅ Found {len(brand_list)} brands in 'Proteins' category:")
    for i, brand in enumerate(brand_list, 1):
        print(f"{i}. {brand}")
else:
    print("❌ Brand section not found or structure changed.")
