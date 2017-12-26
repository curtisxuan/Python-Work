import os, requests
from selenium import webdriver
import time, json
from PIL import Image
from yundama import identify


"""using chrome"""
# chromedriver = "/usr/local/bin/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)

"""using phantomjs"""
driver = webdriver.PhantomJS()  # desired_capabilities=dcap)

"""logging in"""
driver.set_window_size(1080, 880)
driver.get("http://mousehuntgame.com")
username = driver.find_element_by_name("accountName")
username.send_keys("curtisxuan")
password = driver.find_element_by_name("password")
password.send_keys("uzumakinaruto")
loginButton = driver.find_element_by_name("doLogin")
loginButton.click()

"""get cookie"""
# cookie={}
# for i in driver.get_cookies():
#     cookie[i["name"]] = i["value"]
# print cookie
#
# html = requests.get("http://www.mousehuntgame.com", cookies=cookie)
# print html.content
# driver.exit()

"""autobot"""
time.sleep(3)
count = 0
while (True):
    horn = driver.find_element_by_id("hornArea")
    horn.click()
    print driver.find_element_by_id("hornMessage").text

    """clear KR"""
    if "Click here to claim" in driver.find_element_by_id("hornMessage").text:
        print "KR IS HERE"
        """using phantomjs"""
        driver2 = webdriver.PhantomJS()  # desired_capabilities=dcap)
        driver2.set_window_size(1080, 880)
        driver2.get("http://mousehuntgame.com")
        username = driver2.find_element_by_name("accountName")
        username.send_keys("curtisxuan")
        password = driver2.find_element_by_name("password")
        password.send_keys("uzumakinaruto")
        loginButton = driver2.find_element_by_name("doLogin")
        loginButton.click()
        image = driver2.find_element_by_id("puzzleImage")
        driver2.save_screenshot("bb.png")
        x = int(image.location["x"])
        y = int(image.location["y"])
        im = Image.open("bb.png")
        im.crop((x - 5, y, 150 + x, y + 50)).save("bc.png")
        code_txt=""
        if count < 2:
            code_txt = identify()
        count=count+1
        code = driver2.find_element_by_id("puzzle_answer")
        code.send_keys(code_txt)
        submit = driver2.find_element_by_id("puzzle_submit")
        submit.click()
        time.sleep(3)
        driver2.quit()
        driver.get("http://mousehuntgame.com")
    if not "Click here to claim" in driver.find_element_by_id("hornMessage").text:
        count = 0
    time.sleep(5)

"""find lucky tower"""
# img = driver.find_element_by_class_name("riftBristleWoodsHUD-chamberTitle")
# x = int(img.location["x"])
# y = int(img.location["y"])
# print x
# print y
# driver.save_screenshot("aa.png")
# im = Image.open("aa.png")
# im.crop((x+60, y+20 , x+200 , y+40 )).save("ab.png")
