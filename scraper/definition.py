from bs4 import BeautifulSoup
import urllib.request
import json
# Varghese Rony George




base_url = "https://www.scotiaitrade.com/en/direct-investing-and-online-trading/investment-types/bonds.html"
ido='button--bellow-6ea716ab-ade3-4607-93ce-29b5055e2804-body'

def parse_definition(url,idOFGlossary):
    definitions = {}
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    # print(soup)
    # the digit is the nth accordian on the page
    digit = 1
    reference = soup.find_all( class_='button--bellow-body-content')[digit].find_all('div')[0].find_all('p')
    glossary =[[t.replace('\xa0', '') for t in i.text.splitlines()] for i in reference]
   

    def filterWaste(l):
        for item in l:
            if (len(item)<=1):
                return False
        return True
    glossary=list(filter(filterWaste,glossary))
    # reference = reference.find(attrs={"role" : "tabpanel"})
    # reference=reference.find('div').find('div')

    # glossary = reference.find_all('p')
    # for define in glossary:
    #     key = define.find('b').get_text().strip()
    #     definitions[key]= define.find('br').next_siblings
    # return definitions
    return glossary



print(parse_definition(base_url,ido))