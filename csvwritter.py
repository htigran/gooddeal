import csv


class CsvWritter:
    def __init__(self, filename):
        self.filename = filename
        self.rows = []

    def add(self, row):
        self.rows.append(row)

    def write(self):
        with open(self.filename, 'wb') as file:
            writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for row in self.rows:
                row = [str(s).encode('UTF-8', 'ignore') for s in row]
                writer.writerow(row)
