from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Dancer has heard about a cool new online to-do app. He goes to check out 
        # it's homepage
        
        self.browser.get('http://localhost:8000')
        
        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        
        # He is invited to enter a to-do item straight away

        # He types "Buy blades oil" into a test box (Dancer's hobby is assasination)

        # When he hits enter, the page updates, and now the page lists "1: Buy blades oil" 
        # as an item in a to-do list

        # there is still a tesxt box inviting him to add another item. he enters 
        # "Clean obsidian blades" Dancer is VERY methodical about his blades 

        # The page updates again, and now shows both items on his list

        # Dancer wonders whethere the site will remember his list. Then he sees that the 
        # site generated  a unique URL for her -- There is some explantory text to that 
        # effect

        # He visits the URL- his to do list is still there

        # Satisfied, he goes back to sleep
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')

