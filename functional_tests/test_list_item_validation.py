from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

        
class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Dancer goes to the home page and accidently tries to submit an empty list item. 
        # He hits Enter on the empty input box
        
        # The home page refereshes, and there is an error message saying that list items 
        # cannot be blank
        
        # He tries again with some test for the item, which now works
        
        # Perversely, he now decides to sbumit a second blank list item
        
        # He receives a similar warning on the list page
        
        # And he can correct it by filling some text in
        
        self.fail('write me!')

    
