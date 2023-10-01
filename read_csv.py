"""
import csv

def import_data(file):
    with open(file, 'r') as file:
        csvreader = csv.reader(file)
        # skip header
        next(csvreader)
        for row in csvreader:
            circle = Circle()
            circle.name=row[0]
            circle.slug_name=row[1]
            circle.is_public=row[2]
            circle.verified=row[3]
            circle.members_limit=row[4]
            circle.save()
            print(row[0])

import_data('circles.csv')
 """
