#Import the csv file

import os
import csv

#Locate the file path of the CSV file
budget_data = os.path.join("resources/budget_data.csv")

#Define variables
TotalMonths = 0
TotalProfLoss = 0
Value = 0
Change = 0
Dates = []
Profits = []

#Open and read the CSV file budget_data.csv
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csvHeader = next(csvreader)

    #Read the first row
    FirstRow = next(csvreader)
    TotalMonths += 1
    TotalProfLoss += int(FirstRow[1])
    Value = int(FirstRow[1])

 #Look at each row of data and start the 'for' loop through
    for row in csvreader:
        # note the dates using .append
        Dates.append(row[0])

        # Calculate the change and profit tracking it using .append
        Change = int(row[1])-Value
        Profits.append(Change)
        Value = int(row[1])

        #Look at total number of months
        TotalMonths += 1

        #Look at total net amount of profit/loss
        TotalProfLoss = TotalProfLoss + int(row[1])
#Look at the greatest increase in profits using max function
    GreatestIncrease = max(Profits)
    GreatestIndex = Profits.index(GreatestIncrease)
    GreatestDate = Dates[GreatestIndex]

    #Look at greatest decrease in profits using min function
    GreatestDecrease = min(Profits)
    DecreaseIndex = Profits.index(GreatestDecrease)
    DecreaseDate = Dates[DecreaseIndex]

    #Calculate the average change in profit loss using average/sum function
    AvgChange = sum(Profits)/len(Profits)


#What information to display
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(TotalMonths)}")
print(f"Total: ${str(TotalProfLoss)}")
print(f"Average Change: ${str(round(AvgChange,2))}")
print(f"Greatest Increase in Profits: {GreatestDate} (${str(GreatestIncrease)})")
print(f"Greatest Decrease in Profits: {DecreaseDate} (${str(GreatestDecrease)})")

#Export to txt file
output = open("output.txt", "w")
line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"TotalMonths: {str(TotalMonths)}")
line4 = str(f"Total: ${str(TotalProfLoss)}")
line5 = str(f"Average Change: ${str(round(AvgChange,2))}")
line6 = str(f"Greatest Increase in Profits: {GreatestDate} (${str(GreatestIncrease)})")
line7 = str(f"Greatest Decrease in Profits: {DecreaseDate} (${str(GreatestDecrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
