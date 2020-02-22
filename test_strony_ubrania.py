from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.ui import Select

email='nima@brak.pl'
name='Anna'
lastname='Kowalska'
password='aaa'
birthday='5'
birthmonth='7'
birthyear='1990'
adres='9 Mainstreet'
city='Austin'
state='Texas'
postalcode='90887'
country='United States'
phonenumber='907555674'
adressalias='home adress'


class APRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')
        #przed kazda funkcja bedzie czekac MAX 2 s na odpowiedz
        self.driver.implicitly_wait(2)

    def testCorrectRegistration(self):
        driver=self.driver

        # odnajdz sign in
        sign_in=driver.find_element_by_class_name('login')

        # kliknij sign in
        sign_in.click()

        # wpisz adres email
        email_input=driver.find_element_by_id('email_create')
        email_input.send_keys(email)

        # kliknij create an account
        create_btn=driver.find_element_by_id('SubmitCreate')
        create_btn.click()

        # wybierz tytul
        gender_match=driver.find_element_by_id('id_gender2')
        gender_match.click()

        # wpisz imie
        name_give=driver.find_element_by_id('customer_firstname')
        name_give.send_keys(name)

        # wpisz nazwisko
        lastname_give=driver.find_element_by_id('customer_lastname')
        lastname_give.send_keys(lastname)

        # sprawdz maila
        email_text=driver.find_element_by_id('email').get_attribute('value')
        assert email_text == email
        print 'mail is fine'

        # wpisz niepoprawne haslo
        password_give=driver.find_element_by_id('passwd')
        password_give.send_keys(password)

        # podaj date
        birth_day=Select(driver.find_element_by_id('days'))
        birth_day.select_by_value(birthday)

        birth_month=Select(driver.find_element_by_id('months'))
        birth_month.select_by_value(birthmonth)

        birth_year=Select(driver.find_element_by_id('years'))
        birth_year.select_by_value(birthyear)

        # sprawdz imie
        name_check=driver.find_element_by_id('firstname').get_attribute('value')
        assert name_check == name
        print 'name is fine'

        # sprawdz nazwisko
        lastname_check=driver.find_element_by_id('lastname').get_attribute('value')
        assert lastname_check == lastname
        print 'lastname is fine'

        # podaj adres
        adress_input=driver.find_element_by_id('address1')
        adress_input.send_keys(adres)

        #podaj miasto
        city_input=driver.find_element_by_id('city')
        city_input.send_keys(city)

        # wybierz stan
        state_input=Select(driver.find_element_by_id('id_state'))
        state_input.select_by_visible_text(state)

        # podaj kod pocztowy
        postal_input=driver.find_element_by_id('postcode')
        postal_input.send_keys(postalcode)

        # wybierz kraj
        country_input=Select(driver.find_element_by_id('id_country'))
        country_input.select_by_visible_text(country)

        # wpisz numer telefonu
        phone_number=driver.find_element_by_id('phone_mobile')
        phone_number.send_keys(phonenumber)

        # podaj alias
        alias_input=driver.find_element_by_id('alias')
        alias_input.clear()
        alias_input.send_keys(adressalias)

        #kliknij Register
        register_btn=driver.find_element_by_id('submitAccount')
        register_btn.click()


        sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
