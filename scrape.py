
import requests
from bs4 import BeautifulSoup
import json

valuesList = {}
r = requests.get("https://tailwindcss.com/docs/installation")
soup = BeautifulSoup(r.content, 'html.parser')
data = soup.findAll("a", attrs={'class': 'block border-l pl-4 -ml-px border-transparent hover:border-slate-400 dark:hover:border-slate-500 text-slate-700 hover:text-slate-900 dark:text-slate-400 dark:hover:text-slate-300'})
for div in data[20:40]:
    if(div.get("href").startswith("/")):
        b = requests.get("https://tailwindcss.com/" + div.get("href"))
        Ssoup = BeautifulSoup(b.content, 'html.parser')
        tables = Ssoup.findAll("tbody", attrs={'class': 'align-baseline'})

        for table in tables:
            if(len(table) > 0):
                trs = table.findAll("tr")
                for tr in trs:
                    if(len(tr) > 0):
                        tds = tr.findAll("td")
                        if(len(tds) == 2):
                            valuesList[tds[0].text] = tds[1].text
                        # for td in tds:
                            # print(td.text)

with open('values.json', 'w') as f:
    json.dump(valuesList, f)