from csvwritter import CsvWritter
from searchconfig import SearchConfig
from donedealfinder import DoneDealFinder
# from donedealfinderapi import DoneDealFinderApi


def main():

    config = SearchConfig()

    finder = DoneDealFinder()
    finder.find(config)

    writer = CsvWritter("file.csv")
    for car in finder.cars:
        writer.add(car.make_list())
    writer.write()

if __name__  == "__main__":
    main()