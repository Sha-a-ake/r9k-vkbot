import unittest

import search
from chat import Chat

class SearchingTestCase(unittest.TestCase):
    def setUp(self):
        self.chat = Chat(1) # айди тут значения не имеет, любой

    def test_empty(self):
        self.assertFalse(self.chat.searchString("Nothing"))

    def test_same(self):
        self.chat.searchString("Nothing")
        self.assertTrue(self.chat.searchString("Nothing"))

    def test_different(self):
        self.chat.searchString("Nothing")
        self.assertFalse(self.chat.searchString("Nothing1"))
    
    

if __name__ == '__main__':
    unittest.main()
