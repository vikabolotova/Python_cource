import csv
from collections import Counter
import re

class ManipulationCSV:

    def __init__(self, file_path):
        self.file_path = file_path
        self. data_file = []

    def read_file(self):
        file = open ('nlo.csv', 'r')
        file_reader = csv.DictReader(file, delimiter=',')
        self.data_file = list(file_reader)


    def max_country(self):

        countries = []

        for row in self.data_file:
            country = row['country']
            countries.append(country)
        country_counts = Counter(countries)
        country_maximum = country_counts.most_common(1)
        return country_maximum[0][0]


    def month_nlo_max(self):

        nmy = []
        for row in self.data_file:
            country = row['datetime']
            nmy.append(country)

        months = []
        for i in nmy:
            res = re.match(r'\d{1,2}/', i)
            months.append(res.group())
        months_count = Counter(months)
        month_max = months_count.most_common(1)

        return month_max[0][0]


file_path = 'nlo.csv'
analyzer = ManipulationCSV(file_path)
analyzer.read_file()
print(analyzer.max_country())

print(analyzer.month_nlo_max())