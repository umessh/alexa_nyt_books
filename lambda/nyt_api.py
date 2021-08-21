import os
import requests


class NYTBookAPI():
    def __init__(self) -> None:
        self.url = 'https://api.nytimes.com/svc/books/v3/'
        self.api_key = os.environ['NYT_API']

    def append_key(self, url):
        if '?' in url:
            url = url + '&api-key=' + self.api_key
        else:
            url = url + '?api-key=' + self.api_key
        return url
    
    def get_lists(self):
        list_names_url = self.url + 'lists/names.json'
        request_url = self.append_key(list_names_url)
        resp = requests.get(request_url)
        return resp

    def get_best_seller(self, list_name):
        date_str = 'current'
        best_seller_url = self.url + 'lists/{date_str}/{list_name}.json'.format(
                    date_str = date_str, list_name = list_name)
        request_url = self.append_key(best_seller_url)
        resp = requests.get(request_url)
        status_code = resp.status_code
        best_seller_book = {}
        if status_code == 200:
            json_response = resp.json()
            best_seller_book = json_response['results']['books'][0]
        return (status_code, best_seller_book)

