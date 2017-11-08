
# Practical responsibilities!

* Add 30 minutes to lectures for 'talking through the practical'
* Add questions into the practical to test higher-level knowledge/understanding

* 1: Code Camp Recap [JM]
    * Scripts vs Notebooks
    * Errors
    * Data Types & Input
    * Operators
    * Comments
    * Conditionals & Logic
    * Some basic loops
* 2: Functions & Packages [JR]
    * Lists
    * Dictionaries
    * More loops [Lists of Lists; Dictionaries of Lists]
    * Use a lib to read a remote file
    * Use string.split to parse CSV data
    * Use a lib to parse CSV data
    * Create a function to read a remote file
    * Create a function to parse CSV data
    * Calculating values derived from CSV data (using function on LoL)
    * Calculating values derived from CSV data (using function on DoL)
* 3: Working with Data [JM]
    * Methods (for Pandas)
    * Link back to Week 2 and DoL
    * Pandas syntax for columns (both '.' and foo['bar'] and why they exist)
    * Describe, summary, etc.
    * Introduce string.format()
    * Max/Min/Range and other stats functions (e.g. IQR)
    * Also an opportunity to introduce reading .gz/.zip files directly in pandas
    * Look at basic pandas plotting functionality (lead into Seaborn in Week 4)
* 4: Visualising Data [JR? Complete]
    * Using pandas with header data
    * Statistics as judgement, not truth -- plotting as first step on this path
    * Seaborn 
    * 3D plots
    * [Interpreting plots and other summary metrics]
    * Saving a plot
    * Automating analysis (loops but over data series now)
* 5: Assessed Notebook [JR]
    * _Assign reading for following week: Openshaw 1998 and Wyly 2014_
* 6: Working with Subsets of Data [JM]
    * Non-spatial Joins - join air quality data to existing LSOA data
    * Using the index [from Week 4]
    * Renaming columns (show how this was done in Data Loader nb)
    * Finding values, grouping by values (for Boroughs) [from Week 4]
    * Sampling data [from Week 4] -- will just highlight quickly
    * Matching on parts of a word, extracting parts of a word [from Week 4]
    * Exercises: Initial exploratory analysis of pollution data 
* 7: Transformation and Standardisation [JR]
    * Thinking in 'data space' [From Week 4]
    * What counts as extreme?
    * Finding outliers
    * Residuals (first exposure to this)
    * Simple Transformations??? [from Week 4]
    * Simple Standardisations??? [from Week 4]
* 8: Making a Map [JR]
    * Objects and methods [copy from Spatial Analysis Week 2? 3?]
        * (use geopandas to anchor this)
    * PySAL and loading shapefiles
    * Look at impact of transforms on understanding of map
    * Joins? (non-spatial already done in week 6)
        * Illustrate using Airbnb raw data (also gives geopandas whirl)!
* 9: Correlation and Residuals [JM]
    * Builds on standardisation and normalisation from Week 7
    * Possibly use scipy here since it has rank and Pearson correlation, and is a very well-used lib in the real world
    * Plot residuals on map and in graph! 
    * Seaborn (can include r^2 and rank correlation)
* 10: Aggregation and group-by [JM]
    * Brings in issues of scale and, implicitly, MAUP
