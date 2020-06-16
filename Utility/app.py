import requests
from bs4  import BeautifulSoup as bs
import pandas as pd
import os
from datetime import datetime

page = requests.get('https://rate.bot.com.tw/xrt?Lang=zh-TW');
soup = bs(page.text, 'html.parser');

currentSell = soup.select('td[data-table="本行現金賣出"]')

currentBuy = soup.select('td[data-table="本行現金買入"]')
currencyTitle = soup.select('.hidden-phone')


getTitle = [];
getChineseTitle =[];
getCurrencySell = [];
getCurrencyBuy =[];

for i in currencyTitle :
    combine = i.text.strip()
    twostrings = combine.split(' ')
    title2 = str(twostrings[0])
    getChineseTitle.append(title2)
    getTitle.append(twostrings[1])
for i in currentSell:
    getCurrencySell.append(i.text.strip())
for i in currentBuy:
    getCurrencyBuy.append(i.text.strip())


getCurrencySell = list(dict.fromkeys(getCurrencySell))
getCurrencyBuy = list(dict.fromkeys(getCurrencyBuy))
collection = {'Currencytitle' : getTitle, 'CurrencyBuy' :getCurrencyBuy,'CurrencySell' : getCurrencySell, 'CurrencyChineseTitle' :getChineseTitle }

tabledata0 = pd.DataFrame(collection)
file_dir = os.path.dirname(os.path.abspath(__file__))
csv_folder = 'everyday_data';
now = datetime.now()
filename = now.strftime("%Y%m%d-%H%M%S") + '.csv';
file_path = os.path.join(file_dir, csv_folder, filename);
tabledata0.to_csv(file_path, index=None,encoding="BIG5")
