import requests
from bs4 import BeautifulSoup 
import pandas as pd


URL = 'https://lol.fandom.com/wiki/LCS/2023_Season/Spring_Season/Player_Statistics'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "lxml")

tbl = soup.find('table',class_="wikitable sortable spstats plainlinks hoverable-rows")
data = []
info = {}

stats = ['G', 'W', 'L', 'WR', 'K', 'D', 'A', 'KDA','CS','CS/M','G','G/M','DMG','DMG/M','KPAR','KS','GS','CP']

for tr in tbl.find_all("tr"):
    td = tr.find_all('td')
    if not td or len(td) < 10:
        continue

    print(td[1].text)
    info['player'] = td[1].text
    info['team'] = td[0].find('a').get('data-to-id')

    for i, stat in enumerate(stats):
        info[stat] = td[i+2].text

    data.append(info.copy())
df = pd.DataFrame(data)
name ='./data/playerstats.csv'
df.to_csv(name)

