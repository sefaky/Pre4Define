import time
from selenium import webdriver
import test
import dbManager

from colorthief import ColorThief
from urllib.request import urlopen
import io
import sys

from colour import Color

def get_Color(url):
    fd = urlopen(url)
    f = io.BytesIO(fd.read())
    color_thief = ColorThief(f)
    return color_thief.get_palette(color_count=2)[:-1]

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

def rgb_to_hsl(r,g,b):
    c = Color(rgb=(r/255, g/255, b/255))
    if(r>g and r>b):
        if(g>b):
            hue= (c.green-c.blue)/(c.red-c.blue)
        else:
            hue = (c.green - c.blue)/(c.red - c.green)
    elif (g > r and g > b):
        if (r > b):
            hue = (c.blue - c.red)/(c.green - c.blue)
        else:
            hue = (c.blue - c.red)/(c.green - c.red)
        hue += 2
    else:
        if (r > g):
            hue = (c.red - c.green)/(c.blue - c.green)
        else:
            hue = (c.red - c.green)/(c.blue - c.red)
        hue += 4

    hue *= 60

    if(hue < 0):
        hue += 360

    return '({}, {}%, {}%)'.format(int(hue),int((round(c.saturation,2))*100),int((round(c.luminance,2))*100))


def getTopHundred():
    category = "Music"
    driver_path = r'C:\Users\Gokturk\Desktop\pythonProject\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    time.sleep(2)  # see the result
    driver.get(r'C:\Users\Gokturk\PycharmProjects\page.html')
    gameNames = []
    count = 2
    while(count<101):
        gameNames.append(driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[5]/div[2]/div/div[2]/div[1]/div[8]/table/tbody/tr[{}]/td[4]/a".format(str(count))).text)
        count+=1

    time.sleep(2)  # see the result
    count = 56  #kaçta takıldıysa o numarayı yaz baslangıc 0  --- consolda ne yazıyorsa 1 fazlası

    driver.get(r'https://play.google.com/store/apps/details?id=com.redhands.twoplayergames&hl=en'.format(gameNames[count - 1]))
    time.sleep(2)  # see the result
    while count<100:
        print(count)
        driver.get(r'https://play.google.com/store/search?q={}&c=apps&hl=en'.format(gameNames[count]))
        time.sleep(2)  # see the result,
        if len(driver.find_elements_by_xpath("//div[contains(text(), '{}')]".format(gameNames[count])))>0:
            driver.find_element_by_xpath("//div[contains(text(), '{}')]".format(gameNames[count])).click()
        else:
            count+=1
            driver.get(r'https://play.google.com/store/search?q={}&c=apps&hl=en'.format(gameNames[count]))
            time.sleep(2)  # see the result
            driver.find_element_by_xpath("//div[contains(text(), '{}')]".format(gameNames[count])).click()
        time.sleep(2)  # see the result
        ct = 0
        counter = 0
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        ##################################

        pegi = int(driver.find_element_by_xpath("//div[contains(text(), 'PEGI')]").text[5:])
        commentcount = int(driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/div/main/div/div[1]/c-wiz/div[1]/span/span[2]").text.replace(',',''))
        commentscore = float(driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/div/main/div/div[1]/c-wiz/div[1]/div[1]").text)
        appsizemb = driver.find_element_by_xpath("//div[contains(text(), 'Size')]/following-sibling::span/div/span").text


        if("Cihaza göre" in appsizemb):
            appsizemb = -1
        elif("M" in appsizemb):
            appsizemb = int(float(appsizemb[:-1]))
        else:
            appsizemb = int(-1)
        appprice = -1
        downloads = driver.find_element_by_xpath("//div[contains(text(), 'Installs')]/following-sibling::span/div/span").text
        downloads = downloads.replace(',','')
        downloads = downloads[:-1]
        downloads = int(downloads)

        ranking = count+1

        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        while len(driver.find_elements_by_xpath("//button[@data-screenshot-item-index='{}']".format(ct))) > 0 and counter<2:
            try:
                uri = driver.find_element_by_xpath("//button[@aria-label='Open screenshot {}']/img".format(ct)).get_attribute("src")
                print(uri)
                wordList = test.detect_text_uri(uri)
                if len(wordList)>1:
                    for a in wordList:
                        dbManager.push_new_word_to_db(a, category, pegi, commentcount, commentscore, appsizemb, downloads, ranking)

            except:
                try:
                    uri = driver.find_element_by_xpath("//button[@aria-label='Open screenshot {}']/img".format(ct)).get_attribute("srcset")
                    print(uri.split(' ', 1)[0])
                    wordList = test.detect_text_uri(uri)
                    if len(wordList) > 1:
                        for a in wordList:
                            dbManager.push_new_word_to_db(a, category, pegi, commentcount, commentscore, appsizemb, downloads, ranking)

                except:
                    uri = driver.find_element_by_xpath("//button[@aria-label='Open screenshot {}']/img".format(ct)).get_attribute("data-srcset")
                    print(uri.split(' ', 1)[0])
                    wordList = test.detect_text_uri(uri)
                    if len(wordList) > 1:
                        for a in wordList:
                            dbManager.push_new_word_to_db(a, category, pegi, commentcount, commentscore, appsizemb, downloads, ranking)

            rgbValue = get_Color(uri)
            hexFirst = rgb2hex(rgbValue[0][0],rgbValue[0][1],rgbValue[0][2])
            hexSecond = rgb2hex(rgbValue[1][0],rgbValue[1][1],rgbValue[1][2])
            hslFirst = rgb_to_hsl(rgbValue[0][0],rgbValue[0][1],rgbValue[0][2])
            hslSecond = rgb_to_hsl(rgbValue[1][0],rgbValue[1][1],rgbValue[1][2])
            dbManager.push_new_color_to_db(category,pegi,commentcount,commentscore,appsizemb,downloads,ranking,str(rgbValue[0]),hexFirst,hslFirst,str(rgbValue[1]),hexSecond,hslSecond)

            ct += 1
            counter+=1
            time.sleep(2)
        count += 1
        time.sleep(5)  # see the result

getTopHundred()