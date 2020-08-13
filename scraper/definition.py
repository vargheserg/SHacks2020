from bs4 import BeautifulSoup
import urllib.request
import json
# Varghese Rony George




base_url = "https://www.scotiaitrade.com/en/direct-investing-and-online-trading/investment-types/bonds.html"


def parse_definition(url):
    definitions = {}
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    
    reference = soup.find('div', class_='section--content').find('div', class_='accordian-container').find('div', class_='button--bellow-cdfdbf0f-db21-4cbe-94fd-874e2173c1e7-body')
    glossary = reference.find('div', class_='cmp cmp-text').find_all('p')
    for def in glossary
    key = def.find('b').get_text().strip()
    definitions[key]= def.find('br').next_siblings
    return definitions
print(parse_definition(base_url))