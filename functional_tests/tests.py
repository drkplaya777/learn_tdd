import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from django.test import LiveServerTestCase

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
        
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
    
                self.assertIn(row_text, [row.text for row in rows])
                
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    
    def test_can_start_a_list_for_one_user(self):
        # Dancer has heard about a cool new online to-do app. He goes to check out 
        # it's homepage
        self.browser.get(self.live_server_url)
        
        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        
        header_text = self.browser.find_element_by_tag_name('h1').text
        
        self.assertIn('To-Do', header_text)
        
        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 
            'Enter a to-do item'
        )

        # He types "Buy blades oil" into a test box (Dancer's hobby is assasination)
        inputbox.send_keys('Buy blades oil')

        # When he hits enter, the page updates, and now the page lists "1: Buy blades oil" 
        # as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        
        self.wait_for_row_in_list_table('1: Buy blades oil')

        # there is still a text box inviting him to add another item. he enters 
        # "Clean obsidian blades" Dancer is VERY methodical about his blades 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Clean obsidian blades')
        inputbox.send_keys(Keys.ENTER)
        
        # The page updates again, and now shows both items on his list
        self.wait_for_row_in_list_table('1: Buy blades oil')
        self.wait_for_row_in_list_table('2: Clean obsidian blades')
        
        # Dancer wonders whethere the site will remember his list. Then he sees that the 
        # site generated  a unique URL for her -- There is some explantory text to that 
        # effect
        self.fail('Finish the test!')

        # He visits the URL- his to do list is still there

        # Satisfied, he goes back to sleep
        
    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Dancer starts a new to-do list
        self.browser.get(self.live_server_url)
        
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy blades oil')
        inputbox.send_keys(Keys.ENTER)
        
        self.wait_for_row_in_list_table('1: Buy blades oil')
        
        # He notices that his list has a unique URL
        dancer_list_url = self.browser.current_url
        
        self.assertRegex(dancer_list_url, '/lists/.+')
        
        # Now a new user, Kellanved, comes along to the site
        
        ## We use a new browser session to makes sure that no inofrmation
        ## of Dancer's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        # Kellanved visits the home page. There is no sign of Dancer's list
        self.browser.get(self.live_server_url)
        
        page_text = self.browser.find_element_by_tag_name('body').text
        
        self.assertNotIn('Buy blades oil', page_text)
        self.assertNotIn('Clean obsidian blades', page_text)
        
        # Kellanved starts a new list by entering a new item. He is less interesting then
        # Dancer
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy robes')
        inputbox.send_keys(Keys.ENTER)
        
        self.wait_for_row_in_list_table('1: Buy robes')
        
        # Kellanved gets his own unique URL
        kellanved_list_url = self.browser.current_url
        
        self.assertRegex(kellanved_list_url, '/lists/.+')
        self.assertNotEqual(kellanved_list_url, dancer_list_url)
        
        # Again there is no trace of Dancer's list
        page_text = self.browser.find_element_by_tag_name('body').text
        
        self.assertNotIn('Buy blades oil', page_text)
        self.assertIn('Buy robes', page_text)
        
        # Satisfied, they both go back to sleep
    
