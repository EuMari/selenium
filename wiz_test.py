from selenium import webdriver
import time
from time import sleep
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

imie='Anna'
nazwisko='Kowalska'
gender='female'
#gender='male'
kod_kraju='PL'
numer_tel='908777657'
zly_mail='hjsija.pl'
haslo='jhdoaoij7987'
kraj='Polska'


class WizzRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://wizzair.com/pl-pl#/')
        #self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.quit()

    def testWrongEmail(self):
        driver=self.driver
    # XPATH    //button[@data-test="navigation-menu-signin"]
    # CSS selector button[data-test="navigation-menu-signin"] ??
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        sign_in=driver.find_element_by_xpath("//button[@data-test='navigation-menu-signin']")
        sign_in.click()
        #sleep(5)

        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Rejestracja "]')))
        register_btn=driver.find_element_by_xpath("//button[text()=' Rejestracja ']")
        register_btn.click()
        #sleep(5)
        #WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="registrationmodal-first-name-input"]')))
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.NAME, 'firstName')))
        name_input=driver.find_element_by_name('firstName')
        name_input.send_keys(imie)

        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.NAME, 'lastName')))
        lastname_input=driver.find_element_by_name('lastName')
        lastname_input.send_keys(nazwisko)

        if gender == 'male':
            m = driver.find_element_by_xpath('//label[@data-test="register-gendermale"]')
            name_input.click()
            m.click()
        else:
            driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]').click()

        #country_code=Select(driver.find_element_by_name('phone-number-country-code'))
        #country_code.select_by_value(kod_kraju)
        #country_code=driver.find_element_by_name('phone-number-country-code')
        #country_code.send_keys(kod_kraju)
        country_code=driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')
        country_code.click()
        cc=driver.find_element_by_name('phone-number-country-code')
        cc.send_keys(kod_kraju)

        code_to_choose=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[@data-test='PL']")))
        code_to_choose.click()

        phone=driver.find_element_by_name('phoneNumberValidDigits')
        phone.send_keys(numer_tel)

        email_input=driver.find_element_by_name('email')
        email_input.send_keys(zly_mail)


        passwd_input=driver.find_element_by_name('password')
        passwd_input.send_keys(haslo)

        nation=driver.find_element_by_name('country-select')
        nation.click()
        #sleep(4)
        nation_list=driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        nation_names=nation_list.find_elements_by_tag_name("label")
        #sleep(90)
        for label in nation_names:
            option=label.find_element_by_tag_name('strong')
            if option.get_attribute("innerText") == kraj:
                option.location_once_scrolled_into_view
                option.click()
                break

        driver.find_element_by_xpath("//label[@for='registration-privacy-policy-checkbox'][@class='rf-checkbox__label']").click()

        driver.find_element_by_xpath("//button[@data-test='booking-register-submit']").click()

if __name__=='__main__':
    unittest.main(verbosity=2)
