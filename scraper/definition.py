from bs4 import BeautifulSoup
import urllib.request
import json
# Varghese Rony George




base_url = "https://www.scotiaitrade.com/en/direct-investing-and-online-trading/investment-types/gics.html"
term='GICs'

def parse_definition(url,term):
    definitions = {}
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')    
    # print(soup)
    # the digit is the nth accordian on the page
    digit = 1
    reference = soup.find_all( class_='button--bellow-body-content')[digit].find_all('div')[0].find_all('p')
    glossary =[[t.replace('\xa0', '') for t in i.text.splitlines()] for i in reference]
    
    def filterWaste(l):
        if (len(l)<=1):
            return False
        return True
    glossary=list(filter(filterWaste,glossary))
    for i in glossary:
        if(len(i)!=2):
            print(i)


  

    out = {}
    for xe in glossary:
        out[xe[0]]={"defi":xe[1], "mention":{"link":base_url,"term":term}}

    with open('definitions.json') as fr:    
        newData = {**out, **json.load(fr)} 
    with open('definitions.json', 'w') as fp:
        json.dump(newData, fp, sort_keys=True, indent=4)

    return glossary


print(parse_definition(base_url,term))

