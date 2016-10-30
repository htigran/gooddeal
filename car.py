
from pprint import pprint as pp


globalID = 0

class Car():

    def __init__(self, brief=None, details=None):
        global globalID

        self.age            = self._item_at(brief['age'])
        self.county         = self._item_at(brief['county'])
        self.currency       = self._item_at(brief['currency'])
        self.description    = self._item_at(brief['description'])
        self.friendlyUrl    = self._item_at(brief['friendlyUrl'])
        self.header         = self._item_at(brief['header'])
        # self.id             = self._item_at(brief['id'])
        self.id             = str(++globalID)

        price               = self._item_at(brief['price'])
        price = price.replace(',', '')
        if self.currency == 'EUR':
            self.price = price
        else:
            self.price = str(int(int(price) * 1.18))
            self.currency = 'EUR(GBP)'

        self.year           = self._item_at(brief['year'])
        self.brief_json     = brief

    def _item_at(self, item):
        if isinstance(item, unicode):
            return item.encode('ascii', 'ignore')
        elif isinstance(item, str):
            return item
        elif isinstance(item, int):
            return str(item)
        else:
            raise ValueError('unsupported type - %s' % type(item))

    def add_details(self, details):

        for attr in details['displayAttributes']:
            if attr['name'] == u'NCT':
                self.nct = self._item_at(attr['value'])
            elif attr['name'] == u'bodyType':
                self.body_type = self._item_at(attr['value'])
            elif attr['name'] == u'fuelType':
                self.fuel_type = self._item_at(attr['value'])
            elif attr['name'] == u'make':
                self.make = self._item_at(attr['value'])
            elif attr['name'] == u'mileage':
                mileage = self._item_at(attr['value'])
                mileage = mileage.replace(',', '')
                number, _, unit = mileage.partition(' ')
                num_int = int(number)
                if unit == u'mi':
                    num_int = int(num_int * 1.60934)
                self.mileage = str(num_int)
            elif attr['name'] == u'model':
                self.model = self._item_at(attr['value'])
            elif attr['name'] == u'roadTax':
                self.road_tax = self._item_at(attr['value'])
            elif attr['name'] == u'transmission':
                self.transmission = self._item_at(attr['value'])
            elif attr['name'] == u'year':
                self.year = self._item_at(attr['value'])

        self.details_json = details

    def __str__(self):
        str = '{car.make} {car.model} {car.year} {car.mileage} {car.fuel_type} {car.price}{car.currency}'.format(car=self)
        return str

    def make_list(self):
        list = [self.id, self.make, self.model, self.year, self.mileage,
                self.fuel_type, self.price, self.currency, self.friendlyUrl]

        return list
