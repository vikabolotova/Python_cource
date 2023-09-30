import numpy as np
import csv
from collections import Counter

class AnalysisDataFile:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data_file = []

    def read_file(self):
        file = open(file_path, 'r')
        file_reader = csv.DictReader(file, delimiter=',')
        self.data_file = list(file_reader)



    def max_review(self):
        payments = []

        for row in self.data_file:
            if row['Review'] != '':
                payment = row['Free/Paid/Other']
                payments.append(payment)

        payment_counts = Counter(payments)
        payment_maximum = payment_counts.most_common(1)

        return payment_maximum[0][0]


    def usable_for(self):

        usablfors = []
        for row in self.data_file:
            if row['Free/Paid/Other'] == 'Free':
                usablfor = row ['Useable For']
                usablfors.append(usablfor)
        usablfor_counts = Counter(usablfors)
        usablefor_maximum = usablfor_counts.most_common(1)


        return usablefor_maximum[0][0]

    def top_3(self, paid=None, usefor=None, category=None):
        filtered_data = self.data_file

        if paid is not None:
            filtered_data = [row for row in filtered_data if row['Free/Paid/Other'] == paid]
        if usefor is not None:
            filtered_data = [row for row in filtered_data if usefor in row['Useable For']]
        if category is not None:
            filtered_data = [row for row in filtered_data if category in row['Major Category']]

        counter = Counter(row['AI Tool Name'] for row in filtered_data)
        top_instruments = counter.most_common(3)

        return [instrument for instrument, count in top_instruments]





file_path = 'all_ai_tool.csv'
analyzer = AnalysisDataFile(file_path)
analyzer.read_file()
print(analyzer.max_review())
print(analyzer.usable_for())

print(analyzer.top_3('Free', None, None))
print(analyzer.top_3('Free', '/ experiments', 'other'))
print(analyzer.top_3('Freemium', None, 'text'))
print(analyzer.top_3(None, '/ e', None))