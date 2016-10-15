#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################
# Standalone script #4: reading a 
# remote CSV file and calculating
# a range of metrics using a DoL
# (dictionary-of-lists) approach.
#
# I've added comments and other clues
# to help you work it out, but you'll
# have to put together a lot of different
# ideas in one place to make this work.
##############################

import urllib2
import csv

# Redefine the function
def readRemoteCSV(url):
    """
    Reads a remote CSV file and returns
    a dictionary-of-lists containing the data.
    """
    urlData = [] # Somewhere to store the raw data
    
    # Read the raw data and store it
    response = urllib2.urlopen(url)
    reader   = csv.reader(response)
    for row in reader: 
        urlData.append( row )
    
    # A dictionary to hold the processed data
    myData = {}
    
    # We need to know the names of the fields 
    # in the data set because these become the
    # keys in the dictionary-of-lists.
    header = urlData[0]
    print("Header is: " + ", ".join(header)) # Debugging
    
    # Initialise each key in myData with an empty list. 
    # So this will give us: 
    #     myData['Names'] = []
    #     myData['Latitudes'] = []
    #     ...
    # The advantage here is that we can just append each 
    # field from each row to the end of the list.
    for h in header:
        myData[h] = []
    
    # Now we have to parse the CSV data the we 
    # retrieved. The one tricky thing is that we
    # don't necessarily know what type of data is
    # in each column. But that's something we can
    # let the user fix later.
    for i in xrange(1, len(urlData)):
        for j in xrange(len(urlData[i])):
            myData[ header[j] ].append(urlData[i][j])
    
    return myData

print "URL 1:\n"
data1 = readRemoteCSV("http://www.reades.com/CitiesWithWikipediaData-simple.csv")
# print data1 # To debug

# Now fix the numeric fields so that we can treat them
# as numbers, not strings... Population, Rank, Latitude
# and Longitude all need to be converted.
# 
# Let me Google that for you: convert list of strings to list of floats python
data1['Rank']       = [int(i) for i in data1['Rank']]
data1['Population'] = [int(i) for i in data1['Population']]
data1['Latitude']   = [float(i) for i in data1['Latitude']]
data1['Longitude']  = [float(i) for i in data1['Longitude']]

# Find the population of Manchester
pop = data1['Population'][data1['Name'].index('Greater Manchester')]
print "The population of Manchester is: " + str(pop)

# Find the easternmost city
city = data1['Name'][data1['Longitude'].index(max(data1['Longitude']))]
print "The easternmost city is: " + str(city)

# Find the mean population of the cities
import numpy as np # Need to import a useful package
mean = np.mean(data1['Population'])
print "The mean population is: " + str(mean)

print "URL 2:\n"
data2 = readRemoteCSV("http://www.reades.com/CitiesWithWikipediaData.csv")
# print data2 # To debug

data2['Rank']       = [int(i) for i in data2['Rank']]
data2['Population'] = [int(i) for i in data2['Population']]
data2['Latitude']   = [float(i) for i in data2['Latitude']]
data2['Longitude']  = [float(i) for i in data2['Longitude']]

# Find the population of Manchester
pop = data2['Population'][data2['Name'].index('Greater Manchester')]
print "The population of Manchester is: " + str(pop)

# Find the easternmost city
city = data2['Name'][data2['Longitude'].index(max(data2['Longitude']))]
print "The easternmost city is: " + str(city)

# Find the mean population of the cities
import numpy as np # Need to import a useful package
mean = np.mean(data2['Population'])
print "The mean population is: " + str(mean)

# Bonus! Find the standard deviation of city sizes