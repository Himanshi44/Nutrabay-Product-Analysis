# Nutrabay-Product-Analysis
E-commerce product analysis project using Python web scraping, Excel, and Power BI to analyze product pricing, ratings, reviews, discounts, categories, and brand performance through interactive dashboards.
# Nutrabay Product Analysis | Python, Excel & Power BI

## 📌 Project Overview

The **Nutrabay Product Analysis** project focuses on collecting, cleaning, organizing, and analyzing e-commerce product data to understand product pricing, customer ratings, reviews, discounts, categories, flavors, weights, and brand performance.

The project combines **Python web scraping, Excel-based data handling, and Power BI visualization** to turn raw product information into meaningful insights that can support product comparisons and data-driven business decisions.

The analysis explores questions such as:

- Which product categories have the highest number of products?
- How do product prices and customer ratings vary across categories?
- Which products and brands receive the most customer reviews?
- Which brands offer the highest discounts?
- Which flavors and product weights are most common?
- Which products offer attractive combinations of price, ratings, and discounts?
- How does product distribution vary across brands?

## 🎯 Project Objectives

1. Collect product information from Nutrabay's publicly accessible web pages using Python.
2. Extract product attributes such as names, prices, ratings, reviews, brands, discounts, flavors, and weights where available.
3. Organize scraped data into CSV datasets and Excel files for further analysis.
4. Analyze category-level and brand-level product performance.
5. Build an interactive, five-page Power BI dashboard to present key metrics and findings.
6. Demonstrate an end-to-end data analysis workflow, from raw data collection to business-oriented visualization.

## 🛠️ Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| Python | Data collection and preprocessing |
| Requests | Sending HTTP requests to product pages |
| BeautifulSoup | Parsing HTML and extracting product information |
| Pandas | Organizing, transforming, and exporting tabular data |
| Selenium | Automating browser interactions for selected scraping tasks |
| WebDriver Manager | Managing the browser driver setup |
| Instaloader | Collecting selected publicly accessible Instagram profile and post information |
| Microsoft Excel | Reviewing and organizing datasets |
| Power BI | Building interactive reports and visualizing KPIs |
| DAX | Defining measures and calculations in Power BI, where applicable |
| GitHub | Version control and project documentation |

## 🔄 Project Workflow

The project follows this general workflow:

1. **Data collection:** Python scripts retrieve product information from selected Nutrabay category pages.
2. **HTML parsing:** Requests and BeautifulSoup are used to inspect web pages and extract relevant fields. Selenium is used for selected browser-based tasks.
3. **Data organization:** Pandas structures the extracted information into tabular datasets and exports data to CSV files.
4. **Data preparation:** Product datasets are reviewed and organized for analysis in Excel and Power BI.
5. **Data modeling:** The available datasets are loaded into Power BI and used to create category, product, and brand analyses.
6. **Dashboard development:** Visuals, KPI cards, charts, and tables present the findings across five report pages.
7. **Business interpretation:** The resulting dashboard helps identify product distribution patterns, pricing differences, customer engagement, and discount opportunities.

## 🐍 Python Web Scraping

The Python component contains scripts for collecting product information from multiple Nutrabay product categories.

### Data collection scripts

The repository includes scripts associated with categories such as:

- Amino Acids
- Creatine
- Health Food and Drinks
- Mass and Weight Gainers
- Multivitamins
- Pre-Workout
- Sports Nutrition
- Vitamins and Supplements
- Workout Equipment

Additional scripts support brand extraction, product-name processing, price extraction, and selected Instagram data collection.

### Libraries used

**Requests:** Sends HTTP requests to retrieve web page content.

**BeautifulSoup:** Parses HTML and helps locate product information using HTML elements and CSS selectors.

**Pandas:** Converts extracted information into DataFrames, organizes the records, and exports results to CSV files.

**Selenium:** Opens and interacts with web pages through a browser when browser-based access is needed.

**Instaloader:** Supports the separate Instagram-related data collection script.

### Product attributes

Depending on the category page and the script, the extracted attributes may include:

- Product name
- Product price
- Customer rating
- Review count
- Discount percentage
- Brand
- Flavor
- Product weight or size

Not every field is available in every dataset. The exact fields depend on the source page and the corresponding scraping script.

### Example scraping workflow

A typical Requests and BeautifulSoup workflow looks like this:

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "YOUR_PRODUCT_CATEGORY_URL"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Inspect the page and replace this selector
# with the correct product-card selector.
products = soup.select("YOUR_PRODUCT_CARD_SELECTOR")

records = []

for product in products:
    records.append({
        "Product Name": product.get_text(" ", strip=True)
    })

df = pd.DataFrame(records)
print(df.head())
```

This is an illustrative example, not a replacement for the original project scripts. The URL, CSS selectors, and extraction logic must be adapted to the current page structure. Some websites render product information dynamically, which may require Selenium or another appropriate approach.

## 📂 Dataset Overview

The project includes category-wise CSV files and an Excel workbook used for data review and analysis.

The CSV datasets cover product categories such as Sports Nutrition, Vitamins and Supplements, Amino Acids, Proteins, Health Food and Drinks, Pre-Workout, Multivitamins, and Creatine, among others.

### Why category-wise datasets are useful

- They make it easier to inspect individual product categories.
- They support category-level comparisons of prices, ratings, and reviews.
- They allow data quality issues to be identified before analysis.
- They provide a foundation for combining product information into a broader analytical dataset.

### Data preparation considerations

Before drawing conclusions from the data, the following checks are important:

- Standardize column names and data types.
- Convert price, rating, review count, and discount fields to appropriate numeric formats.
- Handle missing values consistently.
- Check for duplicate products and inconsistent product names.
- Standardize brand, flavor, and weight labels where possible.
- Verify that prices use a consistent currency and format.
- Confirm whether each dataset represents unique products or scraped product listings.
- Check that the Excel workbook and Power BI model use the intended data sources.

Some category files may contain different columns or inconsistent naming conventions. These differences should be addressed before combining datasets or comparing categories.

## 📊 Power BI Dashboard

The Power BI report contains five main pages, each designed to answer a different set of business questions.

### 1. Executive Overview

**Purpose:** Provide a high-level summary of the product catalog.

Key dashboard elements include:

- Total Unique Products
- Average Product Price
- Average Customer Rating
- Total Reviews
- Average Rating by Category
- Average Price by Product Category
- Category-Wise Product Distribution
- Product or SKU Distribution across categories

**Questions answered:**

- How large is the product catalog?
- What is the average listed product price?
- How do ratings vary across product categories?
- Which categories account for a larger share of the analyzed records?

This page gives viewers a quick overview before they explore individual categories and brands.

### 2. Category Insights

**Purpose:** Compare product categories and examine pricing and customer feedback.

Key visuals include:

- Product or category rating comparisons
- Price-versus-rating scatter plot
- Brand-level pricing analysis
- Product volume across brands
- Review-based popularity analysis
- Product details table

**Questions answered:**

- How do prices vary across categories?
- Are higher-priced products necessarily rated more highly?
- Which categories or brands have greater product representation?
- Which products have strong customer ratings?

The scatter plot can help explore the relationship between price and rating. However, a relationship in the chart does not by itself establish that price causes a higher or lower rating.

### 3. Flavor & Weight Analysis

**Purpose:** Understand product variations based on flavor and package size.

Key visuals include:

- Flavor-wise product distribution
- Top-rated or highest-scoring flavors
- Product count by weight
- Average price by weight
- Product and flavor comparisons

**Questions answered:**

- Which flavors appear most frequently in the analyzed catalog?
- Which flavors have stronger ratings or scores?
- Which package weights are most common?
- How does average price vary by product weight?

This analysis can help compare the available product options. Price comparisons should account for differences in product type and package size before treating one option as better value than another.

### 4. Discounts & Value Deals

**Purpose:** Examine listed discounts and identify products that may offer attractive deals.

Key visuals include:

- Brand-wise discount trends
- Average discount by category
- Products with high review counts
- Brands offering larger discounts
- Value-for-money product comparisons
- Products with the largest listed discounts

One example highlighted in the dashboard is **Nutrabay Pure Creatine Monohydrate Micronized**, shown with a listed price of ₹729, a 33% discount, a 4.7 rating, and 2,402 reviews in the displayed report.

**Questions answered:**

- Which categories show higher average discounts?
- Which brands advertise larger discounts?
- Which discounted products also have substantial customer feedback?
- Which products should be examined more closely for price and rating comparisons?

A listed discount does not automatically establish that a product is the best deal. Value comparisons should also consider the actual selling price, package size, rating, review volume, and comparable alternatives.

### 5. Brand Intelligence

**Purpose:** Compare brands based on catalog representation, customer ratings, and review activity.

Key visuals include:

- Overall Brand Performance Score
- Highest-Rated Brand
- Most Popular Brand by Review Count
- Product Share by Brand
- Product Volume by Brand
- Brand-wise product distribution

The dashboard highlights **Ronnie Coleman** as the highest-rated brand in the displayed report and **Nutrabay** as the brand with the greatest review volume.

**Questions answered:**

- Which brands have the most products in the analyzed data?
- Which brands have the highest displayed ratings?
- Which brands receive the greatest volume of customer reviews?
- How is product representation distributed across brands?

Brand ratings, product counts, and review totals measure different aspects of performance. They should be interpreted separately unless a clearly defined and validated scoring method combines them.

## 📈 Key Findings and Insights

The dashboard provides a starting point for investigating several patterns in the collected data:

- **Product distribution:** Sports Nutrition and Vitamins and Supplements represent substantial portions of the category data shown in the report.
- **Price variation:** Average listed prices differ across categories, making category-level comparisons useful.
- **Customer feedback:** Review counts and ratings can be used together to understand customer engagement and reported satisfaction.
- **Discount opportunities:** Some categories and brands show higher displayed discount percentages than others.
- **Product variations:** Flavor and weight analyses help compare the range of available product options.
- **Brand representation:** Nutrabay has a prominent presence in the displayed brand and review analysis.

These observations describe the analyzed product listings, not necessarily total market demand, sales performance, revenue, or profitability. The results may change with the collection date, available pages, data cleaning, and report filters.

## 🖼️ Dashboard Screenshots

Screenshots of the Power BI dashboard can be added here to make the repository easier to understand without requiring visitors to open the PBIX file.

Create a folder named `screenshots` in the repository and upload your dashboard screenshots with these filenames, or change the links below to match your actual filenames.

### Executive Overview

<img width="1202" height="677" alt="image" src="https://github.com/user-attachments/assets/a12dbf51-e7d4-423a-9f54-87b5cb1c7087" />

### Category Insights

<img width="1185" height="672" alt="image" src="https://github.com/user-attachments/assets/68602e15-d729-4df1-8715-29efcf65ba61" />

### Flavor & Weight Analysis

<img width="1177" height="663" alt="image" src="https://github.com/user-attachments/assets/8b3a86ba-3b45-4431-b10c-c0c0f837259a" />


### Discounts & Value Deals

<img width="1172" height="662" alt="image" src="https://github.com/user-attachments/assets/05b79b95-d6d1-4a7c-b186-6a4576846c50" />


### Brand Intelligence

<img width="1176" height="658" alt="image" src="https://github.com/user-attachments/assets/b1d76f7a-97a3-4bbd-bc54-53048c4bfdd3" />


*Note: These are suggested filenames. The images will display on GitHub only after the corresponding screenshots have been uploaded to the `screenshots` folder.*

## 📁 Repository Structure

A suggested repository structure is:

```text
Nutrabay-Product-Analysis/
│
├── README.md
├── .gitignore
│
├── NUTRABAY_Python-File/
│   ├── webdata.py
│   ├── brandextract.py
│   ├── nameextract.py
│   ├── instadata.py
│   ├── AminoAcidsdata.py
│   ├── Creatinedataweb.py
│   ├── HealthFoodandDrinksdata.py
│   ├── MassandWeightGainersdata.py
│   ├── Multivitaminsdataweb.py
│   ├── PreWorkoutdata.py
│   ├── Sports Nutrition.py
│   ├── VitaminsandSupplementsdata.py
│   └── WorkoutEquipmentdata.py
│
├── NUTRABAY_dataset/
│   ├── Sports Nutrition.csv
│   ├── Vitamins and Supplements.csv
│   ├── Amino Acids.csv
│   ├── Proteins.csv
│   └── ...
│
├── AllData.xlsx
│
├── Nutrabay_project.pbix
├── Nutrabay_Project-Dashboard.pdf
│
└── screenshots/
    ├── 01-executive-overview.png
    ├── 02-category-insights.png
    ├── 03-flavor-weight-analysis.png
    ├── 04-discounts-value-deals.png
    └── 05-brand-intelligence.png
```

This structure is a recommended organization. Adjust the folder names and file paths to match the files you actually upload to GitHub.

## ⚙️ How to Run the Python Scripts

### Prerequisites

Install the following before running the scraping scripts:

- Python 3.10 or another version compatible with the libraries used
- pip
- A code editor such as Visual Studio Code
- Internet access
- A compatible browser and driver configuration for Selenium-based scripts

### 1. Clone the repository

After uploading the project to GitHub, run:

```bash
git clone https://github.com/YOUR-USERNAME/Nutrabay-Product-Analysis.git
cd Nutrabay-Product-Analysis
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

On Windows, activate it with:

```bash
.venv\Scripts\activate
```

### 3. Install the required libraries

```bash
pip install requests beautifulsoup4 pandas selenium webdriver-manager instaloader
```

Additional dependencies may be needed depending on the imports in the individual scripts. Check the scripts before running them, and consider adding a `requirements.txt` file with the verified dependencies.

### 4. Run a Python script

For example:

```bash
python NUTRABAY_Python-File/webdata.py
```

Run commands from the repository root, and check whether each script expects to be launched from a particular working directory.

**Important:** Some scripts may use hard-coded URLs, local file paths, browser settings, or page-specific HTML selectors. You may need to update these settings before they work in a new environment. Websites can also change their HTML structure, restrict automated requests, or load content dynamically.

### 5. Open the Power BI report

Open `Nutrabay_project.pbix` in Microsoft Power BI Desktop to explore the report, visuals, filters, and data model.

The report may need its data-source paths updated if the underlying CSV or Excel files are stored in a different location. Refresh the data and verify the measures before relying on the displayed results.

## 📋 Business Use Cases

The project demonstrates how product-catalog data can support:

- **Product comparison:** Compare listed prices and ratings across products.
- **Category analysis:** Understand how products are distributed across categories.
- **Brand analysis:** Examine catalog representation and customer review activity.
- **Discount evaluation:** Identify products with larger displayed discounts for further comparison.
- **Catalog improvement:** Detect missing or inconsistent product attributes.
- **Dashboard reporting:** Present multiple product metrics in one report for easier exploration.

The current data is primarily product-listing and customer-feedback information. It does not, by itself, establish sales, conversion rates, inventory availability, profit margins, or revenue.

## ⚠️ Limitations and Future Improvements

### Current limitations

- Web scraping depends on the current page structure and may break when CSS selectors or website layouts change.
- Some category datasets may contain missing or inconsistent fields.
- Product records collected from different pages may overlap.
- Brand extraction based on product-name text may misclassify some products.
- Some dashboard measures, including composite scores, need their calculation definitions documented before their interpretation can be fully validated.
- A product catalog snapshot does not necessarily represent the full catalog or current prices.

### Future improvements

- Add automated data validation and duplicate detection.
- Standardize column names, currencies, brand labels, and numeric formats.
- Consolidate category datasets into a documented master dataset.
- Add a repeatable data-refresh workflow and collection timestamps.
- Document the Power BI data model, relationships, and DAX measures.
- Add tests and error handling to the scraping scripts.
- Compare price per unit or serving where package-size information is available and comparable.
- Track historical prices and discounts across multiple collection dates.
- Add a `requirements.txt` file and clear configuration instructions.
- Improve the README with final screenshots and links to individual project files.

## 🎓 Skills Demonstrated

- Python programming
- Web scraping with Requests and BeautifulSoup
- Browser automation with Selenium
- Data manipulation using Pandas
- CSV and Excel data handling
- Data cleaning and validation
- Exploratory data analysis
- Power BI dashboard development
- KPI reporting and visualization
- Business insight communication
- GitHub project documentation

## 👩‍💻 Project Summary

The Nutrabay Product Analysis project demonstrates an end-to-end approach to product-catalog analytics. It combines Python-based data collection, structured datasets, Excel-based review, and a five-page Power BI dashboard to explore product categories, pricing, ratings, discounts, flavors, weights, and brand representation.

The project illustrates how raw e-commerce listing data can be transformed into organized datasets and visual reports that help users investigate product and catalog patterns.

## ⚖️ Disclaimer

This project is intended for educational and portfolio purposes. Nutrabay is referenced as the subject of the analysis. This project is not an official Nutrabay product or an endorsement by Nutrabay.

Data availability, product prices, discounts, ratings, reviews, and page structures may change over time. Any conclusions should be interpreted in the context of the collected data and the report's filters and calculation definitions.

---

**Tools:** Python · Requests · BeautifulSoup · Pandas · Selenium · Excel · Power BI · DAX
