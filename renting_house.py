from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # нажимаем на кнопку и переходим на новую страницу
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    browser.switch_to.window(browser.window_handles[1])

    # считываем x со страницы и вычисляем значение выражения
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # вставляем ответ в поле для ввода
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()