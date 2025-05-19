# Importing libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


URL = "https://www.amazon.in/s?k=playstation+5&sprefix=pla%2Caps%2C464&ref=nb_sb_ss_ts-doa-p_1_3"


HEADERS = {
    "User-Agent": "your user agent",
    "Accept-Language": "en-US, en;q=0.5",
}

# making request to the website
webpage = requests.get(URL, headers=HEADERS, timeout=10)

# checking connection
print(webpage.status_code)  # 200 means request is successful

# printing the content of the webpage
print(webpage.content)  # but it gives response in bytes format


soup = BeautifulSoup(webpage.content, "html.parser")

# find different links in the webpage
links = soup.find_all(
    "a",
    class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal",
)

# print the links
print(links[0].get("href"))  # but the links are not complete


link = links[0].get("href")
product_list = "https://www.amazon.in" + link
print(product_list)


new_webpage = requests.get(product_list, headers=HEADERS, timeout=10)

# checking connection
print(new_webpage.status_code)  # 200 means request is successful

# printing the content of the webpage
new_soup = BeautifulSoup(new_webpage.content, "html.parser")
print(new_soup)


title = new_soup.find("span", attrs={"id": 'productTitle'}).text.strip()
print(title)


new_soup.find(
    "span",
    attrs={
        "class": "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"
    },
)

new_soup.find("span", attrs={"class": "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"}, ).find(
    "span", attrs={"class": "a-offscreen"}).text

# Now need to find the rating of the product
new_soup.find("span", attrs={"class": "a-icon-alt"}).text
