from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем x со страницы и вычисляем значение выражения
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # вставляем ответ в поле для ввода
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # нажимаем на галку "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # нажимаем кнопку Robot rule
    robots_rule_button = browser.find_element(By.ID, "robotsRule")
    robots_rule_button.click()

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()