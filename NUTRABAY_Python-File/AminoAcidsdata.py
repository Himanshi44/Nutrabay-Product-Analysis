import pandas as pd
import requests
from bs4 import BeautifulSoup

print("✅ Libraries imported successfully!")

# Set base URL and headers
base_url = 'https://nutrabay.com/product-category/amino-acids/?pn={}'
headers = {
    'User-Agent': 'Mozilla/5.0'
}



# Fetch first page once to get brand list
first_page = requests.get(base_url.format(1), headers=headers)
first_soup = BeautifulSoup(first_page.content, 'html.parser')

# Step 1: Locate the exact accordion section for brands
brand_section = first_soup.select_one('div.accordion_acContainer__bFZDW > div:nth-child(3)')

brand_list = []
if brand_section:
    brand_labels = brand_section.find_all('label', class_='checkBoxWrap checkBoxWrap_sm')
    for label in brand_labels:
        span_tags = label.find_all('span')
        if len(span_tags) >= 1:
            brand_name = span_tags[0].text.strip()
            brand_list.append(brand_name)

print(f"🔎 Found {len(brand_list)} brands in the Brand filter:")
print(brand_list)

# print("\n🏷️ List of Extracted Brands:")
# for i, brand in enumerate(brand_list, 1):
#     print(f"{i}. {brand}")





# # Data collection
# data = []

# # Loop through first N pages (e.g., 1 to 5)
# for page in range(1, 5):  # You can change 6 to however many pages you want
#     print(f"\n🔄 Scraping Page {page}...")
#     url = base_url.format(page)

#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find all product cards on the current page
#     products = soup.find_all('div', class_='whiteBox plpProduct_productItem__ZMZND ProductHitsContainer_productCrad__FtBCS')

#     # Stop if no products are found (end of pages)
#     if not products:
#         print("❌ No products found. Stopping pagination.")
#         break

#     # Scrape product details
#     for product in products:
#         name_tag = product.find('span', class_='twoLineTruncate plpProduct_product_card__KoJif')
#         name = name_tag.text.strip() if name_tag else 'N/A'

#         price_tag = product.find('span', class_='plpProduct_ourPrice__057hc')
#         price = price_tag.text.strip() if price_tag else 'N/A'

#         rating_tag = product.find('div', class_='Rating_rating__g3c_g plpProduct_star__Ct_kd')
#         rating = rating_tag.get('data-rating') if rating_tag and rating_tag.has_attr('data-rating') else 'No rating'

#         review_count_tag = product.find('span', class_='plpProduct_count__KlfOS')
#         review_count = review_count_tag.text.strip() if review_count_tag else 'N/A'

#          # Discount %
#         discount_tag = product.find('div', class_='tag_leftTag__Xhv_P green-tag undefined')
#         discount = discount_tag.text.strip().replace('OFF', '').strip() if discount_tag else 'No discount'

#         # Weight & Flavor
#         info_tag = product.find('p', class_='product_productInfo__GE_f7')
#         if info_tag:
#             info_text = info_tag.text.strip()
#             if ',' in info_text:
#                 weight, flavor = map(str.strip, info_text.split(',', 1))
#             else:
#                 weight, flavor = info_text.strip(), 'N/A'
#         else:
#             weight, flavor = 'N/A', 'N/A'


# # ✅ Detect brand by checking which brand name is in product title
#         matched_brand = next((brand for brand in brand_list if brand.lower() in name.lower()), 'Unknown')



#         data.append({
#             'Product Name': name,
#             'Brand': matched_brand,
#             'Price': price,
#             'Rating': rating,
#             'Review Count': review_count,
#             'Discount': discount,
#             'Weight': weight,
#             'Flavor': flavor

#         })

# # Convert to DataFrame
# df = pd.DataFrame(data)

# # ✅ Show preview
# print("\n📋 Preview of Scraped Data:")
# print(df.head(10))
# #print(df)

# #print(f"\n✅ Total products scraped: {len(df)}")

# print("Total scraped:", len(df))
# print("Unique products:", df['Product Name'].nunique())
# print("Unique brands detected:", df['Brand'].nunique())



# # Save to CSV (optional)
# df.to_csv('nutrabayAminoAcids.csv', index=False)
# print("📁 CSV saved.")
