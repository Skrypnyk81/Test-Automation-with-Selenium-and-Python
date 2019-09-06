from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(int(x))

    browser.execute_script('window.scrollBy(0, 100);')

    element = browser.find_element_by_css_selector('#answer')
    element.send_keys(str(y))

    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
