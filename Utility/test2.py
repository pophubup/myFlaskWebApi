from selenium import webdriver
from time import sleep
import json


class DATOInforLoader():
    def __init__(self, username, filepath, totalpage):
        self.url = "https://twlolstats.com/summoner/?summoner={}".format(
            username)
        self.path = filepath
        self.totalpage = totalpage

    def GetDataAsJson(self):
        driver = webdriver.Edge(
            executable_path=r"C:\Users\Yohoo\Downloads\msedgedriver.exe")
        driver.maximize_window()
        driver.get(self.url)
        gather2 = []
        x = [i for i in range(2, self.totalpage) if i != self.totalpage]
        for i in x:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
            str = '#game{} input'.format(i)
            driver.find_elements_by_css_selector(str)[0].click()
            sleep(1)
            str = '#game{} table tbody td:nth-child(3) div:nth-child(1) b'.format(
                i)
            isWin = driver.find_elements_by_css_selector(str)
            str2 = '#game{} table tbody td:nth-child(3) div:nth-child(2)'.format(
                i)
            Kind = driver.find_elements_by_css_selector(str2)
            str3 = '#game{} table tbody td:nth-child(3) div:nth-child(3)'.format(
                i)
            FinshTime = driver.find_elements_by_css_selector(str3)
            str4 = '#game{} table tbody td:nth-child(3) div:nth-child(4)'.format(
                i)
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
            with open(self.path, 'w') as outfile:
                json.dump(gather2, outfile, sort_keys=True, indent=4,
                          ensure_ascii=False)
        return "finish"


obj = DATOInforLoader(
    "c.y", r'C:\Users\Yohoo\OneDrive\桌面\myFlaskWebApi\Utility\data.json', 30)
print(obj.GetDataAsJson())
