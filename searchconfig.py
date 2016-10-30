
class SearchConfig():

    def __init__(self):
        self.model          = ""
        self.year_from      = 2008
        self.year_to        = 2010
        self.price_from     = 2000
        self.price_to       = 8000
        self.mileage_from   = 1000
        self.mileage_to     = 150000
        self.engine_from    = 1.0
        self.engine_to      = 1.9
        self.fuel_type      = "Diesel"
        self.cars = {
            # 'Ford': 'Fusion',
            'VolksWagen': 'Golf',
        }
        self.url            = "https://www.donedeal.co.uk/cars"
        self.pageCounter    = 0
        self.area           = ''

    def nextPage(self):
        self.pageCounter    += 30