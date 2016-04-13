__author__ = 'riccardo'
import ast
from itertools import islice
import re
# with open('/Users/riccardo/Documents/progetti/BIopen/Mappe_Negozi_e_Locali_Storici.csv', 'rb') as csvfile:
#         firstRow = csvfile.readlines(1)
#         fieldnames = tuple(firstRow[0].strip('\n').split(","))
#
# print fieldnames

cursor = {}  # Placeholder for the dictionaries/documents
with open('/Users/riccardo/Documents/progetti/BIopen/Mappe_Negozi_e_Locali_Storici.csv', 'rb') as csvfile:
    firstRow = csvfile.readlines(1)
    fieldnames = tuple(firstRow[0].strip('\n').split(","))
    fieldnames = fieldnames[:5]+('Civico',)+fieldnames[5:]
    print fieldnames
    next(csvfile)
    line_sample = islice(csvfile, 10)
    for row in line_sample:
        print row
        values = list(row.strip('\n').split(","))
    #     #values = list(row.split(','))
        print values
        for i, v in enumerate(values):
            #print i, fieldnames[i], v
            if re.match('[a-zA-Z]', v):
                cursor[fieldnames[i]] = 'text'
            elif re.match('\d', v):
                cursor[fieldnames[i]] = 'double precision'
print cursor

