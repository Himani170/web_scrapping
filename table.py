import requests 
from bs4 import BeautifulSoup 
import pandas as pd

url = "https://chandigarhtourism.gov.in/pages/page/rock-garden"

r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")

timings = soup.find_all("tr")
data = {}

# print(timings)
# making columns as th and rows as td
for x in timings:
    th = x.find_all("th")
    td = x.find_all("td")
    for i in range(len(th)):
        print(th[i])
        if len(td)>0:
            print(td[i])
            data[th[i].text] = td[i].text

    # print("========")



# print(data)
            
with open('rock_garden_data.csv', 'w') as file:
    for key, value in data.items():
        file.write('%s: %s\n' % (key, value))

# # data = {'Timings': timings, 'Entry Fee': fee, 'Open Status': open_status}
# df = pd.DataFrame(data)
# df.to_csv('rock_garden_data.csv', index=False)
