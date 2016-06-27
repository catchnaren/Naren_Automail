#import re
import sys
#import tailer
from datetime import datetime
from selenium import webdriver
#from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.common.action_chains import ActionChains

#display = Display(visible=0, size=(800, 600))
#display.start()

class loginDriver:
    def webDriver(self, url, user, passwd, item):
        driver = webdriver.Chrome('C:\Users\chromedriver')
        driver.get(url)
        emailElem = driver.find_element_by_id('ap_email')
        emailElem.send_keys(user)
        passElem = driver.find_element_by_id('ap_password')
        passElem.send_keys(passwd)
        passElem.submit()
        driver.implicitly_wait(150)
        bal = driver.find_element_by_xpath(item)
        global currentBal
        currentBal = [bal.text[1:], bal.text[4:], bal.text[2:]]
        #print (bal.text)
        driver.close()

    def autoEmail(self, emailUsr, index, forex):
        i = datetime.now()
        today = i.strftime('%d/%m/%Y %I:%M')
        sub = 'Account Balance Info'
        bodyMsg = 'Account Balance as of ' + today + '\n\nCurrent balance for ' + emailUsr + ' is: ' + currentBal[index] + forex
        #header = 'To:' + to + '\n' + 'From:' + fromUsr + '\n' + 'Subject:' + sub + '\n'
        #print (header)
        msg = '\n' + bodyMsg + '\n\n'
        sys.stdout = open('Balance.txt','a')
        print (msg)

        '''today = str(datetime.date.today())
        dateRegex = re.compile(r'\d\d/\d\d/\d\d\d\d')
        f = open('test.txt')
        for line in f:
            line = line.rstrip()
            mo = dateRegex.search(line)
            if mo.group() == today:
                fhand = open('balance.txt', 'a')
                fhand.write(line)
                fhand.close'''

    def currentFile(self, f):
        msg2 = tailer.tail(open(f), 3)
        fhand = open('test.txt', 'w')
        fhand.write(msg)
        fhand.close

def main():
    try:
        payload = {
        'URL1' : 'https://www.amazon.co.uk/gp/css/gc/balance?ie=UTF8&ref_=ya_view_gc&',
        'URL2' : 'https://www.amazon.de/gp/css/gc/balance?ie=UTF8&ref_=ya_view_gc',
        'URL3' : 'https://www.amazon.co.jp/gp/css/gc/balance?ie=UTF8&ref_=ya_view_gc',
        'USERNAME1' : '*****', # User account
        'PASSWORD1' : '*****', # Account Password
        'USERNAME2' : '*****',
        'PASSWORD2' : '*****',
        'USERNAME3' : '*****',
        'PASSWORD3' : '*****',
        'item1' : '/html/body/div[5]/table/tbody/tr/td[2]/div[1]/div[1]/div/div/table/tbody/tr/td[1]/h3/span',
        'item2' : '/html/body/div[5]/table/tbody/tr/td[2]/div[1]/div[1]/div/div/table/tbody/tr/td[1]/h3/span',
        'item3' : '/html/body/div[5]/table/tbody/tr/td[2]/div/div[1]/div/div/table/tbody/tr/td[1]/h3/span',
        }

        logIn = {
        'USER1' : 'UK Account',
        'USER2' : 'DE Account',
        'USER3' : 'JP Account'
        }

        ukAccount = loginDriver()
        deAccount = loginDriver()
        jpAccount = loginDriver()
        ukAccount.webDriver(payload['URL1'], payload['USERNAME1'], payload['PASSWORD1'], payload['item1'])
        ukAccount.autoEmail(logIn['USER1'], 0, 'GBP')
        deAccount.webDriver(payload['URL2'], payload['USERNAME2'], payload['PASSWORD2'], payload['item2'])
        deAccount.autoEmail(logIn['USER2'], 1, 'EURO')
        jpAccount.webDriver(payload['URL3'], payload['USERNAME3'], payload['PASSWORD3'], payload['item3'])
        jpAccount.autoEmail(logIn['USER3'], 2, 'JPY')

    except Exception, e:
        print str(e)

if __name__ == '__main__':
    main()
