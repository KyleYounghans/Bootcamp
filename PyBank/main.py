# Import Dependencies
import os
import csv

csvpath = os.path.join('..', 'PyBank', 'PyBank.csv')

# Create variables
months = []
profit = []
net_change = []
 
# Open csv file
with open(csvpath,newline="") as PyBank:

    
    csvreader = csv.reader(PyBank,delimiter=",") 

    # Bypass the Header
    header = next(csvreader)  

    # Loop to append for variables
    for row in csvreader: 

        # Append the total months and total profits
        months.append(row[0])
        profit.append(int(row[1]))

    # Loop to find difference between months
    for i in range(len(profit)-1):
        
        # Appending Net_Change for the difference between months
        net_change.append(profit[i+1]-profit[i])
        
# Finding the Max and Min changes
maximum = max(net_change)
minimum = min(net_change)


best_month = net_change.index(max(net_change)) + 1
worst_month = net_change.index(min(net_change)) + 1 

# Print to Console

print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(net_change)/len(net_change),2)}")
print(f"Greatest Increase in Profits: {months[best_month]} (${(str(maximum))})")
print(f"Greatest Decrease in Profits: {months[worst_month]} (${(str(minimum))})")



# Create TXT File

with open("FinancialAnalysis.txt", "w") as text_file:
    print(f"Financial Analysis", file=text_file)
    print(f"------------------", file=text_file)
    print(f"Total Months: {len(months)}", file=text_file)
    print(f"Total: ${sum(profit)}", file=text_file)
    print(f"Average Change: {round(sum(net_change)/len(net_change),2)}", file=text_file)
    print(f"Greatest Increase in Profits: {months[best_month]} (${(str(maximum))})", file=text_file)
    print(f"Greatest Decrease in Profits: {months[worst_month]} (${(str(minimum))})", file=text_file)
