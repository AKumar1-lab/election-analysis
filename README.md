# Election_Analysis

AKumar1-lab/election_analysis

## Purpose
In module 3, ability to utilize Python as the programming language.  Python is much more robust and faster than Excel or VBA.  It is also the base programming language that will be applied for the next series of modules and programming languages.

## Background

The Colorado Board of Elections employees Tom and Seth had given a task to complete an election audit of a recent Congressional election.  The counties in the district that were audited are:  Arapahoe, Denver, and Jefferson.
The tasks were as follows:
1.	Calculate the total number of votes cast.
2.	Get a complete list of candidates who received the votes.
3.	Calculate the total number of votes each candidate received.
4.	Calculate the percentage of votes each candidate won.
5.	Determine the winner of the election based on the popular vote.
6.	Once the base is completed, the challenge is to include the number of county votes and largest voter turnout.

## Resources

Data source: election_results.csv

Software: Python 3.7.6, Visual Studio Code 3.8.8 64-bit, Gitbash, Github

## Deliverables

This new assignment consists of two technical analysis deliverables and a written report to deliver your results. 

**Deliverable 1: The Election Results Printed to the Command Line**

Candidate Results

Total Votes in the election are printed to the terminal. 
Each candidate’s total votes and percentage of votes are printed to the terminal. 
The winner of the election, winning vote count, and winning percentage of votes are printed to the terminal. 

County Results
Each county and its total vote count are printed to the terminal. 
Each county and its percentage of the total votes are printed to the terminal. 
The county with the largest number of voters is printed to the terminal. 

<img width="266" alt="Complete election results" src="https://user-images.githubusercontent.com/85860367/129425548-72662b4d-65b8-42c1-b9ea-7e1a6256f150.PNG">


**Deliverable 2: The Election Results Saved to a Text File**

Candidate Results

Total Votes in the election are saved in the election_results.txt file. 
Each candidate’s total votes and percentage of votes are saved in the election_results.txt file. 
The winner of the election, winning vote count, and winning percentage of votes are saved in the election_results.txt file. 

<img width="400" alt="Capture candidate to text file" src="https://user-images.githubusercontent.com/85860367/129426682-b4f11ec1-a578-4104-94a8-e9fb2e31e26c.PNG">

<img width="310" alt="Percentage of Candidates" src="https://user-images.githubusercontent.com/85860367/129425685-f1f50e0c-d188-4a04-86b2-b56bec7eee28.PNG">

County Results

Each county and its total vote count are saved in the election_results.txt file. 
Each county and its percentage of the total votes are saved in the election_results.txt file. 
The county with the largest number of voters is saved in the election_results.txt file. 

<img width="400" alt="Capture County to text file" src="https://user-images.githubusercontent.com/85860367/129425863-6590345e-5c82-4430-8118-bdf114cb66b1.PNG">

<img width="310" alt="Capture county results including largest county" src="https://user-images.githubusercontent.com/85860367/129426834-2ffa5411-2272-42ca-ab4f-dfaf6dd9f7a5.PNG">

**Deliverable 3: A written Analysis of the Election Audit (README.md)**

Overview of Election Audit: Explain the purpose of this election audit analysis.

Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.
How many votes were cast in this congressional election?
Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
Which county had the largest number of votes?
Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

## Overview of Election Audit:

The overview of the Election Audit was to capture the the total votes, identify the candidates, identify the number each candidate received, the counties that participated, the number of votes, the county with the largest voter turnout and also determine who the winning candidate, the number of votes and the percentage of total votes.

## Summary

Election-Audit Results:

**Election Results: Total Votes that were casted was 369,711.**

**County Results:**

Jefferson: 10.5% (38,855)

Denver: 82.8% (306,055)

Arapahoe: 6.7% (24,801)

**Largest County Turnout: Denver**

**The candidates were in alphabetical order by name:**

1. Charles Casper Stockham
2. Diana DeGette
3. Raymon Anthony Doane

**The candidate results were the following:**

Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,607)

**The winner announced is:**

Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%

<img width="266" alt="Complete election results" src="https://user-images.githubusercontent.com/85860367/129424919-b40cff68-4c60-49c9-b293-21490d5d3cfb.PNG">

**Election-Audit Summary:**

The Election Audit has made a recommendation that the script for this election could be used in other elections, including the presidential.  The script would need to be expanded to include the number of candidates, and counties.  One of the modifications will be appending the new counties to the existing dictonaries for candidates and counties.  There will also need to be a recalculation of the total votes in an election for the percentages to be calculated correctly and accurately for the candidates.  If there is any mistakes, this can be problematic in determining the winner of the election. Having inaccurate results has risks and ramifications which can have dire effects in the long run including the credibility of future elections.
