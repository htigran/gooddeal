
from bs4 import BeautifulSoup
import requests
import re
import json
from car import Car
from profiler import start_timer, print_time

host = 'https://donedeal.ie'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

class DoneDealException(Exception):
    pass

class DoneDealFinderApi():

    def __init__(self, config):

        if host:
            self.host = host

        if headers:
            self.headers = headers

        data = {
            # 'section': "all",
            # 'adType': "forsale",
            # 'source': '',
            # 'sort': 'relevance desc',
            # 'area': [],
            # 'max': 30,
            # 'start': 0,
        }

        self.cars = self._find(data)

    def _find(self, data):
        """ Search donedeal using following params:
            :param data: `dict` containging the key value pairs of:
            {
                section: "all"
                adType: "forsale"
                source: ''
                sort: 'relevance desc'
                area: []
                max: 30, // must be a common denominator for balanced
                    2 or 3-column layout (eg 6|12|18|24|30) etc
                start: 0
            }
        """
        uri = '{host}/search/api/v4/find/'.format(host=self.host)
        resp = requests.post(uri, data=json.dumps(data), headers=self.headers)
        if resp.status_code != 200:
            print("{resp.status_code} {resp.reason}".format(resp=resp))
            raise DoneDealException(
                'Got invalid response code of {}'.format(resp.status_code)
            )

        return resp.json()