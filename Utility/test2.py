from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from time import sleep

imdb_home = "https://statementdog.com/screeners/pe_ranking"
driver = webdriver.Chrome(executable_path="C:\\Users\\teres\\Desktop\\chromedriver.exe") #Use Chrome
driver.get(imdb_home);
driver.find_element_by_id("member-login").click();
driver.find_elements_by_class_name('g-login')[0].click();
sleep(3);
driver.find_elements_by_id("identifierId")[0].send_keys("Yohoo0987@gmail.com");
driver.find_elements_by_id('identifierNext')[0].click();
sleep(3);
driver.find_element_by_xpath('//input[@type="password"]').send_keys("Home7996");
driver.find_element_by_xpath('//*[@id="passwordNext"]').click();
sleep(3);
driver.find_element_by_id("stockid").send_keys("2377");
driver.find_elements_by_class_name('icon-font-search')[0].click();
sleep(3);
class container:
    def __init__(self, value0, value1, value2, value3, value4):
            self.本益比 = value0
            self.殖利率 = value1
            self.股價淨值比 = value2
            self.近四季EPS = value3
            self.近四季ROE = value4

data = container(driver.find_elements_by_class_name('v')[0].text, 
          driver.find_elements_by_class_name('v')[1].text,
          driver.find_elements_by_class_name('v')[2].text,
          driver.find_elements_by_class_name('v')[3].text,
          driver.find_elements_by_class_name('v')[4].text)
print(data.本益比, data.殖利率)


