import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class TestSomething(unittest.TestCase):

    def setUp(self):
        self.login = input('Введите свой логин: ')
        self.passwd = input('Введите свой пароль: ')
        self.driver = webdriver.Chrome()
        self.url = 'https://passport.yandex.ru/auth'

    def test_selenium(self):
        driver = self.driver
        driver.get(self.url)
        assert driver.title == 'Авторизация', 'Сайт не открывается'
        login = driver.find_element(By.NAME, 'login')
        login.send_keys(self.login)
        driver.find_element(By.ID, 'passp:sign-in').click()
        driver.implicitly_wait(3)
        try:
            driver.find_element(By.ID, 'field:input-login:hint')
            res = True
        except NoSuchElementException:
            res = False
        self.assertFalse(res, 'Такого аккаунта нет')
        passwd = driver.find_element(By.NAME, 'passwd')
        passwd.send_keys(self.passwd)
        driver.find_element(By.ID, 'passp:sign-in').click()
        driver.implicitly_wait(3)
        try:
            driver.find_element(By.ID, 'field:input-passwd:hint')
            res = True
        except NoSuchElementException:
            res = False
        self.assertFalse(res, 'Неверный пароль')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()




