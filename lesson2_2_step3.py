from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x = browser.find_element_by_css_selector("#num1").text
    y = browser.find_element_by_css_selector("#num2").text
    total = str(int(x) + int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(total)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
