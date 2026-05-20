import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]

    data.append({
        "title": title,
        "price": price,
        "rating": rating
    })

df = pd.DataFrame(data)

# Save CSV
df.to_csv("books_data.csv", index=False)

# Save Excel
df.to_excel("books_data.xlsx", index=False)

print("=" * 50)
print("CODEALPHA WEB SCRAPING PROJECT")
print("=" * 50)
print(f"Total Books Scraped : {len(df)}")
print("CSV File            : books_data.csv")
print("Excel File          : books_data.xlsx")
print("PROJECT STATUS      : SUCCESS")
print("=" * 50)