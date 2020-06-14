from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

def get_exchangeRate():
    d = pq("https://rate.bot.com.tw/xrt?Lang=zh-TW").find('table[title="牌告匯率"] tbody');
    currentSell = d.find('td[data-table="本行現金賣出"]');
    currentBuy =d.find('td[data-table="本行現金買入"]');
    currencyTitle =d.find('.hidden-phone');
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
    return collection