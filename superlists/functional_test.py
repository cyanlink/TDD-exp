from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user goes to our todo list site
        self.browser.get('http://localhost:8000')
        # user noticed the page title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # user enters a todo item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # user input Buy peacock feathers into textbox
        inputbox.send_keys('Buy peacock feathers')

        # user hits enter then page updates, page shows peacok feather todo list entry
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly',
            [row.text for row in rows])
        # still a text box to add another item, usr enter

        self.fail('Finish the Test!')

        # page update

        # generated unique URL permalink for the list

        # user revisit the permalink and see the same todo list again


if __name__ == '__main__':
    unittest.main(warnings='ignore')
