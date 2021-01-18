# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# define function to calculate percentage


def calc_percentage(votes, total_votes):
    return float(votes) / float(total_votes) * 100


# Add a variable to load a file from a path.
file_to_load = os.path.join("data", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis_challenge.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
counties = {}
largest_turnout_county = ""
largest_turnout_votes = 0
largest_turnout_percentage = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_votes.keys():

            # Add the candidate name to the candidate list.
            candidate_votes[candidate_name] = {}

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name]["votes"] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name]["votes"] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county not in counties.keys():
            # 4b: Add the existing county to the list of counties.
            counties[county] = {}
            # 4c: Begin tracking the county's vote count.
            counties[county]["total_votes"] = 0
        # 5: Add a vote to that county's vote count.
        counties[county]["total_votes"] += 1

        # track a candidate's vote for the county
        if candidate_name not in counties[county].keys():
            counties[county][candidate_name] = 0

        counties[county][candidate_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county, data in counties.items():

        # 6b: Retrieve the county vote count.
        county_total_votes = data["total_votes"]

        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = calc_percentage(
            county_total_votes, total_votes)
        county_results = (
            f"-------------------------\n"
            f"County {county} Results:\n"
            f"Total votes of {county_total_votes:,} which is {county_vote_percentage:.1f}% of total votes.\n")
        print(county_results)
        txt_file.write(county_results)
        for candidate, votes in data.items():
            if candidate != "total_votes":
                # print out the county votes
                vote_percentage = calc_percentage(votes, county_total_votes)
                candidate_results = f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
                # 6d: Print the county results to the terminal.
                print(candidate_results)
                txt_file.write(candidate_results)
        # 6f: Write an if statement to determine the winning county and get its vote count.
        if county_total_votes > largest_turnout_votes:
            largest_turnout_county = county
            largest_turnout_percentage = county_vote_percentage
            largest_turnout_votes = county_total_votes

    print(f"-------------------------\n", end="")
    txt_file.write(f"-------------------------\n\n")

    # 7: Print the county with the largest turnout to the terminal.
    winning_county_results = (
        f"Winning County:\n"
        f"-------------------------\n"
        f"{largest_turnout_county} with {largest_turnout_votes:,} votes, which is {largest_turnout_percentage:.1f}% of total votes.\n"
        f"-------------------------\n\n")
    print(winning_county_results)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_results)

    # Save the final candidate vote count to the text file.
    print("Popular Vote Counts\n")
    print(f"-------------------------\n")
    txt_file.write("Popular Vote Counts\n")
    txt_file.write(f"-------------------------\n")
    for candidate_name, data in candidate_votes.items():

        # Retrieve vote count and percentage
        votes = data["votes"]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    txt_file.write(f"\n")
    winning_candidate_summary = (
        f"Winner of the popular vote:\n"
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
