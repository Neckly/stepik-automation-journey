from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # вычисляем значение выражения
    y = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)

    # выбираем нужное значение в списке
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))

    # Нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()