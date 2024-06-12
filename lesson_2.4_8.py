import time, math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")
   
    # создаем условие чтобы нажатие на кнопку "book" происходило только при цене "$100"
    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.ID, "book")
    button.click()
    # считаем чему равен результат функции
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    # находим селектор "x = ..." и превращаем в число
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # задаем переменную для результата функции
    y = calc(x)
    # вписываем получившийся ответ в поле для ответа
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    # отправляем получившийся результат
    button = browser.find_element(By.ID, "solve")
    button.click()
    print(browser.switch_to.alert.text)
 
finally:
    time.sleep(15)
    browser.quit()