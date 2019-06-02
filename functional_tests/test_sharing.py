from selenium import webdriver
from .base import FunctionalTest
from .list_page import ListPage
from .my_lists_page import MyListsPage

def quit_if_possible(browser):
    try:
        browser.quit()
    except:
        pass
        

class SharingTest(FunctionalTest):

    def test_can_share_a_list_with_another_user(self):
        # Dancer is a logged in user
        self.create_pre_authenticated_session('dancer@shadow.com')
        
        dancer_browser = self.browser
        self.addCleanup(lambda: quit_if_possible(dancer_browser))
        
        # His friend Kellanved is also hanging out on the lists site
        kell_browser = webdriver.Firefox()
        self.addCleanup(lambda: quit_if_possible(kell_browser))
        
        self.browser = kell_browser
        self.create_pre_authenticated_session('kellanved@shadow.com')
        
        # Dancer goes to the home page and starts a list
        self.browser = dancer_browser
        self.browser.get(self.live_server_url)
        list_page = ListPage(self).add_list_item('Get help')
        
        # He notices a "Share this list" option
        share_box = list_page.get_share_box()
        
        self.assertEqual(   
            share_box.get_attribute('placeholder'),
            'your-friend@example.com'
        )

        # He shares his list
        # The page updates to say that it's shared with Kellanved
        list_page.share_list_with('kellanved@shadow.com')
        
        # Kellanved now goes to the lists page with his browser
        self.browser = kell_browser
        MyListsPage(self).go_to_my_lists_page()
        
        # He sees Dancer's list in there!
        self.browser.find_element_by_link_text('Get help').click()

        # On the list page, Kellanved can see that it's Dancer's list
        self.wait_for(lambda: self.assertEqual(
            list_page.get_list_owner(),
            'dancer@shadow.com'
        ))
        
        # He adds an item to the list
        list_page.add_list_item('Howdie Dancer!')
        
        # When Dancer refreshes the page, he sees Kellanved's addition
        self.browser = dancer_browser
        self.browser.refresh()
        
        list_page.wait_for_row_in_list_table('Howdie Dancer!', 2)

