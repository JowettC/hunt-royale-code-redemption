from bs4 import BeautifulSoup
import requests
import os


def getCodes():
    page = requests.get("https://ucngame.com/codes/hunt-royale-redeem-codes/")
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="wp-block-table").find_all("tr")
    code = []
    description = []
    codeDesc = []
    # print(results[1].prettify())
    for i in range(1,len(results)):
        code = results[i].find_all("td")
        code = code[0].find("strong").getText()
        description = results[i].find_all("td")[1].getText()
        codeDesc.append(code + " --- " + description)
    return codeDesc

# print(getCodes())