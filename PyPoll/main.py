# Import dependencies
import os
import csv


csvpath = os.path.join('..', 'PyPoll', 'Election_Data.csv')

# Create Variables 
total_votes = 0 
khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0

# Open csv file
with open(csvpath, newline="") as results:

    
    csvreader = csv.reader(results, delimiter=",") 

    # Bypass the Header
    header = next(csvreader)     

    # Loop through rows to then count up the votes 
    for row in csvreader: 

        total_votes += 1

        if row[2] == "Khan": 
            khan_total += 1
        elif row[2] == "Correy":
            correy_total += 1
        elif row[2] == "Li": 
            li_total += 1
        elif row[2] == "O'Tooley":
            otooley_total += 1

 # Create a dictionary
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_total, correy_total,li_total,otooley_total]

# Zip the dictionary and then call the max function to determine winner
dict_results = dict(zip(candidates,votes))
winner = max(dict_results, key=dict_results.get)

# Calculate the percent totals
khan_percent = (khan_total/total_votes) *100
correy_percent = (correy_total/total_votes) * 100
li_percent = (li_total/total_votes)* 100
otooley_percent = (otooley_total/total_votes) * 100

# Print to the console
print(f"Election Results")
print(f"========================")
print(f"Total Votes: {total_votes}")
print(f"========================")
print(f"Khan: {khan_percent:.2f}% ({khan_total})")
print(f"Correy: {correy_percent:.2f}% ({correy_total})")
print(f"Li: {li_percent:.2f}% ({li_total})")
print(f"O'Tooley: {otooley_percent:.2f}% ({otooley_total})")
print(f"========================")
print(f"Winner: {winner}")
print(f"========================")

# Create a TXT file
with open("ElectionsResults.txt", "w") as text_file:
    print(f"Election Results:", file=text_file)
    print(f"========================", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print(f"========================", file=text_file)
    print(f"Khan: {khan_percent:.2f}% ({khan_total})", file=text_file)
    print(f"Correy: {correy_percent:.2f}% ({correy_total})", file=text_file)
    print(f"Li: {li_percent:.2f}% ({li_total})", file=text_file)
    print(f"O'Tooley: {otooley_percent:.2f}% ({otooley_total})", file=text_file)
    print(f"========================", file=text_file)
    print(f"Winner: {winner}", file=text_file)
    print(f"========================", file=text_file)
