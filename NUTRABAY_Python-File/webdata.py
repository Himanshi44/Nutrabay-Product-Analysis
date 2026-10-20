import requests
from bs4 import BeautifulSoup
import pandas as pd

# Page with Top 10 Products
url = 'https://nutrabay.com/product-category/health-food-drinks/?pn=1'
headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all product rows in the table (based on the price class)
product_rows = soup.find_all('span', class_='plpstyles_tablePrice__cTL4F')

top_10_data = []

for price_tag in product_rows:
    # Go up to the parent to find the product name
    parent = price_tag.find_parent('tr') or price_tag.find_parent()
    name_tag = parent.find('a') if parent else None

    name = name_tag.text.strip() if name_tag else 'N/A'
    price = price_tag.text.strip()

    # Filter out weird or unrelated entries (optional but helpful)
    if name != 'N/A' and "Home" not in name:
        top_10_data.append({
            'Top Product': name,
            'Price': price
        })

# Take only first 10
df_top_10 = pd.DataFrame(top_10_data[:10])

print("\n🏆 Top 10 Products from Bottom Table:")
print(df_top_10)
