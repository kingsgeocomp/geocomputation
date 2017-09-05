
# Practical responsibilities!

* Create a notebook that downloads and merges a range of public data
    * Work at Output Area scale (ca. 30k)
    * Derive distance to nearest park (one column per class) from each OA
    * Derive air quality measures for each OA
    * Derive distance from A & M-class roads (one column per class)?
    * Add some Census variables (3-4?)
    * Add aggregate AirBnB measures for each OA (look at what people are using in their research)
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
    * Possibly introduce concept of objects and methods [copy from Spatial Analysis Week 2? 3?]
    * Link back to Week 2 and DoL
    * Pandas syntax for columns (both '.' and foo['bar'] and why they exist)
    * Describe, summary, etc.
    * Max/Min/Range and other stats functions (e.g. IQR)
    * Simple calculations
    * Changing column types
    * [Working with time data]
    * Introducing... AirBnB data? (we dropped APIs, they're now in optional Practical-03b)
      * I would start by using the city data from the previous week and _then_ introducing real data near the end
      * Might also be worth just using the listings.csv data instead of the fuller .gz file for speed/simplicity and then I will use the full file in the following week.
      * Also an opportunity to introduce reading .gz/.zip files directly in pandas
* 4: Visualising Data [JR? Complete]
    * Using pandas with header data
    * Statistics as judgement, not truth -- plotting as first step on this path
    * Seaborn 
    * 3D plots
    * [Interpreting plots and other summary metrics]
    * Saving a plot
    * Automating analysis (loops but over data series now)
* 5: Assessed Notebook [JR]
    * _Any content we want to add for practicing for the next week? Or a re-cap assignment?_
* 6: Working with Subsets of Data [JM]
    * More on Boolean algebra in pandas selection
    * Links to vector and raster analysis? 
    * Using the index [from Week 4]
    * Finding values, grouping by values, etc. [from Week 4]
    * Sampling data [from Week 4] -- could be very useful for exploring big-_n_ problem so maybe not here?
    * Using loc/iloc (now superseded in some latest pandas???) [from Week 4]
    * Matching on parts of a word, extracting parts of a word [from Week 4]
* 7: Transformation and Standardisation [JR]
    * Thinking in 'data space' [From Week 4]
    * What counts as extreme?
    * Finding outliers
    * Residuals (first exposure to this)
    * Simple Transformations??? [from Week 4]
    * Simple Standardisations??? [from Week 4]
* 8: Making a Map [JR]
    * PySAL and loading shapefiles
    * Look at impact of transforms on understanding of map
    * Joins (non-spatial only?)
* 9: Correlation and Residuals [JM]
    * Builds on standardisation and normalisation from Week 7
    * Possibly use scipy here since it has rank and Pearson correlation, and is a very well-used lib in the real world
    * Plot residuals on map and in graph! 
    * Seaborn (can include r^2 and rank correlation)
* 10: Aggregation and group-by [JM]
    * Brings in issues of scale and, implicitly, MAUP
