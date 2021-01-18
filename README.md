# Election Analysis

## Project Overview
-------------------------

A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
1. Get a complete list of candidates who recieved votes.
1. Calculate the total number of votes each candidate received.
1. Calculate the percentage of votes each candidate won.
1. Determine the winner of the election based on popular vote.

## Resources
-------------------------

- Data Source: election_results.csv
- Software: Python 3.8.5, Visual Studio Code v1.52.1

## Summary
-------------------------
The analysis of the election show that:

- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGettes
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham recieved 23% of the vote and 85,213 number of votes.
  - Diana DeGettes recieved 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane recieved 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who recieved 73.8% of the vote and 272,892 number of votes.

## Challenge Overview
-------------------------
The election commission has requested some additional data to complete the audit:

- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

I also will provide a breakdown of which candiate won which county.

## Challenge Summary
-------------------------

### Election Results

- Total Votes: 369,711

- County Votes:
  - County Jefferson:
    - 38,855 votes
    - 10.5% of total votes
    - Charles Casper Stockham: 50.8% (19,723)
    - Diana DeGette: 46.2% (17,963)
    - Raymon Anthony Doane: 3.0% (1,169)
  - County Denver:
    - 306,055 votes 
    - 82.8% of total votes
    - Charles Casper Stockham: 18.7% (57,188)
    - Diana DeGette: 78.2% (239,282)
    - Raymon Anthony Doane: 3.1% (9,585)
  - County Arapahoe:
    - 24,801 votes
    - 6.7% of total votes
    - Charles Casper Stockham: 33.5% (8,302)
    - Diana DeGette: 63.1% (15,647)
    - Raymon Anthony Doane: 3.4% (852)
  - Winning County:
    - Denver with 306,055 votes, which is 82.8% of total votes.
  - Notes:
    - Diana DeGette won both Arapahoe and Denver counties, but lost Jefferson county to Charles Casper Sotckham which had 50.8% of the votes vs. DeGette's 46.2% of the county's vote.


- Popular Vote Counts
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)

- Winner of the popular vote:
  - Diana DeGette
  - Vote: 272,892
  - Percentage: 73.8%

As you can see, this gives a decent breakdown of each county's vote and gives the results of both popular vote and county vote. With a few adjustments, such as pointint to a different csv file via prompt or exracting data from a database, this script could be used to analyze other elections as well.