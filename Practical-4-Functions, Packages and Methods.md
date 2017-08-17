
# This Week’s Overview

This week we're going to apply a number of the concepts covered in class in order to read a remote CSV file, turn it into data, and then perform some simple analyses on it. We're going to first do it 'by hand' (building the tools we need) and then using the 'pandas' package that gives us a very different way to do things.

## Learning Outcomes

By the end of this practical you should:
- Have read a remote data file
- Written a function to derive some statistics
- Have imported a package
- Have made use of methods

# Taking a Second to Think

To a computer, reading data from a remote location (e.g. a web site halfway around the world) is not really any different from reading one that's sitting on your desktop, you just need to make set it up a bit differently and, in Python, make use of a different _package_. In all cases – local and remote – Python gives you back a 'filedhandle' that knows how to 'read a line' or 'close an open file'. You can think of a filehandle as something that gives you a 'grip' on a file-like object.

I also want you to understand how we're approaching the problem I've just set: we want to read a remote file (i.e. a text file somewhere the planet), turn it into a local data structure (i.e a list or a dictionary), and then perform operations on it using functions (e.g. calculate the mean, find the easternmost city, etc.).

_**But**_, we _don't_ try to do all of this at once by writing a whole lot of code and the hoping for the best; when you're tackling a problem like this you break it down into separate, simpler steps, and then tick them off one by one. So first we'll get Python _reading_ remote data, then we'll _convert_ text into data, and finally we'll _analyse_ the data using functions.

_**Note**_: you might also find it helpful to take a close look at the URL that we are reading by pasting this link into a web browser: http://www.reades.com/CitiesWithWikipediaData-simple.csv. 

# Step 1: Reading a Remote File

So, as I said, we are going to parse a data file hosted on a remote web site at `http://www.reades.com/CitiesWithWikipediaData-simple.csv`. This is just the first step: we are going to build from this first step towards more substantial exercises and, eventually, you could easily request Megabytes of data in real-time according to flexibly-specified parameters!

You'll probably need to do a quick Google in order to make sense of what you're about to do; I'd suggest "`read remote CSV file Python urllib2`".


```python
import urllib2

help(urllib2.urlopen) # Notice!

# Give what I've written above, what do you 
# think the value of 'url' should be? What
# type of variable is it? int? string? 
url = ???
print("URL: " + url + ".\n")

# Read the URL and copy the results to 
# a variable called 'response'.
response = urllib2.urlopen(url)

# 'response' can behave like a list in 
# a for loop... we can create a temporary
# variable called line, and each time we 
# ask 'response' it will give us a new line.
for line in response:
    print ???.rstrip()
```

If you've managed to get the code above to run after fixing the '???' and have received 11 rows of text in response to your `urlopen` query then, congratulations, You've now read a text file sitting on a server in, I think, Alberta, Canada and Python _didn't care_. 

The last row should be `10,Sheffield,10,-163545.3257,7055177.403,685368`.

### URLLIB2

In this particular case, I 'gave' you the fact that you'd need to make use of the `urllib2` package in order to read the file. But you could certainly have Googled this for yourself using something like 'Python read file on server' or 'Python read remote file'...

Urllib2 is a very useful library, but compared to pandas (which we'll see next week), it's pretty simple since it just sends a 'request' to a web site and 'reads' the results. You can also do things like submit a form (e.g. you could submit hundreds of applications for a free TV if someone ran a competition... that's why they have 'captchas' now).

Anyway, that's some background, let's move on to step 2! 

## Step 2: Turning Text into Data

We now need to work on turning the response we got to our `urllib2` request into useful data. You'll notice that we are dealing with a _CSV_ (Comma-Separated Value) file and that the format is quite simple since none of the rows have fields that *themselves* contain commas. So to turn this into data we just need to _split_ the row into separate fields using the commas.

In the code below, `dir('string')` lists the available methods for strings (because `'string'` is itself a _String_; we could as easily written `dir('foo')` or `dir('supercalifragilisticexpialidocious')`. In the output below, the methods that start and end with `__` are generally considered private, so you can skip over these and focus on the ones further down that are designed to be useful to programmers. Can you spot the method that is most likely to be useful?

### A Brief Interlude

Just in case you need help pronouncing supercalifragilisticexpialidocious:

[![Mary Poppins](http://img.youtube.com/vi/tRFHXMQP-QU/0.jpg)](http://www.youtube.com/watch?v=tRFHXMQP-QU)

Remember that you can find out what _method_ are supported by a string using `dir(<string>)`:
```python
dir('supercalifragilisticexpialidocious')
```
I'm going to save you some time (_this_ time!) and tell you that we're interested in the `split` method. Why not use the `help` function to figure out how to make use of it?


```python
help('supercalifragilisticexpialidocious'.split)
```

Now, how would you use `split` to turn this into a list like this: 
```python
['sup','rcalifragilisticexpialidocious']
```


```python
print 'supercalifragilisticexpialidocious'.split(???)

# Some other methods
print 'supercalifragilisticexpialidocious'.upper()
print 'supercalifragilisticexpialidocious'.title()
```

OK, so you've tracked down the way to split a string using a delimiter and _even_ how to limit the number of 'words' that come out of the split operation. You might want to make a mental note of some of the other useful functions that are available for strings: `splitlines`, `upper`, `lower`, `rstrip`, and the whole `is...` series. We work a lot with strings, so it's handy to get to know the readily-available methods well.

Let's test string splitting using our sample data (the last line of the 'simple' CSV file) to make sure it works the way we think it does... How do we turn the string below into a list like this:
`['10', 'Sheffield', '10', '-163545.3257', '7055177.403', '685368']`?


```python
test = "10,Sheffield,10,-163545.3257,7055177.403,685368".split(???)
print test
```

Cool! But, first, a question: why do you think that I consider `['10', 'Sheffield', '10', '-163545.3257', '7055177.403', '685368']` to be data when `"10,Sheffield,10,-163545.3257,7055177.403,685368"` is not?

Here's a clue:
```python
print("The population of " + myList[1] + " is " + myList[5])
```

Now that you've figured out how to make use of the appropriate method using `help` and a simple test, it's time to revise the code above so that it turns the remote file into data. You can hopefully see how we're breaking a complex problem down into a set of _increments_, each of which is a bit easier to write and understand. 

Now, remember that ultimately we want to make use of the data in this file, so simply printing it back out isn't particularly helpful. What we really want to do is stash the data we've read in some kind of _data structure_ that resembles the CSV file but is easier and faster for the computer to navigate.

Instinctively\* it seems like we need:
1. To keep the rows in order
2. To keep the columns in order

With what we've covered in previous sessions and what we've covered in class, what approach might allow us to do this? _Hint:_ is it likely to be a dictionary? 

_\* We'll see why instinct isn't always right later..._


```python
import urllib2

url = "http://www.reades.com/CitiesWithWikipediaData-simple.csv"

cityData = [] # Somewhere to store the data

response = urllib2.urlopen(url) 
for line in response: 
    cityData.append( line.rstrip().split(',') )

print cityData # Check it worked!
```

If it worked, then you should have this output:
```python
[['id', 'Name', 'Rank', 'Longitude', 'Latitude', 'Population'], ['1', 'Greater London', '1', '-18162.92767', '6711153.709', '9787426'], ['2', 'Greater Manchester', '2', '-251761.802', '7073067.458', '2553379'], ['3', 'West Midlands', '3', '-210635.2396', '6878950.083', '2440986'], ['4', 'West Yorkshire', '4', '-185959.3022', '7145450.207', '1777934'], ['5', 'Glasgow', '5', '-473845.2389', '7538620.144', '1209143'], ['6', 'Liverpool', '6', '-340595.1768', '7063197.083', '864122'], ['7', 'South Hampshire', '7', '-174443.8647', '6589419.084', '855569'], ['8', 'Tyneside', '8', '-187604.3647', '7356018.207', '774891'], ['9', 'Nottingham', '9', '-131672.2399', '6979298.895', '729977'], ['10', 'Sheffield', '10', '-163545.3257', '7055177.403', '685368']]
```
To you that might look a lot _worse_ that the data that you original saw at http://www.reades.com/CitiesWithWikipediaData-simple.csv, but to a computer that list-of-lists is something it can work with; check it out:


```python
for c in cityData:
    print("The population of " + c[1] + " is " + c[5])
```

# Functions

Everything we do form here on out will be modelled on the code that we've just finished, so if you get lost you can always come back to this step and start over! Sometimes, you can tie yourself in knots thinking about a problem and it ends up being easier to throw everything out and start again with a simpler approach or new angle...

We can write functions in much the same way that we developed the code above: incrementally. Rather than just sitting down, typing out your function, and hoping for the best, it's often easier to write the code first and _then_ turn it into a function! Let's try this for the code we've written so far by creating a function that will access _any_ URL and return a 'simple' list-of-lists that represents any CSV data stored at the URL's location. 

### Designing a function

The first stage in writing a function is to figure out what inputs and outputs it should have. For this function that is fairly straightforward:
* We give the function a URL that we want to it read in
* The function gives us back a list-of-lists containing the CSV data

We should also give it a name that is fairly obvious to anyone else who comes along and tries to read our code; how about: `readRemoteCSV`?

### Creating  a function

This is a good point to hit Google or StackOverflow for some help. We're trying to `"write a function in Python"` so why not search for that? I quickly found some useful hints on sites like TutorialPoint and, obviously, in the online Python documentation itself.

I've created the sketch of a function below but have left out quite a bit that you'll have to fill in by searching on your own.


```python
def readRemoteCSV(url):
    """
    Reads a remote CSV file and returns
    a list-of-lists containing the data.
    """
    urlData = [] # Somewhere to store the data

    # You've seen all of this before -- we're just
    # doing the work inside a function now, instead
    # of as standalone code.
    response = urllib2.urlopen(???)
    for line in response: 
        urlData.append( line.rstrip().split(???) )
        
    # Where did we store the data? Isn't 
    # that the thing that we want to return?
    return ???

print "URL 1:\n"
data1 = readRemoteCSV("http://www.reades.com/CitiesWithWikipediaData-simple.csv")
print data1

# Now...

print "URL 2:\n"
data2 = readRemoteCSV("http://www.reades.com/CitiesWithWikipediaData.csv")
print data2

```

### Review!

OK, let's just take a look at that again: do you see how, by packaging up the code as a function, we have made it more useful and more re-usable? We now have a little snippet of code that we can _call_ to process _any_ valid URL. So we called `readRemoteCSV` once to read the 'Cities-simple.csv' file, and again to read to the much larger 'Cities.csv' file. We could read 1,000 other URLs using the same function! Now our code is a lot cleaner because we don't need to keep reading (and writing) lots of lines of code about calling remote files and parsing them. The other big gain is that it's also a lot easier to maintain our code now because if we want to _change_ the way that we parse remote CSV files then we only need to do it in _one place_ and then everywhere that we use this function benefits form the improvement... which is what we're going to do now.

## Using the CSV library

Our little CSV function is already useful, but it's a little naive: we are implicitly _assuming_ that none of the fields can containg a comma. Why is that? Before you continue reading, take a moment to think about what `split(',')` does and why it won't work well with a line of data that looks like this:
```python
11,"Cardiff,Caerdydd",11,51.483333,-3.183333,447287
```
Let's try it:


```python
'11,"Cardiff,Caerdydd",11,51.483333,-3.183333,447287'.split(',')
```

Do you see the problem now? Will this code still work:

```python
for c in cityData:
    print("The population of " + c[1] + " is " + c[5])
```

This is where using code that someone _else_ has written and contributed is helpful: we don't need to think through how to deal with this sort of thing ourselves, we can just import the library that we need and make use of its functionality.

I've given you the skeleton of the answer below, but you'll need to do a little Googling to find out how to `"read csv urllib2 python"`.


```python
import urllib2
import csv

# Redefine the function
def readRemoteCSV(url):
    """
    Reads a remote CSV file and returns
    a list-of-lists containing the data.
    """
    urlData = [] # Somewhere to store the data

    response = urllib2.urlopen(url)
    reader   = ???
    for row in reader: 
        urlData.append( ??? )
        
    return urlData

print "URL 1:\n"
data1 = readRemoteCSV("http://www.reades.com/CitiesWithWikipediaData-simple.csv")
print data1
```

The advantage of this switch (from `split` to using the `csv` library) is that the csv library knows how to deal with fields that contain commas (or newlines!) and so is much more flexible and consistent that our naive `split` approach. The vast majority of _common_ tasks (reading certain types of files, getting remote files, etc.) have libraries that do exactly what you want without you needing to write much code yourself to take advantage of it. You should always have a look around online to see if a library exists before thinking that you need to write everything/anything from scratch. The tricky part is knowing what words to use for your search and how to read the answers that you find...

## Calculating the Mean

Now I'd like you to write a function that will enable you to calculate the mean city size from data retrieved from _any_ URL that contains city data. So you should be able to call _one_ function that will work for both `Cities.csv` and `Cities-simple.csv`. You'll need to look closely at how the two files are 'laid out': where is the population column, and how would we iterate over the rows to find the mean?

### Designing the Function

OK, we know that `readRemoteCSV` will give us back a list-of-lists: the 'big list' contains a large number of 'small lists', each of which represents a row in the data set. Let's break this down:
* We know that we will have a LoL (List-of-Lists) to work from
* We know that each 'small list' represents a row in the data
* We know that the position of the column of interest might change from data set to data set, but it won't change _within_ a data set
* We know that we'll need to convert every value to a... `float`? `int`? Let's assume `float` just to be safe.
* We know that we'll need to sum up the values
* We know that we'll need to keep track of how many rows of data there are

As before, let's start by working it out _as code_, and then package it up _as a function_ once it's working.


```python
# The starting point... using the data retreived
# from the function that we wrote above...
for row in data1:
    print row
```


```python
# Now let's track a particular column
col = 3
for row in ???:
    print row[???]
```


```python
# And now let's figure out the mean
col   = 3
total = 0 # What's the sum of the values?
count = 0 # How many values have we read?
for row in data1:
    print row[col]
    value = row[col]
    count += 1
    total += value
```

Ooops, that last one didn't work so well. How would you fix this?

Here are _two_ hints:
1. What is the count when you are reading the first row (which contains the column name)?
2. If the value is a `string`, how do you convert it to an `int` or `float`

_P.S._ I also broke one very important thing deliberately


```python
# And now let's figure out the mean
col   = 5   # Which column to read?
total = 0.0 # What's the sum of the values?
count = 0   # How many values have we read?

for row in data1:
    #print(row[col]) # Uncomment to debug
    if count > 0:
        value = float(???)
        total += total
    count += 1

print total/count
```

You'll notice that there's a line in the above that says:
```python
    #print(row[col]) # Uncomment to debug
```
This is a really common technique used by programmers to figure out what's happening in their code. Many people will spend _more_ time debugging than they will writing the code in the first place! One of the most important ways to debug is simply to print out the values of whatever you're working with: are you seeing what you expected to see? are there values that you hadn't counted on? are all of the values printed out or are some missing? And so on... To 'turn on' debugging, all we have to do is remove the `#` in front of the print statement and everything will start printing out as we process the file. Simple. And useful.

OK, we're almost there now: we know _how_ to calculate the mean for any column that is numeric (dealing with non-numeric columns would be nice but that's just adding extra difficulty to this notebook). Now we want to package this up as a function so that you can just write `calcMean(...)` and get back an answer!

Here's a skeleton to get you started:


```python
def calcMean(data, col):
    "Take a list-of-lists and derive the mean for a specified column."
    total = 0.0
    count = 0
    
    for row in data:
        # print(row[col]) # Uncomment to debug
        if count > 0:
            value = float(???)
            total += value
        count += 1
    
    return total/count

data1 = readRemoteCSV("http://www.reades.com/CitiesWithWikipediaData-simple.csv")
print "Mean of simple file populations is: " + str(calcMean(data1,5))

# Now...

data2 = readRemoteCSV("http://www.reades.com/CitiesWithWikipediaData.csv")
print "Mean of big file populations is: " + str(calcMean(data2,5))
```

And there you go! Done.

You've written two functions: one to read a remote file from a URL, and one to calculate the mean for a simple CSV file of _any_ size. I hope you'll agree that that is pretty handy, but that it's also pretty awkward: we're not doing any type-checking (to see if something is an integer, float, or string) and if we get it wrong the whole thing 'blows up' on us. It's also just kind of _inelegant_ since we have all of these counters (`total` and `count`) to keep track of things... is this what's really going on behind the scenes?

# Thinking About Data

I've said before that the way a computer 'thinks' and the way that we think doesn't always line up naturally. Experienced programmers can think their way _around_ a problem by working _with_ the computer, rather than against it. Let's apply this approach to the parsing of CSV files.

## What's an _Appropriate_ Data Structure?

As you saw when I asked you to calculate the mean population of British cities twice – once using the simple file, and once using the bigger, more complex file – there is a 'problem': our list-of-lists isn't very easy to navigate. Not only _might_ the location of the Population column be different in the two files (as it was, deliberately), but when we want to work out the mean we need to step through a lot of irrelevant data as well (we need to skip past the name, latitude, longitude, etc.). And if I asked you to find the _largest_ city you'd need to do even more work.

So how does the experienced programmer get around this? 'Simple': she realises that the data is organised the wrong way! We humans naturally tend to think in rows of data: London has the following _attributes_ (population, location, etc.), and York has a different set of attributes. Se we read across the row because that's the easiest way for us to read it.

But a computer doesn't have to work that way. For a computer, it's as easy to read _down_ a column as it is to read _across_ a row. In fact, it's easier, because each column has a consistent _type_ of data: so one column contains names (strings), another column contains populations (integers), and other columns contain other types of data (floats, etc.). Better still, the order of the columns often doesn't matter as long as we know what they are called: it's easier to ask for the 'population column' than it is to ask for the 6th column since, for all we know, the population column might be in a different place for different files but they are all (relatively) likely to use the 'population' label for the column itself.

## A Dictionary of Lists

So, if we don't mind about column order and only row order (so that we can still find all of the attributes for London) then a dictionary of lists would be a nice way to handle things. Why is that? Well, here are the first four rows of data from the simple city file as a list-of-lists:

```python
['id', 'Name', 'Rank', 'Longitude', 'Latitude', 'Population'], 
['1', 'Greater London', '1', '-18162.92767', '6711153.709', '9787426'], 
['2', 'Greater Manchester', '2', '-251761.802', '7073067.458', '2553379'], 
['3', 'West Midlands', '3', '-210635.2396', '6878950.083', '2440986']
```

Now, here's how it would look as a dictionary of lists organised by _column_, not by row:

```python
myData = {
    'id'         : [1, 2, 3],
    'Name'       : ['London', 'Manchester', 'West Midlands'],
    'Rank'       : [1, 2, 3],
    'Longitude'  : [-18162.92767, -251761.802, -210635.2396],
    'Latitude'   : [6711153.709, 7073067.458, 6878950.083],
    'Population' : [9787426, 2553379, 2440986],
}

```

What does this do better? Well, for starters, we know that everything in the 'Name' column will be a string, and that everything in the 'Longitude' column is a float, while the 'Population' column contains integers. So that's made life easier already. But let's test this out and see how it works.


```python
myData = {
    'Name'       : ['London','Manchester','West Midlands'],
    'Rank'       : [1, 2, 3, 4],
    'Longitude'  : [-18162.92767, -251761.802, -210635.2396],
    'Latitude'   : [6711153.709, 7073067.458, 6878950.083],
    'Population' : [9787426, 2553379, 2440986],
}

# Find the population of Manchester
pop = myData['Population'][myData['Name'].index('Manchester')]
print "The population of Manchester is: " + str(pop)

# Find the easternmost city
city = myData['Name'][myData['Longitude'].index(max(myData['Longitude']))]
print "The easternmost city is: " + str(city)

# Find the mean population of the cities
import numpy as np # Need to import a useful package
mean = np.mean(myData['Population'])
print "The mean population is: " + str(mean)
```

## Review!

There's a _lot_ of content to process in the code above, so do _not_ rush blindly on if this is confusing. Stop. Think it through. We'll go through each one in turn, but they nearly all work in the same way.

### The Population of Manchester

The code can look pretty daunting, so let's break it down into two parts.

What would you get if you ran just this code?
```python
myData['Population'][0]
```
Remember that this is a dictionary-of-lists (DoL). So, Python first looks for a key named `Population` in the myData dictionary. It finds out that the value associated with this key is a _list_ (`[9787426, 2553379, 2440986]`). And this example, it just pulls out the first value (index 0), which is `9787426`. Does that make sense?

Now, to the second part:
```python
myData['Name'].index('Manchester')

```
This is very similar: we look in the dictionary for the key `Name` and find that that's _also_ a list (`['London','Manchester','West Midlands']`, since you asked). If you don't remember what `index` does, don't worry, here's the output from Python's `help()` function:
```
Help on built-in function index:

index(...)
    L.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.
```
So all we're doing is asking Python to find out the index of 'Manchester' in the list associated with the dictionary key 'Name' _instead_ of just sticking in a `0` to get the first index value. Putting these two things back together what we're doing is:
* Finding the index (i.e. **row**) of 'Manchester' in the Name column,
* Using that index to read a value out of the Population column (by **row**).

Does that make sense? If it does then you should be having a kind of an Alice-through-the-Looking-Glass moment because what we've done by taking a column view, rather than a row view is to make Python's ``index()`` command do the work for us. Instead of having to look through each row for a field that matches 'Name' and then check to see if it's 'Manchester', we've pointed Python at the right column immediately and asked it to find the match (which it can do very quickly). Once we have a match then we _also_ have the row number to go and do the lookup in the 'Population' column because the index _is_ the row number!

### The Easternmost City

Where this approach really comes into its own is on problems that involve maths. To figure out the easternmost city in this list we need to find the _maximum_ Longitude and then use _that_ value to look up the city name. So let's do the same process of pulling this apart into two steps:

It should be _pretty_ obvious what this does:
```python
myData['Name'][0]
```
But we don't just want the first city in the list, we want the one with the highest longitude. So to achieve that we need to replace the `0` with an index that we found by looking in the `Longitude` list.
```python
myData['Longitude'].index(max(myData['Longitude']))

```
Ugh, that's still a little hard to read, isn't it? Let's write it down another way to make it easier to read:

```python
myData['Longitude'].index(
    max(myData['Longitude'])
)

```
There's the same `.index` which tells us that Python is going to look for something in the list associated with the `Longitude` key. All we've done is change what's _inside_ that index function: `max(myData['Longitude'])` is telling Python to find the _maximum_ value in the `myData['Longitude']` list. So to explain this in three steps, what we're doing is:
* Finding the maximum value in the Longitude column (we know there must be one, but we don't know what it is!),
* Finding the index (position) of that maximum value in the Longitude column (now we know what the value is!),
* Using that index to read a value out of the Name column.

I _am_ a geek, but that's pretty cool, right? In one line of code we managed to quickly find out where the data we needed was even though it involved three discrete steps. Remember how much work it was to find the mean when you were still thinking in _rows_, not _columns_?

### The Average City Size

Yeah, let's try that too.

Here we're going to 'cheat' a little bit: rather than writing our own function, we're going to import a package and use someone _else's_ function. The `numpy` package contains a _lot_ of useful functions that we can call on (if you don't believe me, add "`dir(np)`" on a new line after the `import` statement), and one of them calculates the average of a list or array of data.
```python
import numpy as np # Need to import a useful package
mean = np.mean(myData['Population'])
```
This is where our new approach really comes into its own: because all of the population data is in one place (a.k.a. a _series_ or column), we can just throw the whole list into the `np.mean` function rather than having to use all of those convoluted loops and counters. Simples, right?

## Review!

So the _really_ clever bit in all of this isn't switching from a list-of-lists to a dictionary-of-lists, it's recognising that the latter is a _better_ way to work _with_ the data that we're trying to analyse and that that there are useful functions that we can exploit to do the heavy lifting for us. Simply be changing the way that we stored the data in a 'data structure' (i.e. complex arrangement of lists, dictionaries, and variables) we were able to do away with lots of for loops and counters and conditions, and reduce many difficult operations to something that could be done on one line! 

# Formatting a Number

A final, handy trick if you want to output numbers in a _pretty_ way is to understand how the `format` method associated with string objects works: different cultures format numbers differently, so the English use commas as the thousands separator and a full-stop as the decimal separator but the French, naturally, do it their own way.

Here's an example:


```python
print "{:,.2f}".format(mean)

import locale
locale.setlocale(locale.LC_ALL, 'fr_FR')
print locale.format('%0.2f', mean, grouping=True, monetary=True)
```

Unfortunately, most programming languages were written by Anglophones and so most applications will happily output Anglo-formatted numbers but are rather less happy doing anyone else's.

More on `format` in the _Python String Format Cookbook_: https://mkaz.tech/python-string-format.html

# Writing a Script

If all of this has made sense to you then the _final_ step in this practical should be easy... Nah, I'm just kidding: there is a _lot_ to make sense of in this practical and you shouldn't worry if it hasn't all become clear to you just yet. But what I _can_ say is that you should read, and re-read this, until it _does_ make sense. Talk to your classmates. Talk to your teachers. This is the practical that unlocks everything that comes after: how to write code that can be re-used, how to make use of code written by other people, and a little bit about how to _think like a computer_. 

The _best_ way to be sure that you've understood the concepts here is to write a standalone Python script that takes any URL, parses it as a CSV file, and returns a dictionary-of-lists on which you can perform simple numerical analyses like the ones we just did above. You shouldn't need to write much in the way of new code because what you need to do involves _remixing_ the code that we've just been working with! The _only_ thing that will really require some thought is how to change the `readRemoteCSV` function from return a list-of-lists to a dictionary-of-lists. That won't be easy, but it shouldn't be impossible either. Remember that you can always start by breaking the problem down into little steps: how do you turn the header row into dictionary keys? how do you keep track of which column is associated with which key?

Do this now...
