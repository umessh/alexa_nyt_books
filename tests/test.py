import os
import sys
import unittest

sys.path.insert(
    0, os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'lambda')))

from nyt_api import NYTBookAPI


class NYTBookAPITestCase(unittest.TestCase):

    def test_append_key(self):
        url1 = 'https://api.nytimes.com/svc/books/v3/?X=1'
        url1_res = 'https://api.nytimes.com/svc/books/v3/?X=1&api-key='+ \
            os.environ['NYT_API']
        url2 = 'https://api.nytimes.com/svc/books/v3/'
        url2_res = 'https://api.nytimes.com/svc/books/v3/?api-key=' + \
            os.environ['NYT_API']
        nyt_book_api = NYTBookAPI()
        self.assertEqual(nyt_book_api.append_key(url1), url1_res)
        self.assertEqual(nyt_book_api.append_key(url2), url2_res)
    
    def test_get_lists(self):
        nyt_book_api = NYTBookAPI()
        self.assertEqual(nyt_book_api.get_lists().status_code, 200)
    
    def test_get_best_seller(self):
        nyt_book_api = NYTBookAPI()
        list_names = ["Hardcover Fiction", "Hardcover Nonfiction",
                    "Travel", "Science"]
        for list_name in list_names:
            best_seller_data = nyt_book_api.get_best_seller(list_name)
            self.assertEqual(best_seller_data[0], 200)
            print(best_seller_data[1]['title'])
            self.assertNotEqual(best_seller_data[1]['title'],'')

if __name__=='__main__':
    unittest.main()
