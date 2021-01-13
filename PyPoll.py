import os
import csv

file_to_load = os.path.join("data", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    # for row in file_reader:
    #     print(row)
