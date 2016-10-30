
from bs4 import BeautifulSoup
import requests
import re
import json
from car import Car
from profiler import start_timer, print_time, profdec

class DoneDealFinder():

    def __init__(self):

        self.session = requests.session()

    @profdec
    def find(self, config):
        self.cars = self._get_cars(config)
        while(self._get_next_cars(config)):
            self.cars.extend(self.__next_cars)

        for car in self.cars:
            self._get_car_details(car)

    def _get_make_model(self, cars):
        result = ""
        for make, model in cars.items():
            newstr = "&make={0};model:{1}".format(make, model)
            result = ''.join([result, newstr])

        return result

    def _generate_url(self, config):

        cars = self._get_make_model(config.cars)
        query = '{config.url}' \
                '?year_from={config.year_from}' \
                '&year_to={config.year_to}' \
                '&price_from={config.price_from}' \
                '&price_to={config.price_to}' \
                '&mileage_from={config.mileage_from}' \
                '&mileage_to={config.mileage_to}' \
                '&engine_from={config.engine_from}' \
                '&engine_to={config.engine_to}' \
                '&fuelType={config.fuel_type}' \
                '{cars}'.format(config=config, cars=cars)

        if config.area:
            query = ''.join([query, "&area=", config.area])

        if config.pageCounter:
            query = ''.join([query, "&start=", str(config.pageCounter)])

        return query

    def _get_js_variable(self, url, var):
        start_timer()
        html = self.session.get(url)
        print_time("request")

        result = re.search("%s\s*=\s*(.*);" % var, html.text).group(1)
        return result

    def _get_cars(self, config):
        url = self._generate_url(config)
        search_results = self._get_js_variable(url, "window.searchResults")
        if not 'ads' in search_results:
            return None
        json_data = json.loads(search_results)
        cars = [Car(brief=ad) for ad in json_data['ads']]
        return cars

    def _get_next_cars(self, config):
        config.nextPage()
        self.__next_cars = self._get_cars(config)
        return self.__next_cars != None

    def _get_car_details(self, car):
        search_results = self._get_js_variable(car.friendlyUrl, "window.adDetails")
        json_data = json.loads(search_results)
        car.add_details(json_data)