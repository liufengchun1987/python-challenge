import os
import csv
import sys

csvpath = os.path.join('..','python-challenge-resources','election_data.csv')

with open(csvpath, newline ="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    total_votes = 0
    candidate_dict = {}
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] not in candidate_dict:
            candidate_dict[row[2]] = 1
        else:
            candidate_dict[row[2]] = candidate_dict[row[2]] + 1

def output():
    print(f"Election Results")
    print("-----------------------------")
    print(f"Total Votes: I’m {total_votes}")
    print("-----------------------------") 

    winner = ""
    winner_vote = 0
    for candidate in candidate_dict:
        print(f"{candidate}: {round((candidate_dict[candidate]/total_votes)*100,2)}00% {candidate_dict[candidate]}")  

        if candidate_dict[candidate] > winner_vote:
            winner_vote = candidate_dict[candidate]
            winner = candidate
    print("-----------------------------")            
    print(f"Winner: {winner}")
    print("-----------------------------")       

sys.stdout=open("PayPoll.txt","w")
output()