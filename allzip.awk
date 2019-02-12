BEGIN{
    popAndZip= "uszipsv1.4.txt" 
    file= "crime_Zipcodes"
    dogfile= "AlldogsZipsCount"
    bigDogs= "bigDogZips"
    FS= "\t"
    #Create a key data pair for a zip code and the population
    while ((getline < popAndZip) >0){
	popCount[$1]= $9
    }
    FS= " "
    #Gerate unique crime zipcodes and add to the total zipcode array
    while ((getline  <file) > 0){
	CrimeZips[$0]++
	zipcodes[$0]++
    }
    #Generate unique dog zipcodes and add to the total zipcode array
    while ((getline < dogfile) >0){
	dogzip[$1]= $2
	zipcodes[$1]++
    }
    #generate a big dog zip code count 
    while ((getline <bigDogs) >0){
	bigDogZips[$0]++
    }
    #Create a pipe delimited file with all the data
    #zipcode|totalDogs|totalBigDogs|big/totalDogs|TotalCrimes|PopulationCount|CrimeperCapita|DogsperCapita
    for (each in zipcodes){
	if (each != 10018 && each != 10006){
	    if (CrimeZips[each] == None)
		CrimeZips[each]= 0
	    if (popCount[each] >0){
		print each,"|",dogzip[each],"|",bigDogZips[each],"|",bigDogZips[each]/dogzip[each],"|",CrimeZips[each],"|",popCount[each],"|", (CrimeZips[each]/popCount[each]),"|", (dogzip[each]/popCount[each])#*1000
	}
	
	#else
	 #   print each,"|",dogzip[each],"|",bigDogZips[each],"|",bigDogZips[each]/dogzip[each],"|",CrimeZips[each],"|",popCount[each]
        }
    }
    
        
}
