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

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

       # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
         # Add it to the list of candidates.
         # Add the candidate name to the candidate list.
         candidate_options.append(candidate_name)
         # 2. Begin tracking that candidate's vote count.
         candidate_votes[candidate_name] = 0
         # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# 3. Print the total votes.
print(total_votes)

# Print the candidate list.
print(candidate_options)

# Print the candidate vote dictionary.
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")


with open(file_to_save, "w") as txt_file:
   txt_file.write("Counties in the Election\n")
   txt_file.write("-" * 20)
   txt_file.write("\nArapahoe\nDenver\nJefferson")
txt_file.close()