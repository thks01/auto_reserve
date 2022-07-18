import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 크롬 드라이브를 불러온다.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)
driver.minimize_window()

driver.get('http://tzone.megastudy.net/new_main.asp')

driver.find_element(By.CSS_SELECTOR, 'body > form > div > div.login--radioWrap > label:nth-child(2) > input[type=radio]').click()
driver.find_element(By.CSS_SELECTOR, '#id').send_keys('id')
driver.find_element(By.CSS_SELECTOR, '#passwd').send_keys('pw')
driver.find_element(By.CSS_SELECTOR, '#sp_smsct').click()
driver.find_element(By.CSS_SELECTOR, '#sp_login').click()

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#a594').click()
driver.find_element(By.CSS_SELECTOR, '#aa602').click()

driver.switch_to.frame('ifrmContents')

while True:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    first_question = soup.select_one('body > div.list > div.rt1 > table > tbody > tr > td:nth-child(1)').text

    if first_question == '등록된 정보가 없습니다.':
        first_question = '0'

    try:
        if first_question.strip() > previous_question.strip():
            driver.find_element(By.CSS_SELECTOR, 'body > div.list > div.rt1 > table > tbody > tr > td:nth-child(5) > a').click()
            driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(3) > div.list--btnWrap > div > a:nth-child(1)').click()
    except:
        previous_question = first_question

    previous_question = first_question

    driver.switch_to.default_content()
    driver.find_element(By.CSS_SELECTOR, '#aa602').click()
    driver.switch_to.frame('ifrmContents')
