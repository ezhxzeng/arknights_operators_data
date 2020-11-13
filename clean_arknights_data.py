import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://gamepress.gg/arknights/tools/interactive-operator-list#tags=stats"
req_result = requests.get(url)
soup = BeautifulSoup(req_result.content, 'html.parser')
operators = soup.find_all("tr", class_="operators-row")
df = pd.DataFrame([o.attrs for o in operators])

desired_columns = [
    'data-rarity',
    'data-name',
    'data-hp-trust',
    'data-atk-trust',
    'data-def-trust',
    'data-hp-potential',
    'data-atk-potential',
    'data-def-potential',
    'data-hp-full',
    'data-atk-full',
    'data-def-full',
    'data-hp',
    'data-atk',
    'data-def',
    'data-profession',
    'data-target',
    'data-damagetype',
    'data-availserver',
    'data-created',
    'data-dp-cost',
    'data-atk-time',
    'data-res',
    'data-block',
    'data-redeploy',
    'data-position'
]

df = df[desired_columns]

desired_columns = [name[5:] for name in desired_columns]
df.columns = desired_columns

df.to_csv("arknights_operators.csv", index=None)