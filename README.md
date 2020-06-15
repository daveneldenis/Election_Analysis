# Election_Analysis
Election Analysis using Python
## Project Overview
Client provided data source in a csv file to extrapolate election results and determine the winner.

## Resources
Software - VS Code Version 1.45.1, Python 3.8.2
Data Source - Election_results.csv
## Summary
Imported CSV and OS data sources to determine all votes casted. Coverted votes to percentages and 
determined the winner to be Diana DeGette. Total votes casted were 369,711 and of those 272, 892 (73.8%)
went to the winner.

## Challenge Overview
Create a list for the counties.
Create a dictionary where the county is the key and the votes cast for each county in the election are the values.
Create an empty string that will hold the county name that had the largest turnout.
Declare a variable that represents the number of votes that a county received. Hint: Inside a for loop, add an if statement to check if the county name has already been recorded. If not, add it to the list of county names.
Inside the with open() function where you are outputting the file, do the following:
Create three if statements to print out the voter turnout results similar to the results shown above.
Add the results to the output file.
Print the results to the command line.

## Challenge Summary
Election Results
-------------------------
Total Votes: 369,711
-------------------------

County Votes:

Jefferson: 10.5% (38,855)

Denver: 82.8% (306,055)

Arapahoe: 6.7% (24,801)

-------------------------
Largest County Turnout: Denver
-------------------------

Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)

-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------
