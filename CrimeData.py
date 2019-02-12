import subprocess
import re
f= open("./CrimeRecords")

coordPattern = re.compile(r'.*?/[0-9]{4},[0-9]{3},.*?,[0-9]+,(.*?),.*?\(([0-9]+.[0-9]+, -[0-9]+.[0-9]+)\)',flags=re.DOTALL)
#crimePattern= re.compile(r'(LARCENY|HARASSMENT|ASSAULT|ROBBERY|STRANGULATION|TRESPASS|AGGRAVATED|BURGLARY|ABUSE) ')
crimePattern= re.compile(r'(BURGLARY|LARCENY|ROBBERY)')
trans= str.maketrans("!@#$%^&*()_+{}|:\"<>?=[]\\;',/",
                     "                            ")
string= ""
#Filter for aggresive crimes and isolate the latitude and longitude where the crime was committed 
for line in f:
    found=str(re.findall(coordPattern,line))
    formatted=found.translate(trans)
    #Search for a violent crime
    if re.search(crimePattern,formatted):
            latLong= formatted.split()
            strlen= len(latLong)
            print(latLong[strlen-2],latLong[strlen-1])
            
f.close()
