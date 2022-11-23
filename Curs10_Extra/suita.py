import unittest

import HtmlTestRunner

from Curs9_Verificari.test_unit import MyTestCase, RulesTestCase
from Curs9_Verificari.mihais_tema09 import HerokuAuthenticationTestCase
from Curs9_Verificari.homework_verificari import LoginTests

class MyFirstTestSuite(unittest.TestCase):

    def test_suite(self):
        # facem un obiect din clasa TestSuite
        my_test_suite = unittest.TestSuite()
        # In acest obiect, adaugam (prin load) testele din toate clasele pe care vrem sa le rulam
        my_test_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(MyTestCase),
            # unittest.defaultTestLoader.loadTestsFromTestCase(EmagTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(RulesTestCase),
            # unittest.defaultTestLoader.loadTestsFromTestCase(HerokuAuthenticationTestCase),
            # unittest.defaultTestLoader.loadTestsFromTestCase(LoginTests)
        ])
        # facem un test runner HTML, care va genera pentru noi niste rapoarte human-friendly pentru toate testele rulate
        test_runner = HtmlTestRunner.HTMLTestRunner(
            report_title="My first report",
            report_name="curs10_report",
            combine_reports=True
        )
        # la final ii zicem runner-ului sa ruleze intreaga suita de teste
        test_runner.run(my_test_suite)

