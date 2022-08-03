from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *

link = "https://stellarburgers.nomoreparties.site/"


class TestRegistration:
    def test_registration_valid_data(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainLocators.button_login).click()
        driver.find_element(By.XPATH, AuthLocators.link_register).click()
        driver.find_element(By.XPATH, RegLocators.input_name).send_keys('Beerzerk')
        driver.find_element(By.XPATH, RegLocators.input_email).send_keys('test+testov+1@yandex.ru')
        driver.find_element(By.XPATH, RegLocators.input_password).send_keys('Qwerty001!')
        driver.find_element(By.XPATH, RegLocators.button_submit_reg).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, AuthLocators.button_submit_login), "Registration Error"

        driver.quit()

    def test_registration_invalid_password(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainLocators.button_login).click()
        driver.find_element(By.XPATH, AuthLocators.link_register).click()
        driver.find_element(By.XPATH, RegLocators.input_name).send_keys('Beerzerk')
        driver.find_element(By.XPATH, RegLocators.input_email).send_keys('test+testov+2@yandex.ru')
        driver.find_element(By.XPATH, RegLocators.input_password).send_keys('123456')
        driver.find_element(By.XPATH, RegLocators.button_submit_reg).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, RegLocators.text_invalid_password), "Registration successfully"

        driver.quit()


class TestAuthorization:
    def test_auth_main_page(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainLocators.button_login).click()
        driver.find_element(By.XPATH, AuthLocators.input_email).send_keys('test+testov+1@yandex.ru')
        driver.find_element(By.XPATH, RegLocators.input_password).send_keys('Qwerty001!')
        driver.find_element(By.XPATH, AuthLocators.button_submit_login).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, MainLocators.button_submit), "Authorization unsuccessfully"

        driver.quit()

    def test_auth_account(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainLocators.menu_item_account).click()
        driver.find_element(By.XPATH, AuthLocators.input_email).send_keys('test+testov+1@yandex.ru')
        driver.find_element(By.XPATH, RegLocators.input_password).send_keys('Qwerty001!')
        driver.find_element(By.XPATH, AuthLocators.button_submit_login).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, MainLocators.button_submit), "Authorization unsuccessfully"

        driver.quit()

    def test_auth_registration_page(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainLocators.menu_item_account).click()
        driver.find_element(By.XPATH, AuthLocators.link_register).click()
        driver.find_element(By.XPATH, RegLocators.link_login).click()
        driver.find_element(By.XPATH, AuthLocators.input_email).send_keys('test+testov+1@yandex.ru')
        driver.find_element(By.XPATH, RegLocators.input_password).send_keys('Qwerty001!')
        driver.find_element(By.XPATH, AuthLocators.button_submit_login).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, MainLocators.button_submit), "Authorization unsuccessfully"

        driver.quit()

    def test_auth_forgot_password_page(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainLocators.menu_item_account).click()
        driver.find_element(By.XPATH, AuthLocators.link_forgot_password).click()
        driver.find_element(By.XPATH, RegLocators.link_login).click()
        driver.find_element(By.XPATH, AuthLocators.input_email).send_keys('test+testov+1@yandex.ru')
        driver.find_element(By.XPATH, RegLocators.input_password).send_keys('Qwerty001!')
        driver.find_element(By.XPATH, AuthLocators.button_submit_login).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, MainLocators.button_submit), "Authorization unsuccessfully"

        driver.quit()

    def test_logout(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainLocators.button_login).click()
        driver.find_element(By.XPATH, AuthLocators.input_email).send_keys('test+testov+1@yandex.ru')
        driver.find_element(By.XPATH, RegLocators.input_password).send_keys('Qwerty001!')
        driver.find_element(By.XPATH, AuthLocators.button_submit_login).click()
        driver.find_element(By.XPATH, MainLocators.menu_item_account).click()
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, MainLocators.button_logout).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, AuthLocators.button_submit_login), "Logout unsuccessfully"

        driver.quit()


class TestMenuAndConstructor:
    def test_to_account(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainLocators.button_login).click()
        driver.find_element(By.XPATH, AuthLocators.input_email).send_keys('test+testov+1@yandex.ru')
        driver.find_element(By.XPATH, RegLocators.input_password).send_keys('Qwerty001!')
        driver.find_element(By.XPATH, AuthLocators.button_submit_login).click()
        driver.find_element(By.XPATH, MainLocators.menu_item_account).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, MainLocators.button_logout), "Account found unsuccessfully"

        driver.quit()

    def test_from_account_by_logo(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainLocators.button_login).click()
        driver.find_element(By.XPATH, AuthLocators.input_email).send_keys('test+testov+1@yandex.ru')
        driver.find_element(By.XPATH, RegLocators.input_password).send_keys('Qwerty001!')
        driver.find_element(By.XPATH, AuthLocators.button_submit_login).click()
        driver.find_element(By.XPATH, MainLocators.menu_item_account).click()
        driver.find_element(By.XPATH, MainLocators.menu_item_logo).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, MainLocators.button_submit), "Failed to open constructor by logo"

        driver.quit()

    def test_from_account_by_constructor(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainLocators.button_login).click()
        driver.find_element(By.XPATH, AuthLocators.input_email).send_keys('test+testov+1@yandex.ru')
        driver.find_element(By.XPATH, RegLocators.input_password).send_keys('Qwerty001!')
        driver.find_element(By.XPATH, AuthLocators.button_submit_login).click()
        driver.find_element(By.XPATH, MainLocators.menu_item_account).click()
        driver.find_element(By.XPATH, MainLocators.menu_item_constructor).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, MainLocators.button_submit), "Failed to open constructor by logo"

        driver.quit()

    def test_navigation_by_items_fillings(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainLocators.title_menu_fillings).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, MainLocators.title_fillings), "Failed to open constructor by Fillings"

        driver.quit()

    def test_navigation_by_items_sauces(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainLocators.title_menu_sauces).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, MainLocators.title_sauces), "Failed to open constructor by Sauces"

        driver.quit()

    def test_navigation_by_items_buns(self):
        driver = webdriver.Chrome()

        driver.get(link)
        driver.find_element(By.XPATH, MainLocators.title_menu_fillings).click()
        driver.find_element(By.XPATH, MainLocators.title_menu_buns).click()

        driver.implicitly_wait(1)
        assert driver.find_element(By.XPATH, MainLocators.title_buns), "Failed to open constructor by Buns"

        driver.quit()
