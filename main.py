import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.amazon.in/"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
product_links = []

for x in range(1,17):
    url = f"https://www.amazon.in/s?k=bags&page={x}&qid=1675339897&ref=sr_pg_1"
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    productlist = soup.find_all('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')

    for item in productlist:
        for link in item.find_all('a', href=True):
            product_links.append(base_url + link['href'])

#testlink = "https://www.amazon.in/Urban-Tribe-Laptop-Backpack-Havana/dp/B01LXNNFDF/ref=sr_1_17_sspa?keywords=bags&qid=1675350376&sr=8-17-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfbmV4dA&smid=A385M0TPSNV7VS&th=1"

products_list = []
for link in product_links:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")

    name = soup.find("h1", class_="a-size-large a-spacing-none").text.strip()
    price = soup.find("span", class_="a-offscreen").text.strip()
    rating = soup.find("span", class_="a-icon-alt").text.strip()
    review = soup.find("span", class_="a-size-base").text.strip()

    product = {
        'name': name,
        'price': price,
        'rating': rating,
        'review' : review
    }
    products_list.append(product)


df = pd.DataFrame(products_list)

df.to_csv(r'C:\Users\Amaan Shaikh\PycharmProjects\Web_Scraping2\file1.csv')
