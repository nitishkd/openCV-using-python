import numpy as no
import csv as csv
count = 0
readdata = csv.reader(open("/home/nitish/Analytics Assignment/OfferCategorization.csv"))
for row in readdata:
    for x in row:
        if x=="60000":
            print row
            count = count + 1
print count
