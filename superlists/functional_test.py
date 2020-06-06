from selenium import webdriver
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
        self.fail('Finish the Test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

# user enters a todo item

# user input Buy peacock feathers into textbox

# user hits enter then page updates, page shows peacok feather todo list entry

# still a text box to add another item, usr enter

# page update

# generated unique URL permalink for the list

# user revisit the permalink and see the same todo list again

browser.quit()

