import os
import csv

file_to_load = os.path.join("data", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
cadidate_options = []
candidate_votes = {}

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        # count total votes
        total_votes += 1

        # handle candidate names and add them to the map
        candidate_name = row[2]
        if candidate_name not in candidate_votes.keys():
            candidate_votes[candidate_name] = {}
            candidate_votes[candidate_name]["votes"] = 0

        # increment the vote for candidate
        candidate_votes[candidate_name]["votes"] += 1

for candidate_name, data in candidate_votes.items():
    votes = data["votes"]
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_votes[candidate_name]["percentage"] = vote_percentage
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

# Find the winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

for candidate_name, data in candidate_votes.items():
    if data["votes"] > winning_count:
        winning_candidate = candidate_name
        winning_count = data["votes"]
        winning_percentage = data["percentage"]

# print out the winner
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)
