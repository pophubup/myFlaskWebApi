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

def get_data_from_EPSList():
     d = pq("https://statementdog.com/screeners/pe_ranking").find('#ranking-list-body');
     rank = d.find('li:eq(0)').text();
     stockName= d.find('li:eq(1)').text();
     peRatio = d.find('li:eq(2)').text();
     stockPrice = d.find('li:eq(3)').text();
     eps_with4years = d.find('li:eq(4)').text();
     
     return {"rank": rank.split(' '), "stockName": stockName, "peRatio":peRatio.split(' '), "stockPrice" : stockPrice.split(' '), "eps_with4years": eps_with4years.split(' ')};

def get_single_data_from_website(id):
     d = pq("https://statementdog.com/analysis/tpe/" + id); 
     return  { "EPS" : d.find('.v')[0].text, 
               "Rate" : d.find('.v')[1].text, 
               "Net value" : d.find('.v')[2].text ,
               "YOY" : d.find('.v')[3].text,
               "EPS" : d.find('.v')[4].text,
               "ROE" : d.find('.v')[5].text};