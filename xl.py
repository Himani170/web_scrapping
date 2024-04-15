import requests 
from bs4 import BeautifulSoup 
import pandas as pd

url = "https://chandigarhtourism.gov.in/pages/page/rock-garden"

r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")

timings = soup.find_all("tr")
data = {}

# making columns as th and rows as td
for x in timings:
    th = x.find_all("th")
    td = x.find_all("td")
    for i in range(len(th)):
        if len(td) > 0:
            key = th[i].text
            value = td[i].text
            if key in data:
                data[key].append(value)
            else:
                data[key] = [value]

df = pd.DataFrame(data)
df.to_csv('rock_garden_data.csv', index=False)
