######### Importing libraries #########
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import names
import winsound
start_time = time.time()
######### Starting browser #########
options = webdriver.ChromeOptions()
options.add_argument("--enable-javascript")
options.headless = False
######### Number of accounts to create #########
n = int(input("How many accounts do you wish to create?"))
######### Going to SignUp page & filling in #########
l = []
c = 0
for i in range(n):
    acc = []
    browser = webdriver.Chrome(options=options)
    first = names.get_first_name()
    last = names.get_last_name()
    user = first + last
    browser.get(('https://a1.zxd.workers.dev/#form'))
    time.sleep(2)
    lastname = browser.find_element_by_name('lastname')
    time.sleep(3)
    lastname.click()
    lastname.send_keys(first)
    firstname = browser.find_element_by_name('firstname')
    firstname.click()
    firstname.send_keys(last)
    username = browser.find_element_by_name('username')
    username.click()
    username.send_keys(user)
    username.submit()
    time.sleep(2)
    confirm = browser.find_element_by_link_text('确认')
    confirm.click()
    time.sleep(5)
    emails = browser.find_element_by_xpath("//input[@class='mdui-textfield-input cremail']")
    emails.click()
    email = emails.get_attribute("value")
    acc.append(email)
    passwords = browser.find_element_by_xpath("//input[@class='mdui-textfield-input crpass']")
    passwords.click()
    password = passwords.get_attribute("value")
    acc.append(password)
    l.append(acc)
    time.sleep(1)
    c += 1
    print(c, "Almost done")
    browser.quit()
file = open("Accounts.txt", "a")
c = 0
for a in l:
    file.write(a[0])
    file.write(":")
    file.write(a[1])
    file.write("\n")
    c += 1
    print(c, "done")
file.close()
winsound.Beep(2500, 2000)
print("Done. Give a big hand to the developer :)")
print("This took around --- %s seconds ---" % (time.time() - start_time))
