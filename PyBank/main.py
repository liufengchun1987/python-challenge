import os
import csv

csvpath = os.path.join('..','python-challenge-resources','budget_data.csv')

with open(csvpath, newline ="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    total_months = 0
    total_amount = 0
    pre_month_amount = 0
    total_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    for row in csvreader:
        total_months = total_months + 1
        total_amount = total_amount + int(row[1])
        current_month_amount = int(row[1])
        if total_months != 1:
            monthly_change = current_month_amount - pre_month_amount
            total_change = total_change + monthly_change
            if monthly_change > greatest_increase:
                greatest_increase = monthly_change
                greatest_increase_month = row[0]
            if monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                greatest_decrease_month = row[0]
        pre_month_amount = current_month_amount
    

output=(    
    f"Financial Analysis\n"
    f"-------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total_amount}\n"
    f"Average Change: {round(total_change/(total_months-1),2)}\n"
    f"Greatest Increse in Profits:{greatest_increase_month}  (${greatest_increase})\n"
    f"Greatest Decrese in Profits:{greatest_decrease_month} (${greatest_decrease})\n"
)

my_file = open("PyBank.txt", "w")
my_file.write(output)
