# Import Files
import os
# Read CSV file
import csv

# Join path
csvpath=os.path.join('Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    # Declare Election Variables
    votes = []
    county = []
    candidates = []
    Stockham = []
    DeGette = []
    Doane = []
    Stockham_votes = 0
    DeGette_votes = 0
    Doane_votes = 0

    # Read rows of data after header
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    # Calcualte votes
    total_votes = (len(votes))
    

    # Votes by Candidates
    for candidate in candidates:
        if candidate == "Charles Casper Stockham":
            Stockham.append(candidates)
            Stockham_votes = len(Stockham)
            
        elif candidate == "Diana DeGette":
            DeGette.append(candidates)
            DeGette_votes = len(DeGette)
            
        else:
            Doane.append(candidates)
            Doane_votes = len(Doane)
    
 
    
    
    # Voting Percentages
    Stockham_percent = round(((Stockham_votes / total_votes) * 100), 3)
    DeGette_percent = round(((DeGette_votes / total_votes) * 100), 3)
    Doane_percent = round(((Doane_votes / total_votes) * 100), 3)
    

    
    # Winner based on Popular vote 
    if Stockham_percent > max(DeGette_percent, Doane_percent):
        winner = "Charles_Casper_Stockham"
    elif DeGette_percent > max(Stockham_percent, Doane_percent):
        winner = "Diana_DeGette"  
    else:
        winner = "Raymon_Anthony_Doane"


    # Print Statements
    print(f'''Election Results
-----------------------------------
Total Votes: {total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {Stockham_percent}% ({Stockham_votes})
Diana_DeGette: {DeGette_percent}% ({DeGette_votes})
Raymon_Anthony_Doane: {Doane_percent}% ({Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')


    # Output to a text file
    file = open("output.txt","w")
    file.write(f'''Election Results
-----------------------------------
Total Votes: {total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {Stockham_percent}% ({Stockham_votes})
Diana_DeGette: {DeGette_percent}% ({DeGette_votes})
Raymon_Anthony_Doane: {Doane_percent}% ({Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')

    file.close()