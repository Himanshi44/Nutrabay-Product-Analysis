import pandas as pd

# Step 1: Load your CSV file
df = pd.read_csv("nutrabay_Creatine_all_pages.csv")  # ✅ Use read_csv for CSV files

# Step 2: Define function to extract first 2 words as brand
def extract_brand(name):
    words = str(name).strip().split()
    return ' '.join(words[:2]) if len(words) >= 2 else words[0]

# Step 3: Apply function to create 'Brand' column
df['Brand'] = df['Product Name'].apply(extract_brand)

# Step 4: Preview result
print("\n🆕 Product Names with Extracted Brands:")
print(df[['Product Name', 'Brand']].head(10))

print(f"\n🔢 Total Unique Brands Extracted: {df['Brand'].nunique()}")


# Step 5 (optional): Save to new CSV
df.to_csv("products_with_brands.csv", index=False)
