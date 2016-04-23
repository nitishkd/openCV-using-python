import numpy as no
import csv as csv
count = 0
readdata = csv.reader(open("/home/nitish/Analytics Assignment/CustomerMaster.csv"))
for row in readdata:
    for x in row:
        if x=="Airtel" or x=="airtel":
            print x
            count = count + 1
    #print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-"


print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-"
print count
