#list of zipcode, breed, and license of everydog. 
import subprocess
import re
data = open("./NYC_Dog_Licensing_Dataset.csv")
smallDogs= open("./smallDogs")
realZips= open("realzips")
string= ""
d = {}
for e in realZips:
    zips= e.split(" ")
    if len(zips)==2:
        d[zips[0]]= zips[1]
#make a list of the small dogs 
for each in smallDogs:
    string= string+ " "+ each
#for each record of Dog License: 
f1= open("smallDogZips","w")
f2= open("unknownDogZips","w")
f3= open("bigDogZips","w")
for each in data:          #extract the zipcode, and the breed  
    if re.search(r'\t',each):
        line= each.split("\t")
    else:
        line= each.split(",")
    zipcode= line[6]
    if zipcode in d:
        zipcode= d[zipcode]
    breed = line[4]
    #if the breed is a small dog:
    if breed in string:
        if len(zipcode)==5:
            output=zipcode
            f1.write(output+"\n")
    #if the breed is a medium/big dog:
    elif breed == "unknown" or breed== "Unknown":
        if len(zipcode) ==5:
            output= zipcode
            f2.write(output+"\n")
    else:
        if len(zipcode) ==5:
            output=zipcode
            f3.write(output+"\n")
f1.close()
f2.close()
f3.close()
data.close()
smallDogs.close()
