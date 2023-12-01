# Creating the file

import os

# Reading the cvs file
import csv

# Join path
budget_data = os.path.join('.',"Resources", "budget_data.csv")

# Open and read csv file
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    # Find net amount of profit & loss
    Profit = []
    months = []

    # Read each row of data after header
    for rows in csvreader:
        Profit.append(int(rows[1]))
        months.append(rows[0])

    # Find the profit/loss change
    pl_change =[]

    for x in range(1, len(Profit)):
        pl_change.append((int(Profit[x]) - int(Profit[x-1])))

    # Calculate average profit/loss change
    pl_average_change = sum(pl_change) / len(pl_change)
    pl_average = round(pl_average_change, 2)

    # Calculate total months
    total_months = len(months)

    # Greatest increase in profits
    greatest_increase = max(pl_change)

    #greatest decrease in profits
    greatest_decrease = min(pl_change)


    # Print Statements

    print (f"Financial Analysis")

    print(f"....................................................................................")

    print (f"Total Months:" + str(total_months))

    print(f"Total:" + "$" + str(sum(Profit)))

    print (f"Average Change:" + "$" + str(pl_average))

    print(f"Greatest Increase in Profits: " + str(months[pl_change.index(max(pl_change))+1]) + " " + "($" + str(greatest_increase) + ")")

    print(f"Greatest Decrease in Profits: " + str(months[pl_change.index(min(pl_change))+1]) + " " + "($" + str(greatest_decrease) + ")")


    # Write Financial Analysis Summary

    file = open(f"output.txt","w")

    file.write(f"Financial Analysis" + "\n")

    file.write(f"...................................................................................." + "\n")

    file.write(f"total months: " + str(total_months) + "\n")

    file.write(f"Total: " + "$" + str(sum(Profit)) + "\n")

    file.write(f"Average change: " + "$" + str(pl_average) + "\n")

    file.write(f"Greatest Increase in Profits: " + str(months[pl_change.index(max(pl_change))+1]) + " " + "($" + str(greatest_increase) + ")\n")

    file.write(f"Greatest Decrease in Profits: " + str(months[pl_change.index(min(pl_change))+1]) + " " + "($" + str(greatest_decrease) + ")\n")

    file.close()