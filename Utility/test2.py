from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import pandas as pd
import json
url = "https://twlolstats.com/summoner/?summoner=c.y"


driver = webdriver.Edge(
    executable_path=r"C:\Users\Yohoo\Downloads\msedgedriver.exe")
driver.maximize_window()
driver.get(url)

gather2 = []
x = [i for i in range(2, 15) if i != 15]
for i in x:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    str = '#game{} input'.format(i)
    driver.find_elements_by_css_selector(str)[0].click()
    sleep(1)
    str = '#game{} table tbody td:nth-child(3) div:nth-child(1) b'.format(i)
    isWin = driver.find_elements_by_css_selector(str)
    str2 = '#game{} table tbody td:nth-child(3) div:nth-child(2)'.format(i)
    Kind = driver.find_elements_by_css_selector(str2)
    str3 = '#game{} table tbody td:nth-child(3) div:nth-child(3)'.format(i)
    FinshTime = driver.find_elements_by_css_selector(str3)
    str4 = '#game{} table tbody td:nth-child(3) div:nth-child(4)'.format(i)
    TotalHour = driver.find_elements_by_css_selector(str4)
    final1 = [{"項目": g + 1, "輸贏": isWin[g].text, "類型": Kind[g].text,
               "結束時間": FinshTime[g].text, "遊玩時間": TotalHour[g].text} for g, v in enumerate(isWin)]
    gather2.append({"頁": i, "結果": final1})


isWin = driver.find_elements_by_css_selector(
    'table:nth-child(2) tbody td:nth-child(3) div:nth-child(1) b')
Kind = driver.find_elements_by_css_selector(
    'table:nth-child(2) tbody td:nth-child(3) div:nth-child(2)')
FinshTime = driver.find_elements_by_css_selector(
    'table:nth-child(2) tbody td:nth-child(3) div:nth-child(3)')
TotalHour = driver.find_elements_by_css_selector(
    'table:nth-child(2) tbody td:nth-child(3) div:nth-child(4)')

final1 = [{"項目": g + 1, "輸贏": isWin[g].text, "類型": Kind[g].text,
           "結束時間": FinshTime[g].text, "遊玩時間": TotalHour[g].text} for g, v in enumerate(isWin)]
gather2.insert(0, {"頁": 1, "結果": final1})


with open(r'C:\Users\Yohoo\OneDrive\桌面\myFlaskWebApi\Utility\data.json', 'w') as outfile:
    json.dump(gather2, outfile, sort_keys=True, indent=4,
              ensure_ascii=False)
# pd.DataFrame(gather).to_csv(
#     r'C:\Users\Yohoo\OneDrive\桌面\myFlaskWebApi\Utility\file.csv', encoding="utf_8_sig")


# url = "https://statementdog.com/screeners/pe_ranking"
# # Use Chrome

# driver = webdriver.Edge(
#     executable_path=r"C:\Users\Yohoo\Downloads\msedgedriver.exe")

# driver.get(url)
# driver.find_element_by_id("member-login").click()
# driver.find_elements_by_class_name('g-login')[0].click()
# sleep(3)
# driver.find_elements_by_id("identifierId")[0].send_keys("Yohoo0987@gmail.com")
# driver.find_elements_by_id('identifierNext')[0].click()
# sleep(3)
# # print(driver.find_element_by_tag_name('button'))
# # driver.find_element_by_tag_name('button').click()
# # sleep(3)

# driver.find_elements_by_id("identifierId")[0].send_keys("Yohoo0987@gmail.com")
# driver.find_elements_by_id('identifierNext')[0].click()
# sleep(3)
# driver.find_element_by_xpath('//input[@type="password"]').send_keys("Home7996")
# driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
# sleep(3)
# driver.find_element_by_id("stockid").send_keys("2377")
# driver.find_elements_by_class_name('icon-font-search')[0].click()
# sleep(3)


# class container:
#     def __init__(self, value0, value1, value2, value3, value4):
#         self.本益比 = value0
#         self.殖利率 = value1
#         self.股價淨值比 = value2
#         self.近四季EPS = value3
#         self.近四季ROE = value4


# data = container(driver.find_elements_by_class_name('v')[0].text,
#                  driver.find_elements_by_class_name('v')[1].text,
#                  driver.find_elements_by_class_name('v')[2].text,
#                  driver.find_elements_by_class_name('v')[3].text,
#                  driver.find_elements_by_class_name('v')[4].text)
# print(data.本益比, data.殖利率)
