import requests
from bs4 import BeautifulSoup 
import pandas as pd


URL = 'https://lol.fandom.com/wiki/LCS/2023_Season/Spring_Season/Picks_and_Bans'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "lxml")

tbl = soup.find('table',attrs={'id': 'pbh-table'})

data = []
info = {}

for tr in tbl.find_all("tr"):
    td = tr.find_all('td')
    if not td:
        continue
    info['patch'] = td[4].text
    if td[1].get('class'):
        info["winside"] = 'Blue'
    else:
        info["winside"] = 'Red'
    info['BB1'] = td[5].get('data-c1')
    info['RB1'] = td[6].get('data-c1')
    info['BB2'] = td[7].get('data-c1')
    info['RB2'] = td[8].get('data-c1')
    info['BB3'] = td[9].get('data-c1')
    info['RB3'] = td[10].get('data-c1')
    info['BP1'] = td[11].get('data-c1')
    info['RP1'] = td[12].get('data-c1')
    info['RP2'] = td[12].get('data-c2')
    info['BP2'] = td[13].get('data-c2')
    info['BP3'] = td[13].get('data-c2')
    info['RP3'] = td[14].get('data-c1')
    info['RB4'] = td[15].get('data-c1')
    info['BB4'] = td[16].get('data-c1')
    info['RB5'] = td[17].get('data-c1')
    info['BB5'] = td[18].get('data-c1')
    info['RP4'] = td[19].get('data-c1')
    info['BP4'] = td[20].get('data-c1')
    info['BP5'] = td[20].get('data-c2')
    info['RP5'] = td[21].get('data-c1')
    data.append(info.copy())
df = pd.DataFrame(data)
name ='./data/draft.csv'
df.to_csv(name)

