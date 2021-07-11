# The data we neet to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.


import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("election_analysis","Resources", "election_results.csv")
file_to_save = os.path.join("election_analysis","analysis","election_analysis.txt" )

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

with open(file_to_save, "w") as txt_file:
   txt_file.write("hello world!!!!!")
   txt_file.write("Arapahoe")
   txt_file.write("Denver")
   txt_file.write("Jefferson")
txt_file.close()