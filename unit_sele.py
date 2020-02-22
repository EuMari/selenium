# import bibliotek
from selenium import webdriver
from time import sleep
import unittest

# tworzymy klase wsbplcheck dziedziczaca po Test Case
# z modulu unittest
class WsbPlCheck(unittest.TestCase):
    # analogia: scenariusz testowy

    # warunki wstepne
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    #tutaj wlasciwe testy
    def testWsb(self):
        driver = self.driver
        # wejdz na strone
        driver.get("http://www.wsb.pl")
        # sprwdz czy "Bankowe" znajduje sie w tytule strony
        self.assertIn("Bankowe", driver.title)
        print(driver.title)


    #sprzatanie po tescie
    def tearDown(self):
        self.driver.quit()

# jesli to glowny plik, uruchom metode main, ktora uruchomi testy
if __name__=='__main__':
    unittest.main(verbosity=2)
