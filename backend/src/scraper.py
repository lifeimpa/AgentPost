# Scraper
import requests
from bs4 import BeautifulSoup

def scrape(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    products = []
    # extract logic
    return products
