import requests
from bs4 import BeautifulSoup

url = 'https://olcha.uz/ru/category/noutbuki-planshety-kompyutery'
not_url = "https://olcha.uz/ru/category/noutbuki-planshety-kompyutery/noutbuki"

response = requests.get(not_url)
soup = BeautifulSoup(response.content, 'html.parser')

categories = []
productss = []

# category_links = soup.find_all('div', {'class': 'subcategory-list__item'})
products_links = soup.find_all('div', {'class': 'product-card__brand-name'})

# for link in category_links:
#     category_name = link.text.strip()

#     categories.append(category_name)

for prod in products_links:
    products_name = prod.text.strip()

    productss.append(products_name)


for category in productss:
    print(category)





