import unittest

import search

class SearchingTestCase(unittest.TestCase):
    def setUp(self):
        search.init() 

    def test_empty(self):
        self.assertFalse(search.duplicateString("Nothing"))

    def test_same(self):
        search.duplicateString("Nothing")
        self.assertTrue(search.duplicateString("Nothing"))

    def test_different(self):
        search.duplicateString("Nothing")
        self.assertFalse(search.duplicateString("Nothing1"))
    
    

if __name__ == '__main__':
    unittest.main()
