#Generate unique Zipcodes and get a count for how many dogs are found in each zipcode 
import subprocess
import re
arr=dict()
data= open("./NYC_Dog_Licensing_Dataset.csv")
realZips= open("realzips")
d= {}
for e in realZips:
    zips=e.split(" ")
    if len(zips) ==2:
        d[zips[0]]= zips[1]
for each in data:
    if re.search(r'\t',each):
        line= each.split("\t")
    else:
        line= each.split(",")
    zipcode= line[6]  #get the zip code
    if zipcode in d:
        zipcode= d[zipcode]
    if len(zipcode) == 5:
        if zipcode in arr:
            arr[zipcode]+=1     #create a count for each zipcode 
        else:
            arr[zipcode]=1

for each in arr:
    print(each, arr[each])
data.close()
